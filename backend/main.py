from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Libera CORS para o frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def ping():
    return {"message": "Sigonota backend rodando"}

@app.post("/processar/")
async def processar_nfes(xmls: list[UploadFile] = File(...), planilha: UploadFile = File(...)):
    # Aqui vai a lógica que você já tem no parse_nfe e salvar_em_excel
    return {"sucesso": True, "mensagem": "Arquivos processados com sucesso"}
