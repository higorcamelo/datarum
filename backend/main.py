import tempfile
import uuid
import os
import logging
import time
import sys
from datetime import datetime
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pathlib import Path

# Adicionar o diretório atual ao path para imports funcionarem no Vercel
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from utils.xml_parser import parse_nfe
    from utils.excel_handler import salvar_em_excel
except ImportError:
    # Fallback para imports relativos se estiver em ambiente local
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))
    from utils.xml_parser import parse_nfe
    from utils.excel_handler import salvar_em_excel

import config
from validador import validar_xml_nfe, validar_tamanho_arquivo, contar_itens_xml

# Configurar logging para ambiente serverless (Vercel)
# No Vercel, só podemos usar stdout/stderr, não arquivos
if os.getenv('VERCEL_ENV') or os.getenv('VERCEL') or os.getenv('ENVIRONMENT') == 'production':
    # Configuração para Vercel - apenas console
    logging.basicConfig(
        level=getattr(logging, config.LOG_LEVEL),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )
else:
    # Configuração para desenvolvimento local
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

# CORS configuração - DEVE ser a primeira coisa após criar o app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ou especificar domínios: ["https://sigonota.vercel.app"]
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# Configurar arquivos estáticos do frontend (se existirem)
static_dir = Path(__file__).parent / "static"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")
    
    @app.get("/")
    async def serve_frontend():
        """Servir frontend (index.html)"""
        index_file = static_dir / "index.html"
        if index_file.exists():
            return FileResponse(str(index_file))
        else:
            return {"status": "ok", "message": "Datarum API Online - Fly.io", "timestamp": datetime.now().isoformat()}
else:
    @app.get("/")
    async def root():
        """Endpoint raiz com informações da API"""
        return {"status": "ok", "message": "Datarum API Online - Fly.io", "timestamp": datetime.now().isoformat()}

# CORS configurável
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especificar domínios
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

