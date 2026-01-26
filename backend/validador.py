"""
Validador SIMPLES para arquivos XML de NFe
"""

import xmltodict
import logging

logger = logging.getLogger(__name__)

def validar_xml_nfe(xml_content: bytes) -> dict:
    """
    Valida se é um XML válido de NFe e extrai dados básicos
    
    Returns:
        dict: {"valido": bool, "erro": str, "dados": dict}
    """
    
    try:
        # Tenta fazer parse do XML
        # Segurança: rejeitar XMLs com DOCTYPE ou ENTITY (mitigar XXE)
        try:
            xml_str = xml_content.decode('utf-8', errors='ignore')
        except Exception:
            xml_str = xml_content.decode('latin-1', errors='ignore')

        upper = xml_str.upper()
        if '<!DOCTYPE' in upper or '<!ENTITY' in upper:
            return {
                "valido": False,
                "erro": "XML contém declarações DOCTYPE/ENTITY — arquivo recusado por segurança",
                "dados": {}
            }

        dados_xml = xmltodict.parse(xml_str)
        
        # Verifica se tem estrutura básica de NFe
        if 'nfeProc' in dados_xml:
            nfe = dados_xml['nfeProc']['NFe']['infNFe']
        elif 'NFe' in dados_xml:
            nfe = dados_xml['NFe']['infNFe']
        else:
            return {
                "valido": False,
                "erro": "Arquivo não é uma NFe válida",
                "dados": {}
            }
        
        # Extrai dados básicos para validação
        ide = nfe.get('ide', {})
        emit = nfe.get('emit', {})
        total = nfe.get('total', {})
        
        dados_basicos = {
            "numero": ide.get('@nNF') or ide.get('nNF', 'N/A'),
            "serie": ide.get('@serie') or ide.get('serie', 'N/A'),
            "emitente": emit.get('xNome', 'N/A'),
            "valor_total": total.get('ICMSTot', {}).get('@vNF') or total.get('ICMSTot', {}).get('vNF', '0'),
            "data_emissao": ide.get('@dhEmi') or ide.get('dhEmi', 'N/A')
        }
        
        logger.debug(f"XML validado: NFe {dados_basicos['numero']}")
        
        return {
            "valido": True,
            "erro": "",
            "dados": dados_basicos
        }
        
    except UnicodeDecodeError:
        return {
            "valido": False,
            "erro": "Arquivo não é um XML válido (encoding)",
            "dados": {}
        }
    except Exception as e:
        return {
            "valido": False,
            "erro": f"Erro ao processar XML: {str(e)[:100]}",
            "dados": {}
        }

def validar_tamanho_arquivo(tamanho_bytes: int, max_mb: int = 10) -> dict:
    """
    Valida tamanho do arquivo
    
    Returns:
        dict: {"valido": bool, "erro": str}
    """
    
    max_bytes = max_mb * 1024 * 1024
    
    if tamanho_bytes > max_bytes:
        return {
            "valido": False,
            "erro": f"Arquivo muito grande ({tamanho_bytes/1024/1024:.1f}MB). Máximo: {max_mb}MB"
        }
    
    return {"valido": True, "erro": ""}

def contar_itens_xml(xml_content: bytes) -> int:
    """
    Conta quantos itens tem na NFe (para estimativa de processamento)
    """
    
    try:
        xml_str = xml_content.decode('utf-8')
        dados_xml = xmltodict.parse(xml_str)
        
        if 'nfeProc' in dados_xml:
            nfe = dados_xml['nfeProc']['NFe']['infNFe']
        elif 'NFe' in dados_xml:
            nfe = dados_xml['NFe']['infNFe']
        else:
            return 0
            
        # Conta itens
        detalhes = nfe.get('det', [])
        if isinstance(detalhes, list):
            return len(detalhes)
        elif isinstance(detalhes, dict):
            return 1
        else:
            return 0
            
    except:
        return 0
