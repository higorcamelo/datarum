import pandas as pd
from pathlib import Path


def salvar_em_excel(dados: list[dict], caminho_planilha: str):
    """
    Salva os dados extraídos no final da planilha existente.
    Se a planilha não existir, cria com os dados.
    """
    caminho = Path(caminho_planilha)

    df_novos = pd.DataFrame(dados)

    if caminho.exists():
        df_existente = pd.read_excel(caminho)
        df_final = pd.concat([df_existente, df_novos], ignore_index=True)
    else:
        df_final = df_novos

    df_final.to_excel(caminho, index=False)
    return len(df_novos)
