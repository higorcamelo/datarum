"""
Configurações específicas para Datarum v1.1
Inclui mapeamentos de campos, presets e opções avançadas
"""

# Versão da API
VERSION = "1.1.0"

# Configurações de campos disponíveis com mapeamentos
CAMPOS_DISPONIVEIS = {
    # Dados da nota
    "numero_nota": {"tipo": "texto", "categoria": "nota", "xpath": "//ide/nNF", "obrigatorio": True},
    "data_emissao": {"tipo": "data", "categoria": "nota", "xpath": "//ide/dhEmi|//ide/dEmi", "obrigatorio": True},
    "data_vencimento": {"tipo": "data", "categoria": "nota", "xpath": "//ide/dVenc", "obrigatorio": False},
    "valor_total": {"tipo": "moeda", "categoria": "nota", "xpath": "//total/ICMSTot/vNF", "obrigatorio": True},
    "natureza_operacao": {"tipo": "texto", "categoria": "nota", "xpath": "//ide/natOp", "obrigatorio": False},
    "serie": {"tipo": "numero", "categoria": "nota", "xpath": "//ide/serie", "obrigatorio": False},
    "modelo": {"tipo": "numero", "categoria": "nota", "xpath": "//ide/mod", "obrigatorio": False},
    "chave_acesso": {"tipo": "texto", "categoria": "nota", "xpath": "//infNFe/@Id", "obrigatorio": False},
    
    # Dados do emitente
    "emitente_nome": {"tipo": "texto", "categoria": "emitente", "xpath": "//emit/xNome", "obrigatorio": True},
    "emitente_cnpj": {"tipo": "cnpj", "categoria": "emitente", "xpath": "//emit/CNPJ", "obrigatorio": True},
    "emitente_inscricao": {"tipo": "texto", "categoria": "emitente", "xpath": "//emit/IE", "obrigatorio": False},
    "emitente_endereco": {"tipo": "texto", "categoria": "emitente", "xpath": "//emit/enderEmit/xLgr", "obrigatorio": False},
    "emitente_cidade": {"tipo": "texto", "categoria": "emitente", "xpath": "//emit/enderEmit/xMun", "obrigatorio": False},
    "emitente_uf": {"tipo": "texto", "categoria": "emitente", "xpath": "//emit/enderEmit/UF", "obrigatorio": False},
    "emitente_cep": {"tipo": "cep", "categoria": "emitente", "xpath": "//emit/enderEmit/CEP", "obrigatorio": False},
    "emitente_telefone": {"tipo": "texto", "categoria": "emitente", "xpath": "//emit/enderEmit/fone", "obrigatorio": False},
    
    # Dados do destinatário
    "destinatario_nome": {"tipo": "texto", "categoria": "destinatario", "xpath": "//dest/xNome", "obrigatorio": False},
    "destinatario_cpf_cnpj": {"tipo": "texto", "categoria": "destinatario", "xpath": "//dest/CPF|//dest/CNPJ", "obrigatorio": False},
    
    # Produtos e impostos
    "produto_descricao": {"tipo": "texto", "categoria": "produto", "xpath": "prod/xProd", "obrigatorio": True},
    "produto_codigo": {"tipo": "texto", "categoria": "produto", "xpath": "prod/cProd", "obrigatorio": False},
    "produto_ncm": {"tipo": "numero", "categoria": "produto", "xpath": "prod/NCM", "obrigatorio": False},
    "produto_cfop": {"tipo": "numero", "categoria": "produto", "xpath": "prod/CFOP", "obrigatorio": False},
    "produto_quantidade": {"tipo": "decimal", "categoria": "produto", "xpath": "prod/qCom", "obrigatorio": False},
    "produto_unidade": {"tipo": "texto", "categoria": "produto", "xpath": "prod/uCom", "obrigatorio": False},
    "produto_valor_unitario": {"tipo": "moeda", "categoria": "produto", "xpath": "prod/vUnCom", "obrigatorio": False},
    "produto_valor": {"tipo": "moeda", "categoria": "produto", "xpath": "prod/vProd", "obrigatorio": True},
    
    # Impostos
    "icms_base": {"tipo": "moeda", "categoria": "imposto", "xpath": "imposto/ICMS/*/vBC", "obrigatorio": False},
    "icms_aliquota": {"tipo": "percentual", "categoria": "imposto", "xpath": "imposto/ICMS/*/pICMS", "obrigatorio": False},
    "icms_valor": {"tipo": "moeda", "categoria": "imposto", "xpath": "imposto/ICMS/*/vICMS", "obrigatorio": False},
    "ipi_aliquota": {"tipo": "percentual", "categoria": "imposto", "xpath": "imposto/IPI/*/pIPI", "obrigatorio": False},
    "ipi_valor": {"tipo": "moeda", "categoria": "imposto", "xpath": "imposto/IPI/*/vIPI", "obrigatorio": False},
    "pis_aliquota": {"tipo": "percentual", "categoria": "imposto", "xpath": "imposto/PIS/*/pPIS", "obrigatorio": False},
    "pis_valor": {"tipo": "moeda", "categoria": "imposto", "xpath": "imposto/PIS/*/vPIS", "obrigatorio": False},
    "cofins_aliquota": {"tipo": "percentual", "categoria": "imposto", "xpath": "imposto/COFINS/*/pCOFINS", "obrigatorio": False},
    "cofins_valor": {"tipo": "moeda", "categoria": "imposto", "xpath": "imposto/COFINS/*/vCOFINS", "obrigatorio": False},
    
    # Campos legados para compatibilidade
    "numero_nf": {"tipo": "texto", "categoria": "nota", "xpath": "//ide/nNF", "obrigatorio": True},
    "emitente": {"tipo": "texto", "categoria": "emitente", "xpath": "//emit/xNome", "obrigatorio": True},
    "cnpj_emitente": {"tipo": "cnpj", "categoria": "emitente", "xpath": "//emit/CNPJ", "obrigatorio": True},
    "valor_total_nf": {"tipo": "moeda", "categoria": "nota", "xpath": "//total/ICMSTot/vNF", "obrigatorio": True},
    "codigo_produto": {"tipo": "texto", "categoria": "produto", "xpath": "prod/cProd", "obrigatorio": False},
    "descricao_produto": {"tipo": "texto", "categoria": "produto", "xpath": "prod/xProd", "obrigatorio": True},
    "quantidade": {"tipo": "decimal", "categoria": "produto", "xpath": "prod/qCom", "obrigatorio": False},
    "valor_unitario": {"tipo": "moeda", "categoria": "produto", "xpath": "prod/vUnCom", "obrigatorio": False},
    "valor_total_item": {"tipo": "moeda", "categoria": "produto", "xpath": "prod/vProd", "obrigatorio": True},
    "cfop": {"tipo": "numero", "categoria": "produto", "xpath": "prod/CFOP", "obrigatorio": False},
    "ncm": {"tipo": "numero", "categoria": "produto", "xpath": "prod/NCM", "obrigatorio": False},
    "cst_icms": {"tipo": "texto", "categoria": "imposto", "xpath": "imposto/ICMS/*/CST", "obrigatorio": False},
    "valor_icms": {"tipo": "moeda", "categoria": "imposto", "xpath": "imposto/ICMS/*/vICMS", "obrigatorio": False},
    "versao_nfe": {"tipo": "texto", "categoria": "nota", "valor_fixo": "4.00", "obrigatorio": False},
    "destinatario": {"tipo": "texto", "categoria": "destinatario", "xpath": "//dest/xNome", "obrigatorio": False}
}

