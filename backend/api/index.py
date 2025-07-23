import sys
import os

# Adicionar o diretório parent ao path para imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

# Handler para Vercel
handler = app
