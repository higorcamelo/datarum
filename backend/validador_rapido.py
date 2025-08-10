#!/usr/bin/env python3
"""
Validador Rápido de Filtragem - Backend v1.1
============================================
Script simples para validar se a filtragem está funcionando
"""

import json
import os
import sys
import tempfile

# Imports do projeto
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils.xml_parser import parse_nfe
from config_v11 import CAMPOS_DISPONIVEIS, PRESETS, get_campos_por_preset

def test_presets_rapido():
    """Teste rápido dos presets com XML simples"""
    
    # XML mínimo funcional
    xml_test = '''<?xml version="1.0" encoding="UTF-8"?>
<nfeProc xmlns="http://www.portalfiscal.inf.br/nfe" versao="4.00">
  <NFe>
    <infNFe Id="NFe35240101234567890123650010000123451234567890" versao="4.00">
      <ide>
        <nNF>12345</nNF>
        <serie>1</serie>
        <dhEmi>2024-01-15T10:30:00-03:00</dhEmi>
        <natOp>Venda</natOp>
      </ide>
      <emit>
        <xNome>Empresa Teste LTDA</xNome>
        <CNPJ>12345678901234</CNPJ>
        <IE>123456789</IE>
        <enderEmit>
          <xLgr>Rua Teste</xLgr>
          <xMun>São Paulo</xMun>
          <UF>SP</UF>
        </enderEmit>
      </emit>
      <dest>
        <xNome>Cliente Teste</xNome>
      </dest>
      <det nItem="1">
        <prod>
          <cProd>PROD001</cProd>
          <xProd>Produto Teste</xProd>
          <CFOP>5102</CFOP>
          <qCom>1.0000</qCom>
          <vUnCom>100.0000</vUnCom>
          <vProd>100.00</vProd>
        </prod>
        <imposto>
          <ICMS>
            <ICMS00>
              <vICMS>18.00</vICMS>
            </ICMS00>
          </ICMS>
        </imposto>
      </det>
      <total>
        <ICMSTot>
          <vNF>100.00</vNF>
        </ICMSTot>
      </total>
    </infNFe>
  </NFe>
</nfeProc>'''
    
    print("🔍 VALIDAÇÃO RÁPIDA DE FILTRAGEM")
    print("=" * 40)
    
    # Salvar XML temporário
    with tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False, encoding='utf-8') as f:
        f.write(xml_test)
        xml_path = f.name
    
    try:
        resultados = []
        
        # Testar cada preset
        for preset_nome in PRESETS.keys():
            campos = get_campos_por_preset(preset_nome)
            
            try:
                itens = parse_nfe(xml_path, campos_selecionados=campos)
                
                if itens and len(itens) > 0:
                    campos_extraidos = list(itens[0].keys())
                    print(f"✅ {preset_nome:10} | {len(campos_extraidos):2d}/{len(campos):2d} campos")
                    
                    # Mostrar alguns exemplos
                    exemplo = {}
                    for i, (k, v) in enumerate(itens[0].items()):
                        if i < 3:  # Primeiros 3 campos
                            exemplo[k] = v[:30] + "..." if isinstance(v, str) and len(v) > 30 else v
                    
                    print(f"   📋 Exemplo: {exemplo}")
                    resultados.append({"preset": preset_nome, "sucesso": True, "campos": len(campos_extraidos)})
                else:
                    print(f"❌ {preset_nome:10} | Nenhum item processado")
                    resultados.append({"preset": preset_nome, "sucesso": False, "campos": 0})
                    
            except Exception as e:
                print(f"💥 {preset_nome:10} | ERRO: {str(e)[:50]}...")
                resultados.append({"preset": preset_nome, "sucesso": False, "erro": str(e)})
        
        # Teste especial: campos específicos
        print("\n🎯 TESTE DE CAMPOS ESPECÍFICOS")
        print("-" * 30)
        
        campos_teste = ["numero_nf", "emitente", "descricao_produto", "valor_total_item"]
        itens = parse_nfe(xml_path, campos_selecionados=campos_teste)
        
        if itens:
            print(f"✅ Filtro customizado: {len(itens[0].keys())} campos extraídos")
            print(f"   🔍 Campos: {', '.join(itens[0].keys())}")
            print(f"   📊 Valores: {list(itens[0].values())}")
        else:
            print("❌ Filtro customizado falhou")
        
        # Resumo final
        sucessos = len([r for r in resultados if r.get("sucesso", False)])
        total = len(resultados)
        
        print(f"\n📊 RESUMO: {sucessos}/{total} presets OK")
        
        if sucessos == total:
            print("🎉 FILTRAGEM FUNCIONANDO PERFEITAMENTE!")
            return True
        else:
            print("⚠️ Alguns presets falharam - verifique os logs acima")
            return False
            
    finally:
        os.unlink(xml_path)

def test_campos_count():
    """Mostra contagem de campos por categoria"""
    print("\n📈 ESTATÍSTICAS DOS CAMPOS")
    print("-" * 30)
    
    categorias = {}
    for campo, config in CAMPOS_DISPONIVEIS.items():
        cat = config.get("categoria", "outros")
        if cat not in categorias:
            categorias[cat] = []
        categorias[cat].append(campo)
    
    total = 0
    for cat, campos in sorted(categorias.items()):
        print(f"📁 {cat:12} | {len(campos):2d} campos")
        total += len(campos)
    
    print(f"📊 {'TOTAL':12} | {total:2d} campos")
    
    # Campos por preset
    print(f"\n📋 PRESETS:")
    for preset, config in PRESETS.items():
        campos_count = len(config.get("campos", []))
        print(f"🎯 {preset:10} | {campos_count:2d} campos")

def main():
    """Função principal"""
    try:
        sucesso = test_presets_rapido()
        test_campos_count()
        
        print("\n" + "=" * 40)
        if sucesso:
            print("✅ VALIDAÇÃO CONCLUÍDA COM SUCESSO!")
            return 0
        else:
            print("⚠️ VALIDAÇÃO COM PROBLEMAS")
            return 1
            
    except Exception as e:
        print(f"💥 ERRO NA VALIDAÇÃO: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
