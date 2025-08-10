#!/usr/bin/env python3
"""
Script SIMPLES para executar o Datarum
"""

if __name__ == "__main__":
    print("🚀 Iniciando Datarum API...")
    print()
    
    try:
        import uvicorn
        from main import app
        import config
        
        print("📍 Servidor rodando em: http://localhost:8000")
        print("📖 Documentação em: http://localhost:8000/docs")
        print("🔄 Auto-reload ativado para desenvolvimento")
        print(f"🌐 CORS permitido para: {', '.join(config.CORS_ORIGINS)}")
        print()
        print("⚠️  IMPORTANTE sobre URLs:")
        print("   Para produção, edite o arquivo config.py")
        print("   e adicione suas URLs reais na lista CORS_ORIGINS")
        print()
        
        uvicorn.run(
            "main:app", 
            host="localhost", 
            port=8000, 
            reload=config.DEBUG,
            log_level="info"
        )
        
    except ImportError as e:
        print(f"❌ Dependência não encontrada: {e}")
        print("📦 Execute: pip install -r requirements.txt")
    except Exception as e:
        print(f"❌ Erro ao iniciar: {e}")
