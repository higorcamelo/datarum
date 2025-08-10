# Datarum API - Sistema Robusto de Conversão NFe

Sistema profissional para conversão de XMLs de Nota Fiscal Eletrônica em planilhas Excel, com tratamento robusto de erros, logging avançado, métricas e escalabilidade.

## 🚀 Características Principais

### ✅ Sistema de Tratamento de Erros
- **Exceções customizadas** com códigos de erro padronizados
- **Validação robusta** de arquivos e conteúdo
- **Mensagens de erro claras** para usuários finais
- **Logging detalhado** para desenvolvedores

### ✅ Logging Avançado
- **Logging estruturado** com contexto de requisição
- **Diferentes níveis** por ambiente (dev/staging/prod)
- **Rotação automática** de arquivos de log
- **Formato JSON** para produção

### ✅ Métricas e Monitoramento
- **Métricas de performance** em tempo real
- **Health checks** avançados
- **Monitoramento de recursos** (CPU, memória, disco)
- **Estatísticas de processamento**

### ✅ Escalabilidade
- **Rate limiting** configurável
- **Controle de concorrência**
- **Timeouts** apropriados
- **Middleware de segurança**

### ✅ Configuração Flexível
- **Configuração por ambiente** (.env)
- **Validação de configurações**
- **Defaults inteligentes**

## 📁 Estrutura do Projeto

```
backend/
├── main.py                 # API principal
├── config.py              # Configurações centralizadas
├── run.py                 # Script de inicialização
├── requirements.txt       # Dependências
├── .env.example          # Exemplo de configuração
├── utils/
│   ├── exceptions.py     # Sistema de exceções
│   ├── logging.py        # Sistema de logging
│   ├── middleware.py     # Middlewares
│   ├── metrics.py        # Métricas e monitoramento
│   ├── validation.py     # Validação robusta
│   ├── xml_parser.py     # Parser de XML
│   └── excel_handler.py  # Geração de Excel
└── logs/                 # Diretório de logs
```

## 🛠️ Instalação e Configuração

### 1. Dependências
```bash
# Instalar dependências
pip install -r requirements.txt
```

### 2. Configuração
```bash
# Copiar arquivo de configuração
cp .env.example .env

# Editar configurações (opcional)
# As configurações padrão funcionam para desenvolvimento
```

### 3. Inicialização
```bash
# Modo mais simples - tudo automático
python run.py

# Ou comandos específicos:
python run.py setup    # Configurar ambiente
python run.py check    # Verificar dependências
python run.py dev      # Iniciar servidor de desenvolvimento
python run.py test     # Executar testes
```

## 🔧 Configurações Principais

### Ambientes Suportados
- **development**: Logs detalhados, debug ativo, limites baixos
- **staging**: Logs moderados, alguns recursos de produção
- **production**: Logs mínimos, máxima performance, segurança

### Configurações Chave (.env)
```bash
# Ambiente
ENVIRONMENT=development  # development/staging/production

# Limites
MAX_FILE_SIZE=5242880   # 5MB
MAX_FILES_COUNT=200      # Máximo de arquivos por request

# Performance
MAX_CONCURRENT_REQUESTS=10  # Requests simultâneas
RATE_LIMIT_PER_MINUTE=60   # Limite de requests por minuto
WORKER_TIMEOUT=300         # Timeout em segundos

# Logging
LOG_LEVEL=INFO            # DEBUG/INFO/WARNING/ERROR
LOG_FILE=logs/datarum.log # Arquivo de log
```

## 📊 Endpoints da API

### `POST /processar`
Processa XMLs e retorna planilha Excel
- **Upload**: Até 50 arquivos XML (5MB cada)
- **Validação**: Completa de arquivos e conteúdo
- **Retorno**: Arquivo Excel para download

### `POST /processar-info`
Retorna estatísticas sem gerar arquivo
- **Mesmo input** do `/processar`
- **Retorno**: JSON com estatísticas detalhadas

### `GET /health`
Health check avançado
- **Sistema**: CPU, memória, disco
- **Aplicação**: Status, métricas, tempo ativo

### `GET /metrics`
Métricas da aplicação (dev/staging apenas)
- **Performance**: Tempo de resposta, throughput
- **Recursos**: Uso de sistema
- **Erros**: Contadores por tipo

## 🛡️ Sistema de Tratamento de Erros

### Códigos de Erro Padronizados
- **4000-4099**: Erros de validação
- **4100-4199**: Erros de processamento XML
- **4200-4299**: Erros de geração Excel
- **5000-5099**: Erros de sistema
- **5100-5199**: Erros de recursos

