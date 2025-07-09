import pandas as pd
from pathlib import Path

def salvar_em_excel(dados: list[dict], caminho_planilha: str):
    """
    Salva os dados extraídos no final da planilha existente.
    Se a planilha não existir, cria com os dados.
    """
    caminho = Path(caminho_planilha)
    df_novos = pd.DataFrame(dados)

    renomear = {
        "numero_nf": "Nº NF",
        "serie": "Série",
        "data_emissao": "Data de Emissão",
        "modelo": "Modelo",
        "tipo_operacao": "Tipo Op.",
        "finalidade": "Finalidade",
        "natureza_operacao": "Natureza da Operação",
        "cnpj_emitente": "CNPJ Emitente",
        "emitente": "Emitente",
        "municipio_emitente": "Cidade Emitente",
        "uf_emitente": "UF Emitente",
        "cnpj_destinatario": "CNPJ Destinatário",
        "destinatario": "Destinatário",
        "municipio_dest": "Cidade Destinatário",
        "uf_dest": "UF Destinatário",
        "valor_total_nf": "Total NF",
        "valor_produtos": "Total Produtos",
        "valor_icms": "Valor ICMS",
        "valor_pis": "Valor PIS",
        "valor_cofins": "Valor COFINS",
        "transportadora": "Transportadora",
        "placa_veiculo": "Placa Veículo",
        "codigo_produto": "Código Produto",
        "descricao_produto": "Produto",
        "cfop": "CFOP",
        "quantidade_comercial": "Quantidade",
        "unidade_comercial": "Unidade",
        "valor_unitario": "Valor Unitário",
        "valor_total_item": "Total Item",
        "icms_valor": "ICMS Item",
        "pis_valor": "PIS Item",
        "cofins_valor": "COFINS Item"
    }

    df_novos.rename(columns=renomear, inplace=True)

    # Conversões seguras
    for col in [
        "Quantidade", "Valor Unitário", "Total Item",
        "Total NF", "Total Produtos", "Valor ICMS", "Valor PIS", "Valor COFINS"
    ]:
        if col in df_novos.columns:
            df_novos[col] = pd.to_numeric(df_novos[col], errors="coerce")

    if caminho.exists():
        df_existente = pd.read_excel(caminho)
        df_final = pd.concat([df_existente, df_novos], ignore_index=True)
    else:
        df_final = df_novos

    df_final.to_excel(caminho, index=False)
    return len(df_novos)
