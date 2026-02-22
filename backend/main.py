import tempfile
import uuid
import os
import logging
import time
import json
from datetime import datetime
from typing import List
import uvicorn


from fastapi import FastAPI, File, UploadFile, Form, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

# Imports internos - Estrutura de pacotes padrão
from utils.xml_parser import parse_nfe
from utils.excel_handler import salvar_em_excel
from api.config import PRESETS, MENSAGENS_ERRO, MAX_FILE_SIZE, LOG_LEVEL
from validador import validar_xml_nfe, validar_tamanho_arquivo

# Configuração de Logging focada em clareza no terminal
logging.basicConfig(
    level=LOG_LEVEL,
    format='%(asctime)s - %(levelname)s - [%(name)s] %(message)s'
)
logger = logging.getLogger("datarum")

app = FastAPI(
    title="Datarum API", 
    description="Conversor de XML NFe para Excel",
    version="1.1.0"
)

# Configuração de CORS - Essencial para integração com o Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def remover_arquivo_temporario(path: str):
    """Remove o arquivo do servidor após o envio ao cliente."""
    try:
        if os.path.exists(path):
            os.remove(path)
            logger.debug(f"Arquivo temporário removido: {path}")
    except Exception as e:
        logger.error(f"Erro ao remover arquivo temporário {path}: {e}")

@app.get("/health")
async def health():
    """Endpoint de verificação de integridade."""
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
    print(">>> CAMPOS RECEBIDOS:", campos_selecionados)
    print(">>> TIPO:", type(campos_selecionados))
    print(">>> PRESET:", preset)
    print("ASSINATURA ATUAL: files")
    request_id = str(uuid.uuid4())[:8]
    start_time = time.time()
    
    logger.info(f"[{request_id}] Iniciando processamento de {len(files)} arquivos.")

    try:
        # 1. Sanitização do nome da planilha (Segurança contra Path Traversal)
        planilha_limpa = "".join(c for c in planilha if c.isalnum() or c in (' ', '_', '-')).strip()
        if not planilha_limpa:
            planilha_limpa = "extracao_datarum"

        # 2. Parse das Configurações (Campos e Opções)
        try:
            campos_lista = json.loads(campos_selecionados) if campos_selecionados else []
            opcoes_dict = json.loads(opcoes) if opcoes else {}
        except json.JSONDecodeError:
            raise HTTPException(status_code=400, detail="Parâmetros JSON mal formatados.")
        
        # Se não houver campos manuais, aplica a configuração do Preset
        if campos_selecionados is None:
            p_conf = PRESETS.get(preset, PRESETS["basico"])
            campos_lista = p_conf["campos"]
            opcoes_dict = p_conf["opcoes"]
        else:
            campos_lista = json.loads(campos_selecionados)

        todos_itens = []
        arquivos_processados = []
        erros = []

        # 3. Loop de Processamento de Arquivos
        for xml in files:
            content = await xml.read()
            
            # Validação de Tamanho e Estrutura XML
            v_tamanho = validar_tamanho_arquivo(len(content), MAX_FILE_SIZE // (1024*1024))
            v_xml = validar_xml_nfe(content)

            if not v_tamanho["valido"]:
                erros.append({"arquivo": xml.filename, "erro": v_tamanho["erro"]})
                continue
            
            if not v_xml["valido"]:
                erros.append({"arquivo": xml.filename, "erro": v_xml["erro"]})
                continue

            try:
                # Extração dos dados usando o parser
                # Passamos o content (bytes) - certifique-se que seu xml_parser lide com bytes ou decodifique
                itens = parse_nfe(content, campos_selecionados=campos_lista)
                
                if itens:
                    todos_itens.extend(itens)
                    arquivos_processados.append(xml.filename)
                else:
                    erros.append({"arquivo": xml.filename, "erro": "Nenhum item encontrado no XML"})
                    
            except Exception as e:
                logger.warning(f"[{request_id}] Erro ao processar {xml.filename}: {e}")
                erros.append({"arquivo": xml.filename, "erro": str(e)})

        # 4. Verificação de Resultados
        if not todos_itens:
            raise HTTPException(status_code=400, detail=MENSAGENS_ERRO["sem_dados"])

        # 5. Geração do Arquivo Excel Temporário
        temp_path = os.path.join(tempfile.gettempdir(), f"{planilha_limpa}_{request_id}.xlsx")

        config_excel = {
            'campos_selecionados': campos_lista,
            'opcoes': opcoes_dict,
            'preset': preset,
            'arquivos_processados': arquivos_processados,
            'erros': erros
        }

        salvar_em_excel(todos_itens, temp_path, configuracao=config_excel)

        total_time = time.time() - start_time
        logger.info(f"[{request_id}] Concluído em {total_time:.2f}s. {len(todos_itens)} itens extraídos.")

        # 6. Retorno do Arquivo com Limpeza em Background
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
        raise HTTPException(status_code=500, detail=MENSAGENS_ERRO["processamento_erro"])

if __name__ == "__main__":
    # Rodar localmente para testes
    uvicorn.run(app, host="0.0.0.0", port=8000)