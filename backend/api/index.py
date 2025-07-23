from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse, Response
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import tempfile
import os
import sys
from datetime import datetime

# Adicionar o diretório backend ao path para importar utils
backend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)))
if backend_path not in sys.path:
    sys.path.append(backend_path)

from utils.xml_parser import validate_nfe_version
from utils.excel_handler import salvar_em_excel
import xmltodict

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def processar_xml(content: bytes):
    """Processa um arquivo XML de NFe usando o parser do utils"""
    try:
        xml_dict = xmltodict.parse(content.decode('utf-8'))
        
        # Validar NFe usando a função do utils
        validacao = validate_nfe_version(xml_dict)
        if not validacao["valid"]:
            return [{
                'numero_nf': 'ERRO',
                'data_emissao': '2025-01-01',
                'emitente': f'NFe inválida: {validacao["error"]}',
                'erro': validacao["error"]
            }]
        
        # A nota pode estar aninhada de formas diferentes
        nfe_root = xml_dict.get("NFe") \
            or xml_dict.get("nfeProc", {}).get("NFe") \
            or xml_dict.get("nfeProc", {}).get("nfe:NFe")

        if not nfe_root:
            return [{
                'numero_nf': 'ERRO',
                'data_emissao': '2025-01-01',
                'emitente': 'Estrutura NFe não encontrada',
                'erro': 'Estrutura NFe não encontrada'
            }]

        inf_nfe = nfe_root.get("infNFe") or nfe_root.get("nfe:infNFe")

        # Função auxiliar para acessos seguros
        def g(dic, path, default=""):
            for p in path.split("."):
                dic = dic.get(p, {})
            return dic or default

        # Dados do cabeçalho
        ide = inf_nfe.get("ide", {})
        emit = inf_nfe.get("emit", {})
        dest = inf_nfe.get("dest", {})
        total = inf_nfe.get("total", {}).get("ICMSTot", {})
        transp = inf_nfe.get("transp", {})

        dados_comuns = {
            "numero_nf": g(ide, "nNF"),
            "serie": g(ide, "serie"),
            "data_emissao": g(ide, "dEmi") or g(ide, "dhEmi", "")[:10],
            "modelo": g(ide, "mod"),
            "tipo_operacao": g(ide, "tpNF"),
            "finalidade": g(ide, "finNFe"),
            "natureza_operacao": g(ide, "natOp"),
            "versao_nfe": validacao["version"],

            "cnpj_emitente": g(emit, "CNPJ"),
            "emitente": g(emit, "xNome"),
            "municipio_emitente": g(emit, "enderEmit.xMun"),
            "uf_emitente": g(emit, "enderEmit.UF"),

            "cnpj_destinatario": g(dest, "CNPJ"),
            "destinatario": g(dest, "xNome"),
            "municipio_dest": g(dest, "enderDest.xMun"),
            "uf_dest": g(dest, "enderDest.UF"),

            "valor_total_nf": g(total, "vNF"),
            "valor_produtos": g(total, "vProd"),
            "valor_icms": g(total, "vICMS"),
            "valor_pis": g(total, "vPIS"),
            "valor_cofins": g(total, "vCOFINS"),

            "transportadora": g(transp, "transporta.xNome"),
            "placa_veiculo": g(transp, "veicTransp.placa"),
        }

        # Produtos
        itens = inf_nfe.get("det", [])
        if isinstance(itens, dict):  # caso haja apenas 1 item
            itens = [itens]

        resultado = []
        for item in itens:
            prod = item.get("prod", {})
            imposto = item.get("imposto", {})

            icms = next(iter(imposto.get("ICMS", {}).values()), {})
            pis = next(iter(imposto.get("PIS", {}).values()), {})
            cofins = next(iter(imposto.get("COFINS", {}).values()), {})

            item_extraido = {
                **dados_comuns,
                "codigo_produto": prod.get("cProd", ""),
                "descricao_produto": prod.get("xProd", ""),
                "cfop": prod.get("CFOP", ""),
                "quantidade_comercial": prod.get("qCom", ""),
                "unidade_comercial": prod.get("uCom", ""),
                "valor_unitario": prod.get("vUnCom", ""),
                "valor_total_item": prod.get("vProd", ""),

                "icms_valor": icms.get("vICMS", ""),
                "pis_valor": pis.get("vPIS", ""),
                "cofins_valor": cofins.get("vCOFINS", "")
            }

            resultado.append(item_extraido)

        return resultado or [dados_comuns]
        
    except Exception as e:
        return [{
            'numero_nf': 'ERRO',
            'data_emissao': '2025-01-01',
            'emitente': f'Erro: {str(e)[:50]}',
            'erro': str(e)
        }]

@app.get("/")
async def root():
    return {
        "status": "ok", 
        "message": "Datarum API Online", 
        "timestamp": datetime.now().isoformat()
    }

@app.post("/processar-info")
async def processar_info(files: List[UploadFile] = File(...)):
    try:
        todos_dados = []
        stats = {'processados': 0, 'itens': 0, 'notas': [], 'emitentes': set(), 'valor_total': 0.0}
        
        for file in files:
            if file.filename and file.filename.lower().endswith('.xml'):
                content = await file.read()
                dados_nfe = processar_xml(content)
                if dados_nfe:
                    todos_dados.extend(dados_nfe)
                    stats['processados'] += 1
                    stats['itens'] += len(dados_nfe)
                    
                    for item in dados_nfe:
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
        
        return JSONResponse(content={
            'message': 'Processamento concluído!',
            'arquivos_processados': stats['processados'],
            'itens_processados': stats['itens'],
            'notas_encontradas': list(stats['notas'])[:10],
            'emitentes': list(stats['emitentes'])[:10],
            'valor_total': round(stats['valor_total'], 2),
            'session_id': f"session_{stats['processados']}",
            'planilha_destino': 'datarum_processamento.xlsx',
            'dados': todos_dados  # Incluir dados na resposta para usar no próximo endpoint
        })
        
    except Exception as e:
        return JSONResponse(content={'message': f'Erro: {str(e)}', 'erro': True}, status_code=500)

@app.post("/processar")
async def processar_excel(files: List[UploadFile] = File(...)):
    try:
        todos_dados = []
        
        for file in files:
            if file.filename and file.filename.lower().endswith('.xml'):
                content = await file.read()
                dados_nfe = processar_xml(content)
                if dados_nfe:
                    todos_dados.extend(dados_nfe)
        
        if not todos_dados:
            raise HTTPException(status_code=400, detail="Nenhum arquivo XML válido encontrado")
        
        # Criar arquivo temporário
        with tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx') as tmp_file:
            tmp_path = tmp_file.name
        
        # Usar a função do utils para salvar em Excel
        num_linhas = salvar_em_excel(todos_dados, tmp_path)
        
        # Ler arquivo Excel
        with open(tmp_path, 'rb') as f:
            excel_content = f.read()
        
        # Limpar arquivo temporário
        os.unlink(tmp_path)
        
        return Response(
            content=excel_content,
            media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            headers={'Content-Disposition': 'attachment; filename=datarum_processamento.xlsx'}
        )
        
    except Exception as e:
        # Em caso de erro, retornar CSV de erro
        error_csv = f'Erro,{str(e)}\nContate o suporte,suporte@datarum.com.br'
        return Response(
            content=error_csv.encode('utf-8'),
            media_type='text/csv; charset=utf-8',
            headers={'Content-Disposition': 'attachment; filename=datarum_erro.csv'}
        )

# Handler para Vercel
from mangum import Mangum
handler = Mangum(app)
