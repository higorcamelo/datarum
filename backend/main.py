import tempfile
import uuid
import os
import logging
import time
import json
from datetime import datetime
from typing import List
import uvicorn
from api.config import CAMPOS_DISPONIVEIS

from fastapi import FastAPI, File, UploadFile, Form, HTTPException, BackgroundTasks, Request
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

# Imports internos
from utils.xml_parser import parse_nfe
from utils.excel_handler import salvar_em_excel
from api.config import (
    MENSAGENS_ERRO,
    MAX_FILE_SIZE,
    LOG_LEVEL,
    get_preset_config,
    PRESETS,
    CORS_ORIGINS
)
from validador import validar_xml_nfe, validar_tamanho_arquivo


def resolver_campos(preset: str, campos_personalizados=None):
    if preset == "personalizado":
        if not campos_personalizados:
            raise HTTPException(
                status_code=400,
                detail="Campos personalizados não informados."
            )
        return campos_personalizados

    if preset not in PRESETS:
        raise HTTPException(status_code=400, detail="Preset inválido.")

    config = get_preset_config(preset)
    return config["campos"]


# Configuração de Logging
logging.basicConfig(
    level=LOG_LEVEL,
    format='%(asctime)s - %(levelname)s - [%(name)s] %(message)s'
)
logger = logging.getLogger("datarum")

app = FastAPI(
    title="Datarum API",
    description="Conversor de XML NFe para Excel",
    version="1.0.0"
)

# CORS vindo do config
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def remover_arquivo_temporario(path: str):
    try:
        if os.path.exists(path):
            os.remove(path)
            logger.debug(f"Arquivo temporário removido: {path}")
    except Exception as e:
        logger.error(f"Erro ao remover arquivo temporário {path}: {e}")

@app.middleware("http")
async def check_api_key(request: Request, call_next):
    if request.url.path in ["/", "/health", "/docs"]:
        return await call_next(request)

    api_key = request.headers.get("x-api-key")

    if api_key != os.getenv("GCP_KEY"):
        raise HTTPException(status_code=403, detail="Forbidden")

    return await call_next(request)

@app.get("/config")
async def get_config():
    return {
        "presets": PRESETS,
        "campos": CAMPOS_DISPONIVEIS
    }
    
@app.get("/")
async def root():
    return {
        "status": "online",
        "service": "Datarum API",
        "health": "/health",
        "docs": "/docs"
    }
    
    
@app.get("/health")
async def health():
    return {
        "status": "online",
        "timestamp": datetime.now().isoformat(),
        "service": "Datarum Parser"
    }


@app.post("/processar")
async def processar(
    background_tasks: BackgroundTasks,
    files: List[UploadFile] = File(...),
    planilha: str = Form("extracao_datarum"),
    campos_selecionados: str = Form(None),
    opcoes: str = Form(None),
    preset: str = Form("basico")
):
    request_id = str(uuid.uuid4())[:8]
    start_time = time.time()

    logger.info(f"[{request_id}] Iniciando processamento de {len(files)} arquivos.")

    try:
        # 1. Sanitização do nome da planilha
        planilha_limpa = "".join(
            c for c in planilha if c.isalnum() or c in (' ', '_', '-')
        ).strip()

        if not planilha_limpa:
            planilha_limpa = "extracao_datarum"

        # 2. Parse de JSON
        try:
            if campos_selecionados:
                campos_lista = json.loads(campos_selecionados)
                if not isinstance(campos_lista, list):
                    raise HTTPException(400, "campos_selecionados deve ser lista")
            else:
                campos_lista = []
            opcoes_dict = json.loads(opcoes) if opcoes else {}
        except json.JSONDecodeError:
            raise HTTPException(status_code=400, detail="Parâmetros JSON mal formatados.")

        # 3. Resolver preset
        campos = resolver_campos(preset, campos_lista)

        todos_itens = []
        arquivos_processados = []
        erros = []

        # 4. Processamento dos arquivos
        for xml in files:
            content = await xml.read()

            v_tamanho = validar_tamanho_arquivo(
                len(content),
                MAX_FILE_SIZE // (1024 * 1024)
            )
            v_xml = validar_xml_nfe(content)

            if not v_tamanho["valido"]:
                erros.append({"arquivo": xml.filename, "erro": v_tamanho["erro"]})
                continue

            if not v_xml["valido"]:
                erros.append({"arquivo": xml.filename, "erro": v_xml["erro"]})
                continue

            try:
                dados = parse_nfe(content, campos_selecionados=campos)

                if dados:
                    todos_itens.extend(dados)
                    arquivos_processados.append(xml.filename)
                else:
                    erros.append({
                        "arquivo": xml.filename,
                        "erro": "Nenhum item encontrado no XML"
                    })

            except Exception as e:
                logger.warning(f"[{request_id}] Erro ao processar {xml.filename}: {e}")
                erros.append({"arquivo": xml.filename, "erro": str(e)})

        # 5. Verificação de dados extraídos
        if not todos_itens:
            raise HTTPException(status_code=400, detail=MENSAGENS_ERRO["sem_dados"])

        # 6. Gerar Excel temporário
        temp_path = os.path.join(
            tempfile.gettempdir(),
            f"{planilha_limpa}_{request_id}.xlsx"
        )

        config_excel = {
            "campos_selecionados": campos,
            "opcoes": opcoes_dict,
            "preset": preset,
            "arquivos_processados": arquivos_processados,
            "erros": erros
        }

        salvar_em_excel(todos_itens, temp_path, configuracao=config_excel)

        total_time = time.time() - start_time
        logger.info(
            f"[{request_id}] Concluído em {total_time:.2f}s. "
            f"{len(todos_itens)} itens extraídos."
        )

        background_tasks.add_task(remover_arquivo_temporario, temp_path)

        return FileResponse(
            path=temp_path,
            filename=f"{planilha_limpa}.xlsx",
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"[{request_id}] Erro crítico: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=MENSAGENS_ERRO["processamento_erro"]
        )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)