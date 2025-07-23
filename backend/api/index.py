from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

# Vercel
from mangum import Mangum
handler = Mangum(app)
