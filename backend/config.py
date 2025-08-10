# Configuração simples do Datarum
import os
import json

# URLs permitidas para CORS - com suporte a variáveis de ambiente
def get_cors_origins():
    """Obter origens CORS das variáveis de ambiente ou padrão"""
    cors_env = os.getenv("CORS_ORIGINS")
    if cors_env:
        try:
            return json.loads(cors_env)
        except json.JSONDecodeError:
            # Se não for JSON, tratar como lista separada por vírgula
            return [origin.strip() for origin in cors_env.split(",")]
    
    # Padrão para desenvolvimento
    return [
        "http://localhost:3000",
        "http://localhost:5173", 
        "http://127.0.0.1:5173",
    ]

CORS_ORIGINS = get_cors_origins()

# Limites básicos - configuráveis via ambiente
MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", 5 * 1024 * 1024))  # 5MB padrão
MAX_FILES_COUNT = int(os.getenv("MAX_FILES_COUNT", 50))

# Configuração de ambiente
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
DEBUG = ENVIRONMENT == "development"

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO" if ENVIRONMENT == "production" else "DEBUG")
