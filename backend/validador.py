import xmltodict
import logging

logger = logging.getLogger(__name__)

def validar_xml_nfe(xml_content: bytes) -> dict:
    """
    Valida a estrutura da NFe, extrai dados básicos e conta itens em um único parse.
    """
    detalhes = {"versao": "N/A", "tipo": "desconhecido", "qtd_itens": 0}
    
    try:
        # 1. Decodificação Robusta
        try:
            xml_str = xml_content.decode('utf-8')
        except UnicodeDecodeError:
            xml_str = xml_content.decode('latin-1', errors='ignore')

        # 2. Segurança (Proteção XXE)
        upper = xml_str.upper()
        if '<!DOCTYPE' in upper or '<!ENTITY' in upper:
            return {"valido": False, "erro": "XML recusado: contém declarações externas perigosas", "dados": {}}

        # 3. Parse Único
        dados_xml = xmltodict.parse(xml_str)
        
        # 4. Localização da Raiz da NFe
        if 'nfeProc' in dados_xml:
            infNFe = dados_xml['nfeProc'].get('NFe', {}).get('infNFe', {})
            detalhes["tipo"] = "nfeProc"
        elif 'NFe' in dados_xml:
            infNFe = dados_xml['NFe'].get('infNFe', {})
            detalhes["tipo"] = "NFe"
        else:
            return {"valido": False, "erro": "Estrutura NFe não encontrada", "dados": {}}

        # 5. Extração de Dados Obrigatórios
        ide = infNFe.get('ide', {})
        emit = infNFe.get('emit', {})
        total = infNFe.get('total', {}).get('ICMSTot', {})
        
        numero_nf = ide.get('nNF')
        emitente = emit.get('xNome')

        if not numero_nf or not emitente:
            return {"valido": False, "erro": "Campos obrigatórios (nNF/xNome) ausentes", "dados": {}}

        # 6. Contagem de Itens (Otimizada: aproveita o parse já feito)
        det = infNFe.get('det', [])
        qtd_itens = len(det) if isinstance(det, list) else (1 if det else 0)
        detalhes["qtd_itens"] = qtd_itens

        dados_basicos = {
            "numero": numero_nf,
            "emitente": emitente,
            "valor_total": total.get('vNF', '0'),
            "data_emissao": ide.get('dhEmi', ide.get('dEmi', 'N/A')),
            "versao": infNFe.get('@versao', 'N/A'),
            "qtd_itens": qtd_itens
        }

        return {
            "valido": True,
            "erro": "",
            "dados": dados_basicos,
            "detalhes": detalhes
        }
        
    except Exception as e:
        return {"valido": False, "erro": f"Erro técnico no XML: {str(e)[:50]}", "dados": {}}

def validar_tamanho_arquivo(tamanho_bytes: int, max_mb: int = 5) -> dict:
    max_bytes = max_mb * 1024 * 1024
    if tamanho_bytes > max_bytes:
        return {"valido": False, "erro": f"Arquivo excede {max_mb}MB"}
    return {"valido": True, "erro": ""}