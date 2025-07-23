<template>
  <div v-if="currentView === 'landing'">
    <LandingPage @goToApp="currentView = 'app'" />
  </div>
  <div v-else class="min-h-screen flex flex-col bg-gradient-to-br from-purple-100 via-white to-purple-200">
    <!-- Header -->
    <header class="w-full bg-white/80 backdrop-blur shadow-md py-3 px-8 flex items-center justify-between fixed top-0 left-0 z-10 border-b border-purple-100">
      <div class="flex items-center gap-3">
        <button @click="currentView = 'landing'" class="flex items-center gap-3 hover:opacity-80 transition">
          <span class="inline-flex items-center justify-center w-11 h-11 bg-purple-600 rounded-full text-white text-2xl font-bold shadow">D</span>
          <div class="flex flex-col">
            <span class="text-2xl font-extrabold text-purple-700 tracking-tight">Datarum</span>
            <span class="text-xs text-purple-600 font-medium">Automação fiscal com inteligência e clareza</span>
          </div>
        </button>
      </div>
      <div class="flex items-center gap-4">
        <!-- Indicador de versão -->
        <div class="hidden md:flex items-center gap-2 bg-purple-50 px-3 py-1 rounded-full">
          <span class="text-xs font-medium text-purple-600">v1.0 Beta</span>
        </div>
        <button @click="currentView = 'landing'" class="text-purple-600 hover:text-purple-700 text-sm font-medium transition">
          ← Voltar ao início
        </button>
      </div>
    </header>

    <div class="h-20"></div>

    <!-- Conteúdo principal -->
    <main class="flex-1 flex justify-center px-4 py-8">
      <div class="w-full max-w-7xl flex flex-col lg:flex-row gap-6 lg:gap-8">
        
        <!-- Sidebar Esquerda -->
        <aside class="w-full lg:w-72 order-2 lg:order-1">
          <div class="flex lg:flex-col gap-4 lg:gap-6 overflow-x-auto lg:overflow-x-visible">
          <!-- Stats Card -->
          <div class="bg-white/90 rounded-2xl shadow-lg p-4 lg:p-6 border border-purple-100 flex-shrink-0 w-64 lg:w-full">
            <div class="flex items-center gap-3 mb-4">
              <div class="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center">
                <svg class="w-5 h-5 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
                </svg>
              </div>
              <h3 class="font-bold text-purple-700">Estatísticas</h3>
            </div>
            <div class="space-y-3">
              <div class="flex justify-between">
                <span class="text-sm text-gray-600">Sessão atual</span>
                <span class="font-semibold text-purple-600">{{ selectedFiles.length }} arquivos</span>
              </div>
              <div class="flex justify-between">
                <span class="text-sm text-gray-600">Suporte NFe</span>
                <span class="font-semibold text-purple-600">v1.10 - v4.00</span>
              </div>
              <div class="flex justify-between">
                <span class="text-sm text-gray-600">Formato saída</span>
                <span class="font-semibold text-purple-600">Excel (.xlsx)</span>
              </div>
            </div>
          </div>

          <!-- Dicas Card -->
          <div class="bg-gradient-to-br from-purple-50 to-purple-100 rounded-2xl shadow-lg p-4 lg:p-6 border border-purple-200 flex-shrink-0 w-64 lg:w-full">
            <div class="flex items-center gap-3 mb-4">
              <div class="w-10 h-10 bg-purple-200 rounded-lg flex items-center justify-center">
                <svg class="w-5 h-5 text-purple-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/>
                </svg>
              </div>
              <h3 class="font-bold text-purple-700">Dicas de Uso</h3>
            </div>
            <div class="space-y-3 text-sm text-purple-600">
              <div class="flex items-start gap-2">
                <span class="text-purple-400 mt-0.5">•</span>
                <span>Arraste múltiplos XMLs de uma vez</span>
              </div>
              <div class="flex items-start gap-2">
                <span class="text-purple-400 mt-0.5">•</span>
                <span>Máximo 50 arquivos por vez</span>
              </div>
              <div class="flex items-start gap-2">
                <span class="text-purple-400 mt-0.5">•</span>
                <span>Nome da planilha será o nome do arquivo</span>
              </div>
            </div>
          </div>

          <!-- Versões NFe -->
          <div class="bg-white/90 rounded-2xl shadow-lg p-6 border border-purple-100 flex-shrink-0 w-64 lg:w-full">
            <div class="flex items-center gap-3 mb-4">
              <div class="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center">
                <svg class="w-5 h-5 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
                </svg>
              </div>
              <h3 class="font-bold text-purple-700">Compatibilidade</h3>
            </div>
            <div class="grid grid-cols-2 gap-2">
              <div class="text-center p-2 bg-purple-50 rounded-lg">
                <div class="text-xs text-purple-600 font-semibold">NFe 1.10</div>
                <div class="text-xs text-green-600">✓ Suportado</div>
              </div>
              <div class="text-center p-2 bg-purple-50 rounded-lg">
                <div class="text-xs text-purple-600 font-semibold">NFe 2.00</div>
                <div class="text-xs text-green-600">✓ Suportado</div>
              </div>
              <div class="text-center p-2 bg-purple-50 rounded-lg">
                <div class="text-xs text-purple-600 font-semibold">NFe 3.10</div>
                <div class="text-xs text-green-600">✓ Suportado</div>
              </div>
              <div class="text-center p-2 bg-purple-50 rounded-lg">
                <div class="text-xs text-purple-600 font-semibold">NFe 4.00</div>
                <div class="text-xs text-green-600">✓ Suportado</div>
              </div>
            </div>
          </div>
          </div>
        </aside>

        <!-- Conteúdo Principal -->
        <div class="flex-1 max-w-2xl mx-auto order-1 lg:order-2">
          <div class="bg-white/90 rounded-3xl shadow-2xl p-10 border border-purple-100">
        <div class="flex flex-col items-center mb-8">
          <div class="bg-gradient-to-br from-purple-200 to-purple-400 rounded-full p-4 shadow-lg mb-4">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-purple-700" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" /></svg>
          </div>
          <h1 class="text-3xl font-extrabold text-purple-700 mb-1 text-center">Extrator de XMLs NFe</h1>
          <p class="text-gray-500 mb-2 text-center">Converta arquivos XML de NFe em planilhas Excel organizadas e inteligentes.</p>
        </div>

        <!-- Área de upload com drag & drop -->
        <section class="mb-8">
          <label class="block text-sm font-semibold text-purple-700 mb-2">
            Selecione arquivos XML (máx. 50 arquivos, 5MB cada)
          </label>
          <div 
            @dragover.prevent="dragOver = true"
            @dragleave.prevent="dragOver = false"
            @drop.prevent="handleDrop"
            :class="[
              'relative border-2 border-dashed rounded-lg p-8 transition-all duration-200 cursor-pointer',
              dragOver ? 'border-purple-400 bg-purple-50 scale-105' : 'border-purple-200 hover:border-purple-300'
            ]"
          >
            <input 
              type="file" 
              id="xmlUpload" 
              multiple 
              accept=".xml" 
              @change="handleFileChange" 
              class="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
            />
            <div class="text-center">
              <svg class="mx-auto h-12 w-12 text-purple-400 mb-4" stroke="currentColor" fill="none" viewBox="0 0 48 48">
                <path d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <p class="text-lg font-medium text-purple-600 mb-1">
                <span class="underline">Clique para selecionar</span> ou arraste arquivos XML aqui
              </p>
              <p class="text-sm text-gray-500">Máximo 50 arquivos, 5MB cada</p>
            </div>
          </div>
          
          <!-- Lista de arquivos selecionados -->
          <div v-if="selectedFiles.length" class="mt-4 space-y-2">
            <div class="flex items-center justify-between text-sm text-purple-700 font-medium">
              <span>{{ selectedFiles.length }} arquivo(s) selecionado(s)</span>
              <button @click="clearFiles" class="text-red-500 hover:text-red-700 transition-colors">
                Limpar tudo
              </button>
            </div>
            <ul class="space-y-2 max-h-32 overflow-y-auto">
              <li v-for="(file, index) in selectedFiles" :key="index" 
                  :class="[
                    'flex items-center justify-between p-2 rounded border text-sm',
                    getFileStatus(file).valid ? 'bg-emerald-50 border-emerald-200' : 'bg-red-50 border-red-200'
                  ]">
                <div class="flex items-center gap-2 flex-1 min-w-0">
                  <svg :class="[
                    'h-4 w-4 flex-shrink-0',
                    getFileStatus(file).valid ? 'text-emerald-500' : 'text-red-500'
                  ]" fill="currentColor" viewBox="0 0 20 20">
                    <path v-if="getFileStatus(file).valid" fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
                    <path v-else fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"/>
                  </svg>
                  <span class="truncate font-medium">{{ file.name }}</span>
                </div>
                <div class="flex items-center gap-2">
                  <span class="text-xs text-gray-500">{{ formatFileSize(file.size) }}</span>
                  <button @click="removeFile(index)" class="text-red-400 hover:text-red-600 transition-colors">
                    <svg class="h-4 w-4" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"/>
                    </svg>
                  </button>
                </div>
              </li>
            </ul>
            <!-- Avisos de validação -->
            <div v-if="validationMessage" class="p-2 rounded text-sm"
                 :class="validationMessage.type === 'error' ? 'bg-red-50 text-red-700' : 'bg-yellow-50 text-yellow-700'">
              {{ validationMessage.text }}
            </div>
          </div>
        </section>

        <!-- Criar nova planilha -->
        <section class="mb-8">
          <label for="nomePlanilha" class="block text-sm font-semibold text-purple-700 mb-2">
            Nome da nova planilha
          </label>
          <div class="relative rounded-lg shadow-sm">
            <input 
              type="text" 
              id="nomePlanilha"
              v-model="nomePlanilha"
              placeholder="ex: Notas Recebidas"
              class="block w-full rounded-lg border border-purple-300 focus:border-purple-500 focus:ring-1 focus:ring-purple-500 text-sm p-3 pr-36 transition"
              aria-describedby="sugestaoPlanilha"
            />
            <button 
              v-if="!nomePlanilha"
              @click="usarSugestao"
              type="button"
              class="absolute right-2 top-1/2 -translate-y-1/2 bg-purple-50 text-purple-600 px-3 py-1 text-xs rounded-md hover:bg-purple-100 transition"
            >
              Usar sugestão
            </button>
          </div>
          <p id="sugestaoPlanilha" class="text-xs text-gray-500 mt-1">
            Dica: dê um nome claro. Ou clique em <strong>"Usar sugestão"</strong> para gerar um nome automático.
          </p>
        </section>

        <!-- Botão de envio com loading -->
        <section class="mb-8">
          <button 
            @click="enviarArquivos" 
            :disabled="!selectedFiles.length || !nomePlanilha.trim() || loading"
            class="w-full bg-purple-600 text-white py-3 px-4 rounded-lg hover:bg-purple-700 disabled:bg-gray-300 disabled:cursor-not-allowed transition-all font-bold shadow-md flex items-center justify-center gap-2 text-lg"
          >
            <svg v-if="!loading" xmlns='http://www.w3.org/2000/svg' class='h-5 w-5' fill='none' viewBox='0 0 24 24' stroke='currentColor'><path stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M5 13l4 4L19 7'/></svg>
            <svg v-else class="animate-spin h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            {{ loading ? 'Processando...' : 'Enviar para processamento' }}
          </button>
        </section>

        <!-- Mensagem -->
        <section v-if="mensagem" class="p-4 rounded-lg text-left font-semibold shadow-sm whitespace-pre-line mb-4"
         :class="mensagem.includes('✅') ? 'bg-emerald-50 text-emerald-800' : 'bg-red-50 text-red-800'">
          {{ mensagem }}
        </section>

          </div>
        </div>

      </div>
    </main>

    <!-- Footer -->
    <footer class="w-full text-center text-purple-400 text-xs py-4 mt-8">
      &copy; {{ new Date().getFullYear() }} Datarum. Todos os direitos reservados.
    </footer>
  </div>
