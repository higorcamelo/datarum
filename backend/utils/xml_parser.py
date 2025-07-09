import xmltodict
from pathlib import Path
from typing import Union, List, Dict

def parse_nfe(xml_path: Union[str, Path]) -> List[Dict]:
    """
    Extrai informações estruturadas de uma NF-e (versões 1.10, 2.00, 3.10, 4.00).
    Retorna uma lista de dicionários, um por item (det) da nota.
    """

    with open(xml_path, 'rb') as file:
        raw = file.read()
        xml_dict = xmltodict.parse(raw)

    # A nota pode estar aninhada de formas diferentes
    nfe_root = xml_dict.get("NFe") \
        or xml_dict.get("nfeProc", {}).get("NFe") \
        or xml_dict.get("nfeProc", {}).get("nfe:NFe")  # namespaces

    if not nfe_root:
        raise ValueError(f"Não foi possível identificar o conteúdo da NF-e em: {xml_path}")

    inf_nfe = nfe_root.get("infNFe") or nfe_root.get("nfe:infNFe")

    # Acessos seguros com fallback
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

    return resultado


