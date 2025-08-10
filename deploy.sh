#!/usr/bin/env bash
# Script de deploy simplificado para Vercel

echo "🚀 Preparando deploy do Sigonota Web..."

# Verificar se está na raiz do projeto
if [ ! -f "vercel.json" ]; then
    echo "❌ Execute este script na raiz do projeto (onde está o vercel.json)"
    exit 1
fi

echo "📦 Verificando dependências..."

# Verificar se o Vercel CLI está instalado
if ! command -v vercel &> /dev/null; then
    echo "🔧 Instalando Vercel CLI..."
    npm install -g vercel
fi

echo "🏗️ Fazendo build local para testar..."

# Build do frontend
cd frontend/sigonota-frontend
npm install
npm run build

if [ $? -ne 0 ]; then
    echo "❌ Erro no build do frontend"
    exit 1
fi

cd ../..

echo "✅ Build OK! Iniciando deploy..."

# Deploy
vercel --prod

echo "🎉 Deploy concluído!"
echo "📋 Não esqueça de configurar as variáveis de ambiente no dashboard do Vercel"
echo "📋 Exemplo: CORS_ORIGINS=[\"https://seu-dominio.vercel.app\"]"
