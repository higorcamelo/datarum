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

    # Usar diretório temporário seguro para XMLs
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

    # Criar arquivo temporário para Excel que não será deletado automaticamente
    temp_excel_fd, temp_excel_path = tempfile.mkstemp(suffix='.xlsx', prefix=f'{planilha}_')
    os.close(temp_excel_fd)  # Fechar o file descriptor
    
    try:
        salvar_em_excel(todos_itens, temp_excel_path)

        # Criar uma response que deleta o arquivo após o envio
        class FileResponseWithCleanup(FileResponse):
            def __init__(self, *args, **kwargs):
                self.temp_path = kwargs.pop('temp_path', None)
                super().__init__(*args, **kwargs)
            
            async def __call__(self, scope, receive, send):
                try:
                    await super().__call__(scope, receive, send)
                finally:
                    # Deletar arquivo temporário após envio
                    if self.temp_path and os.path.exists(self.temp_path):
                        os.unlink(self.temp_path)

        return FileResponseWithCleanup(
            path=temp_excel_path,
            filename=f"{planilha}.xlsx",
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            temp_path=temp_excel_path
        )
    except Exception as e:
        # Se der erro, limpar o arquivo temporário
        if os.path.exists(temp_excel_path):
            os.unlink(temp_excel_path)
        raise e

@app.post("/processar-info")
async def processar_info(
    xmls: List[UploadFile] = File(...),
    planilha: str = Form(...)
):
    """Retorna apenas informações sobre o processamento, sem arquivo"""
    todos_itens = []

    # Usar diretório temporário seguro
    with tempfile.TemporaryDirectory() as temp_dir:
        for xml in xmls:
            contents = await xml.read()
            temp_file = Path(temp_dir) / f"{uuid.uuid4()}.xml"
            temp_file.write_bytes(contents)
            
            itens = parse_nfe(temp_file)
            todos_itens.extend(itens)

    # Resumo para feedback
    numeros_nfe = list({item["numero_nf"] for item in todos_itens if "numero_nf" in item})
    emitentes = list({item["emitente"] for item in todos_itens if "emitente" in item})

    return {
        "itens_processados": len(todos_itens),
        "notas_encontradas": numeros_nfe,
        "emitentes": emitentes,
        "planilha_destino": f"{planilha}.xlsx"
    }