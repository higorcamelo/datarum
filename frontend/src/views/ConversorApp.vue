<template>
  <div class="min-h-screen flex flex-col bg-gradient-to-br from-purple-100 via-white to-purple-200">
    <header class="p-4">
       <button @click="$emit('back')" class="text-purple-600 font-semibold hover:underline">
         ← Voltar para o Início
       </button>
    </header>

    <main class="flex-1 flex justify-center px-4 py-8">
      <div class="w-full max-w-7xl flex flex-col lg:flex-row gap-6 lg:gap-8">
        
        <div class="lg:w-80 space-y-6">
           <div class="bg-white p-6 rounded-2xl shadow-sm border border-purple-100">
              <h3 class="font-bold text-gray-800 mb-2">Resumo da Seleção</h3>
              <p class="text-3xl font-bold text-purple-600">{{ selectedFiles.length }}</p>
              <p class="text-sm text-gray-500">Arquivos XML selecionados</p>
              <button v-if="selectedFiles.length > 0" @click="clearFiles" class="mt-4 text-xs text-red-500 hover:underline">Remover todos</button>
           </div>
        </div>

        <div class="flex-1 max-w-2xl mx-auto order-1 lg:order-2">
          <div class="bg-white/90 rounded-3xl shadow-2xl p-10 border border-purple-100">
            
            <div 
              @dragover.prevent="dragOver = true" 
              @dragleave.prevent="dragOver = false" 
              @drop.prevent="handleDrop"
              :class="['border-2 border-dashed rounded-2xl p-8 text-center transition-all', dragOver ? 'border-purple-500 bg-purple-50' : 'border-purple-200']"
            >
              <input type="file" id="xmlUpload" multiple accept=".xml" class="hidden" @change="handleFileChange">
              <label for="xmlUpload" class="cursor-pointer block">
                <div class="text-purple-500 mb-2 text-4xl">📁</div>
                <p class="text-gray-600 font-medium">Arraste seus XMLs ou clique para selecionar</p>
              </label>
            </div>

            <ConfigPanel 
              v-if="selectedFiles.length > 0"
              v-model="camposSelecionados"
              v-model:preset="presetAtivo"
              :camposDisponiveis="camposDisponiveis"
            />

            <div class="mt-8">
              <label class="block text-sm font-semibold text-purple-700 mb-2">Nome da Planilha de Saída</label>
              <div class="flex gap-2">
                <input v-model="nomePlanilha" type="text" class="flex-1 p-3 rounded-xl border border-purple-200 focus:ring-2 focus:ring-purple-500 outline-none" placeholder="Ex: Notas_Janeiro_2024">
                <button @click="usarSugestao" class="px-4 text-xs bg-purple-50 text-purple-600 rounded-lg border border-purple-100">Sugerir</button>
              </div>
            </div>
            
            <button 
              @click="enviarArquivos"
              :disabled="loading || selectedFiles.length === 0"
              class="w-full mt-8 bg-purple-600 hover:bg-purple-700 disabled:bg-gray-300 text-white py-4 rounded-2xl font-bold shadow-lg shadow-purple-200 transition-all transform active:scale-[0.98]"
            >
              <span v-if="!loading">Gerar Planilha Excel</span>
              <span v-else>Processando... Aguarde</span>
            </button>

            <div v-if="mensagem" class="mt-6 p-4 rounded-xl bg-gray-50 border border-gray-100 text-sm text-gray-700 whitespace-pre-line">
              {{ mensagem }}
            </div>

          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import { ENDPOINTS } from '../config/api';
import ConfigPanel from '../components/ConfigPanel.vue'; // Certifique-se que o caminho está correto

export default {
  components: {
    ConfigPanel
  },
  data() {
    return {
      selectedFiles: [],
      mensagem: '',
      nomePlanilha: '',
      loading: false,
      dragOver: false,
      validationMessage: null,

      // Configurações do ConfigPanel
      presetAtivo: 'basico',
      camposSelecionados: ['nfe', 'data_emissao', 'cnpj_emitente', 'nome_emitente', 'valor_total'],
      
      camposDisponiveis: {
        nota: [
          { id: 'nfe', nome: 'Número NF-e' },
          { id: 'serie', nome: 'Série' },
          { id: 'data_emissao', nome: 'Data Emissão' },
          { id: 'chave', nome: 'Chave de Acesso' }
        ],
        emitente: [
          { id: 'cnpj_emitente', nome: 'CNPJ Emitente' },
          { id: 'nome_emitente', nome: 'Razão Social' },
          { id: 'uf_emitente', nome: 'UF' }
        ],
        produtos: [
          { id: 'cprod', nome: 'Cód. Produto' },
          { id: 'xprod', nome: 'Descrição' },
          { id: 'vuncom', nome: 'Valor Unitário' }
        ],
        impostos: [
          { id: 'vicms', nome: 'Valor ICMS' },
          { id: 'vipi', nome: 'Valor IPI' }
        ]
      }
    };
  },
  methods: {
    handleFileChange(event) {
      const files = Array.from(event.target.files);
      this.processFiles(files);
    },
    handleDrop(event) {
      this.dragOver = false;
      const files = Array.from(event.dataTransfer.files);
      this.processFiles(files);
    },
    processFiles(files) {
      const xmlFiles = files.filter(file => file.name.toLowerCase().endsWith('.xml'));
      if (xmlFiles.length > 50) {
        this.selectedFiles = xmlFiles.slice(0, 50);
      } else {
        this.selectedFiles = xmlFiles;
      }
    },
    clearFiles() {
      this.selectedFiles = [];
      this.mensagem = '';
    },
    usarSugestao() {
      const data = new Date().toLocaleDateString('pt-BR').replace(/\//g, '-');
      this.nomePlanilha = `planilha_${data}`;
    },
    async enviarArquivos() {
      if (!this.selectedFiles.length || !this.nomePlanilha.trim()) return;

      this.loading = true;
      this.mensagem = '';

      const formData = new FormData();
      this.selectedFiles.forEach(file => formData.append('xmls', file));
      formData.append('planilha', this.nomePlanilha);
      
      // Adicionando os campos selecionados no ConfigPanel para enviar ao Backend
      formData.append('campos', JSON.stringify(this.camposSelecionados));

      try {
        const responseInfo = await fetch(ENDPOINTS.PROCESSAR_INFO, {
          method: 'POST',
          body: formData
        });

        if (!responseInfo.ok) throw new Error(`Erro: ${responseInfo.status}`);
        const info = await responseInfo.json();

        this.mensagem = `✅ Processamento concluído!\n📁 Arquivos: ${info.arquivos_processados}\n💰 Valor: R$ ${info.valor_total.toLocaleString('pt-BR')}`;

        // Lógica de download (simplificada)
        const responseExcel = await fetch(ENDPOINTS.PROCESSAR_EXCEL, { method: 'POST', body: formData });
        const blob = await responseExcel.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `${this.nomePlanilha}.xlsx`;
        a.click();
      } catch (error) {
        this.mensagem = `❌ Erro: ${error.message}`;
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>