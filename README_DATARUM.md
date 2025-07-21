# Datarum - Sistema de Conversão NFe 

## O que faz
Converte arquivos XML de Nota Fiscal Eletrônica (NFe) para planilhas Excel.

## Tecnologias
- **Backend**: FastAPI (Python)
- **Frontend**: Vue.js 3 + Vite
- **Conversão**: pandas + openpyxl + xmltodict

## Como usar

### 1. Instalar dependências
```bash
cd backend
pip install -r requirements.txt
```

### 2. Executar API
```bash
cd backend
python start.py
```

### 3. Executar Frontend
```bash
cd frontend/sigonota-frontend
npm install
npm run dev
```

## URLs importantes
- **API**: http://localhost:8000
- **Frontend**: http://localhost:5173
- **Documentação**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## Configuração

### Para Produção
Edite o arquivo `backend/config.py`:

```python
# Troque estas URLs pelas suas URLs reais:
CORS_ORIGINS = [
    "https://seudominio.com",
    "https://www.seudominio.com"
]

ENVIRONMENT = "production"
DEBUG = False
```

## Estrutura

```
backend/
├── main.py              # API principal
├── start.py             # Script para iniciar
├── config.py            # Configurações
├── validador.py         # Validação de XMLs
├── requirements.txt     # Dependências
└── utils/               # Utilitários
    ├── xml_parser.py    # Parser de XML
    └── excel_handler.py # Gerador de Excel

frontend/sigonota-frontend/
├── src/
│   ├── App.vue         # App principal
│   └── components/     # Componentes
└── package.json        # Dependências
```

## Recursos
- ✅ Upload múltiplo de XMLs
- ✅ Validação automática 
- ✅ Conversão para Excel
- ✅ Logging básico
- ✅ Health check
- ✅ CORS configurável
- ✅ Interface simples

## Logs
Os logs ficam em `backend/logs/`:
- `app.log` - Log geral da aplicação
- Console também mostra logs em tempo real

## Limites
- Máximo 20 arquivos por vez
- Máximo 10MB por arquivo
- Apenas arquivos XML de NFe

## Troubleshooting

### Erro de CORS
- Verifique se as URLs estão corretas em `config.py`
- Para desenvolvimento, localhost já está configurado

### Erro de dependências
```bash
pip install -r requirements.txt
```

### XML não é NFe válida
- Verifique se o arquivo é realmente uma NFe
- Alguns XMLs podem estar corrompidos

## Monitoramento
- Use `/health` para verificar se a API está funcionando
- Logs mostram estatísticas de processamento
- Tempo de resposta é logado automaticamente
