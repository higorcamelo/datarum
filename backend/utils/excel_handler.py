import pandas as pd
import os
from pathlib import Path
from typing import Dict, List, Any

def salvar_em_excel(dados: list[dict], caminho_planilha: str, configuracao: Dict[str, Any] = None):
    """
    Salva os dados extraídos em uma nova planilha Excel v1.1 com opções avançadas.
    
    Args:
        dados: Lista de dicionários com os dados extraídos
        caminho_planilha: Caminho onde salvar a planilha
        configuracao: Configurações de customização (campos, opções, etc.)
    """
    if not dados:
        return 0
    
    config = configuracao or {}
    campos_selecionados = config.get('campos_selecionados', [])
    opcoes = config.get('opcoes', {})
    preset = config.get('preset', 'basico')
    arquivos_com_erro = config.get('arquivos_com_erro', [])
    arquivos_processados = config.get('arquivos_processados', [])
    
    caminho = Path(caminho_planilha)
    df_novos = pd.DataFrame(dados)

    # Renomear colunas (código original + novos campos)
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
        "cofins_valor": "COFINS Item",
        # Novos campos v1.1
        "chave_nfe": "Chave NFe",
        "regime_tributario": "Regime Trib.",
        "ncm": "NCM",
        "cst_icms": "CST ICMS",
        "base_icms": "Base ICMS",
        "aliquota_icms": "Aliq. ICMS",
        "aliquota_ipi": "Aliq. IPI",
        "valor_ipi": "IPI",
        "aliquota_pis": "Aliq. PIS",
        "aliquota_cofins": "Aliq. COFINS"
    }

    # Renomear apenas as colunas que existem
    renomear_existentes = {k: v for k, v in renomear.items() if k in df_novos.columns}
    df_novos.rename(columns=renomear_existentes, inplace=True)

    # Formatação de valores monetários (2 casas decimais)
    colunas_monetarias = [
        "Valor Unitário", "Total Item", "Total NF", "Total Produtos", 
        "Valor ICMS", "Valor PIS", "Valor COFINS", "ICMS Item", "PIS Item", "COFINS Item",
        "Base ICMS", "IPI"
    ]
    for col in colunas_monetarias:
        if col in df_novos.columns:
            df_novos[col] = pd.to_numeric(df_novos[col], errors="coerce").round(2)
    
    # Formatação de percentuais
    colunas_percentuais = ["Aliq. ICMS", "Aliq. IPI", "Aliq. PIS", "Aliq. COFINS"]
    for col in colunas_percentuais:
        if col in df_novos.columns:
            df_novos[col] = pd.to_numeric(df_novos[col], errors="coerce").round(2)
    
    # Formatação de quantidades (3 casas decimais)
    if "Quantidade" in df_novos.columns:
        df_novos["Quantidade"] = pd.to_numeric(df_novos["Quantidade"], errors="coerce").round(3)

    # Formatação de datas
    if "Data de Emissão" in df_novos.columns:
        df_novos["Data de Emissão"] = pd.to_datetime(df_novos["Data de Emissão"], errors="coerce").dt.date

    # Ordenar colunas - se campos específicos foram selecionados, manter a ordem
    if campos_selecionados:
        # Usar ordem baseada nos campos selecionados
        colunas_ordenadas = []
        for campo in campos_selecionados:
            if campo in renomear:
                nome_amigavel = renomear[campo]
                if nome_amigavel in df_novos.columns:
                    colunas_ordenadas.append(nome_amigavel)
        
        # Adicionar colunas que não estavam nos selecionados (caso existam)
        for col in df_novos.columns:
            if col not in colunas_ordenadas:
                colunas_ordenadas.append(col)
        
        df_final = df_novos[colunas_ordenadas]
    else:
        # Ordem padrão (código original)
        ordem_padrao = [
            "Nº NF", "Série", "Data de Emissão", "Modelo", "Versão NFe", "Tipo Op.", "Finalidade", "Natureza da Operação",
            "CNPJ Emitente", "Emitente", "Cidade Emitente", "UF Emitente", "Regime Trib.",
            "CNPJ Destinatário", "Destinatário", "Cidade Destinatário", "UF Destinatário",
            "Código Produto", "Produto", "NCM", "CFOP", "Quantidade", "Unidade", "Valor Unitário", "Total Item",
            "Total Produtos", "Total NF",
            "Valor ICMS", "Valor PIS", "Valor COFINS",
            "ICMS Item", "PIS Item", "COFINS Item", "IPI",
            "CST ICMS", "Base ICMS", "Aliq. ICMS", "Aliq. IPI", "Aliq. PIS", "Aliq. COFINS",
            "Chave NFe", "Transportadora", "Placa Veículo"
        ]
        colunas_finais = [col for col in ordem_padrao if col in df_novos.columns]
        df_final = df_novos[colunas_finais]

    # Configurar o caminho de escrita (código original)
    if os.getenv('VERCEL_ENV') or os.getenv('VERCEL') or os.getenv('ENVIRONMENT') == 'production':
        if not str(caminho).startswith('/tmp'):
            caminho = Path('/tmp') / caminho.name
    else:
        caminho.parent.mkdir(parents=True, exist_ok=True)
    
    # Criar o Excel - versão simplificada
    with pd.ExcelWriter(caminho, engine='openpyxl') as writer:
        # Aba principal
        nome_aba = f"Dados ({preset})" if preset != 'basico' else "Dados"
        df_final.to_excel(writer, sheet_name=nome_aba, index=False)
        
        # Opções adicionais se solicitadas
        if opcoes.get('incluirTotais', False):
            _adicionar_linha_totais(writer, df_final, nome_aba)
        
        if opcoes.get('incluirResumo', False):
            _criar_aba_resumo(writer, dados, arquivos_processados, campos_selecionados, preset)
        
        if opcoes.get('agruparPorEmitente', False):
            _criar_agrupamento_emitente(writer, df_final)
    
    return len(df_novos)