# As rotas da API estão definidas abaixo

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
    planilha: str = Form(...),
    campos_selecionados: str = Form(None),
    opcoes: str = Form(None),
    preset: str = Form("basico")
):
    """Processa XMLs de NFe e retorna planilha Excel - Versão v1.1 com customização"""
    
    # LOGS CRÍTICOS PARA DEBUG
    print("🔥" * 80)
    print("🔥 ENDPOINT /processar CHAMADO - VERSÃO v1.1 🔥")
    print(f"🔥 Parâmetros recebidos:")
    print(f"🔥   - xmls: {len(xmls)} arquivos")
    print(f"🔥   - planilha: '{planilha}'")
    print(f"🔥   - campos_selecionados (raw): '{campos_selecionados}'")
    print(f"🔥   - opcoes (raw): '{opcoes}'")  
    print(f"🔥   - preset: '{preset}'")
    print("🔥" * 80)
    
    start_time = time.time()
    request_id = str(uuid.uuid4())[:8]
    
    logger.info(f"[{request_id}] Iniciando processamento v1.1: {len(xmls)} arquivos, planilha='{planilha}', preset='{preset}'")
    
    # Parse dos parâmetros de customização
    import json
    try:
        campos_lista = json.loads(campos_selecionados) if campos_selecionados else []
        opcoes_dict = json.loads(opcoes) if opcoes else {}
    except json.JSONDecodeError:
        logger.warning(f"[{request_id}] Erro ao processar parâmetros customização")
        campos_lista = []
        opcoes_dict = {}
    
    logger.info(f"[{request_id}] Customização: {len(campos_lista)} campos, preset='{preset}', opções={list(opcoes_dict.keys())}")
    
    # Debug detalhado v1.1
    print(f"[DEBUG main.py] campos_selecionados recebido: {campos_selecionados}")
    print(f"[DEBUG main.py] campos_lista processada: {campos_lista}")
    print(f"[DEBUG main.py] Tipo campos_lista: {type(campos_lista)}")
    print(f"[DEBUG main.py] Tamanho campos_lista: {len(campos_lista)}")
    if campos_lista:
        print(f"[DEBUG main.py] Primeiros 5 campos: {campos_lista[:5]}")
    print(f"[DEBUG main.py] Preset: {preset}")
    print(f"[DEBUG main.py] Opções: {opcoes_dict}")
    
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
        arquivos_com_erro = []
        arquivos_processados = []

        # Usar diretório temporário seguro para XMLs
        with tempfile.TemporaryDirectory() as temp_dir:
            for i, xml in enumerate(xmls):
                filename = xml.filename
                
                try:
                    # Validar tipo de arquivo
                    if not filename.lower().endswith('.xml'):
                        erro_msg = f"Arquivo {filename} não é XML"
                        arquivos_com_erro.append({
                            "arquivo": filename,
                            "erro": erro_msg,
                            "tipo": "formato_invalido"
                        })
                        if not opcoes_dict.get('processarParcialmente', True):
                            logger.error(f"[{request_id}] {erro_msg}")
                            raise HTTPException(status_code=400, detail=erro_msg)
                        continue
                    
                    # Validar tamanho do arquivo
                    contents = await xml.read()
                    file_size = len(contents)
                    total_size += file_size
                    
                    # Validação SIMPLES do tamanho
                    validacao_tamanho = validar_tamanho_arquivo(file_size, config.MAX_FILE_SIZE)
                    if not validacao_tamanho["valido"]:
                        erro_msg = f"{filename}: {validacao_tamanho['erro']}"
                        arquivos_com_erro.append({
                            "arquivo": filename,
                            "erro": validacao_tamanho['erro'],
                            "tipo": "tamanho_excedido",
                            "tamanho_mb": round(file_size / (1024*1024), 2)
                        })
                        if not opcoes_dict.get('processarParcialmente', True):
                            logger.error(f"[{request_id}] {erro_msg}")
                            raise HTTPException(status_code=400, detail=erro_msg)
                        continue
                    
                    # Validação SIMPLES do XML NFe
                    validacao_xml = validar_xml_nfe(contents)
                    if not validacao_xml["valido"]:
                        erro_msg = f"{filename}: {validacao_xml['erro']}"
                        arquivos_com_erro.append({
                            "arquivo": filename,
                            "erro": validacao_xml['erro'],
                            "tipo": "xml_invalido"
                        })
                        if not opcoes_dict.get('processarParcialmente', True):
                            logger.error(f"[{request_id}] {erro_msg}")
                            raise HTTPException(status_code=400, detail=erro_msg)
                        continue
                    
                    # Log dos dados básicos encontrados
                    dados = validacao_xml["dados"]
                    itens_count = contar_itens_xml(contents)
                    logger.info(f"[{request_id}] Processando {filename}: NFe {dados.get('numero', 'N/A')} ({itens_count} itens)")
                    
                    # Criar arquivo temporário seguro
                    temp_file = Path(temp_dir) / f"{request_id}_{i}_{uuid.uuid4().hex[:8]}.xml"
                    temp_file.write_bytes(contents)
                    
                    try:
                        # Processar XML com campos customizados
                        xml_start = time.time()
                        # Ler o conteúdo do arquivo para passar para parse_nfe
                        xml_content = temp_file.read_text(encoding='utf-8')
                        itens = parse_nfe(xml_content, campos_selecionados=campos_lista)
                        xml_time = time.time() - xml_start
                        
                        todos_itens.extend(itens)
                        arquivos_processados.append({
                            "arquivo": filename,
                            "itens": len(itens),
                            "tempo": xml_time,
                            "nfe_numero": dados.get('numero', 'N/A')
                        })
                        logger.info(f"[{request_id}] Processado {filename}: {len(itens)} itens em {xml_time:.2f}s")
                        
                    except Exception as e:
                        erro_msg = f"Erro ao processar {filename}: {str(e)}"
                        arquivos_com_erro.append({
                            "arquivo": filename,
                            "erro": str(e),
                            "tipo": "erro_processamento"
                        })
                        if not opcoes_dict.get('processarParcialmente', True):
                            logger.error(f"[{request_id}] {erro_msg}")
                            raise HTTPException(status_code=400, detail=erro_msg)
                        logger.warning(f"[{request_id}] {erro_msg} (continuando processamento)")
                        
                except Exception as e:
                    erro_msg = f"Erro inesperado com {filename}: {str(e)}"
                    arquivos_com_erro.append({
                        "arquivo": filename,
                        "erro": str(e),
                        "tipo": "erro_inesperado"
                    })
                    if not opcoes_dict.get('processarParcialmente', True):
                        logger.error(f"[{request_id}] {erro_msg}")
                        raise HTTPException(status_code=400, detail=erro_msg)
                    logger.warning(f"[{request_id}] {erro_msg} (continuando processamento)")

        # Verificar se conseguiu processar pelo menos alguns arquivos
        if not todos_itens and arquivos_com_erro:
            logger.error(f"[{request_id}] Nenhum arquivo foi processado com sucesso")
            raise HTTPException(
                status_code=400, 
                detail=f"Nenhum arquivo foi processado. Erros: {'; '.join([e['erro'] for e in arquivos_com_erro[:3]])}"
            )

        # Gerar Excel com customizações
        logger.info(f"[{request_id}] Gerando Excel v1.1: {len(todos_itens)} itens, {len(arquivos_com_erro)} erros")
        
        # Criar arquivo temporário para Excel
        temp_excel_fd, temp_excel_path = tempfile.mkstemp(suffix='.xlsx', prefix=f'{planilha}_{request_id}_')
        os.close(temp_excel_fd)
        
        try:
            excel_start = time.time()
            
            # Configurações para o Excel handler
            configuracao_excel = {
                'campos_selecionados': campos_lista,
                'opcoes': opcoes_dict,
                'preset': preset,
                'arquivos_com_erro': arquivos_com_erro if opcoes_dict.get('incluirRelatorioErros', True) else [],
                'arquivos_processados': arquivos_processados
            }
            
            rows_saved = salvar_em_excel(todos_itens, temp_excel_path, configuracao=configuracao_excel)
            excel_time = time.time() - excel_start
            
            total_time = time.time() - start_time
            file_size = os.path.getsize(temp_excel_path)
            
            success_msg = f"Sucesso v1.1! {rows_saved} linhas, {len(arquivos_processados)} arquivos OK"
            if arquivos_com_erro:
                success_msg += f", {len(arquivos_com_erro)} com erro"
            success_msg += f", {file_size} bytes, {total_time:.2f}s total"
            
            logger.info(f"[{request_id}] {success_msg}")

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
    planilha: str = Form(...),
    campos_selecionados: str = Form(None),
    opcoes: str = Form(None),
    preset: str = Form("basico")
):
    """Retorna apenas informações sobre o processamento v1.1, sem arquivo"""
    request_id = str(uuid.uuid4())[:8]
    logger.info(f"[{request_id}] Gerando info v1.1 para {len(xmls)} arquivos")
    
    # Parse dos parâmetros
    import json
    try:
        campos_lista = json.loads(campos_selecionados) if campos_selecionados else []
        opcoes_dict = json.loads(opcoes) if opcoes else {}
    except json.JSONDecodeError:
        campos_lista = []
        opcoes_dict = {}
    
    todos_itens = []
    arquivos_com_erro = []

    # Usar diretório temporário seguro
    with tempfile.TemporaryDirectory() as temp_dir:
        for i, xml in enumerate(xmls):
            try:
                contents = await xml.read()
                
                # Validação básica
                validacao_xml = validar_xml_nfe(contents)
                if not validacao_xml["valido"]:
                    arquivos_com_erro.append({
                        "arquivo": xml.filename,
                        "erro": validacao_xml['erro'],
                        "tipo": "xml_invalido"
                    })
                    if not opcoes_dict.get('processarParcialmente', True):
                        continue
                
                temp_file = Path(temp_dir) / f"{request_id}_{i}_{uuid.uuid4().hex[:8]}.xml"
                temp_file.write_bytes(contents)
                
                # Ler o conteúdo do arquivo para passar para parse_nfe  
                xml_content = temp_file.read_text(encoding='utf-8')
                itens = parse_nfe(xml_content, campos_selecionados=campos_lista)
                todos_itens.extend(itens)
                
            except Exception as e:
                arquivos_com_erro.append({
                    "arquivo": xml.filename,
                    "erro": str(e),
                    "tipo": "erro_processamento"
                })
                if not opcoes_dict.get('processarParcialmente', True):
                    continue

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
        "arquivos_processados": len(xmls) - len(arquivos_com_erro),
        "arquivos_com_erro": len(arquivos_com_erro),
        "notas_encontradas": numeros_nfe,
        "emitentes": emitentes,
        "versoes_nfe": versoes_nfe,
        "periodo": periodo,
        "valor_total": round(valor_total, 2) if valor_total > 0 else 0,
        "planilha_destino": f"{planilha}.xlsx",
        "customizacao": {
            "preset": preset,
            "campos_selecionados": len(campos_lista),
            "opcoes_ativas": list(k for k, v in opcoes_dict.items() if v)
        },
        "erros_resumo": arquivos_com_erro[:3] if arquivos_com_erro else []
    }

# Rota catch-all para servir frontend em qualquer path que não seja API
@app.get("/{full_path:path}")
async def serve_spa(full_path: str):
    """Servir Single Page Application (SPA) para qualquer rota que não seja API"""
    static_dir = Path(__file__).parent / "static"
    index_file = static_dir / "index.html"
    
    # Se é uma rota de API, deixar o FastAPI lidar com o 404
    if full_path.startswith("api/"):
        raise HTTPException(status_code=404, detail="API endpoint not found")
    
    # Se o arquivo estático existe, servir ele
    if static_dir.exists() and index_file.exists():
        return FileResponse(str(index_file))
    else:
        # Fallback para API info se não há frontend
        return {
            "name": "Datarum API", 
            "status": "online",
            "message": "Frontend não encontrado, apenas API disponível",
            "endpoints": {
                "processar": "POST /processar",
                "processar-info": "POST /processar-info", 
                "health": "GET /health",
                "docs": "GET /docs"
            }
        }