</template>

<script>
import LandingPage from './LandingPage.vue';

export default {
  components: {
    LandingPage
  },
  data() {
    return {
      currentView: 'landing', // 'landing' ou 'app'
      selectedFiles: [],
      mensagem: '',
      nomePlanilha: '',
      loading: false,
      progress: 0,
      dragOver: false,
      validationMessage: null
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
      // Filtrar apenas arquivos XML
      const xmlFiles = files.filter(file => file.name.toLowerCase().endsWith('.xml'));
      
      if (xmlFiles.length !== files.length) {
        this.showValidation('warning', `${files.length - xmlFiles.length} arquivo(s) ignorado(s) (apenas XML aceitos)`);
      }
      
      // Limitar a 50 arquivos
      if (xmlFiles.length > 50) {
        this.showValidation('error', 'Máximo 50 arquivos permitidos. Alguns foram removidos.');
        this.selectedFiles = xmlFiles.slice(0, 50);
      } else {
        this.selectedFiles = xmlFiles;
      }
      
      this.validateFiles();
    },
    validateFiles() {
      const oversizedFiles = this.selectedFiles.filter(file => file.size > 5 * 1024 * 1024);
      
      if (oversizedFiles.length > 0) {
        this.showValidation('error', `${oversizedFiles.length} arquivo(s) muito grande(s) (máx. 5MB)`);
      } else if (this.selectedFiles.length > 0) {
        this.validationMessage = null;
      }
    },
    showValidation(type, text) {
      this.validationMessage = { type, text };
      setTimeout(() => {
        this.validationMessage = null;
      }, 5000);
    },
    getFileStatus(file) {
      const isXml = file.name.toLowerCase().endsWith('.xml');
      const isValidSize = file.size <= 5 * 1024 * 1024;
      return {
        valid: isXml && isValidSize,
        reason: !isXml ? 'Não é XML' : !isValidSize ? 'Muito grande' : null
      };
    },
    formatFileSize(bytes) {
      if (bytes === 0) return '0 B';
      const k = 1024;
      const sizes = ['B', 'KB', 'MB'];
      const i = Math.floor(Math.log(bytes) / Math.log(k));
      return parseFloat((bytes / Math.pow(k, i)).toFixed(1)) + ' ' + sizes[i];
    },
    removeFile(index) {
      this.selectedFiles.splice(index, 1);
      this.validateFiles();
    },
    clearFiles() {
      this.selectedFiles = [];
      this.validationMessage = null;
      document.getElementById('xmlUpload').value = '';
    },
    usarSugestao() {
      const agora = new Date();
      const pad = (n) => n.toString().padStart(2, '0');
      const sugestao = `datarum_${agora.getFullYear()}-${pad(agora.getMonth()+1)}-${pad(agora.getDate())}_${pad(agora.getHours())}${pad(agora.getMinutes())}`;
      this.nomePlanilha = sugestao;
    },
    async enviarArquivos() {
      if (!this.selectedFiles.length || !this.nomePlanilha.trim()) return;

      this.loading = true;
      this.mensagem = '';
      this.validationMessage = null;

      const formData = new FormData();
      this.selectedFiles.forEach(file => formData.append('files', file));

      // ✅ URL correta do backend
      const API_URL = 'https://datarum-api.fly.dev';

      try {
        // Primeiro: obter informações
        const responseInfo = await fetch(`${API_URL}/processar-info`, {
          method: 'POST',
          body: formData
        });
        
        if (!responseInfo.ok) {
          throw new Error(`Erro ${responseInfo.status}: ${responseInfo.statusText}`);
        }
        
        const info = await responseInfo.json();
        this.showResults(info);
        
        // Depois: baixar Excel
        const responseExcel = await fetch(`${API_URL}/processar`, {
          method: 'POST', 
          body: formData
        });
        
        if (!responseExcel.ok) {
          throw new Error(`Erro ${responseExcel.status}: ${responseExcel.statusText}`);
        }
        
        const blob = await responseExcel.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `${this.nomePlanilha}.xlsx`;
        a.click();
        window.URL.revokeObjectURL(url);
        
      } catch (error) {
        this.mensagem = `Erro: ${error.message}`;
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>

<style>
</style>
