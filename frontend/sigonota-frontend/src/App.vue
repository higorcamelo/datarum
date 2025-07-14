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

        <!-- Área de upload -->
        <section class="mb-8">
          <label for="xmlUpload" class="block text-sm font-semibold text-blue-700 mb-2">Selecione arquivos XML</label>
          <input 
            type="file" 
            id="xmlUpload" 
            multiple 
            accept=".xml" 
            @change="handleFileChange" 
            class="block w-full text-sm text-gray-700 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100 border border-blue-200 shadow-sm"
          />
          <ul class="mt-3 space-y-1">
            <li v-for="(file, index) in selectedFiles" :key="index" class="text-sm text-blue-700 flex items-center gap-2">
              <svg xmlns='http://www.w3.org/2000/svg' class='h-4 w-4 text-blue-400' fill='none' viewBox='0 0 24 24' stroke='currentColor'><path stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M12 4v16m8-8H4'/></svg>
              {{ file.name }}
            </li>
          </ul>
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

        <!-- Histórico (placeholder) -->
        <section class="mt-8">
          <h2 class="text-lg font-bold text-blue-700 mb-2 flex items-center gap-2">
            <svg xmlns='http://www.w3.org/2000/svg' class='h-5 w-5 text-blue-400' fill='none' viewBox='0 0 24 24' stroke='currentColor'><path stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M8 17l4 4 4-4m0-5V3m-8 9V3'/></svg>
            Histórico de importações
          </h2>
          <div class="text-gray-400 text-sm italic">Em breve você verá aqui o histórico das últimas importações.</div>
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
      progress: 0
    };
  },
  methods: {
    handleFileChange(event) {
      this.selectedFiles = Array.from(event.target.files);
    },
    usarSugestao() {
      const agora = new Date();
      const pad = (n) => n.toString().padStart(2, '0');
      const sugestao = `sigonota_${agora.getFullYear()}-${pad(agora.getMonth()+1)}-${pad(agora.getDate())}_${pad(agora.getHours())}${pad(agora.getMinutes())}`;
      this.nomePlanilha = sugestao;
    },
    async enviarArquivos() {
      if (!this.selectedFiles.length || !this.nomePlanilha.trim()) return;

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

        if (!infoResponse.ok) throw new Error('Falha ao processar os arquivos');
        const resultado = await infoResponse.json();

        // � Segundo: fazer download do arquivo
        const downloadResponse = await fetch('http://localhost:8000/processar', {
          method: 'POST',
          body: formData
        });

        if (!downloadResponse.ok) throw new Error('Falha ao gerar arquivo');

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

        // ✅ Feedback rico como antes
        this.mensagem = [
          `✅ ${resultado.itens_processados} itens processados com sucesso!`,
          `📄 Planilha: ${resultado.planilha_destino}`,
          `📦 Notas incluídas: ${resultado.notas_encontradas.join(', ')}`,
          `🏢 Emitentes: ${resultado.emitentes.join(', ')}`
        ].join('\n');

      } catch (err) {
        this.mensagem = `❌ Erro: ${err.message}`;
      }
    }
  }
};
</script>

<style>
</style>
