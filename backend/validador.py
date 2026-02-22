"""
Validador SIMPLES para arquivos XML de NFe
"""

import xmltodict
import logging

logger = logging.getLogger(__name__)

def validar_xml_nfe(xml_content: bytes, detalhado: bool = False) -> dict:
    """
    Valida se é um XML válido de NFe e extrai dados básicos
    
    Args:
        xml_content: Conteúdo binário do XML
        detalhado: Se True, inclui mais detalhes de erro
    
    Returns:
        dict: {"valido": bool, "erro": str, "dados": dict, "detalhes": dict}
    """
    
    detalhes = {"versao": "N/A", "tipo": "desconhecido", "namespaces": []}
    
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
        
        # Detecta namespaces
        if any('xmlns' in str(key) for key in dados_xml.keys()):
            detalhes["namespaces"] = ["Namespaces detectados"]
        
        # Verifica se tem estrutura básica de NFe
        nfe_root = None
        if 'nfeProc' in dados_xml:
            nfe_root = dados_xml['nfeProc']
            detalhes["tipo"] = "NFe processada (nfeProc)"
            nfe = nfe_root.get('NFe', {}).get('infNFe', {})
        elif 'NFe' in dados_xml:
            nfe_root = dados_xml['NFe']
            detalhes["tipo"] = "NFe simples"
            nfe = nfe_root.get('infNFe', {})
        else:
            # Tentar encontrar outras possíveis estruturas
            possible_keys = [k for k in dados_xml.keys() if 'nf' in k.lower()]
            return {
                "valido": False,
                "erro": f"Estrutura NFe não encontrada. Chaves encontradas: {list(dados_xml.keys())[:3]}",
                "dados": {},
                "detalhes": detalhes
            }
        
        # Tentar identificar versão
        versao = nfe.get('@versao') or nfe.get('versao')
        if versao:
            detalhes["versao"] = versao
        
        # Extrai dados básicos para validação
        ide = nfe.get('ide', {})
        emit = nfe.get('emit', {})
        total = nfe.get('total', {})
        
        # Verificações de dados obrigatórios
        numero_nf = ide.get('nNF') or ide.get('@nNF')
        if not numero_nf:
            return {
                "valido": False,
                "erro": "Número da NFe não encontrado no campo ide/nNF",
                "dados": {},
                "detalhes": detalhes
            }
        
        emitente = emit.get('xNome')
        if not emitente:
            return {
                "valido": False,
                "erro": "Nome do emitente não encontrado no campo emit/xNome",
                "dados": {},
                "detalhes": detalhes
            }
        
        dados_basicos = {
            "numero": numero_nf,
            "serie": ide.get('serie', ide.get('@serie', 'N/A')),
            "emitente": emitente,
            "valor_total": total.get('ICMSTot', {}).get('vNF', total.get('ICMSTot', {}).get('@vNF', '0')),
            "data_emissao": ide.get('dhEmi', ide.get('dEmi', ide.get('@dhEmi', 'N/A'))),
            "versao": versao or "N/A"
        }
        
        logger.debug(f"XML validado: NFe {dados_basicos['numero']} v{dados_basicos['versao']}")
        
        return {
            "valido": True,
            "erro": "",
            "dados": dados_basicos,
            "detalhes": detalhes
        }
        
    except UnicodeDecodeError:
        return {
            "valido": False,
            "erro": "Arquivo não é um XML válido (problemas de codificação)",
            "dados": {},
            "detalhes": {"erro_tipo": "encoding", **detalhes}
        }
    except xmltodict.expat.ExpatError as e:
        return {
            "valido": False,
            "erro": f"XML malformado: {str(e)[:100]}",
            "dados": {},
            "detalhes": {"erro_tipo": "xml_malformado", **detalhes}
        }
    except Exception as e:
        return {
            "valido": False,
            "erro": f"Erro ao processar XML: {str(e)[:100]}",
            "dados": {},
            "detalhes": {"erro_tipo": "processamento", **detalhes}
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
