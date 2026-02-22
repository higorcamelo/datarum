"""
Teste básico sem pytest - apenas para verificar se os módulos importam
"""
import sys
from pathlib import Path

# Adicionar o diretório pai ao path
sys.path.insert(0, str(Path(__file__).parent.parent))

def test_imports():
    """Testa se consegue importar os módulos principais"""
    print("Testando importacoes...")
    
    try:
        import main
        print("OK - main.py")
        assert hasattr(main, 'app'), "main.py deve ter 'app'"
    except Exception as e:
        print(f"ERRO - main.py: {e}")
        return False
    
    try:
        import backend.api.config as config
        print("OK - config.py")
        assert hasattr(config, 'CORS_ORIGINS'), "config.py deve ter 'CORS_ORIGINS'"
    except Exception as e:
        print(f"ERRO - config.py: {e}")
        return False
    
    try:
        from validador import validar_xml_nfe
        print("OK - validador.py")
    except Exception as e:
        print(f"ERRO - validador.py: {e}")
        return False
    
    try:
        from utils.xml_parser import parse_nfe
        print("OK - utils/xml_parser.py")
    except Exception as e:
        print(f"ERRO - utils/xml_parser.py: {e}")
        return False
    
    try:
        from utils.excel_handler import salvar_em_excel
        print("OK - utils/excel_handler.py")
    except Exception as e:
        print(f"ERRO - utils/excel_handler.py: {e}")
        return False
    
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("TESTE BASICO - DATARUM API")
    print("=" * 50)
    
    if test_imports():
        print("\nTODOS OS TESTES PASSARAM!")
        print("Sistema pronto para uso")
    else:
        print("\nALGUNS TESTES FALHARAM")
        print("Verifique as dependencias e arquivos")
        sys.exit(1)
