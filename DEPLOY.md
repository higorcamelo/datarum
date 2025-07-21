# Deploy do Sigonota Web

## Preparação para Deploy no Vercel

Este projeto está configurado para deploy no Vercel com:
- Frontend Vue.js (Vite)
- Backend FastAPI (Python)

### Arquivos de Deploy Criados:

1. **`vercel.json`** - Configuração principal do Vercel
2. **`.env.example`** - Exemplo de variáveis de ambiente
3. **Scripts de build** - Adicionados ao package.json

### Deploy Manual no Vercel:

1. **Instalar Vercel CLI:**
```bash
npm i -g vercel
```

2. **Login no Vercel:**
```bash
vercel login
```

3. **Deploy:**
```bash
vercel --prod
```

### Configurar Variáveis de Ambiente no Vercel:

No dashboard do Vercel, adicione:
- `ENVIRONMENT=production`
- `LOG_LEVEL=INFO`
- `CORS_ORIGINS=["https://seu-dominio.vercel.app"]`
- `MAX_FILES_COUNT=50`
- `MAX_FILE_SIZE=10485760`

### Deploy via GitHub:

1. Conecte o repositório ao Vercel
2. Configure as variáveis de ambiente
3. Deploy automático a cada push

### URLs após Deploy:

- **API**: `https://seu-projeto.vercel.app/api/`
- **Frontend**: `https://seu-projeto.vercel.app/`
- **Health Check**: `https://seu-projeto.vercel.app/api/health`

### Estrutura de Rotas:

- `/api/*` → Backend FastAPI
- `/*` → Frontend Vue.js

O arquivo `vercel.json` configura automaticamente essas rotas.
