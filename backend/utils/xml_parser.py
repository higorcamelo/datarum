import xmltodict
from pathlib import Path
from typing import Union, List, Dict

def validate_nfe_version(xml_dict: dict) -> dict:
    # Tentar encontrar a estrutura NFe
    nfe_root = xml_dict.get("NFe") \
        or xml_dict.get("nfeProc", {}).get("NFe") \
        or xml_dict.get("nfeProc", {}).get("nfe:NFe")
    
    if not nfe_root:
        return {
            "valid": False,
            "version": None,
            "error": "Estrutura NFe não encontrada"
        }
    
    # Tentar identificar versão pelo atributo
    inf_nfe = nfe_root.get("infNFe") or nfe_root.get("nfe:infNFe", {})
    version = inf_nfe.get("@versao") or inf_nfe.get("@versão")
    
    # Se não encontrar versão, tentar inferir pela estrutura
    if not version:
        ide = inf_nfe.get("ide", {})
        if "dhEmi" in ide:  # Data/hora de emissão (versões mais novas)
            version = "4.00"  # Provável versão 4.00
        elif "dEmi" in ide:  # Apenas data (versões antigas)
            version = "3.10"  # Provável versão 3.10 ou anterior
        else:
            version = "Desconhecida"
    
    return {
        "valid": True,
        "version": version,
        "error": None
    }

def parse_nfe(xml_content: str, campos_selecionados: List[str] = None) -> List[Dict]:
    xml_dict = xmltodict.parse(xml_content.encode('utf-8') if isinstance(xml_content, str) else xml_content)

    # Valida versão da NFe
    validacao = validate_nfe_version(xml_dict)
    if not validacao["valid"]:
        raise ValueError(f"NFe inválida: {validacao['error']}")

    # A nota pode estar aninhada de formas diferentes
    nfe_root = xml_dict.get("NFe") \
        or xml_dict.get("nfeProc", {}).get("NFe") \
        or xml_dict.get("nfeProc", {}).get("nfe:NFe")  # namespaces

    if not nfe_root:
        raise ValueError(f"Não foi possível identificar o conteúdo da NF-e")

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
        "valor_ipi": g(total, "vIPI"),
        "valor_frete": g(total, "vFrete"),
        "valor_desconto": g(total, "vDesc"),
        "valor_tributos": g(total, "vTotTrib"),
        "regime_tributario": g(emit, "CRT"),
        "info_adicional": g(inf_nfe, "infAdic.infCpl"),
        "chave_nfe": g(inf_nfe, "@Id", "").replace('NFe', ''),

        "transportadora": g(transp, "transporta.xNome"),
        "placa_veiculo": g(transp, "veicTransp.placa"),
        "data_saida": g(ide, "dSaiEnt") or g(ide, "dhSaiEnt", "")[:10],
    }

    # Produtos
    itens = inf_nfe.get("det", [])
    if isinstance(itens, dict):  # caso haja apenas 1 item
        itens = [itens]

    print(f"[DEBUG] Encontrados {len(itens)} itens para processar")

    resultado = []
    for item in itens:
        # Verificações de tipo mais robustas
        if not isinstance(item, dict):
            print(f"[DEBUG] Item inválido (não é dict): {type(item)}")
            continue
            
        prod = item.get("prod", {})
        imposto = item.get("imposto", {})
        
        # Verificar se prod é dict
        if not isinstance(prod, dict):
            print(f"[DEBUG] Produto inválido (não é dict): {type(prod)}")
            prod = {}
        
        # Verificar se imposto é dict
        if not isinstance(imposto, dict):
            print(f"[DEBUG] Imposto inválido (não é dict): {type(imposto)}")
            imposto = {}

        # Acessar impostos com verificação de tipo
        icms_dict = imposto.get("ICMS", {})
        if isinstance(icms_dict, dict) and icms_dict:
            icms = next(iter(icms_dict.values()), {})
        else:
            icms = {}
            
        ipi_dict = imposto.get("IPI", {})  
        if isinstance(ipi_dict, dict) and ipi_dict:
            ipi = next(iter(ipi_dict.values()), {})
        else:
            ipi = {}
            
        pis_dict = imposto.get("PIS", {})
        if isinstance(pis_dict, dict) and pis_dict:
            pis = next(iter(pis_dict.values()), {})
        else:
            pis = {}
            
        cofins_dict = imposto.get("COFINS", {})
        if isinstance(cofins_dict, dict) and cofins_dict:
            cofins = next(iter(cofins_dict.values()), {})
        else:
            cofins = {}

        # Dados completos do item (como era originalmente)
        item_completo = {
            **dados_comuns,
            "codigo_produto": prod.get("cProd", ""),
            "descricao_produto": prod.get("xProd", ""),
            "cfop": prod.get("CFOP", ""),
            "quantidade_comercial": prod.get("qCom", ""),
            "unidade_comercial": prod.get("uCom", ""),
            "valor_unitario": prod.get("vUnCom", ""),
            "valor_total_item": prod.get("vProd", ""),
            "ncm": prod.get("NCM", ""),

            "icms_valor": icms.get("vICMS", "") if isinstance(icms, dict) else "",
            "pis_valor": pis.get("vPIS", "") if isinstance(pis, dict) else "",
            "cofins_valor": cofins.get("vCOFINS", "") if isinstance(cofins, dict) else "",
            "cst_icms": icms.get("CST", "") if isinstance(icms, dict) else "",
            "base_icms": icms.get("vBC", "") if isinstance(icms, dict) else "",
            "aliquota_icms": icms.get("pICMS", "") if isinstance(icms, dict) else "",
            "aliquota_ipi": ipi.get("pIPI", "") if isinstance(ipi, dict) else "",
            "valor_ipi": ipi.get("vIPI", "") if isinstance(ipi, dict) else "",
            "aliquota_pis": pis.get("pPIS", "") if isinstance(pis, dict) else "",
            "aliquota_cofins": cofins.get("pCOFINS", "") if isinstance(cofins, dict) else ""
        }

        print(f"[DEBUG] Item completo tem {len(item_completo)} campos")

        # Se campos específicos foram selecionados, filtrar
        if campos_selecionados and len(campos_selecionados) > 0:
            print(f"[DEBUG] APLICANDO FILTRO! Campos solicitados: {campos_selecionados}")
            item_filtrado = {}
            for campo in campos_selecionados:
                if campo in item_completo:
                    item_filtrado[campo] = item_completo[campo]
                else:
                    print(f"[DEBUG] Campo '{campo}' não encontrado!")
            print(f"[DEBUG] Item filtrado tem {len(item_filtrado)} campos")
            resultado.append(item_filtrado)
        else:
            print("[DEBUG] SEM FILTRO - usando todos os campos")
            # Modo original - todos os campos
            resultado.append(item_completo)

    print(f"[DEBUG] Retornando {len(resultado)} itens")
    return resultado


