# Estágio 1: Build do frontend
FROM node:20-alpine AS frontend-build

WORKDIR /frontend

# Copiar package.json do frontend
COPY frontend/sigonota-frontend/package*.json ./
RUN npm ci --only=production

# Copiar código do frontend e buildar
COPY frontend/sigonota-frontend/ ./
RUN npm run build

# Estágio 2: Backend Python + frontend servido via FastAPI
FROM python:3.12-alpine

WORKDIR /app

# Instalar dependências do sistema
RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    && rm -rf /var/cache/apk/*

# Copiar requirements do backend
COPY backend/requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copiar código do backend
COPY backend/ .

# Copiar frontend buildado
COPY --from=frontend-build /frontend/dist ./static/

# Criar usuário não-root
RUN adduser -D -s /bin/sh app && chown -R app:app /app
USER app

# Expor porta
EXPOSE 8000

# Comando para rodar (FastAPI vai servir tanto API quanto static)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
