import sys
sys.path.append('.')
from utils.xml_parser import parse_nfe
from validador import validar_xml_nfe, contar_itens_xml
import tempfile
import os

def testar_xml_real(xml_content, nome_arquivo):
    """Testa um XML real para ver se a extração funciona"""
    print(f"\n{'='*60}")
    print(f"TESTANDO: {nome_arquivo}")
    print(f"{'='*60}")
    
    # Testar validador
    print("\n1. VALIDAÇÃO:")
    validacao = validar_xml_nfe(xml_content.encode('utf-8'))
    print(f"   Válido: {validacao['valido']}")
    if validacao['valido']:
        dados = validacao['dados']
        print(f"   NFe Número: {dados.get('numero', 'N/A')}")
        print(f"   Série: {dados.get('serie', 'N/A')}")
        print(f"   Emitente: {dados.get('emitente', 'N/A')}")
        print(f"   Valor Total: {dados.get('valor_total', 'N/A')}")
        print(f"   Data Emissão: {dados.get('data_emissao', 'N/A')}")
    else:
        print(f"   Erro: {validacao['erro']}")
        return False
    
    # Contar itens
    print("\n2. CONTAGEM DE ITENS:")
    itens_count = contar_itens_xml(xml_content.encode('utf-8'))
    print(f"   Total de itens: {itens_count}")
    
    # Testar parser
    print("\n3. EXTRAÇÃO DE DADOS:")
    try:
        # Criar arquivo temporário
        with tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False, encoding='utf-8') as f:
            f.write(xml_content)
            temp_path = f.name
        
        # Extrair dados
        dados_extraidos = parse_nfe(temp_path)
        print(f"   Linhas extraídas: {len(dados_extraidos)}")
        
        if dados_extraidos:
            item = dados_extraidos[0]
            print(f"   Campos disponíveis: {len(item.keys())}")
            print("\n   Amostra dos dados extraídos:")
            for key, value in sorted(item.items())[:10]:  # Mostrar apenas 10 primeiros
                print(f"     {key}: {value}")
            
            if len(item.keys()) > 10:
                print(f"     ... e mais {len(item.keys()) - 10} campos")
        
        # Limpar arquivo temporário
        os.unlink(temp_path)
        return True
        
    except Exception as e:
        print(f"   ERRO na extração: {e}")
        return False

