# Sistema de configuração robusto para Datarum v1.1
import os
import json
from typing import List, Dict, Any, Union
from pathlib import Path

# Carregar python-dotenv se disponível
try:
    from dotenv import load_dotenv
    # Carregar .env do diretório atual
    env_path = Path(__file__).parent / '.env'
    if env_path.exists():
        load_dotenv(env_path)
        print(f"✅ Configurações carregadas de {env_path}")
    else:
        print(f"⚠️ Arquivo .env não encontrado em {env_path}")
except ImportError:
    print("⚠️ python-dotenv não instalado, usando apenas variáveis de ambiente do sistema")

def get_env_bool(key: str, default: bool = False) -> bool:
    """Converte variável de ambiente para boolean"""
    value = os.getenv(key, str(default)).lower()
    return value in ('true', '1', 'yes', 'on', 'enabled')

def get_env_int(key: str, default: int = 0) -> int:
    """Converte variável de ambiente para int"""
    try:
        return int(os.getenv(key, str(default)))
    except ValueError:
        return default

def get_env_list(key: str, default: List[str] = None) -> List[str]:
    """Converte variável de ambiente para lista"""
    if default is None:
        default = []
    
    value = os.getenv(key, "")
    if not value:
        return default
    
    try:
        # Tentar como JSON primeiro
        return json.loads(value)
    except json.JSONDecodeError:
        # Fallback para split por vírgula
        return [item.strip() for item in value.split(',') if item.strip()]

# URLs permitidas para CORS - com suporte a variáveis de ambiente
def get_cors_origins():
    """Obter origens CORS das variáveis de ambiente ou padrão"""
    return get_env_list("CORS_ORIGINS", [
        "http://localhost:3000",
        "http://localhost:5173", 
        "http://127.0.0.1:5173",
    ])

# Configurações principais
CORS_ORIGINS = get_cors_origins()

# === LIMITES DE PROCESSAMENTO ===
MAX_FILE_SIZE = get_env_int("MAX_FILE_SIZE", 5 * 1024 * 1024)  # 5MB padrão
MAX_FILES_COUNT = get_env_int("MAX_FILES_COUNT", 200)  # ATUALIZADO PARA 200!
MAX_ARQUIVOS_BATCH = get_env_int('MAX_ARQUIVOS_BATCH', 200)
MAX_SIZE_MB_ARQUIVO = get_env_int('MAX_SIZE_MB_ARQUIVO', 5)

# === AMBIENTE ===
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
DEBUG = get_env_bool('DEBUG', True)
LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')

# === RECURSOS GRATUITOS ===
LIMITE_XMLS_MENSAL = get_env_int('LIMITE_XMLS_MENSAL', 750)

# Print de configuração para debug
if get_env_bool('DEBUG', True):
    print(f"🔧 Configurações do Datarum:")
    print(f"   - MAX_FILES_COUNT: {MAX_FILES_COUNT}")
    print(f"   - MAX_ARQUIVOS_BATCH: {MAX_ARQUIVOS_BATCH}") 
    print(f"   - MAX_SIZE_MB_ARQUIVO: {MAX_SIZE_MB_ARQUIVO}MB")
    print(f"   - LIMITE_XMLS_MENSAL: {LIMITE_XMLS_MENSAL}")
    print(f"   - CORS_ORIGINS: {len(CORS_ORIGINS)} origem(ns)")
    print(f"   - ENVIRONMENT: {ENVIRONMENT}")
DEBUG = ENVIRONMENT == "development"

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO" if ENVIRONMENT == "production" else "DEBUG")
