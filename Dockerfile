FROM python:3.12-alpine

WORKDIR /app

# Instalar dependências do sistema necessárias para pandas/openpyxl
RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    && rm -rf /var/cache/apk/*

# Copiar requirements
COPY backend/requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copiar todo o código
COPY backend/ .

# Criar usuário não-root para segurança
RUN adduser -D -s /bin/sh app && chown -R app:app /app
USER app

# Expor porta
EXPOSE 8000

# Comando para rodar
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