# Presets pré-configurados
PRESETS = {
    "basico": {
        "nome": "Básico",
        "descricao": "Dados essenciais para controle básico",
        "campos": [
            "numero_nf", "data_emissao", "emitente", "cnpj_emitente", 
            "valor_total_nf", "descricao_produto", "valor_total_item"
        ],
        "opcoes": {
            "incluirTotais": True,
            "agruparPorEmitente": False,
            "incluirResumo": False
        }
    },
    "completo": {
        "nome": "Completo",
        "descricao": "Extração completa com todos os dados disponíveis",
        "campos": [
            # Dados da nota
            "numero_nf", "data_emissao", "serie", "natureza_operacao", "valor_total_nf", "chave_acesso",
            # Dados do emitente
            "emitente", "cnpj_emitente", "municipio_emitente", "uf_emitente",
            # Dados do destinatário
            "destinatario", "cnpj_destinatario", "municipio_dest", "uf_dest",
            # Produtos completos
            "descricao_produto", "codigo_produto", "ncm", "cfop", "quantidade_comercial", "unidade_comercial", "valor_unitario", "valor_total_item",
            # Impostos principais
            "icms_valor", "ipi_valor", "pis_valor", "cofins_valor"
        ],
        "opcoes": {
            "incluirTotais": True,
            "agruparPorEmitente": True,
            "incluirResumo": True
        }
    },
    "fiscal": {
        "nome": "Fiscal",
        "descricao": "Foco em dados fiscais e tributários",
        "campos": [
            "numero_nf", "data_emissao", "emitente", "cnpj_emitente", "valor_total_nf",
            "descricao_produto", "cfop", "ncm", "valor_total_item", 
            "icms_base", "icms_aliquota", "icms_valor", "ipi_aliquota", "ipi_valor", 
            "pis_aliquota", "pis_valor", "cofins_aliquota", "cofins_valor"
        ],
        "opcoes": {
            "incluirTotais": True,
            "agruparPorEmitente": True,
            "incluirResumo": False
        }
    }
}

