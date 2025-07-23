# Estágio 1: Build do frontend
FROM node:22-alpine AS frontend-build

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

# Dependências do sistema
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev libxml2-dev libxslt-dev

# Instalar dependências Python
COPY backend/requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar código do backend
COPY backend/ .

# Copiar frontend buildado
COPY --from=frontend-build /frontend/dist ./static/

# Usuário não-root
RUN adduser -D -s /bin/sh app && chown -R app:app /app
USER app

# Expor porta
EXPOSE 8080

# Comando correto para FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
