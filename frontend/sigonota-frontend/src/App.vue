<template>
  <div class="min-h-screen flex flex-col bg-gradient-to-br from-blue-100 via-white to-blue-200">
    <!-- Header -->
    <header class="w-full bg-white/80 backdrop-blur shadow-md py-3 px-8 flex items-center justify-between fixed top-0 left-0 z-10 border-b border-blue-100">
      <div class="flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-11 h-11 bg-blue-600 rounded-full text-white text-2xl font-bold shadow">S</span>
        <span class="text-2xl font-extrabold text-blue-700 tracking-tight">Sigonota</span>
      </div>
      <nav class="hidden md:flex gap-8 text-blue-700 font-medium">
        <a href="#" class="hover:text-blue-500 transition-colors">Importar</a>
        <a href="#" class="hover:text-blue-500 transition-colors">Planilhas</a>
        <a href="#" class="hover:text-blue-500 transition-colors">Histórico</a>
      </nav>
      <div class="flex items-center gap-3">
        <span class="w-9 h-9 rounded-full bg-blue-200 flex items-center justify-center text-blue-700 font-bold">A</span>
      </div>
    </header>

    <div class="h-20"></div>

    <!-- Conteúdo principal -->
    <main class="flex-1 flex flex-col items-center justify-center px-4">
      <div class="w-full max-w-2xl bg-white/90 rounded-3xl shadow-2xl p-10 mt-8 border border-blue-100">
        <div class="flex flex-col items-center mb-8">
          <div class="bg-gradient-to-br from-blue-200 to-blue-400 rounded-full p-4 shadow-lg mb-4">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-blue-700" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" /></svg>
          </div>
          <h1 class="text-3xl font-extrabold text-blue-700 mb-1 text-center">Importe seus XMLs</h1>
          <p class="text-gray-500 mb-2 text-center">Faça upload dos arquivos XML para processar suas notas fiscais.</p>
        </div>

        <!-- Área de upload com drag & drop -->
        <section class="mb-8">
          <label class="block text-sm font-semibold text-blue-700 mb-2">
            Selecione arquivos XML (máx. 50 arquivos, 5MB cada)
          </label>
          <div 
            @dragover.prevent="dragOver = true"
            @dragleave.prevent="dragOver = false"
            @drop.prevent="handleDrop"
            :class="[
              'relative border-2 border-dashed rounded-lg p-8 transition-all duration-200 cursor-pointer',
              dragOver ? 'border-blue-400 bg-blue-50 scale-105' : 'border-blue-200 hover:border-blue-300'
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
              <svg class="mx-auto h-12 w-12 text-blue-400 mb-4" stroke="currentColor" fill="none" viewBox="0 0 48 48">
                <path d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <p class="text-lg font-medium text-blue-600 mb-1">
                <span class="underline">Clique para selecionar</span> ou arraste arquivos XML aqui
              </p>
              <p class="text-sm text-gray-500">Máximo 50 arquivos, 5MB cada</p>
            </div>
          </div>
          
          <!-- Lista de arquivos selecionados -->
          <div v-if="selectedFiles.length" class="mt-4 space-y-2">
            <div class="flex items-center justify-between text-sm text-blue-700 font-medium">
              <span>{{ selectedFiles.length }} arquivo(s) selecionado(s)</span>
              <button @click="clearFiles" class="text-red-500 hover:text-red-700 transition-colors">
                Limpar tudo
              </button>
            </div>
            <ul class="space-y-2 max-h-32 overflow-y-auto">
              <li v-for="(file, index) in selectedFiles" :key="index" 
                  :class="[
                    'flex items-center justify-between p-2 rounded border text-sm',
                    getFileStatus(file).valid ? 'bg-green-50 border-green-200' : 'bg-red-50 border-red-200'
                  ]">
                <div class="flex items-center gap-2 flex-1 min-w-0">
                  <svg :class="[
                    'h-4 w-4 flex-shrink-0',
                    getFileStatus(file).valid ? 'text-green-500' : 'text-red-500'
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
          <label for="nomePlanilha" class="block text-sm font-semibold text-blue-700 mb-2">
            Nome da nova planilha
          </label>
          <div class="relative rounded-lg shadow-sm">
            <input 
              type="text" 
              id="nomePlanilha"
              v-model="nomePlanilha"
              placeholder="ex: Notas Recebidas"
              class="block w-full rounded-lg border border-blue-300 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 text-sm p-3 pr-36 transition"
              aria-describedby="sugestaoPlanilha"
            />
            <button 
              v-if="!nomePlanilha"
              @click="usarSugestao"
              type="button"
              class="absolute right-2 top-1/2 -translate-y-1/2 bg-blue-50 text-blue-600 px-3 py-1 text-xs rounded-md hover:bg-blue-100 transition"
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
            class="w-full bg-blue-600 text-white py-3 px-4 rounded-lg hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed transition-all font-bold shadow-md flex items-center justify-center gap-2 text-lg"
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
         :class="mensagem.includes('✅') ? 'bg-green-50 text-green-800' : 'bg-red-50 text-red-800'">
          {{ mensagem }}
        </section>

        <!-- Histórico/Preview (melhorado) -->
        <section class="mt-8">
          <h2 class="text-lg font-bold text-blue-700 mb-2 flex items-center gap-2">
            <svg xmlns='http://www.w3.org/2000/svg' class='h-5 w-5 text-blue-400' fill='none' viewBox='0 0 24 24' stroke='currentColor'><path stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z'/></svg>
            Últimos Processamentos
          </h2>
          <div class="text-gray-400 text-sm italic">
            Versão 1.0 - Funcionalidade básica de conversão XML → Excel<br>
            <span class="text-xs">💡 Em breve: histórico, templates personalizados e mais automações</span>
          </div>
        </section>
      </div>
    </main>

    <!-- Footer -->
    <footer class="w-full text-center text-blue-400 text-xs py-4 mt-8">
      &copy; {{ new Date().getFullYear() }} Sigonota. Todos os direitos reservados.
    </footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
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
      const sugestao = `sigonota_${agora.getFullYear()}-${pad(agora.getMonth()+1)}-${pad(agora.getDate())}_${pad(agora.getHours())}${pad(agora.getMinutes())}`;
      this.nomePlanilha = sugestao;
    },
    async enviarArquivos() {
      if (!this.selectedFiles.length || !this.nomePlanilha.trim()) return;

      this.isLoading = true;
      this.mensagem = '';
      this.validationMessage = null;

      const formData = new FormData();
      this.selectedFiles.forEach(file => formData.append('xmls', file));
      formData.append('planilha', this.nomePlanilha.trim());

      try {
        // 📊 Primeiro: obter informações sobre o processamento
        const formDataInfo = new FormData();
        this.selectedFiles.forEach(file => formDataInfo.append('xmls', file));
        formDataInfo.append('planilha', this.nomePlanilha.trim());

        const infoResponse = await fetch('http://localhost:8000/processar-info', {
          method: 'POST',
          body: formDataInfo
        });

        if (!infoResponse.ok) {
          const errorData = await infoResponse.json().catch(() => ({}));
          throw new Error(errorData.detail || 'Falha ao processar os arquivos');
        }
        const resultado = await infoResponse.json();

        // � Segundo: fazer download do arquivo
        const downloadResponse = await fetch('http://localhost:8000/processar', {
          method: 'POST',
          body: formData
        });

        if (!downloadResponse.ok) {
          const errorData = await downloadResponse.json().catch(() => ({}));
          throw new Error(errorData.detail || 'Falha ao gerar arquivo');
        }

        // �🔽 Força o download
        const blob = await downloadResponse.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `${this.nomePlanilha.trim()}.xlsx`;
        document.body.appendChild(a);
        a.click();
        a.remove();
        window.URL.revokeObjectURL(url);

        // ✅ Feedback rico com estatísticas avançadas
        const feedback = [
          `✅ ${resultado.itens_processados} itens processados com sucesso!`,
          `📄 Planilha: ${resultado.planilha_destino}`,
          `📦 ${resultado.arquivos_processados} arquivos XML processados`
        ];

        if (resultado.notas_encontradas && resultado.notas_encontradas.length > 0) {
          const notasTexto = resultado.notas_encontradas.length > 5 
            ? `${resultado.notas_encontradas.slice(0, 5).join(', ')}... (+${resultado.notas_encontradas.length - 5} mais)`
            : resultado.notas_encontradas.join(', ');
          feedback.push(`🧾 Notas: ${notasTexto}`);
        }

        if (resultado.emitentes && resultado.emitentes.length > 0) {
          const emitentesTexto = resultado.emitentes.length > 3
            ? `${resultado.emitentes.slice(0, 3).join(', ')}... (+${resultado.emitentes.length - 3} mais)`
            : resultado.emitentes.join(', ');
          feedback.push(`🏢 Emitentes: ${emitentesTexto}`);
        }

        if (resultado.versoes_nfe && resultado.versoes_nfe.length > 0) {
          feedback.push(`📋 Versões NFe: ${resultado.versoes_nfe.join(', ')}`);
        }

        if (resultado.periodo && resultado.periodo.inicio) {
          feedback.push(`📅 Período: ${resultado.periodo.inicio} a ${resultado.periodo.fim}`);
        }

        if (resultado.valor_total && resultado.valor_total > 0) {
          feedback.push(`💰 Valor Total: R$ ${resultado.valor_total.toLocaleString('pt-BR', {minimumFractionDigits: 2})}`);
        }

        this.mensagem = feedback.join('\n');

        // 🧹 Auto-limpeza após sucesso
        setTimeout(() => {
          this.clearFiles();
          this.nomePlanilha = '';
          this.mensagem = '';
        }, 8000);

      } catch (err) {
        this.mensagem = `❌ Erro: ${err.message}`;
        this.showValidation('error', 'Erro no processamento. Verifique os arquivos e tente novamente.');
      } finally {
        this.isLoading = false;
      }
    }
  }
};
</script>

<style>
</style>
