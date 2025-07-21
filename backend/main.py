import tempfile
import uuid
import os
import logging
import time
from datetime import datetime
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pathlib import Path
from utils.xml_parser import parse_nfe
from utils.excel_handler import salvar_em_excel
import config
from validador import validar_xml_nfe, validar_tamanho_arquivo, contar_itens_xml

# Configurar logging básico
os.makedirs('logs', exist_ok=True)
logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/datarum.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("datarum")

app = FastAPI(
    title="Datarum API",
    description="API para conversão de XMLs de NFe em planilhas Excel - Sistema com logging e configuração flexível",
    version="1.0.1"
)

# CORS configurável
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Endpoint raiz com informações da API"""
    logger.info("Root endpoint accessed")
    return {
        "name": "Datarum API",
        "version": "1.0.1",
        "description": "Conversor de XMLs de NFe para Excel",
        "status": "online",
        "environment": config.ENVIRONMENT,
        "cors_origins": config.CORS_ORIGINS,
        "endpoints": {
            "processar": "POST /processar - Processa XMLs e retorna Excel",
            "processar-info": "POST /processar-info - Retorna estatísticas sem arquivo",
            "health": "GET /health - Status da API"
        }
    }

@app.get("/health")
async def health_check():
    """Health check SIMPLES para monitoramento"""
    import os
    import time
    
    logger.debug("Health check accessed")
    
    # Verificação básica do sistema
    status_info = {
        "status": "healthy",
        "timestamp": time.time(),
        "version": "1.0.1", 
        "environment": config.ENVIRONMENT,
        "uptime_info": "API online"
    }
    
    # Adiciona info de espaço em disco se possível
    try:
        if hasattr(os, 'statvfs'):
            statvfs = os.statvfs(".")
            disk_space_mb = round(statvfs.f_bavail * statvfs.f_frsize / (1024*1024), 2)
            status_info["disk_space_mb"] = disk_space_mb
    except:
        pass  # Ignora erro silenciosamente
        
    return status_info

@app.post("/processar")
async def processar(
    xmls: List[UploadFile] = File(...),
    planilha: str = Form(...)
):
    """Processa XMLs de NFe e retorna planilha Excel - Versão com logging"""
    start_time = time.time()
    request_id = str(uuid.uuid4())[:8]
    
    logger.info(f"[{request_id}] Iniciando processamento: {len(xmls)} arquivos, planilha='{planilha}'")
    
    try:
        # Validações de segurança
        if not xmls or len(xmls) > config.MAX_FILES_COUNT:
            logger.warning(f"[{request_id}] Muitos arquivos: {len(xmls)}")
            raise HTTPException(status_code=400, detail=f"Máximo {config.MAX_FILES_COUNT} arquivos permitidos")
        
        # Sanitizar nome da planilha
        planilha_original = planilha
        planilha = "".join(c for c in planilha if c.isalnum() or c in (' ', '_', '-')).strip()
        
        # Validações mais rigorosas de segurança
        if not planilha or len(planilha) > 100:
            logger.warning(f"[{request_id}] Nome inválido: '{planilha_original}'")
            raise HTTPException(status_code=400, detail="Nome de planilha inválido")
        
        # Bloquear tentativas de path traversal
        if '..' in planilha_original or '/' in planilha_original or '\\' in planilha_original:
            logger.warning(f"[{request_id}] Tentativa de path traversal: '{planilha_original}'")
            raise HTTPException(status_code=400, detail="Nome de planilha contém caracteres não permitidos")
        
        # Bloquear nomes de arquivos perigosos
        nomes_proibidos = ['con', 'aux', 'prn', 'nul', 'com1', 'com2', 'lpt1', 'lpt2']
        if planilha.lower() in nomes_proibidos:
            logger.warning(f"[{request_id}] Nome reservado: '{planilha}'")
            raise HTTPException(status_code=400, detail="Nome de planilha é um nome reservado do sistema")
        
        todos_itens = []
        total_size = 0

        # Usar diretório temporário seguro para XMLs
        with tempfile.TemporaryDirectory() as temp_dir:
            for i, xml in enumerate(xmls):
                filename = xml.filename
                
                # Validar tipo de arquivo
                if not filename.lower().endswith('.xml'):
                    logger.error(f"[{request_id}] Arquivo não-XML: {filename}")
                    raise HTTPException(status_code=400, detail=f"Arquivo {filename} não é XML")
                
                # Validar tamanho do arquivo
                contents = await xml.read()
                file_size = len(contents)
                total_size += file_size
                
                # Validação SIMPLES do tamanho
                validacao_tamanho = validar_tamanho_arquivo(file_size, config.MAX_FILE_SIZE)
                if not validacao_tamanho["valido"]:
                    logger.error(f"[{request_id}] Arquivo muito grande: {filename}")
                    raise HTTPException(status_code=400, detail=f"{filename}: {validacao_tamanho['erro']}")
                
                # Validação SIMPLES do XML NFe
                validacao_xml = validar_xml_nfe(contents)
                if not validacao_xml["valido"]:
                    logger.error(f"[{request_id}] XML inválido: {filename} - {validacao_xml['erro']}")
                    raise HTTPException(status_code=400, detail=f"{filename}: {validacao_xml['erro']}")
                
                # Log dos dados básicos encontrados
                dados = validacao_xml["dados"]
                itens_count = contar_itens_xml(contents)
                logger.info(f"[{request_id}] Processando {filename}: NFe {dados.get('numero', 'N/A')} ({itens_count} itens)")
                
                # Criar arquivo temporário seguro
                temp_file = Path(temp_dir) / f"{request_id}_{i}_{uuid.uuid4().hex[:8]}.xml"
                temp_file.write_bytes(contents)
                
                try:
                    # Processar XML
                    xml_start = time.time()
                    itens = parse_nfe(temp_file)
                    xml_time = time.time() - xml_start
                    
                    todos_itens.extend(itens)
                    logger.info(f"[{request_id}] Processado {filename}: {len(itens)} itens em {xml_time:.2f}s")
                    
                except Exception as e:
                    logger.error(f"[{request_id}] Erro processando {filename}: {str(e)}")
                    raise HTTPException(status_code=400, detail=f"Erro ao processar {filename}: {str(e)}")

        # Gerar Excel
        logger.info(f"[{request_id}] Gerando Excel: {len(todos_itens)} itens totais")
        
        # Criar arquivo temporário para Excel
        temp_excel_fd, temp_excel_path = tempfile.mkstemp(suffix='.xlsx', prefix=f'{planilha}_{request_id}_')
        os.close(temp_excel_fd)
        
        try:
            excel_start = time.time()
            rows_saved = salvar_em_excel(todos_itens, temp_excel_path)
            excel_time = time.time() - excel_start
            
            total_time = time.time() - start_time
            file_size = os.path.getsize(temp_excel_path)
            
            logger.info(f"[{request_id}] Sucesso! {rows_saved} linhas, {file_size} bytes, {total_time:.2f}s total")

            # Classe para limpeza automática
            class FileResponseWithCleanup(FileResponse):
                def __init__(self, *args, **kwargs):
                    self.temp_path = kwargs.pop('temp_path', None)
                    self.request_id = kwargs.pop('request_id', 'unknown')
                    super().__init__(*args, **kwargs)
                
                async def __call__(self, scope, receive, send):
                    try:
                        await super().__call__(scope, receive, send)
                        logger.info(f"[{self.request_id}] Arquivo enviado com sucesso")
                    finally:
                        # Deletar arquivo temporário após envio
                        if self.temp_path and os.path.exists(self.temp_path):
                            try:
                                os.unlink(self.temp_path)
                                logger.debug(f"[{self.request_id}] Arquivo temporário removido")
                            except Exception as e:
                                logger.warning(f"[{self.request_id}] Erro removendo temp: {e}")

            return FileResponseWithCleanup(
                path=temp_excel_path,
                filename=f"{planilha}.xlsx",
                media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                temp_path=temp_excel_path,
                request_id=request_id
            )
            
        except Exception as e:
            # Limpar arquivo temporário em caso de erro
            if os.path.exists(temp_excel_path):
                os.unlink(temp_excel_path)
            logger.error(f"[{request_id}] Erro gerando Excel: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Erro ao gerar planilha: {str(e)}")
            
    except HTTPException:
        # Re-raise HTTPExceptions
        raise
    except Exception as e:
        # Log e tratar erros não previstos
        total_time = time.time() - start_time
        logger.exception(f"[{request_id}] Erro inesperado após {total_time:.2f}s: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno do servidor")

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

    # Resumo para feedback com estatísticas avançadas
    numeros_nfe = list({item["numero_nf"] for item in todos_itens if "numero_nf" in item})
    emitentes = list({item["emitente"] for item in todos_itens if "emitente" in item})
    versoes_nfe = list({item["versao_nfe"] for item in todos_itens if "versao_nfe" in item})
    
    # Calcular período das notas
    datas = [item.get("data_emissao") for item in todos_itens if item.get("data_emissao")]
    datas_validas = [d for d in datas if d and d != ""]
    
    periodo = {}
    if datas_validas:
        periodo = {
            "inicio": min(datas_validas),
            "fim": max(datas_validas)
        }
    
    # Calcular valor total
    try:
        valores = [float(item.get("valor_total_nf", 0)) for item in todos_itens if item.get("valor_total_nf")]
        valor_total = sum(v for v in valores if v > 0)
    except:
        valor_total = 0

    return {
        "itens_processados": len(todos_itens),
        "arquivos_processados": len(xmls),
        "notas_encontradas": numeros_nfe,
        "emitentes": emitentes,
        "versoes_nfe": versoes_nfe,
        "periodo": periodo,
        "valor_total": round(valor_total, 2) if valor_total > 0 else 0,
        "planilha_destino": f"{planilha}.xlsx"
    }