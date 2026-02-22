if __name__ == "__main__":
    print("Iniciando Datarum API...")
    print()
    
    try:
        import uvicorn
        from main import app
        import config
        
        print(f"🌐 CORS permitido para: {', '.join(config.CORS_ORIGINS)}")
        
        uvicorn.run(
            "main:app", 
            host="localhost", 
            port=8000, 
            reload=config.DEBUG,
            log_level="info"
        )
        
    except ImportError as e:
        print(f"Dependência não encontrada: {e}")

    except Exception as e:
        print(f"Erro ao iniciar: {e}")