# Opções disponíveis
OPCOES_DISPONIVEIS = {
    "incluirTotais": {
        "nome": "Incluir linha de totais",
        "descricao": "Adiciona uma linha final com soma dos valores",
        "padrao": True
    },
    "agruparPorEmitente": {
        "nome": "Agrupar por emitente",
        "descricao": "Organiza dados por fornecedor com subtotais",
        "padrao": False
    },
    "incluirResumo": {
        "nome": "Aba de resumo",
        "descricao": "Cria aba adicional com estatísticas gerais",
        "padrao": False
    }
}

# Tipos de dados e suas validações
TIPOS_DADOS = {
    "texto": {"formato": str, "validacao": None},
    "numero": {"formato": int, "validacao": "^[0-9]+$"},
    "decimal": {"formato": float, "validacao": "^[0-9]+(\.[0-9]+)?$"},
    "moeda": {"formato": float, "validacao": "^[0-9]+(\.[0-9]{1,2})?$"},
    "percentual": {"formato": float, "validacao": "^[0-9]+(\.[0-9]+)?$"},
    "data": {"formato": "date", "validacao": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$"},
    "cnpj": {"formato": str, "validacao": "^[0-9]{2}\.?[0-9]{3}\.?[0-9]{3}\/?[0-9]{4}-?[0-9]{2}$"},
    "cep": {"formato": str, "validacao": "^[0-9]{5}-?[0-9]{3}$"}
}

# Mensagens de erro customizadas
MENSAGENS_ERRO = {
    "xml_invalido": "O arquivo não é um XML válido de NFe",
    "xml_malformado": "O XML está corrompido ou malformado", 
    "tamanho_excedido": "Arquivo muito grande (máximo {max_mb}MB)",
    "formato_invalido": "Apenas arquivos .xml são aceitos",
    "campos_invalidos": "Campos selecionados contêm IDs inválidos",
    "preset_inexistente": "Preset '{preset}' não existe",
    "processamento_erro": "Erro durante o processamento do arquivo",
    "sem_dados": "Nenhum dado foi extraído dos arquivos fornecidos",
    "limite_arquivos": "Máximo {max_files} arquivos por vez",
    "versao_nfe": "Versão da NFe não suportada: {version}"
}

# Configurações de performance
PERFORMANCE = {
    "max_arquivos_batch": 200,
    "max_size_mb_arquivo": 5,
    "timeout_processamento": 300,  # 5 minutos
    "cache_xml_parsed": False,  # Não usar cache em produção para economizar memória
    "parallel_processing": False  # Processamento sequencial por segurança
}

def get_preset(nome: str) -> dict:
    """Retorna configuração de um preset específico"""
    return PRESETS.get(nome, PRESETS["basico"])

def get_campos_por_preset(nome: str) -> list:
    """Retorna lista de campos de um preset específico"""
    preset = PRESETS.get(nome, PRESETS["basico"])
    return preset.get("campos", [])

def get_campos_by_categoria(categoria: str) -> list:
    """Retorna campos de uma categoria específica"""
    return CAMPOS_DISPONIVEIS.get(categoria, [])

def get_todos_campos() -> list:
    """Retorna todos os campos disponíveis"""
    return list(CAMPOS_DISPONIVEIS.keys())

def validar_campos_selecionados(campos: list) -> tuple[bool, str]:
    """Valida se os campos selecionados são válidos"""
    todos_ids = list(CAMPOS_DISPONIVEIS.keys())
    
    for campo in campos:
        if campo not in todos_ids:
            return False, f"Campo '{campo}' não existe"
    
    return True, ""

def get_mensagem_erro(tipo: str, **kwargs) -> str:
    """Retorna mensagem de erro formatada"""
    mensagem = MENSAGENS_ERRO.get(tipo, "Erro desconhecido")
    try:
        return mensagem.format(**kwargs)
    except KeyError:
        return mensagem
