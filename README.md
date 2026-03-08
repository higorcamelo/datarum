# Datarum

**Automação fiscal com inteligência e clareza**

Sistema web para processamento de arquivos XML de Notas Fiscais Eletrônicas (NFe), convertendo-os para planilhas Excel formatadas.

## **Sobre o Projeto**

O Datarum facilita o processo de extração e organização de dados de NFes, reduzindo a necessidade de processamento manual.

### **Funcionalidades**
-  Upload de múltiplos arquivos XML via drag & drop
-  Validação automática de arquivos e tamanhos
-  Processamento de dados de NFe com parsing de XML
-  Geração de planilhas Excel formatadas
-  Interface responsiva com feedback
-  Suporte para múltiplas versões de NFe (1.10, 2.00, 3.10, 4.00)

## **Tecnologias Utilizadas**

### **Frontend**
- **Vue.js 3** - Framework JavaScript reativo moderno
- **Tailwind CSS** - Framework CSS utilitário com design system
- **Vite** - Bundler e servidor de desenvolvimento ultra-rápido

### **Backend**
- **FastAPI** - Framework Python para APIs de alta performance
- **Pandas** - Manipulação e análise avançada de dados
- **OpenPyXL** - Geração de arquivos Excel com formatação profissional
- **XML parsing** - Extração inteligente de dados estruturados

## **Como Executar**

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
cd frontend
npm install
npm run dev
```

### **Acessar aplicação**
- Frontend: `http://localhost:5173`
- API: `http://localhost:8000`

## **Funcionalidades Técnicas**

### **Validações**
- Formato XML obrigatório
- Tamanho máximo de 5MB por arquivo
- Verificação de estrutura NFe

### **Processamento**
- Parsing XML com tratamento de erros
- Extração de dados fiscais relevantes
- Formatação automática de valores
- Geração de planilha Excel

### **Segurança**
- Validação de tipos de arquivo
- Sanitização de nomes
- Tratamento de exceções
- Limpeza de arquivos temporários

## **Próximas Funcionalidades**

- [ ] Dashboard para visualização de dados
- [ ] Templates personalizados de planilha
- [ ] Relatórios automáticos de análise de dados
- [ ] Histórico de processamentos
- [ ] Alertas e notificações inteligentes

---

**Desenvolvido com ❤️ por Higor Camelo**

