import os
import sys
from pathlib import Path

# Garante que o Python encontre os módulos locais (api, utils, validador)
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

def setup_environment():
    """Cria pastas necessárias para o funcionamento local"""
    logs_dir = current_dir / "logs"
    logs_dir.mkdir(exist_ok=True)
    
    # Cria um .env básico se não existir
    env_file = current_dir / ".env"
    if not env_file.exists():
        env_file.write_text("DEBUG=True\nLOG_LEVEL=INFO\nENVIRONMENT=development")
        print("✅ Arquivo .env básico criado.")

def check_dependencies():
    """Verifica se o básico para rodar está instalado"""
    try:
        import fastapi
        import uvicorn
        import pandas
        import xmltodict
        return True
    except ImportError as e:
        print(f"❌ Falta instalar: {e.name}")
        print("📦 Execute: pip install -r requirements.txt")
        return False

def run_server():
    """Executa o servidor FastAPI via Uvicorn"""
    try:
        import uvicorn
        # Importamos as configs para pegar o modo Debug
        from api.config import DEBUG, LOG_LEVEL
        
        print(f"🚀 Datarum API iniciando em http://localhost:8000")
        print(f"🔧 Modo Debug: {DEBUG}")

        uvicorn.run(
            "main:app",
            host="0.0.0.0", # Permite acesso na rede local se necessário
            port=8000,
            reload=DEBUG,   # Reinicia o servidor se você salvar um arquivo
            log_level=LOG_LEVEL.lower()
        )
    except Exception as e:
        print(f"❌ Erro ao iniciar: {e}")

if __name__ == "__main__":
    setup_environment()
    if check_dependencies():
        run_server()