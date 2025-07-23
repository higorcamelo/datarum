"""
API Principal para Vercel - Estrutura Corrigida
"""
import sys
import os
from pathlib import Path

# Configurar paths
current_dir = Path(__file__).parent
backend_dir = current_dir.parent
sys.path.insert(0, str(backend_dir))
sys.path.insert(0, str(backend_dir / 'utils'))

import tempfile
import logging
from datetime import datetime
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("datarum")

# Função para carregar processadores de XML
def get_xml_processors():
    """Carrega processadores de XML com fallbacks"""
    try:
        # Tentar importar módulos originais
        from utils.xml_parser import parse_nfe
        from validador import validar_xml_nfe
        logger.info("✅ Módulos originais carregados")
        return parse_nfe, validar_xml_nfe
    except ImportError as e:
        logger.warning(f"⚠️ Usando fallbacks: {e}")
        
        def parse_nfe_simple(xml_path):
            """Parser simples usando xmltodict"""
            try:
                import xmltodict
                with open(xml_path, 'rb') as f:
                    data = xmltodict.parse(f.read())
                
                # Encontrar NFe
                if 'nfeProc' in data:
                    nfe = data['nfeProc']['NFe']['infNFe']
                elif 'NFe' in data:
                    nfe = data['NFe']['infNFe']
                else:
                    return []
                
                ide = nfe.get('ide', {})
                emit = nfe.get('emit', {})
                
                base_data = {
                    'numero_nf': ide.get('nNF', 'N/A'),
                    'serie': ide.get('serie', '1'),
                    'data_emissao': ide.get('dhEmi', ide.get('dEmi', datetime.now().strftime('%Y-%m-%d'))),
                    'emitente': emit.get('xNome', 'N/A'),
                    'cnpj_emitente': emit.get('CNPJ', 'N/A'),
                    'versao_nfe': nfe.get('@versao', '4.00')
                }
                
                # Processar itens
                det = nfe.get('det', [])
                if not isinstance(det, list):
                    det = [det]
                
                result = []
                for item in det:
                    prod = item.get('prod', {})
                    item_data = base_data.copy()
                    item_data.update({
                        'descricao_produto': prod.get('xProd', 'Produto'),
                        'quantidade_comercial': prod.get('qCom', '1'),
                        'valor_unitario': prod.get('vUnCom', '0'),
                        'valor_total_item': prod.get('vProd', '0'),
                        'cfop': prod.get('CFOP', '5102')
                    })
                    result.append(item_data)
                
                return result or [base_data]
                
            except Exception as e:
                logger.error(f"Erro no parser: {e}")
                return [{
                    'numero_nf': 'ERRO',
                    'serie': '1',
                    'data_emissao': datetime.now().strftime('%Y-%m-%d'),
                    'emitente': 'Erro no processamento',
                    'descricao_produto': f'Erro: {str(e)[:100]}',
                    'erro': str(e)
                }]
        
        def validar_xml_simple(content):
            """Validador simples"""
            try:
                import xmltodict
                xml_str = content.decode('utf-8') if isinstance(content, bytes) else content
                data = xmltodict.parse(xml_str)
                valid = 'nfeProc' in data or 'NFe' in data
                return {"valido": valid, "erro": None if valid else "Não é NFe"}
            except Exception as e:
                return {"valido": False, "erro": f"XML inválido: {str(e)}"}
        
        return parse_nfe_simple, validar_xml_simple

# Carregar funções
parse_nfe, validar_xml_nfe = get_xml_processors()

# Criar FastAPI app
app = FastAPI(
    title="Datarum API",
    description="API para processamento de NFe XML",
    version="1.0.0"
)

# CORS para www.datarum.com.br
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://www.datarum.com.br",
        "https://datarum.com.br",
        "http://localhost:5173",
        "http://localhost:3000",
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cache simples
cache = {}

@app.get("/")
def root():
    """Endpoint raiz"""
    return {
        "message": "🚀 Datarum API Online",
        "status": "ok",
        "timestamp": datetime.now().isoformat(),
        "endpoints": ["/api/processar-info", "/api/processar"]
    }

