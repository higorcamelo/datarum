import pandas as pd
from pathlib import Path

def salvar_em_excel(dados: list[dict], caminho_planilha: str):
    """
    Salva os dados extraídos em uma nova planilha Excel.
    Agora com ordenação e tratamento de tipos.
    """
    if not dados:
        return 0
    
    caminho = Path(caminho_planilha)
    df_novos = pd.DataFrame(dados)

    # Renomear colunas
    renomear = {
        "numero_nf": "Nº NF",
        "serie": "Série",
        "data_emissao": "Data de Emissão",
        "modelo": "Modelo",
        "versao_nfe": "Versão NFe",
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
        "transportadora": "Transportadora",
        "placa_veiculo": "Placa Veículo",
        "codigo_produto": "Código Produto",
        "descricao_produto": "Produto",
        "cfop": "CFOP",
        "quantidade_comercial": "Quantidade",
        "unidade_comercial": "Unidade",
        "valor_unitario": "Valor Unitário",
        "valor_total_item": "Total Item",
        "valor_total_nf": "Total NF",
        "valor_produtos": "Total Produtos",
        "valor_icms": "Valor ICMS",
        "valor_pis": "Valor PIS",
        "valor_cofins": "Valor COFINS",
        "icms_valor": "ICMS Item",
        "pis_valor": "PIS Item",
        "cofins_valor": "COFINS Item"
    }

    df_novos.rename(columns=renomear, inplace=True)

    # Formatação de valores monetários (2 casas decimais)
    for col in [
        "Valor Unitário", "Total Item", "Total NF", "Total Produtos", 
        "Valor ICMS", "Valor PIS", "Valor COFINS", "ICMS Item", "PIS Item", "COFINS Item"
    ]:
        if col in df_novos.columns:
            df_novos[col] = pd.to_numeric(df_novos[col], errors="coerce").round(2)
    
    # Formatação de quantidades (3 casas decimais)
    if "Quantidade" in df_novos.columns:
        df_novos["Quantidade"] = pd.to_numeric(df_novos["Quantidade"], errors="coerce").round(3)

    if "Data de Emissão" in df_novos.columns:
        df_novos["Data de Emissão"] = pd.to_datetime(df_novos["Data de Emissão"], errors="coerce").dt.date

    # Ordenar colunas por bloco lógico
    ordem = [
        "Nº NF", "Série", "Data de Emissão", "Modelo", "Versão NFe", "Tipo Op.", "Finalidade", "Natureza da Operação",
        "CNPJ Emitente", "Emitente", "Cidade Emitente", "UF Emitente",
        "CNPJ Destinatário", "Destinatário", "Cidade Destinatário", "UF Destinatário",
        "Código Produto", "Produto", "CFOP", "Quantidade", "Unidade", "Valor Unitário", "Total Item",
        "Total Produtos", "Total NF",
        "Valor ICMS", "Valor PIS", "Valor COFINS",
        "ICMS Item", "PIS Item", "COFINS Item",
        "Transportadora", "Placa Veículo"
    ]

    # Somente manter colunas que existem
    colunas_finais = [col for col in ordem if col in df_novos.columns]
    df_final = df_novos[colunas_finais]

    # Criar diretório se não existir
    caminho.parent.mkdir(parents=True, exist_ok=True)
    
    df_final.to_excel(caminho, index=False, engine='openpyxl')
    return len(df_novos)