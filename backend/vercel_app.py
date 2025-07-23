from fastapi import FastAPI
from fastapi.responses import JSONResponse
from mangum import Mangum

# Criar uma app simples para testar se funciona
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API funcionando!"}

@app.post("/processar-info") 
async def processar_info():
    return {"message": "Endpoint funcionando!"}

# Handler para Vercel
handler = Mangum(app)
