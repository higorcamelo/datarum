from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import os
from utils.xml_parser import parse_nfe
from utils.excel_handler import salvar_em_excel
import shutil

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # depois troca pro frontend em produção
    allow_methods=["*"],
    allow_headers=["*"],
)

PLANILHA_DIR = "planilhas"
os.makedirs(PLANILHA_DIR, exist_ok=True)

@app.post("/processar")
async def processar(
    xmls: List[UploadFile] = File(...),
    planilha: str = Form(...)
):
    todos_itens = []

    for xml in xmls:
        contents = await xml.read()
        temp_path = f"temp_{xml.filename}"
        with open(temp_path, "wb") as f:
            f.write(contents)
        itens = parse_nfe(temp_path)
        todos_itens.extend(itens)
        os.remove(temp_path)

    caminho_planilha = os.path.join(PLANILHA_DIR, f"{planilha}.xlsx")
    qtd = salvar_em_excel(todos_itens, caminho_planilha)

    # Resumo para feedback
    numeros_nfe = list({item["numero_nf"] for item in todos_itens if "numero_nf" in item})
    emitentes = list({item["emitente"] for item in todos_itens if "emitente" in item})

    return {
        "itens_processados": qtd,
        "notas_encontradas": numeros_nfe,
        "emitentes": emitentes,
        "planilha_destino": f"{planilha}.xlsx"
    }

@app.get("/planilhas")
def listar_planilhas():
    arquivos = os.listdir(PLANILHA_DIR)
    nomes = [arq.replace(".xlsx", "") for arq in arquivos if arq.endswith(".xlsx")]
    return nomes

@app.get("/download/{nome}")
def baixar_planilha(nome: str):
    caminho = os.path.join(PLANILHA_DIR, f"{nome}.xlsx")
    if os.path.exists(caminho):
        return FileResponse(path=caminho, filename=f"{nome}.xlsx", media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    return {"erro": "Arquivo não encontrado."}