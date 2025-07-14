# 📊 Sigonota

Sistema web para processamento automático de arquivos XML de Notas Fiscais Eletrônicas (NFe), convertendo-os para planilhas Excel formatadas.

## 🎯 **Sobre o Projeto**

O Sigonota automatiza o processo de extração e organização de dados de NFes, eliminando a necessidade de processamento manual e oferecendo uma interface moderna e intuitiva.

### **Funcionalidades**
- ✅ Upload de múltiplos arquivos XML via drag & drop
- ✅ Validação automática de arquivos e tamanhos
- ✅ Processamento de dados de NFe com parsing XML
- ✅ Geração de planilhas Excel formatadas
- ✅ Interface responsiva e moderna
- ✅ Feedback visual de progresso e erros

## 🛠️ **Tecnologias Utilizadas**

### **Frontend**
- **Vue.js 3** - Framework JavaScript reativo
- **Tailwind CSS** - Framework CSS utilitário
- **Vite** - Bundler e servidor de desenvolvimento

### **Backend**
- **FastAPI** - Framework Python para APIs
- **Pandas** - Manipulação e análise de dados
- **OpenPyXL** - Geração de arquivos Excel
- **XML parsing** - Extração de dados estruturados

## 🚀 **Como Executar**

### **Pré-requisitos**
- Python 3.8+
- Node.js 16+
- npm ou yarn

### **Backend**
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### **Frontend**
```bash
cd frontend/sigonota-frontend
npm install
npm run dev
```

### **Acessar aplicação**
- Frontend: `http://localhost:5173`
- API: `http://localhost:8000`

## 📁 **Estrutura do Projeto**

```
sigonota-web/
├── backend/
│   ├── main.py              # API principal
│   ├── excel_handler.py     # Processamento de Excel
│   └── requirements.txt     # Dependências Python
├── frontend/
│   └── sigonota-frontend/
│       ├── src/
│       │   ├── App.vue      # Componente principal
│       │   └── main.js      # Entry point
│       └── package.json     # Dependências Node.js
└── README.md
```

## 🎨 **Interface**

A interface oferece uma experiência moderna com:
- Upload por arrastar e soltar
- Validação em tempo real
- Lista de arquivos com status
- Botões de ação intuitivos
- Feedback visual de processamento

## 📋 **Fluxo de Uso**

1. **Upload**: Arraste arquivos XML ou clique para selecionar
2. **Validação**: Sistema verifica formato e tamanho dos arquivos
3. **Nomeação**: Defina o nome da planilha ou use sugestão automática
4. **Processamento**: Clique em "Processar" e aguarde
5. **Download**: Planilha Excel é gerada e baixada automaticamente

## 🔧 **Funcionalidades Técnicas**

### **Validações**
- Formato XML obrigatório
- Limite de 50 arquivos por vez
- Tamanho máximo de 5MB por arquivo
- Verificação de estrutura NFe

### **Processamento**
- Parsing XML com tratamento de erros
- Extração de dados fiscais relevantes
- Formatação automática de valores
- Geração de Excel com estilos

### **Segurança**
- Validação de tipos de arquivo
- Sanitização de nomes
- Tratamento de exceções
- Limpeza de arquivos temporários

## 💡 **Próximas Funcionalidades**

- [ ] Suporte a outros tipos de XML fiscal
- [ ] Templates personalizados de planilha
- [ ] Relatórios de análise de dados
- [ ] API para integrações externas

## 📄 **Licença**

Projeto desenvolvido para fins educacionais e de portfólio.

---

**Desenvolvido com ❤️ por Higor Camelo**

