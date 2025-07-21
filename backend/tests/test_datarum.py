"""
Testes REAIS para o sistema Datarum
Testa funcionalidades importantes, não apenas importações
"""
import pytest
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path
from io import BytesIO

# Adicionar o diretório pai ao path
sys.path.insert(0, str(Path(__file__).parent.parent))

from validador import validar_xml_nfe, validar_tamanho_arquivo, contar_itens_xml


class TestValidador:
    """Testes do validador de XMLs - funcionalidade crítica"""
    
    def test_validar_xml_nfe_valido(self):
        """Testa validação com XML NFe válido"""
        xml_nfe = """<?xml version="1.0" encoding="UTF-8"?>
<nfeProc>
    <NFe>
        <infNFe>
            <ide>
                <nNF>000001</nNF>
                <serie>001</serie>
                <dhEmi>2025-01-21T10:30:00-03:00</dhEmi>
            </ide>
            <emit>
                <xNome>Empresa Teste LTDA</xNome>
            </emit>
            <total>
                <ICMSTot>
                    <vNF>1500.00</vNF>
                </ICMSTot>
            </total>
            <det nItem="1">
                <prod>
                    <xProd>Produto Teste</xProd>
                    <vProd>1500.00</vProd>
                </prod>
            </det>
        </infNFe>
    </NFe>
</nfeProc>"""
        
        resultado = validar_xml_nfe(xml_nfe.encode('utf-8'))
        
        assert resultado["valido"] == True
        assert resultado["erro"] == ""
        assert resultado["dados"]["numero"] == "000001"
        assert resultado["dados"]["serie"] == "001"
        assert resultado["dados"]["emitente"] == "Empresa Teste LTDA"
        assert resultado["dados"]["valor_total"] == "1500.00"
    
    def test_validar_xml_invalido(self):
        """Testa validação com XML inválido"""
        xml_invalido = """<?xml version="1.0"?>
<documento>
    <conteudo>Não é uma NFe</conteudo>
</documento>"""
        
        resultado = validar_xml_nfe(xml_invalido.encode('utf-8'))
        
        assert resultado["valido"] == False
        assert "não é uma NFe válida" in resultado["erro"]
        assert resultado["dados"] == {}
    
    def test_validar_xml_corrompido(self):
        """Testa validação com XML corrompido"""
        xml_corrompido = b"<xml>conteudo inv\xff\xfe"
        
        resultado = validar_xml_nfe(xml_corrompido)
        
        assert resultado["valido"] == False
        assert "encoding" in resultado["erro"] or "XML" in resultado["erro"]
    
    def test_contar_itens_xml(self):
        """Testa contagem de itens na NFe"""
        xml_com_itens = """<?xml version="1.0" encoding="UTF-8"?>
<nfeProc>
    <NFe>
        <infNFe>
            <det nItem="1">
                <prod><xProd>Item 1</xProd></prod>
            </det>
            <det nItem="2">
                <prod><xProd>Item 2</xProd></prod>
            </det>
            <det nItem="3">
                <prod><xProd>Item 3</xProd></prod>
            </det>
        </infNFe>
    </NFe>
</nfeProc>"""
        
        count = contar_itens_xml(xml_com_itens.encode('utf-8'))
        assert count == 3
    
    def test_validar_tamanho_arquivo(self):
        """Testa validação de tamanho de arquivo"""
        # Arquivo pequeno - deve passar
        resultado_ok = validar_tamanho_arquivo(1024, max_mb=1)  # 1KB
        assert resultado_ok["valido"] == True
        
        # Arquivo grande - deve falhar
        resultado_grande = validar_tamanho_arquivo(2 * 1024 * 1024, max_mb=1)  # 2MB
        assert resultado_grande["valido"] == False
        assert "muito grande" in resultado_grande["erro"]


class TestConfig:
    """Testes das configurações do sistema"""
    
    def test_config_existe(self):
        """Testa se arquivo de config existe e tem variáveis necessárias"""
        import config
        
        # Verifica se variáveis obrigatórias existem
        assert hasattr(config, 'CORS_ORIGINS')
        assert hasattr(config, 'ENVIRONMENT')
        assert hasattr(config, 'DEBUG')
        assert hasattr(config, 'LOG_LEVEL')
        
        # Verifica tipos
        assert isinstance(config.CORS_ORIGINS, list)
        assert isinstance(config.DEBUG, bool)
        assert isinstance(config.ENVIRONMENT, str)
        assert config.ENVIRONMENT in ['development', 'production']


class TestUtilsXMLParser:
    """Testes do parser de XML"""
    
    def test_parse_nfe_estrutura_basica(self):
        """Testa se o parser extrai dados básicos corretamente"""
        from utils.xml_parser import parse_nfe
        
        xml_teste = """<?xml version="1.0" encoding="UTF-8"?>
<nfeProc>
    <NFe>
        <infNFe>
            <ide>
                <nNF>123456</nNF>
                <serie>001</serie>
                <dhEmi>2025-01-21T10:30:00-03:00</dhEmi>
            </ide>
            <emit>
                <CNPJ>12345678000195</CNPJ>
                <xNome>Empresa Emitente</xNome>
            </emit>
            <dest>
                <CNPJ>98765432000167</CNPJ>
                <xNome>Empresa Destinataria</xNome>
            </dest>
            <det nItem="1">
                <prod>
                    <cProd>001</cProd>
                    <xProd>Produto Teste</xProd>
                    <vProd>100.00</vProd>
                    <qCom>2</qCom>
                </prod>
            </det>
        </infNFe>
    </NFe>
</nfeProc>"""
        
        # Criar arquivo temporário
        with tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False, encoding='utf-8') as f:
            f.write(xml_teste)
            temp_path = f.name
        
        try:
            dados = parse_nfe(temp_path)
            
            # Verifica se retorna lista
            assert isinstance(dados, list)
            assert len(dados) > 0
            
            # Verifica se tem dados básicos
            item = dados[0]
            assert 'numero_nf' in item
            assert 'emitente' in item
            assert 'destinatario' in item
            assert 'descricao_produto' in item
            
        finally:
            # Limpar arquivo temporário
            Path(temp_path).unlink()


class TestHealthCheck:
    """Testa se a API responde corretamente"""
    
    def test_app_creation(self):
        """Testa se a aplicação FastAPI é criada corretamente"""
        import main
        
        assert hasattr(main, 'app')
        assert main.app is not None
        
        # Verifica se tem as rotas esperadas
        routes = [route.path for route in main.app.routes]
        assert "/" in routes
        assert "/health" in routes
        assert "/processar" in routes


# Configuração de logging para os testes
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - TEST - %(levelname)s - %(message)s'
)

if __name__ == "__main__":
    # Executar com: python -m pytest tests/test_datarum.py -v
    pytest.main([__file__, "-v"])