def _adicionar_linha_totais(writer, df_final, nome_aba):
    """Adiciona linha de totais na aba principal"""
    try:
        # Identificar colunas numéricas para somar
        colunas_numericas = []
        for col in df_final.columns:
            if df_final[col].dtype in ['float64', 'int64'] and any(palavra in col for palavra in ['Valor', 'Total', 'ICMS', 'PIS', 'COFINS', 'IPI']):
                colunas_numericas.append(col)
        
        if colunas_numericas:
            # Criar linha de totais
            linha_totais = pd.Series(index=df_final.columns, dtype=object)
            linha_totais.iloc[0] = 'TOTAL:'
            
            for col in colunas_numericas:
                linha_totais[col] = df_final[col].sum()
            
            # Recriar planilha com totais
            df_com_totais = pd.concat([df_final, linha_totais.to_frame().T], ignore_index=True)
            df_com_totais.to_excel(writer, sheet_name=nome_aba, index=False)
    except Exception as e:
        print(f"Erro ao adicionar totais: {e}")


def _criar_aba_resumo(writer, dados, arquivos_processados, campos_selecionados, preset):
    """Cria aba de resumo estatístico simples"""
    try:
        resumo_data = {
            'Estatística': [
                'Total de Arquivos Processados',
                'Total de Itens Extraídos',
                'Preset Utilizado',
                'Campos Selecionados'
            ],
            'Valor': [
                len(arquivos_processados),
                len(dados),
                preset.title(),
                len(campos_selecionados) if campos_selecionados else 'Todos'
            ]
        }
        
        df_resumo = pd.DataFrame(resumo_data)
        df_resumo.to_excel(writer, sheet_name='Resumo', index=False)
    except Exception as e:
        print(f"Erro ao criar resumo: {e}")


def _criar_agrupamento_emitente(writer, df_final):
    """Cria aba com dados agrupados por emitente"""
    try:
        # Encontrar coluna do emitente
        col_emitente = None
        for col in ['Emitente', 'emitente_nome', 'emitente']:
            if col in df_final.columns:
                col_emitente = col
                break
        
        if col_emitente:
            # Criar agrupamento simples
            colunas_valor = [col for col in df_final.columns if 'Total' in col or 'Valor' in col or 'Quantidade' in col]
            
            if colunas_valor:
                agrupado = df_final.groupby(col_emitente)[colunas_valor].sum().reset_index()
                agrupado.to_excel(writer, sheet_name='Por Emitente', index=False)
    except Exception as e:
        print(f"Erro ao criar agrupamento: {e}")