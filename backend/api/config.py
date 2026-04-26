import os
import json
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# --- CONFIGURAÇÕES DE AMBIENTE ---
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
DEBUG = os.getenv("DEBUG", "true").lower() == "true"
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
VERSION = os.getenv("API_VERSION", "1.0.0")

# --- LIMITES E SEGURANÇA ---
MAX_FILE_SIZE = int(os.getenv("MAX_SIZE_MB_ARQUIVO", 5)) * 1024 * 1024
MAX_FILES_COUNT = int(os.getenv("MAX_ARQUIVOS_BATCH", 200))

def get_cors_origins():
    cors_env = os.getenv("ALLOWED_ORIGINS")
    if cors_env:
        try:
            return json.loads(cors_env)
        except json.JSONDecodeError:
            return [origin.strip() for origin in cors_env.split(",")]
    return ["*"]

CORS_ORIGINS = get_cors_origins()

# --- DICIONÁRIO DE CAMPOS ---
# Sincronizado com as chaves do utils/xml_parser.py
CAMPOS_DISPONIVEIS = {
    # Bloco da Nota (Identificação)
    "numero_nf": {"categoria": "nota", "label": "Nº NF"},
    "serie": {"categoria": "nota", "label": "Série"},
    "data_emissao": {"categoria": "nota", "label": "Data Emissão"},
    "valor_total_nf": {"categoria": "nota", "label": "Total NF"},
    "valor_produtos_total": {"categoria": "nota", "label": "Total Produtos (Nota)"},
    "valor_desconto_total": {"categoria": "nota", "label": "Total Desconto (Nota)"},
    "valor_frete_total": {"categoria": "nota", "label": "Total Frete (Nota)"},
    "chave_nfe": {"categoria": "nota", "label": "Chave NFe"},
    
    # Bloco de Entidades (Parceiros)
    "emitente": {"categoria": "emitente", "label": "Razão Social Emitente"},
    "cnpj_emitente": {"categoria": "emitente", "label": "CNPJ Emitente"},
    "uf_emitente": {"categoria": "emitente", "label": "UF Emitente"},
    "destinatario": {"categoria": "destinatario", "label": "Razão Social Destinatário"},
    "cnpj_destinatario": {"categoria": "destinatario", "label": "CNPJ/CPF Destinatário"},
    "uf_destinatario": {"categoria": "destinatario", "label": "UF Destinatário"},
    
    # Bloco de Produtos (Itens)
    "codigo_produto": {"categoria": "produto", "label": "Cód. Produto"},
    "descricao_produto": {"categoria": "produto", "label": "Produto"},
    "ncm": {"categoria": "produto", "label": "NCM"},
    "cfop": {"categoria": "produto", "label": "CFOP"},
    "quantidade_comercial": {"categoria": "produto", "label": "Qtd"},
    "unidade_comercial": {"categoria": "produto", "label": "Unid"},
    "valor_unitario": {"categoria": "produto", "label": "Vl. Unit"},
    "valor_total_item": {"categoria": "produto", "label": "Total Item"},
    "valor_desconto_item": {"categoria": "produto", "label": "Desconto Item"},
    
    # Bloco Fiscal (Impostos)
    "cst_icms": {"categoria": "imposto", "label": "CST/CSOSN ICMS"},
    "base_icms": {"categoria": "imposto", "label": "Base ICMS"},
    "aliquota_icms": {"categoria": "imposto", "label": "Aliq. ICMS"},
    "icms_valor": {"categoria": "imposto", "label": "Vl. ICMS"},
    "base_icms_st": {"categoria": "imposto", "label": "Base ICMS ST"},
    "icms_st_valor": {"categoria": "imposto", "label": "Vl. ICMS ST"},
    "valor_ipi": {"categoria": "imposto", "label": "Vl. IPI"},
    "pis_valor": {"categoria": "imposto", "label": "Vl. PIS"},
    "cofins_valor": {"categoria": "imposto", "label": "Vl. COFINS"}
}

# --- PRESETS ---
PRESETS = {
    "basico": {
        "nome": "Básico",
        "campos": [
            "numero_nf",
            "data_emissao",
            "emitente",
            "descricao_produto",
            "quantidade_comercial",
            "valor_unitario",
            "valor_total_item",
            "valor_total_nf"
        ],
        "opcoes": {
            "incluirTotais": True,
            "agruparPorEmitente": False,
            "incluirResumo": False
        }
    },
    "fiscal": {
    "nome": "Fiscal",
    "campos": [
        "numero_nf",
        "data_emissao",
        "cnpj_emitente",
        "descricao_produto",
        "cfop",
        "ncm",
        "quantidade_comercial",
        "valor_total_item",
        "cst_icms",
        "base_icms",
        "aliquota_icms",
        "icms_valor",
        "pis_valor",
        "cofins_valor",
        "valor_total_nf",
        "valor_frete_total"
    ],
    "opcoes": {
        "incluirTotais": True,
        "agruparPorEmitente": True,
        "incluirResumo": True
    }
    },
    "completo": {
        "nome": "Completo",
        "campos": list(CAMPOS_DISPONIVEIS.keys()),
        "opcoes": {
            "incluirTotais": True,
            "agruparPorEmitente": True,
            "incluirResumo": True
        }
    }
}

# --- MENSAGENS DE ERRO ---
MENSAGENS_ERRO = {
    "xml_invalido": "O arquivo não é um XML válido de NFe.",
    "tamanho_excedido": f"Arquivo muito grande (máximo {MAX_FILE_SIZE // (1024*1024)}MB).",
    "sem_dados": "Nenhum dado válido foi extraído dos XMLs.",
    "processamento_erro": "Erro interno no processamento dos arquivos.",
    "limite_arquivos": f"Limite de {MAX_FILES_COUNT} arquivos por vez excedido."
}

def get_preset_config(nome: str) -> dict:
    if nome not in PRESETS:
        raise ValueError(f"Preset inválido: {nome}")
    return PRESETS[nome]