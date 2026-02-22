from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import Response, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from typing import List, Optional
from api.config import PRESETS, MENSAGENS_ERRO
from typing import List, Optional
import tempfile
import os
import sys
import pathlib
import json

# Ajuste de Path para Serverless
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from utils.xml_parser import parse_nfe
from utils.excel_handler import salvar_em_excel

app = FastAPI(title="Datarum API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"status": "online", "service": "Datarum Parser"}

@app.post("/processar")
async def processar_excel(
    files: List[UploadFile] = File(...),
    preset_nome: Optional[str] = Form("basico"),
    campos: Optional[List[str]] = Form(None),
    planilha_nome: Optional[str] = Form("datarum_extracao")
):
    print(">>> CAMPOS RECEBIDOS:", campos)
    print(">>> TIPO:", type(campos))
    print(">>> PRESET:", preset_nome)
    print("ASSINATURA ATUAL: files")
    try:
        # 1. Definir o que será extraído (Preset ou Campos Customizados)
        if campos:
            campos_lista = campos
            opcoes = {"incluirTotais": True, "incluirResumo": True}
        else:
            preset_config = PRESETS.get(preset_nome)
            if not preset_config:
                raise HTTPException(status_code=400, detail=MENSAGENS_ERRO["preset_inexistente"].format(preset=preset_nome))
            campos_lista = preset_config["campos"]
            opcoes = preset_config["opcoes"]

        todos_dados = []
        arquivos_processados = []

        # 2. Loop de processamento dos XMLs
        for file in files:
            if not file.filename.lower().endswith('.xml'):
                continue
            
            content = await file.read()
            try:
                # O parse_nfe já filtra os campos internamente
                dados_nfe = parse_nfe(content, campos_selecionados=campos_lista)
                if dados_nfe:
                    todos_dados.extend(dados_nfe)
                    arquivos_processados.append(file.filename)
            except Exception as e:
                print(f"Erro no arquivo {file.filename}: {str(e)}")
                continue

        if not todos_dados:
            return JSONResponse(status_code=400, content={"message": MENSAGENS_ERRO["sem_dados"]})

        # 3. Preparar configuração para o Excel Handler
        config_excel = {
            'campos_selecionados': campos_lista,
            'preset': preset_nome if not campos else 'personalizado',
            'arquivos_processados': arquivos_processados,
            'opcoes': opcoes
        }

        # 4. Gerar arquivo temporário
        with tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx') as tmp:
            tmp_path = tmp.name

        # Salvar usando o handler profissional que você já tem
        salvar_em_excel(todos_dados, tmp_path, configuracao=config_excel)

        # Ler para retornar na resposta
        with open(tmp_path, 'rb') as f:
            excel_content = f.read()

        # Limpeza
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)

        nome_final = f"{planilha_nome}.xlsx" if not planilha_nome.endswith('.xlsx') else planilha_nome

        return Response(
            content=excel_content,
            media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            headers={
                'Content-Disposition': f'attachment; filename="{nome_final}"',
                'Access-Control-Expose-Headers': 'Content-Disposition'
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=500, 
            content={"message": MENSAGENS_ERRO["processamento_erro"], "error": str(e)}
        )

handler = Mangum(app)