### Exemplo de Resposta de Erro
```json
{
  "error_code": "4001",
  "message": "O arquivo 'exemplo.txt' não é um XML válido.",
  "details": {
    "filename": "exemplo.txt",
    "detected_mime_type": "text/plain"
  },
  "timestamp": "2025-07-21T10:30:00Z",
  "request_id": "req-123-456"
}
```

## 📈 Monitoramento e Métricas

### Métricas Coletadas
- **Requests**: Total, por endpoint, tempo de resposta
- **Arquivos**: Processados, tamanho, tempo de parsing
- **Sistema**: CPU, memória, disco
- **Erros**: Por tipo, frequência

### Logs Estruturados
```json
{
  "timestamp": "2025-07-21T10:30:00Z",
  "service": "datarum-api",
  "level": "INFO",
  "message": "File processing completed",
  "request_id": "req-123",
  "files_count": 10,
  "total_items": 50,
  "duration_ms": 1250
}
```

## 🔄 Middleware Stack

1. **ErrorHandlingMiddleware**: Captura e formata erros
2. **SecurityHeadersMiddleware**: Headers de segurança
3. **TimeoutMiddleware**: Timeout de requests
4. **ConcurrentRequestsMiddleware**: Controle de concorrência
5. **RateLimitMiddleware**: Rate limiting
6. **RequestTrackingMiddleware**: Logging e métricas
7. **HealthCheckMiddleware**: Health checks rápidos

## 🚦 Validação Robusta

### Validação de Arquivos
- **Tipo**: Verificação MIME real
- **Tamanho**: Individual e por lote
- **Quantidade**: Limite configurável
- **Nome**: Sanitização automática

### Validação de XML
- **Estrutura**: Elementos obrigatórios NFe
- **Versão**: Suporte 1.10 a 4.00
- **Encoding**: Detecção automática
- **Conteúdo**: Validação de dados extraídos

## 🎯 Performance e Escalabilidade

### Otimizações Implementadas
- **Processamento assíncrono** onde possível
- **Reutilização de conexões**
- **Limpeza automática** de arquivos temporários
- **Controle de memória** por request

### Limites Configuráveis
- **Desenvolvimento**: 5 requests simultâneas, 30/min
- **Staging**: 20 requests simultâneas, 80/min  
- **Produção**: 50 requests simultâneas, 100/min

## 🔐 Segurança

### Headers de Segurança
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY`
- `X-XSS-Protection: 1; mode=block`
- `Content-Security-Policy` (produção)

### Validações de Segurança
- **Sanitização** de nomes de arquivo
- **Validação** de tipos MIME
- **Limpeza** de arquivos temporários
- **Rate limiting** por IP

## 🧪 Testes e Qualidade

### Executar Testes
```bash
python run.py test
```

### Verificar Health
```bash
curl http://localhost:8000/health
```

### Verificar Métricas
```bash
curl http://localhost:8000/metrics
```

## 📝 Logging

### Níveis por Ambiente
- **Development**: DEBUG - Tudo detalhado
- **Staging**: INFO - Operações importantes
- **Production**: WARNING - Apenas problemas

### Localização dos Logs
- **Console**: Sempre ativo
- **Arquivo**: `logs/datarum.log` (se configurado)
- **Rotação**: Automática (10MB, 5 backups)

## 🚀 Deploy em Produção

### Configurações Recomendadas
```bash
# .env para produção
ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=WARNING
MAX_CONCURRENT_REQUESTS=50
RATE_LIMIT_PER_MINUTE=100
ENABLE_CACHE=true
CORS_ORIGINS=https://app.datarum.com.br
```

### Comando de Produção
```bash
# Com gunicorn (recomendado)
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app

# Ou uvicorn simples
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

## 🔍 Troubleshooting

### Problemas Comuns

1. **Erro de dependências**
   ```bash
   python run.py check
   pip install -r requirements.txt
   ```

2. **Arquivo muito grande**
   - Ajustar `MAX_FILE_SIZE` no .env
   - Verificar espaço em disco

3. **Rate limit atingido**
   - Aguardar ou ajustar `RATE_LIMIT_PER_MINUTE`

4. **Timeout**
   - Reduzir número de arquivos
   - Ajustar `WORKER_TIMEOUT`

### Logs de Debug
```bash
# Ativar logs detalhados
echo "LOG_LEVEL=DEBUG" >> .env
python run.py dev
```

---

## 📞 Suporte

Este sistema foi projetado para ser robusto e auto-suficiente. Em caso de problemas:

1. Verificar logs em `logs/datarum.log`
2. Consultar endpoint `/health` para status do sistema
3. Verificar métricas em `/metrics` (dev/staging)
4. Revisar configurações no arquivo `.env`

**Versão**: 1.0.0 - Sistema Robusto  
**Ambiente**: Configurável (dev/staging/prod)  
**Compatibilidade**: NFe versões 1.10 - 4.00
