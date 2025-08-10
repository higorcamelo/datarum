# 📊 Datarum

**Automação fiscal com inteligência e clareza**

Sistema web profissional para processamento automático de arquivos XML de Notas Fiscais Eletrônicas (NFe), convertendo-os para planilhas Excel formatadas com inteligência de dados.

## 🎯 **Sobre o Projeto**

O Datarum revoluciona o processo de extração e organização de dados de NFes, eliminando a necessidade de processamento manual e oferecendo uma interface moderna e intuitiva que transforma dados brutos em insights valiosos.

### **Funcionalidades**
- ✅ Upload de múltiplos arquivos XML via drag & drop
- ✅ Validação automática de arquivos e tamanhos
- ✅ Processamento inteligente de dados de NFe com parsing XML
- ✅ Geração de planilhas Excel formatadas profissionalmente
- ✅ Interface responsiva e moderna com feedback rico
- ✅ Estatísticas em tempo real e análise de dados
- ✅ Suporte para múltiplas versões de NFe (1.10, 2.00, 3.10, 4.00)

## 🛠️ **Tecnologias Utilizadas**

### **Frontend**
- **Vue.js 3** - Framework JavaScript reativo moderno
- **Tailwind CSS** - Framework CSS utilitário com design system
- **Vite** - Bundler e servidor de desenvolvimento ultra-rápido

### **Backend**
- **FastAPI** - Framework Python para APIs de alta performance
- **Pandas** - Manipulação e análise avançada de dados
- **OpenPyXL** - Geração de arquivos Excel com formatação profissional
- **XML parsing** - Extração inteligente de dados estruturados

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

- [ ] Dashboard analítico com insights avançados
- [ ] Suporte a outros tipos de XML fiscal
- [ ] Templates personalizados de planilha
- [ ] Relatórios automáticos de análise de dados
- [ ] API para integrações externas
- [ ] Histórico de processamentos
- [ ] Alertas e notificações inteligentes

## 🎨 **Identidade Visual**

O Datarum utiliza uma paleta de cores profissional baseada em tons de índigo e cinza, transmitindo confiança, tecnologia e inteligência. A interface foi projetada para ser limpa, moderna e focada na experiência do usuário.

## 📄 **Licença**

© 2024 Datarum. Projeto desenvolvido para transformar dados em inteligência.

---

**Datarum** - *Automação fiscal com inteligência e clareza*

**Desenvolvido com ❤️ por Higor Camelo**

