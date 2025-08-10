#!/usr/bin/env python3
"""
Validação Completa do Sistema v1.1 - One-Click Test
===================================================
Script único para validar TUDO: filtragem, presets, backend, testes
Execute este script sempre que quiser ter certeza total do funcionamento
"""

import os
import sys
import subprocess
import time
from pathlib import Path

def run_command(cmd, description):
    """Executa comando e retorna resultado"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return False, "", "Timeout"
    except Exception as e:
        return False, "", str(e)

def main():
    """Executa validação completa do sistema"""
    print("🚀 VALIDAÇÃO COMPLETA DO SISTEMA v1.1")
    print("=" * 50)
    print("⏰ Início:", time.strftime("%Y-%m-%d %H:%M:%S"))
    print()
    
    # Verificar se estamos no diretório correto
    backend_dir = Path(__file__).parent
    os.chdir(backend_dir)
    
    testes = [
        {
            "comando": "python validador_rapido.py",
            "nome": "🎯 Validação Rápida (Presets & Filtragem)",
            "critico": True
        },
        {
            "comando": "python test_robustez_filtragem.py",
            "nome": "🔬 Teste de Robustez",
            "critico": True
        },
        {
            "comando": "python test_validacao_filtragem.py",
            "nome": "🔍 Validação de Consistência",
            "critico": False
        },
        {
            "comando": "python test_simples_v11.py",
            "nome": "📋 Teste de Integração Básica",
            "critico": True
        },
        {
            "comando": "python test_servidor_v11.py",
            "nome": "🌐 Teste do Servidor Backend",
            "critico": True
        }
    ]
    
    resultados = []
    testes_criticos_falharam = 0
    
    for i, teste in enumerate(testes, 1):
        print(f"\n{i}️⃣ {teste['nome']}")
        print("-" * 40)
        
        sucesso, stdout, stderr = run_command(teste["comando"], f"Executando {teste['nome']}")
        
        if sucesso:
            print("✅ PASSOU")
            # Extrair informações importantes do output
            lines = stdout.strip().split('\n')
            importantes = [l for l in lines[-5:] if any(keyword in l.lower() for keyword in 
                         ['sucesso', 'ok', 'passou', 'aprovado', 'funcionando', '✅', '🎉'])]
            if importantes:
                print("📊 Resultado:", importantes[-1].strip())
        else:
            status = "❌ FALHOU (CRÍTICO)" if teste["critico"] else "⚠️ FALHOU"
            print(status)
            if teste["critico"]:
                testes_criticos_falharam += 1
            
            # Mostrar erro resumido
            if stderr:
                error_lines = stderr.strip().split('\n')
                print("❗ Erro:", error_lines[0][:80] + "..." if len(error_lines[0]) > 80 else error_lines[0])
            elif stdout:
                # Procurar por linhas com erro no stdout
                lines = stdout.strip().split('\n')
                error_lines = [l for l in lines if any(keyword in l.lower() for keyword in ['erro', 'falhou', 'failed', 'error', '❌', '💥'])]
                if error_lines:
                    print("❗ Erro:", error_lines[0][:80] + "..." if len(error_lines[0]) > 80 else error_lines[0])
        
        resultados.append({
            "nome": teste["nome"],
            "sucesso": sucesso,
            "critico": teste["critico"]
        })
        
        # Pequena pausa entre testes
        time.sleep(0.5)
    
    # Relatório final
    print("\n" + "=" * 50)
    print("📊 RELATÓRIO FINAL DA VALIDAÇÃO")
    print("=" * 50)
    
    total_testes = len(testes)
    testes_passou = len([r for r in resultados if r["sucesso"]])
    testes_falhou = total_testes - testes_passou
    
    print(f"📈 Total de testes: {total_testes}")
    print(f"✅ Sucessos: {testes_passou}")
    print(f"❌ Falhas: {testes_falhou}")
    print(f"🎯 Taxa de sucesso: {(testes_passou/total_testes)*100:.1f}%")
    
    # Detalhar resultados
    print(f"\n📋 DETALHAMENTO:")
    for resultado in resultados:
        status = "✅" if resultado["sucesso"] else ("🔥" if resultado["critico"] else "⚠️")
        criticidade = " (CRÍTICO)" if resultado["critico"] and not resultado["sucesso"] else ""
        print(f"{status} {resultado['nome']}{criticidade}")
    
    # Resultado final
    print(f"\n🎯 RESULTADO GERAL:")
    if testes_criticos_falharam == 0:
        if testes_passou == total_testes:
            print("🎉 SISTEMA 100% FUNCIONAL - PRONTO PARA PRODUÇÃO!")
            print("🔒 Todos os testes críticos passaram")
            print("✨ Filtragem de campos está funcionando perfeitamente")
            print("🚀 Backend v1.1 totalmente operacional")
            return 0
        else:
            print("✅ SISTEMA FUNCIONAL - Testes críticos OK")
            print("⚠️ Alguns testes não críticos falharam, mas sistema está operacional")
            return 0
    else:
        print("❌ SISTEMA COM PROBLEMAS CRÍTICOS")
        print(f"🔥 {testes_criticos_falharam} teste(s) crítico(s) falharam")
        print("⚠️ Não recomendado para produção até corrigir os problemas")
        return 1

def show_help():
    """Mostra informações de ajuda"""
    print("""
🔧 COMO USAR ESTE VALIDADOR
==========================

Este script executa uma validação completa do sistema v1.1, incluindo:

✅ Testes críticos (devem passar):
   • Validação rápida de presets e filtragem
   • Teste de robustez da filtragem
   • Teste de integração básica
   • Teste do servidor backend

⚠️ Testes opcionais (podem falhar sem impacto):
   • Validação de consistência interna

📋 INTERPRETANDO OS RESULTADOS:
   🎉 = Sistema 100% funcional
   ✅ = Sistema funcional (alguns avisos)
   ❌ = Problemas críticos encontrados

🚀 EXECUÇÃO:
   python validacao_completa.py
   
💡 DICA: Execute sempre após mudanças no código para garantir que
   a filtragem de campos continue funcionando corretamente.
""")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help', 'help']:
        show_help()
        sys.exit(0)
    
    start_time = time.time()
    result = main()
    end_time = time.time()
    
    print(f"\n⏰ Tempo total: {end_time - start_time:.1f}s")
    print(f"🏁 Finalizado: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    sys.exit(result)
