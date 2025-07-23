"""
Versão simplificada da API para debug no Vercel
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

# App simples
app = FastAPI(title="Datarum API Test")

# CORS simples
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "Datarum API está funcionando!",
        "status": "online",
        "timestamp": datetime.now().isoformat(),
        "version": "simplified"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

# Para Vercel
app_instance = app
