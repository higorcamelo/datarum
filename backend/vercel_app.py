from mangum import Mangum
from main import app

# Converter FastAPI para handler compatível com Vercel
handler = Mangum(app)
