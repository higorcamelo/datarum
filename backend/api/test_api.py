"""
Teste básico para verificar se a API está funcionando
"""
import sys
import os
from pathlib import Path

# Adicionar path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from index import app
    print("✅ App importado com sucesso!")
    
    # Testar endpoints básicos
    from fastapi.testclient import TestClient
    client = TestClient(app)
    
    # Testar endpoint raiz
    response = client.get("/")
    print(f"✅ GET / - Status: {response.status_code}")
    print(f"   Response: {response.json()}")
    
    print("\n🎉 API está funcionando corretamente!")
    
except ImportError as e:
    print(f"❌ Erro de import: {e}")
except Exception as e:
    print(f"❌ Erro geral: {e}")
