"""
Configuração simples para a API no Vercel
"""
import os

# Configurações básicas
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
MAX_FILE_SIZE = int(os.getenv('MAX_FILE_SIZE', 10 * 1024 * 1024))  # 10MB
MAX_FILES = int(os.getenv('MAX_FILES', 50))

# Configurações para Vercel
VERCEL_ENV = os.getenv('VERCEL_ENV', 'development')
IS_VERCEL = bool(os.getenv('VERCEL'))

# Configurações de CORS
CORS_ORIGINS = ["*"]

# Timeouts
REQUEST_TIMEOUT = 30  # segundos
