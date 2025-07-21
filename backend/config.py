# Configuração simples do Datarum
import os

# URLs permitidas para CORS
# Para desenvolvimento: localhost
# Para produção: substitua pela URL real
CORS_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173", 
    "http://127.0.0.1:5173",
    # Adicione aqui as URLs de produção quando necessário:
    # "https://datarum.com.br",
    # "https://app.datarum.com.br"
]

# Limites básicos
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
MAX_FILES_COUNT = 50

# Configuração de ambiente
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
DEBUG = ENVIRONMENT == "development"

# Logging
LOG_LEVEL = "INFO" if ENVIRONMENT == "production" else "DEBUG"
