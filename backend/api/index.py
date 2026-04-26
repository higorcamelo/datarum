from fastapi import FastAPI, UploadFile, File, Form, HTTPException, Request
from fastapi.responses import Response, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from typing import List, Optional
from api.config import PRESETS, MENSAGENS_ERRO, CAMPOS_DISPONIVEIS
import tempfile
import os
import sys
import pathlib
import json
from dotenv import load_dotenv
load_dotenv() 

GCP_KEY = os.getenv("GCP_KEY")
# Ajuste de Path para Serverless
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from utils.xml_parser import parse_nfe
from utils.excel_handler import salvar_em_excel

app = FastAPI(title="Datarum API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:5173",
    "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def check_api_key(request: Request, call_next):
    # Permite o root (health check)
    if request.url.path == "/":
        return await call_next(request)

    api_key = request.headers.get("x-api-key")

    if api_key != GCP_KEY:
        raise HTTPException(status_code=403, detail="Forbidden")

    return await call_next(request)

@app.get("/")
async def root():
    return {"status": "online", "service": "Datarum Parser"}


@app.get("/config")
async def get_config():
    return {
        "presets": PRESETS,
        "campos": CAMPOS_DISPONIVEIS
    }
    
@app.post("/processar")
async def processar_excel(
    files: List[UploadFile] = File(...),
    preset: Optional[str] = Form("basico"),
    campos_selecionados: Optional[str] = Form(None),
    planilha: Optional[str] = Form("datarum_extracao")
):

    try:    
        preset = (preset or "basico").strip().lower()
        # Definir campos (Preset ou Customizado)
        if campos_selecionados:
            try:
                campos_lista = json.loads(campos_selecionados)
                if not isinstance(campos_lista, list):
                    raise HTTPException(400, "campos_selecionados precisa ser lista")
            except json.JSONDecodeError:
                raise HTTPException(status_code=400, detail="JSON de campos inválido.")

            opcoes = {"incluirTotais": True, "incluirResumo": True}
            preset_final = "personalizado"

        else:
            preset_config = PRESETS.get(preset)
            if not preset_config:
                raise HTTPException(
                    status_code=400,
                    detail=MENSAGENS_ERRO["preset_inexistente"].format(preset=preset)
                )

            campos_lista = preset_config["campos"]
            opcoes = preset_config["opcoes"]
            preset_final = preset

        todos_dados = []
        arquivos_processados = []

        # Processar XMLs
        for file in files:
            if not file.filename.lower().endswith(".xml"):
                continue

            content = await file.read()

            try:
                dados_nfe = parse_nfe(content, campos_selecionados=campos_lista)

                if dados_nfe:
                    todos_dados.extend(dados_nfe)
                    arquivos_processados.append(file.filename)

            except Exception as e:
                print(f"Erro no arquivo {file.filename}: {str(e)}")
                continue

        if not todos_dados:
            return JSONResponse(
                status_code=400,
                content={"message": MENSAGENS_ERRO["sem_dados"]}
            )

        # Configuração do Excel
        config_excel = {
            "campos_selecionados": campos_lista,
            "preset": preset_final,
            "arquivos_processados": arquivos_processados,
            "opcoes": opcoes,
        }

        # 4️⃣ Criar arquivo temporário
        with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
            tmp_path = tmp.name

        salvar_em_excel(todos_dados, tmp_path, configuracao=config_excel)

        # 5️⃣ Ler conteúdo
        with open(tmp_path, "rb") as f:
            excel_content = f.read()

        # Limpeza
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)

        # Sanitização simples do nome
        planilha_limpa = "".join(
            c for c in planilha if c.isalnum() or c in (" ", "_", "-")
        ).strip()

        if not planilha_limpa:
            planilha_limpa = "datarum_extracao"

        nome_final = (
            f"{planilha_limpa}.xlsx"
            if not planilha_limpa.endswith(".xlsx")
            else planilha_limpa
        )

        return Response(
            content=excel_content,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={
                "Content-Disposition": f'attachment; filename="{nome_final}"',
                "Access-Control-Expose-Headers": "Content-Disposition",
            },
        )

    except HTTPException:
        raise

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "message": MENSAGENS_ERRO["processamento_erro"],
                "error": str(e),
            },
        )


handler = Mangum(app)