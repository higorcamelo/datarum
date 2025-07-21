#!/usr/bin/env python3
"""
Script de inicialização do Datarum API
"""
import os
import sys
import logging
from pathlib import Path

# Adicionar o diretório atual ao Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

def setup_environment():
    """Configura o ambiente para desenvolvimento"""
    # Criar .env se não existir
    env_file = current_dir / ".env"
    env_example = current_dir / ".env.example"
    
    if not env_file.exists() and env_example.exists():
        print("📋 Criando arquivo .env a partir do .env.example...")
        env_file.write_text(env_example.read_text())
        print("✅ Arquivo .env criado. Ajuste as configurações se necessário.")
    
    # Criar diretório de logs
    logs_dir = current_dir / "logs"
    logs_dir.mkdir(exist_ok=True)
    
    print("🔧 Ambiente configurado com sucesso!")

def check_dependencies():
    """Verifica se as dependências estão instaladas"""
    try:
        import fastapi
        import uvicorn
        import pandas
        import openpyxl
        print("✅ Dependências principais encontradas")
        return True
    except ImportError as e:
        print(f"❌ Dependência não encontrada: {e}")
        print("📦 Execute: pip install -r requirements.txt")
        return False

def run_development_server():
    """Executa o servidor de desenvolvimento"""
    try:
        import uvicorn
        import config
        
        print(f"🚀 Iniciando servidor de desenvolvimento...")
        print(f"   Ambiente: {config.ENVIRONMENT}")
        print(f"   URL: http://localhost:8000")
        print(f"   Debug: {config.DEBUG}")
        print(f"   Logs: {config.LOG_LEVEL}")
        print()
        
        uvicorn.run(
            "main:app",
            host="localhost",
            port=8000,
            reload=config.DEBUG,
            log_level=config.LOG_LEVEL.lower(),
            access_log=True
        )
    except Exception as e:
        print(f"❌ Erro ao iniciar servidor: {e}")
        sys.exit(1)

def run_tests():
    """Executa os testes com pytest"""
    tests_dir = current_dir / "tests"
    
    if not tests_dir.exists():
        print("❌ Pasta 'tests' não encontrada")
        print("💡 Para criar testes, execute: python run.py create-tests")
        return
    
    try:
        import pytest
        print("🧪 Executando testes...")
        # Executar com verbosidade e mostrar prints
        pytest.main(["-v", "-s", "tests/"])
    except ImportError:
        print("❌ pytest não encontrado. Instale com: pip install pytest")
    except Exception as e:
        print(f"❌ Erro ao executar testes: {e}")

def create_basic_tests():
    """Cria estrutura básica de testes REAIS"""
    tests_dir = current_dir / "tests"
    
    if tests_dir.exists():
        print("✅ Pasta 'tests' já existe com testes completos!")
        print("💡 Para executar: python run.py test")
        return
    
    print("❌ Os testes REAIS já foram criados em 'tests/'")
    print("❌ Se foram deletados acidentalmente, eles precisam ser recriados manualmente")
    print("💡 Os testes incluem:")
    print("   - Validação de XMLs NFe")
    print("   - Testes de API endpoints")
    print("   - Testes de integração")
    print("   - Validação de configurações")
    print("   - Testes de logging")
    print()
    print("💡 Para executar: python run.py test")

def show_help():
    """Mostra ajuda"""
    print("""
🔧 Datarum API - Script de Inicialização

Comandos disponíveis:
  dev, start          - Iniciar servidor de desenvolvimento
  test                - Executar testes (se pasta tests/ existir)
  create-tests        - Criar estrutura básica de testes
  setup               - Configurar ambiente (criar .env, logs/)
  check               - Verificar dependências
  help, -h, --help    - Mostrar esta ajuda

Exemplos:
  python run.py dev
  python run.py create-tests
  python run.py test
  python run.py setup
""")

def main():
    """Função principal"""
    if len(sys.argv) < 2:
        command = "dev"
    else:
        command = sys.argv[1].lower()
    
    if command in ["help", "-h", "--help"]:
        show_help()
    elif command == "setup":
        setup_environment()
    elif command == "check":
        if check_dependencies():
            print("✅ Todas as dependências estão instaladas")
        else:
            sys.exit(1)
    elif command == "test":
        run_tests()
    elif command == "create-tests":
        create_basic_tests()
    elif command in ["dev", "start"]:
        # Setup automático
        setup_environment()
        
        # Verificar dependências
        if not check_dependencies():
            sys.exit(1)
        
        # Iniciar servidor
        run_development_server()
    else:
        print(f"❌ Comando desconhecido: {command}")
        show_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
