# Build do Frontend Vue.js
FROM node:20-alpine AS frontend-build
WORKDIR /frontend

# Copiar package files do frontend
COPY frontend/sigonota-frontend/package*.json ./

# Instalar dependências (incluindo dev deps para build)
RUN npm ci

# Copiar código do frontend
COPY frontend/sigonota-frontend/ ./

# Build do frontend para produção
RUN npm run build

# Estágio final - Backend Python + Frontend estático
FROM python:3.12-alpine
WORKDIR /app

# Instalar dependências do sistema necessárias para pandas/openpyxl
RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    libxml2-dev \
    libxslt-dev \
    && rm -rf /var/cache/apk/*

# Copiar requirements e instalar dependências Python
COPY backend/requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar todo o código do backend
COPY backend/ .

# Copiar arquivos buildados do frontend para pasta static
COPY --from=frontend-build /frontend/dist ./static

# Criar usuário não-root para segurança
RUN adduser -D -s /bin/sh app && \
    chown -R app:app /app
USER app

# Expor porta 8000
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8000/health')" || exit 1

# Comando para rodar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]