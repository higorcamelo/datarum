# Configuração Datarum - versão limpa e consolidada
import os
import json

# CONFIGURAÇÕES DE AMBIENTE

def get_cors_origins():
    cors_env = os.getenv("CORS_ORIGINS")
    if cors_env:
        try:
            return json.loads(cors_env)
        except json.JSONDecodeError:
            return [origin.strip() for origin in cors_env.split(",")]
    return [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]

CORS_ORIGINS = get_cors_origins()

MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", 5 * 1024 * 1024))  # 5 MB
MAX_FILES_COUNT = int(os.getenv("MAX_FILES_COUNT", 200))
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
DEBUG = ENVIRONMENT == "development"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO" if ENVIRONMENT == "production" else "DEBUG")
VERSION = "1.1.0"

# CAMPOS DISPONÍVEIS

CAMPOS_DISPONIVEIS = {
    # Dados da nota
    "numero_nf": {"tipo": "texto", "categoria": "nota", "xpath": "//ide/nNF", "obrigatorio": True},
    "data_emissao": {"tipo": "data", "categoria": "nota", "xpath": "//ide/dhEmi|//ide/dEmi", "obrigatorio": True},
    "data_vencimento": {"tipo": "data", "categoria": "nota", "xpath": "//ide/dVenc", "obrigatorio": False},
    "valor_total_nf": {"tipo": "moeda", "categoria": "nota", "xpath": "//total/ICMSTot/vNF", "obrigatorio": True},
    "natureza_operacao": {"tipo": "texto", "categoria": "nota", "xpath": "//ide/natOp", "obrigatorio": False},
    "serie": {"tipo": "numero", "categoria": "nota", "xpath": "//ide/serie", "obrigatorio": False},
    "modelo": {"tipo": "numero", "categoria": "nota", "xpath": "//ide/mod", "obrigatorio": False},
    "chave_acesso": {"tipo": "texto", "categoria": "nota", "xpath": "//infNFe/@Id", "obrigatorio": False},
    "versao_nfe": {"tipo": "texto", "categoria": "nota", "valor_fixo": "4.00", "obrigatorio": False},

    # Dados do emitente
    "emitente": {"tipo": "texto", "categoria": "emitente", "xpath": "//emit/xNome", "obrigatorio": True},
    "cnpj_emitente": {"tipo": "cnpj", "categoria": "emitente", "xpath": "//emit/CNPJ", "obrigatorio": True},
    "inscricao_emitente": {"tipo": "texto", "categoria": "emitente", "xpath": "//emit/IE", "obrigatorio": False},
    "endereco_emitente": {"tipo": "texto", "categoria": "emitente", "xpath": "//emit/enderEmit/xLgr", "obrigatorio": False},
    "municipio_emitente": {"tipo": "texto", "categoria": "emitente", "xpath": "//emit/enderEmit/xMun", "obrigatorio": False},
    "uf_emitente": {"tipo": "texto", "categoria": "emitente", "xpath": "//emit/enderEmit/UF", "obrigatorio": False},
    "cep_emitente": {"tipo": "cep", "categoria": "emitente", "xpath": "//emit/enderEmit/CEP", "obrigatorio": False},
    "telefone_emitente": {"tipo": "texto", "categoria": "emitente", "xpath": "//emit/enderEmit/fone", "obrigatorio": False},

    # Dados do destinatário
    "destinatario": {"tipo": "texto", "categoria": "destinatario", "xpath": "//dest/xNome", "obrigatorio": False},
    "cnpj_destinatario": {"tipo": "texto", "categoria": "destinatario", "xpath": "//dest/CPF|//dest/CNPJ", "obrigatorio": False},
    "municipio_dest": {"tipo": "texto", "categoria": "destinatario", "xpath": "//dest/enderDest/xMun", "obrigatorio": False},
    "uf_dest": {"tipo": "texto", "categoria": "destinatario", "xpath": "//dest/enderDest/UF", "obrigatorio": False},

    # Produtos e impostos
    "codigo_produto": {"tipo": "texto", "categoria": "produto", "xpath": "prod/cProd", "obrigatorio": False},
    "descricao_produto": {"tipo": "texto", "categoria": "produto", "xpath": "prod/xProd", "obrigatorio": True},
    "ncm": {"tipo": "numero", "categoria": "produto", "xpath": "prod/NCM", "obrigatorio": False},
    "cfop": {"tipo": "numero", "categoria": "produto", "xpath": "prod/CFOP", "obrigatorio": False},
    "quantidade_comercial": {"tipo": "decimal", "categoria": "produto", "xpath": "prod/qCom", "obrigatorio": False},
    "unidade_comercial": {"tipo": "texto", "categoria": "produto", "xpath": "prod/uCom", "obrigatorio": False},
    "valor_unitario": {"tipo": "moeda", "categoria": "produto", "xpath": "prod/vUnCom", "obrigatorio": False},
    "valor_total_item": {"tipo": "moeda", "categoria": "produto", "xpath": "prod/vProd", "obrigatorio": True},

    # Impostos
    "cst_icms": {"tipo": "texto", "categoria": "imposto", "xpath": "imposto/ICMS/*/CST", "obrigatorio": False},
    "icms_base": {"tipo": "moeda", "categoria": "imposto", "xpath": "imposto/ICMS/*/vBC", "obrigatorio": False},
    "icms_aliquota": {"tipo": "percentual", "categoria": "imposto", "xpath": "imposto/ICMS/*/pICMS", "obrigatorio": False},
    "icms_valor": {"tipo": "moeda", "categoria": "imposto", "xpath": "imposto/ICMS/*/vICMS", "obrigatorio": False},
    "ipi_aliquota": {"tipo": "percentual", "categoria": "imposto", "xpath": "imposto/IPI/*/pIPI", "obrigatorio": False},
    "ipi_valor": {"tipo": "moeda", "categoria": "imposto", "xpath": "imposto/IPI/*/vIPI", "obrigatorio": False},
    "pis_aliquota": {"tipo": "percentual", "categoria": "imposto", "xpath": "imposto/PIS/*/pPIS", "obrigatorio": False},
    "pis_valor": {"tipo": "moeda", "categoria": "imposto", "xpath": "imposto/PIS/*/vPIS", "obrigatorio": False},
    "cofins_aliquota": {"tipo": "percentual", "categoria": "imposto", "xpath": "imposto/COFINS/*/pCOFINS", "obrigatorio": False},
    "cofins_valor": {"tipo": "moeda", "categoria": "imposto", "xpath": "imposto/COFINS/*/vCOFINS", "obrigatorio": False}
}