# XML da NFe1 (versão 1.10)
xml_nfe1 = '''<?xml version="1.0" encoding="UTF-8"?>
<NFe>
   <infNFe Id="NFe35080599999090910270550010000000015180051273" versao="1.10">
      <ide>
         <cUF>35</cUF>
         <cNF>518005127</cNF>
         <natOp>Venda a vista</natOp>
         <indPag>0</indPag>
         <mod>55</mod>
         <serie>1</serie>
         <nNF>1</nNF>
         <dEmi>2008-05-06</dEmi>
         <dSaiEnt>2008-05-06</dSaiEnt>
         <tpNF>0</tpNF>
         <cMunFG>3550308</cMunFG>
         <tpImp>1</tpImp>
         <tpEmis>1</tpEmis>
         <cDV>3</cDV>
         <tpAmb>2</tpAmb>
         <finNFe>1</finNFe>
         <procEmi>0</procEmi>
         <verProc>NF-eletronica.com</verProc>
      </ide>
      <emit>
         <CNPJ>99999090910270</CNPJ>
         <xNome>NF-e Associacao NF-e</xNome>
         <xFant>NF-e</xFant>
         <enderEmit>
            <xLgr>Rua Central</xLgr>
            <nro>100</nro>
            <xCpl>Fundos</xCpl>
            <xBairro>Distrito Industrial</xBairro>
            <cMun>3502200</cMun>
            <xMun>Angatuba</xMun>
            <UF>SP</UF>
            <CEP>17100171</CEP>
            <cPais>1058</cPais>
            <xPais>Brasil</xPais>
            <fone>1733021717</fone>
         </enderEmit>
         <IE>123456789012</IE>
      </emit>
      <dest>
         <CNPJ>00000000000191</CNPJ>
         <xNome>DISTRIBUIDORA DE AGUAS MINERAIS</xNome>
         <enderDest>
            <xLgr>AV DAS FONTES</xLgr>
            <nro>1777</nro>
            <xCpl>10 ANDAR</xCpl>
            <xBairro>PARQUE FONTES</xBairro>
            <cMun>5030801</cMun>
            <xMun>Sao Paulo</xMun>
            <UF>SP</UF>
            <CEP>13950000</CEP>
            <cPais>1058</cPais>
            <xPais>BRASIL</xPais>
            <fone>1932011234</fone>
         </enderDest>
         <IE />
      </dest>
      <det nItem="1">
         <prod>
            <cProd>00001</cProd>
            <cEAN />
            <xProd>Agua Mineral</xProd>
            <CFOP>5101</CFOP>
            <uCom>dz</uCom>
            <qCom>1000000.0000</qCom>
            <vUnCom>1</vUnCom>
            <vProd>10000000.00</vProd>
            <cEANTrib />
            <uTrib>und</uTrib>
            <qTrib>12000000.0000</qTrib>
            <vUnTrib>1</vUnTrib>
         </prod>
         <imposto>
            <ICMS>
               <ICMS00>
                  <orig>0</orig>
                  <CST>00</CST>
                  <modBC>0</modBC>
                  <vBC>10000000.00</vBC>
                  <pICMS>18.00</pICMS>
                  <vICMS>1800000.00</vICMS>
               </ICMS00>
            </ICMS>
         </imposto>
      </det>
      <det nItem="2">
         <prod>
            <cProd>00002</cProd>
            <cEAN />
            <xProd>Agua Mineral</xProd>
            <CFOP>5101</CFOP>
            <uCom>pack</uCom>
            <qCom>5000000.0000</qCom>
            <vUnCom>2</vUnCom>
            <vProd>10000000.00</vProd>
            <cEANTrib />
            <uTrib>und</uTrib>
            <qTrib>3000000.0000</qTrib>
            <vUnTrib>0.3333</vUnTrib>
         </prod>
         <imposto>
            <ICMS>
               <ICMS00>
                  <orig>0</orig>
                  <CST>00</CST>
                  <modBC>0</modBC>
                  <vBC>10000000.00</vBC>
                  <pICMS>18.00</pICMS>
                  <vICMS>1800000.00</vICMS>
               </ICMS00>
            </ICMS>
         </imposto>
      </det>
      <total>
         <ICMSTot>
            <vBC>20000000.00</vBC>
            <vICMS>18.00</vICMS>
            <vBCST>0</vBCST>
            <vST>0</vST>
            <vProd>20000000.00</vProd>
            <vFrete>0</vFrete>
            <vSeg>0</vSeg>
            <vDesc>0</vDesc>
            <vII>0</vII>
            <vIPI>0</vIPI>
            <vPIS>130000.00</vPIS>
            <vCOFINS>400000.00</vCOFINS>
            <vOutro>0</vOutro>
            <vNF>20000000.00</vNF>
         </ICMSTot>
      </total>
      <transp>
         <modFrete>0</modFrete>
         <transporta>
            <CNPJ>99171171000191</CNPJ>
            <xNome>Distribuidora de Bebidas Fazenda de SP Ltda.</xNome>
            <IE>171999999119</IE>
            <xEnder>Rua Central 100 - Fundos - Distrito Industrial</xEnder>
            <xMun>SAO PAULO</xMun>
            <UF>SP</UF>
         </transporta>
         <veicTransp>
            <placa>BXI1717</placa>
            <UF>SP</UF>
            <RNTC>123456789</RNTC>
         </veicTransp>
         <vol>
            <qVol>10000</qVol>
            <esp>CAIXA</esp>
            <marca>LINDOYA</marca>
            <nVol>500</nVol>
            <pesoL>1000000000.000</pesoL>
            <pesoB>1200000000.000</pesoB>
         </vol>
      </transp>
   </infNFe>
</NFe>'''

# Testar diferentes versões
if __name__ == "__main__":
    print("TESTE DE EXTRAÇÃO COM XMLs REAIS")
    print("Verificando se as mudanças não prejudicaram a extração...")
    
    testar_xml_real(xml_nfe1, "NFe1 (versão 1.10)")
    
    print(f"\n{'='*60}")
    print("RESUMO DO TESTE")
    print(f"{'='*60}")
    print("✓ Se todos os testes passaram, a extração está funcionando")
    print("✗ Se houve erros, preciso corrigir os problemas")
