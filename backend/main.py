import tempfile
import uuid
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import os
from pathlib import Path
from utils.xml_parser import parse_nfe
from utils.excel_handler import salvar_em_excel

app = FastAPI()

# CORS - Configuração mais restritiva
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173", "http://127.0.0.1:5173"],  # Apenas origins específicas
    allow_credentials=True,
    allow_methods=["GET", "POST"],  # Apenas métodos necessários
    allow_headers=["*"],
)

PLANILHA_DIR = "planilhas"
os.makedirs(PLANILHA_DIR, exist_ok=True)

@app.post("/processar")
async def processar(
    xmls: List[UploadFile] = File(...),
    planilha: str = Form(...)
):
    # Validações de segurança
    if not xmls or len(xmls) > 50:  # Limite de arquivos
        raise HTTPException(status_code=400, detail="Máximo 50 arquivos permitidos")
    
    # Sanitizar nome da planilha
    planilha = "".join(c for c in planilha if c.isalnum() or c in (' ', '_', '-')).strip()
    if not planilha or len(planilha) > 100:
        raise HTTPException(status_code=400, detail="Nome de planilha inválido")
    
    todos_itens = []

    # Usar diretório temporário seguro
    with tempfile.TemporaryDirectory() as temp_dir:
        for xml in xmls:
            # Validar tipo de arquivo
            if not xml.filename.lower().endswith('.xml'):
                raise HTTPException(status_code=400, detail=f"Arquivo {xml.filename} não é XML")
            
            # Validar tamanho (5MB máximo)
            contents = await xml.read()
            if len(contents) > 5 * 1024 * 1024:
                raise HTTPException(status_code=400, detail=f"Arquivo {xml.filename} muito grande")
            
            # Criar arquivo temporário seguro
            temp_file = Path(temp_dir) / f"{uuid.uuid4()}.xml"
            temp_file.write_bytes(contents)
            
            try:
                itens = parse_nfe(temp_file)
                todos_itens.extend(itens)
            except Exception as e:
                raise HTTPException(status_code=400, detail=f"Erro ao processar {xml.filename}: {str(e)}")

    caminho_planilha = os.path.join(PLANILHA_DIR, f"{planilha}.xlsx")
    salvar_em_excel(todos_itens, caminho_planilha)

    return FileResponse(
        path=caminho_planilha,
        filename=f"{planilha}.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

@app.post("/processar-info")
async def processar_info(
    xmls: List[UploadFile] = File(...),
    planilha: str = Form(...)
):
    """Retorna apenas informações sobre o processamento, sem arquivo"""
    todos_itens = []

    for xml in xmls:
        contents = await xml.read()
        temp_path = f"temp_{xml.filename}"
        with open(temp_path, "wb") as f:
            f.write(contents)
        itens = parse_nfe(temp_path)
        todos_itens.extend(itens)
        os.remove(temp_path)

    # Resumo para feedback
    numeros_nfe = list({item["numero_nf"] for item in todos_itens if "numero_nf" in item})
    emitentes = list({item["emitente"] for item in todos_itens if "emitente" in item})

    return {
        "itens_processados": len(todos_itens),
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