@app.post("/processar-info")
async def processar_info(files: List[UploadFile] = File(...)):
    """Processa XMLs e retorna informações"""
    try:
        resultados = []
        stats = {
            'processados': 0,
            'itens': 0,
            'notas': [],
            'emitentes': set(),
            'valor_total': 0.0
        }
        
        for file in files:
            if not file.filename.lower().endswith('.xml'):
                continue
                
            try:
                content = await file.read()
                
                # Validar
                validacao = validar_xml_nfe(content)
                if not validacao.get('valido', False):
                    continue
                
                # Processar
                with tempfile.NamedTemporaryFile(suffix='.xml', delete=False) as tmp:
                    tmp.write(content)
                    tmp_path = tmp.name
                
                try:
                    dados = parse_nfe(tmp_path)
                    if dados:
                        resultados.extend(dados)
                        stats['processados'] += 1
                        stats['itens'] += len(dados)
                        
                        for item in dados:
                            if item.get('numero_nf'):
                                stats['notas'].append(item['numero_nf'])
                            if item.get('emitente'):
                                stats['emitentes'].add(item['emitente'])
                            if item.get('valor_total_item'):
                                try:
                                    valor = float(str(item['valor_total_item']).replace(',', '.'))
                                    stats['valor_total'] += valor
                                except:
                                    pass
                finally:
                    try:
                        os.unlink(tmp_path)
                    except:
                        pass
                        
            except Exception as e:
                logger.error(f"Erro processando {file.filename}: {e}")
                continue
        
        # Salvar no cache
        session_id = f"session_{len(resultados)}_{int(stats['valor_total'])}"
        cache[session_id] = resultados
        
        return {
            'message': '✅ Processamento concluído',
            'arquivos_processados': stats['processados'],
            'itens_processados': stats['itens'],
            'notas_encontradas': list(stats['notas'])[:10],
            'emitentes': list(stats['emitentes'])[:10],
            'valor_total': round(stats['valor_total'], 2),
            'session_id': session_id,
            'planilha_destino': 'datarum_processamento.csv'
        }
        
    except Exception as e:
        logger.error(f"Erro geral: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/processar")
async def processar_download():
    """Gera e retorna CSV"""
    try:
        # Buscar dados do cache
        dados = []
        if cache:
            latest_session = list(cache.keys())[-1]
            dados = cache[latest_session]
        
        if not dados:
            # Dados de exemplo
            dados = [{
                'numero_nf': '123456',
                'serie': '1',
                'data_emissao': datetime.now().strftime('%Y-%m-%d'),
                'emitente': 'Empresa Exemplo Ltda',
                'cnpj_emitente': '12.345.678/0001-00',
                'descricao_produto': 'Produto de Exemplo',
                'quantidade_comercial': '10',
                'valor_unitario': '100.00',
                'valor_total_item': '1000.00',
                'cfop': '5102'
            }]
        
        # Gerar CSV
        csv_lines = []
        if dados:
            # Headers
            headers = [
                'Nº NF', 'Série', 'Data Emissão', 'Emitente', 'CNPJ Emitente',
                'Produto', 'Quantidade', 'Valor Unitário', 'Total Item', 'CFOP'
            ]
            csv_lines.append(','.join(headers))
            
            # Dados
            for item in dados:
                row = [
                    str(item.get('numero_nf', '')),
                    str(item.get('serie', '')),
                    str(item.get('data_emissao', '')),
                    str(item.get('emitente', '')).replace(',', ';'),
                    str(item.get('cnpj_emitente', '')),
                    str(item.get('descricao_produto', '')).replace(',', ';'),
                    str(item.get('quantidade_comercial', '')),
                    str(item.get('valor_unitario', '')),
                    str(item.get('valor_total_item', '')),
                    str(item.get('cfop', ''))
                ]
                csv_lines.append(','.join(f'"{cell}"' for cell in row))
        
        csv_content = '\n'.join(csv_lines)
        
        # Criar arquivo temporário
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv', encoding='utf-8-sig') as tmp:
            tmp.write(csv_content)
            tmp_path = tmp.name
        
        return FileResponse(
            path=tmp_path,
            filename="datarum_processamento.csv",
            media_type='text/csv; charset=utf-8'
        )
        
    except Exception as e:
        logger.error(f"Erro no download: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# Para Vercel - exportar o app diretamente
def handler(request):
    return app

# Também exportar como app para compatibilidade
app_handler = app
