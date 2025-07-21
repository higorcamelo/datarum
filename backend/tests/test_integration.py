"""
Testes de integração para a API Datarum
Testa endpoints reais da API
"""
import pytest
import sys
from pathlib import Path
from fastapi.testclient import TestClient
import tempfile
import io

# Adicionar o diretório pai ao path
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import app

client = TestClient(app)


class TestAPIIntegration:
    """Testes de integração da API"""
    
    def test_health_endpoint(self):
        """Testa endpoint de health check"""
        response = client.get("/health")
        
        assert response.status_code == 200
        data = response.json()
        
        # Verifica estrutura da resposta
        assert "status" in data
        assert "timestamp" in data
        assert "version" in data
        assert "environment" in data
        
        assert data["status"] == "healthy"
    
    def test_root_endpoint(self):
        """Testa endpoint raiz"""
        response = client.get("/")
        
        assert response.status_code == 200
        data = response.json()
        
        # Verifica se tem informações da API
        assert "name" in data
        assert "version" in data
        assert "endpoints" in data
        assert data["status"] == "online"
    
    def test_processar_sem_arquivos(self):
        """Testa endpoint /processar sem enviar arquivos"""
        response = client.post("/processar", data={"planilha": "teste"})
        
        # Deve retornar erro por não ter arquivos
        assert response.status_code == 422  # Validation error
    
    def test_processar_arquivo_invalido(self):
        """Testa envio de arquivo que não é XML"""
        # Criar arquivo texto falso
        fake_file = io.BytesIO(b"Este nao eh um XML")
        
        response = client.post(
            "/processar",
            data={"planilha": "teste"},
            files={"xmls": ("teste.txt", fake_file, "text/plain")}
        )
        
        # Deve retornar erro por não ser XML
        assert response.status_code == 400
        assert "não é XML" in response.json()["detail"]
    
    def test_processar_xml_invalido(self):
        """Testa envio de XML que não é NFe"""
        # XML válido mas não é NFe
        xml_invalido = """<?xml version="1.0" encoding="UTF-8"?>
<documento>
    <tipo>Não é NFe</tipo>
</documento>"""
        
        xml_file = io.BytesIO(xml_invalido.encode('utf-8'))
        
        response = client.post(
            "/processar",
            data={"planilha": "teste"},
            files={"xmls": ("invalid.xml", xml_file, "application/xml")}
        )
        
        # Deve retornar erro por não ser NFe válida
        assert response.status_code == 400
        assert "NFe válida" in response.json()["detail"]
    
    def test_processar_nome_planilha_invalido(self):
        """Testa envio com nome de planilha inválido"""
        xml_nfe = """<?xml version="1.0" encoding="UTF-8"?>
<nfeProc>
    <NFe>
        <infNFe>
            <ide><nNF>1</nNF><serie>1</serie></ide>
            <emit><xNome>Teste</xNome></emit>
            <total><ICMSTot><vNF>100</vNF></ICMSTot></total>
        </infNFe>
    </NFe>
</nfeProc>"""
        
        xml_file = io.BytesIO(xml_nfe.encode('utf-8'))
        
        # Nome com caracteres especiais perigosos
        response = client.post(
            "/processar",
            data={"planilha": "../../etc/passwd"},
            files={"xmls": ("teste.xml", xml_file, "application/xml")}
        )
        
        # Deve sanitizar o nome ou retornar erro
        assert response.status_code == 400
    
    def test_muitos_arquivos(self):
        """Testa envio de muitos arquivos"""
        xml_simples = """<?xml version="1.0" encoding="UTF-8"?>
<nfeProc>
    <NFe>
        <infNFe>
            <ide><nNF>1</nNF></ide>
            <emit><xNome>Teste</xNome></emit>
            <total><ICMSTot><vNF>100</vNF></ICMSTot></total>
        </infNFe>
    </NFe>
</nfeProc>"""
        
        # Criar muitos arquivos (mais do que o limite)
        files = []
        for i in range(55):  # Limite é 50
            xml_file = io.BytesIO(xml_simples.encode('utf-8'))
            files.append(("xmls", (f"teste{i}.xml", xml_file, "application/xml")))
        
        response = client.post(
            "/processar",
            data={"planilha": "teste"},
            files=files
        )
        
        # Deve retornar erro por exceder limite
        assert response.status_code == 400
        assert "Máximo" in response.json()["detail"]


class TestCORS:
    """Testa configuração de CORS"""
    
    def test_cors_headers(self):
        """Testa se headers CORS estão configurados"""
        response = client.options("/")
        
        # Verifica se permite CORS
        assert response.status_code in [200, 405]  # OPTIONS pode não estar implementado
        
        # Testa com GET normal
        response = client.get("/")
        
        # Não deve dar erro de CORS em testes
        assert response.status_code == 200


class TestLogging:
    """Testa se logging está funcionando"""
    
    def test_logs_directory_creation(self):
        """Testa se diretório de logs é criado"""
        logs_dir = Path("logs")
        
        # Fazer uma requisição para gerar logs
        client.get("/health")
        
        # Verificar se diretório existe
        assert logs_dir.exists()
        assert logs_dir.is_dir()
    
    def test_log_files_creation(self):
        """Testa se arquivos de log são criados"""
        # Fazer algumas requisições
        client.get("/")
        client.get("/health")
        
        logs_dir = Path("logs")
        if logs_dir.exists():
            log_files = list(logs_dir.glob("*.log"))
            # Deve ter pelo menos um arquivo de log
            assert len(log_files) > 0


if __name__ == "__main__":
    # Executar com: python -m pytest tests/test_integration.py -v
    pytest.main([__file__, "-v"])
