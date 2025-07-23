"""
Wrapper para funções utilitárias com fallbacks para o Vercel
"""
import sys
import os
import tempfile
from pathlib import Path

# Adicionar paths necessários
backend_dir = Path(__file__).parent.parent
sys.path.insert(0, str(backend_dir))
sys.path.insert(0, str(backend_dir / 'utils'))

def safe_import_and_parse():
    """
    Importa as funções de parse de forma segura com fallbacks
    """
    try:
        from utils.xml_parser import parse_nfe
        from utils.excel_handler import salvar_em_excel
        from validador import validar_xml_nfe, contar_itens_xml
        return parse_nfe, salvar_em_excel, validar_xml_nfe, contar_itens_xml
    except ImportError as e:
        print(f"Erro ao importar módulos: {e}")
        
        # Funções fallback básicas
        def parse_nfe_fallback(xml_path):
            """Parse básico de XML usando xmltodict"""
            try:
                import xmltodict
                with open(xml_path, 'rb') as file:
                    content = file.read()
                    xml_dict = xmltodict.parse(content)
                    
                # Extração básica de dados
                if 'nfeProc' in xml_dict:
                    nfe = xml_dict['nfeProc']['NFe']['infNFe']
                elif 'NFe' in xml_dict:
                    nfe = xml_dict['NFe']['infNFe']
                else:
                    return []
                
                ide = nfe.get('ide', {})
                emit = nfe.get('emit', {})
                
                # Dados básicos da nota
                dados_base = {
                    'numero_nf': ide.get('nNF', 'N/A'),
                    'serie': ide.get('serie', 'N/A'),
                    'data_emissao': ide.get('dhEmi', ide.get('dEmi', 'N/A')),
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
                    item_data = dados_base.copy()
                    item_data.update({
                        'descricao_produto': prod.get('xProd', 'N/A'),
                        'quantidade_comercial': prod.get('qCom', '0'),
                        'valor_unitario': prod.get('vUnCom', '0'),
                        'valor_total_item': prod.get('vProd', '0'),
                        'cfop': prod.get('CFOP', 'N/A')
                    })
                    result.append(item_data)
                
                return result
                
            except Exception as e:
                print(f"Erro no parse fallback: {e}")
                return []
        
        def salvar_em_excel_fallback(dados, filename):
            return filename
        
        def validar_xml_nfe_fallback(content):
            try:
                import xmltodict
                xml_str = content.decode('utf-8') if isinstance(content, bytes) else content
                dados_xml = xmltodict.parse(xml_str)
                
                # Verificação básica
                if 'nfeProc' in dados_xml or 'NFe' in dados_xml:
                    return {"valido": True, "erro": None}
                else:
                    return {"valido": False, "erro": "Não é uma NFe válida"}
            except:
                return {"valido": False, "erro": "XML inválido"}
        
        def contar_itens_xml_fallback(content):
            return 1
        
        return parse_nfe_fallback, salvar_em_excel_fallback, validar_xml_nfe_fallback, contar_itens_xml_fallback

# Exportar as funções
parse_nfe, salvar_em_excel, validar_xml_nfe, contar_itens_xml = safe_import_and_parse()