# PRESETS

PRESETS = {
    "basico": {
        "nome": "Básico",
        "descricao": "Dados essenciais para controle simples",
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
        "descricao": "Extração detalhada com todos os dados relevantes",
        "campos": [
            "numero_nf", "data_emissao", "serie", "natureza_operacao", "valor_total_nf", "chave_acesso",
            "emitente", "cnpj_emitente", "municipio_emitente", "uf_emitente",
            "destinatario", "cnpj_destinatario", "municipio_dest", "uf_dest",
            "descricao_produto", "codigo_produto", "ncm", "cfop", "quantidade_comercial",
            "unidade_comercial", "valor_unitario", "valor_total_item",
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
            "icms_base", "icms_aliquota", "icms_valor",
            "ipi_aliquota", "ipi_valor", "pis_aliquota", "pis_valor", "cofins_aliquota", "cofins_valor"
        ],
        "opcoes": {
            "incluirTotais": True,
            "agruparPorEmitente": True,
            "incluirResumo": False
        }
    }
}

# OUTRAS CONFIGURAÇÕES

OPCOES_DISPONIVEIS = {
    "incluirTotais": {"nome": "Incluir totais", "descricao": "Adiciona linha final de somatórios", "padrao": True},
    "agruparPorEmitente": {"nome": "Agrupar por emitente", "descricao": "Agrupa notas por fornecedor", "padrao": False},
    "incluirResumo": {"nome": "Incluir resumo", "descricao": "Cria aba de resumo com estatísticas", "padrao": False}
}

TIPOS_DADOS = {
    "texto": {"formato": str, "validacao": None},
    "numero": {"formato": int, "validacao": "^[0-9]+$"},
    "decimal": {"formato": float, "validacao": "^[0-9]+(\\.[0-9]+)?$"},
    "moeda": {"formato": float, "validacao": "^[0-9]+(\\.[0-9]{1,2})?$"},
    "percentual": {"formato": float, "validacao": "^[0-9]+(\\.[0-9]+)?$"},
    "data": {"formato": "date", "validacao": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$"},
    "cnpj": {"formato": str, "validacao": "^[0-9]{2}\\.?[0-9]{3}\\.?[0-9]{3}/?[0-9]{4}-?[0-9]{2}$"},
    "cep": {"formato": str, "validacao": "^[0-9]{5}-?[0-9]{3}$"}
}

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

PERFORMANCE = {
    "max_arquivos_batch": 200,
    "max_size_mb_arquivo": 5,
    "timeout_processamento": 300,
    "cache_xml_parsed": False,
    "parallel_processing": False
}

# FUNÇÕES AUXILIARES

def get_preset(nome: str) -> dict:
    return PRESETS.get(nome, PRESETS["basico"])

def get_campos_por_preset(nome: str) -> list:
    preset = PRESETS.get(nome, PRESETS["basico"])
    return preset.get("campos", [])

def get_campos_by_categoria(categoria: str) -> list:
    """Retorna campos filtrados por categoria"""
    return [k for k, v in CAMPOS_DISPONIVEIS.items() if v["categoria"] == categoria]

def get_todos_campos() -> list:
    return sorted(CAMPOS_DISPONIVEIS.keys())

def validar_campos_selecionados(campos: list) -> tuple[bool, str]:
    todos_ids = list(CAMPOS_DISPONIVEIS.keys())
    for campo in campos:
        if campo not in todos_ids:
            return False, f"Campo '{campo}' não existe"
    return True, ""

def get_mensagem_erro(tipo: str, **kwargs) -> str:
    mensagem = MENSAGENS_ERRO.get(tipo, "Erro desconhecido")
    try:
        return mensagem.format(**kwargs)
    except KeyError:
        return mensagem
