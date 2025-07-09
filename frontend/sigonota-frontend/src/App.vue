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

        <!-- Seleção/criação de planilha -->
        <section class="mb-8">
          <label for="planilha" class="block text-sm font-semibold text-blue-700 mb-2">Escolha uma planilha</label>
          <div class="flex gap-2">
            <select id="planilha" v-model="planilhaSelecionada" class="flex-1 rounded-lg border-blue-200 focus:border-blue-500 focus:ring-blue-500 text-sm shadow-sm">
              <option disabled value="">Selecione...</option>
              <option v-for="planilha in planilhas" :key="planilha" :value="planilha">{{ planilha }}</option>
            </select>
            <button @click="criarNovaPlanilha" class="bg-green-100 text-green-700 px-3 py-1 rounded-lg font-semibold hover:bg-green-200 transition-colors flex items-center gap-1">
              <svg xmlns='http://www.w3.org/2000/svg' class='h-4 w-4' fill='none' viewBox='0 0 24 24' stroke='currentColor'><path stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M12 4v16m8-8H4'/></svg>
              Nova
            </button>
          </div>
        </section>

        <!-- Botão de envio -->
        <section class="mb-8">
          <button 
            @click="enviarArquivos" 
            :disabled="!selectedFiles.length || !planilhaSelecionada"
            class="w-full bg-blue-600 text-white py-3 px-4 rounded-lg hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed transition-all font-bold shadow-md flex items-center justify-center gap-2 text-lg"
          >
            <svg xmlns='http://www.w3.org/2000/svg' class='h-5 w-5' fill='none' viewBox='0 0 24 24' stroke='currentColor'><path stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M5 13l4 4L19 7'/></svg>
            Enviar para processamento
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
      planilhas: ['Planilha 2025', 'Notas Recebidas', 'Financeiro'],
      planilhaSelecionada: ''
    };
  },
  methods: {
    handleFileChange(event) {
      this.selectedFiles = Array.from(event.target.files);
    },
    criarNovaPlanilha() {
      const nome = prompt('Nome da nova planilha:');
      if (nome && !this.planilhas.includes(nome)) {
        this.planilhas.push(nome);
        this.planilhaSelecionada = nome;
      }
    },
    async enviarArquivos() {
      if (!this.selectedFiles.length || !this.planilhaSelecionada) return;

      const formData = new FormData();
      this.selectedFiles.forEach(file => formData.append('xmls', file));
      formData.append('planilha', this.planilhaSelecionada);

      try {
        const response = await fetch('http://localhost:8000/processar', {
          method: 'POST',
          body: formData
        });

        if (!response.ok) throw new Error('Falha ao enviar arquivos');
        const resultado = await response.json();
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
}
</script>

<style>
</style>
