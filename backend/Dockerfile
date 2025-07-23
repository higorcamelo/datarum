# Backend isolado para Fly.io - apenas API
FROM python:3.12-alpine
WORKDIR /app

# Dependências do sistema necessárias para pandas/openpyxl
RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    libxml2-dev \
    libxslt-dev \
    && rm -rf /var/cache/apk/*

# Copiar e instalar dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar código do backend
COPY . .

# Criar usuário não-root para segurança
RUN adduser -D -s /bin/sh app && \
    chown -R app:app /app
USER app

# Expor porta
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8080/health')" || exit 1

# Comando para rodar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
