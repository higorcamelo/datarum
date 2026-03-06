import xmltodict
from typing import List, Dict


def parse_nfe(xml_content: bytes, campos_selecionados: List[str] = None) -> List[Dict]:

    if isinstance(xml_content, str):
        xml_content = xml_content.encode("utf-8")

    try:
        xml_dict = xmltodict.parse(
            xml_content,
            process_namespaces=True,
            namespaces={
                "http://www.portalfiscal.inf.br/nfe": None
            }
        )
    except Exception as e:
        raise ValueError(f"Erro ao processar XML: {e}")

    # Identifica a raiz (suporta nfeProc ou NFe direta)
    nfe_data = (
        xml_dict.get("nfeProc", {}).get("NFe")
        or xml_dict.get("NFe")
    )

    if not nfe_data:
        raise ValueError("Estrutura NFe não encontrada.")

    inf_nfe = nfe_data.get("infNFe", {})

    # Helper seguro de navegação
    def g(dic, path, default=""):
        for p in path.split("."):
            if not isinstance(dic, dict):
                return default
            dic = dic.get(p)
            if dic is None:
                return default
        return dic

    # 1. Dados da Nota
    ide = inf_nfe.get("ide", {})
    total_geral = inf_nfe.get("total", {}).get("ICMSTot", {})

    dh = g(ide, "dhEmi")
    de = g(ide, "dEmi")

    chave = inf_nfe.get("@Id", "")
    dados_comuns = {
        "numero_nf": g(ide, "nNF"),
        "serie": g(ide, "serie"),
        "data_emissao": (dh[:10] if dh else de),
        "chave_nfe": chave.replace("NFe", "") if chave else "",
        "valor_total_nf": g(total_geral, "vNF"),
        "valor_produtos_total": g(total_geral, "vProd"),
        "valor_desconto_total": g(total_geral, "vDesc"),
        "valor_frete_total": g(total_geral, "vFrete"),
    }

    # 2. Emitente e Destinatário
    emit = inf_nfe.get("emit", {})
    dest = inf_nfe.get("dest", {})

    dados_comuns.update({
        "cnpj_emitente": g(emit, "CNPJ") or g(emit, "CPF"),
        "emitente": g(emit, "xNome"),
        "uf_emitente": g(emit, "enderEmit.UF"),
        "cnpj_destinatario": g(dest, "CNPJ") or g(dest, "CPF"),
        "destinatario": g(dest, "xNome"),
        "uf_destinatario": g(dest, "enderDest.UF"),
    })

    # 3. Itens
    detalhes = inf_nfe.get("det") or []

    if isinstance(detalhes, dict):
        detalhes = [detalhes]

    resultado = []

    for item in detalhes:
        prod = item.get("prod", {})
        imposto = item.get("imposto", {})

        # Captura ICMS interno automaticamente (ICMS00, ICMS20, ICMSSN102, etc.)
        def get_tax_inner(group):
            tag = imposto.get(group, {})
            if not isinstance(tag, dict):
                return {}
            return next(iter(tag.values()), {})

        icms = get_tax_inner("ICMS")
        ipi = get_tax_inner("IPI")
        pis = get_tax_inner("PIS")
        cofins = get_tax_inner("COFINS")

        item_completo = {
            **dados_comuns,

            # Produto
            "codigo_produto": g(prod, "cProd"),
            "descricao_produto": g(prod, "xProd"),
            "ncm": g(prod, "NCM"),
            "cfop": g(prod, "CFOP"),
            "unidade_comercial": g(prod, "uCom"),
            "quantidade_comercial": g(prod, "qCom"),
            "valor_unitario": g(prod, "vUnCom"),
            "valor_total_item": g(prod, "vProd"),
            "valor_desconto_item": g(prod, "vDesc", "0.00"),

            # ICMS
            "cst_icms": g(icms, "CST") or g(icms, "CSOSN"),
            "base_icms": g(icms, "vBC"),
            "aliquota_icms": g(icms, "pICMS"),
            "icms_valor": g(icms, "vICMS"),

            # ICMS ST
            "base_icms_st": g(icms, "vBCST"),
            "icms_st_valor": g(icms, "vICMSST"),

            # Outros impostos
            "valor_ipi": g(ipi, "vIPI"),
            "pis_valor": g(pis, "vPIS"),
            "cofins_valor": g(cofins, "vCOFINS"),
        }

        if campos_selecionados:
            resultado.append({
                k: item_completo.get(k, "")
                for k in campos_selecionados
            })
        else:
            resultado.append(item_completo)

    return resultado