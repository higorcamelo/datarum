<template>
  <div class="min-h-screen flex flex-col bg-white relative overflow-x-hidden">
    <!-- Background elemento geométrico sutil -->
    <div class="absolute top-0 right-0 w-96 h-96 bg-gradient-to-br from-orange-800/5 to-transparent rounded-full blur-3xl -z-10"></div>

    <header class="w-full bg-white/95 border-b-2 border-orange-200 py-5 px-8 flex items-center justify-between fixed top-0 left-0 z-10">
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 bg-orange-800 rounded-lg flex items-center justify-center">
          <img
            src="../../assets/logo.svg"
            alt="Datarum"
            class="w-10 h-10 rounded-lg object-contain transition-all duration-200"
          />
        </div>
        <span class="text-lg font-black text-orange-800" style="letter-spacing: -0.5px;">Datarum</span>
      </div>

      <button
        @click="voltarParaInicio"
        class="text-sm font-bold text-orange-700 hover:text-orange-800 focus:outline-none focus:ring-2 focus:ring-orange-800 rounded px-4 py-2 transition-colors"
      >
        ← Voltar
      </button>
    </header>

    <div class="h-24"></div>

    <main class="flex-1 flex pt-32 pb-16 px-8">
      <div class="w-full max-w-5xl mx-auto grid lg:grid-cols-5 gap-16 items-start">
        <!-- LEFT: Drag/Drop Area - 60% width -->
        <div class="lg:col-span-3">
          <div>
            <h1 class="text-7xl lg:text-7xl font-black text-orange-800 mb-4 leading-none" style="letter-spacing: -2px;">
              XMLs →<br />Excel
            </h1>
            <p class="text-lg text-orange-700 mb-12 font-medium leading-relaxed max-w-md">
              Converta seus arquivos em segundos. Sem limite de tamanho. Sem armazenamento.
            </p>
          </div>

          <section>
            <div
              @dragover.prevent="dragOver = true"
              @dragleave.prevent="dragOver = false"
              @drop.prevent="handleDrop"
              role="button"
              tabindex="0"
              @keydown.enter="$event.currentTarget.querySelector('#file-upload').click()"
              @keydown.space.prevent="$event.currentTarget.querySelector('#file-upload').click()"
              aria-label="Área de upload: Arraste arquivos XML ou clique para selecionar. Máximo 500 arquivos."
              :aria-pressed="dragOver"
              :class="[
                'relative border-4 border-dashed rounded-3xl p-12 transition-all duration-200 text-center cursor-pointer',
                dragOver
                  ? 'border-orange-800 bg-orange-50 scale-105'
                  : 'border-orange-200 hover:border-orange-800 hover:bg-orange-50'
              ]"
            >
              <input
                id="file-upload"
                type="file"
                multiple
                accept=".xml"
                @change="handleFileChange"
                class="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
                aria-label="Selecionar arquivos XML para upload"
              />
              <div class="space-y-4">
                <svg class="mx-auto h-16 w-16 text-orange-800" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true" stroke-width="1.5">
                  <path d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <div>
                  <p class="text-orange-800 font-black text-2xl mb-1">Arraste XMLs aqui</p>
                  <p class="text-orange-700 text-sm font-medium">ou clique para selecionar. Máximo 500 por vez.</p>
                </div>
              </div>
            </div>

            <div v-if="selectedFiles.length" class="mt-8">
              <div class="flex justify-between items-center mb-4 pb-4 border-b-2 border-orange-200">
                <div class="flex items-center gap-3">
                  <span class="inline-block w-8 h-8 bg-orange-800 rounded-full flex items-center justify-center text-white text-sm font-black" title="Número de arquivos selecionados">
                    {{ selectedFiles.length }}
                  </span>
                  <span class="text-base font-bold text-orange-800 uppercase tracking-wide">arquivo(s)</span>
                </div>

                <button
                  type="button"
                  @click="clearFiles"
                  aria-label="Limpar todos os arquivos"
                  class="text-sm text-orange-700 hover:text-red-700 focus:outline-none focus:ring-1 focus:ring-red-600 rounded px-4 py-2.5 transition-colors duration-200 font-bold hover:bg-red-50 border-2 border-orange-200 hover:border-red-300 uppercase tracking-wide"
                >
                  ✕ Limpar
                </button>
              </div>

              <div class="space-y-2 max-h-48 overflow-y-auto">
                <div
                  v-for="(file, idx) in selectedFiles"
                  :key="idx"
                  class="flex justify-between items-center text-sm text-orange-700 py-3 px-4 bg-white rounded-xl border-2 border-orange-200 hover:border-orange-300 hover:shadow-md transition-all"
                >
                  <span class="truncate font-semibold" :title="file.name">{{ file.name }}</span>
                  <button
                    type="button"
                    @click="removeFile(idx)"
                    :aria-label="`Remover arquivo: ${file.name}`"
                    class="text-orange-600 hover:text-red-700 focus:outline-none focus:ring-1 focus:ring-red-600 ml-2 flex-shrink-0 font-black rounded transition-colors duration-200 inline-flex items-center justify-center w-10 h-10 min-h-[44px] min-w-[44px]"
                  >
                    ✕
                  </button>
                </div>
              </div>
            </div>
          </section>
        </div>

        <!-- RIGHT: Configurações - 40% width -->
        <transition name="fade-slide">
          <div class="lg:col-span-2 space-y-8 sticky top-32" v-if="selectedFiles.length > 0">
            <ConfigPanel
              v-model="camposSelecionados"
              v-model:presetAtivo="presetAtivo"
              :camposDisponiveis="camposDisponiveis"
            />

            <div class="space-y-2">
              <div class="flex justify-between items-center">
                <label class="text-xs font-black text-orange-800 uppercase tracking-widest">
                  Nome da Planilha
                </label>

                <button
                  type="button"
                  @click="sugerirNome"
                  class="text-xs font-bold text-orange-700 hover:text-orange-800"
                >
                  Sugerir
                </button>
              </div>

              <input
                v-model="nomePlanilha"
                type="text"
                maxlength="100"
                placeholder="Ex: relatorio_janeiro"
                class="w-full px-4 py-3 border-2 border-orange-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-orange-800 focus:border-orange-300 transition-all"
              />
            </div>

            <button
              @click="enviarArquivos"
              :disabled="loading || !selectedFiles.length"
              :aria-busy="loading"
              class="w-full py-4 bg-orange-800 text-white font-black uppercase tracking-wide rounded-xl hover:bg-orange-700 disabled:opacity-50 disabled:cursor-not-allowed focus:outline-none focus:ring-2 focus:ring-orange-800 transition-all duration-200 min-h-[56px]"
            >
              {{ loading ? '⟳ Processando...' : 'Exportar relatório' }}
            </button>
          </div>
        </transition>
      </div>
    </main>

    <div
      v-if="mensagem"
      role="alert"
      aria-live="polite"
      :class="[
        'fixed bottom-8 right-8 p-6 rounded-xl text-base font-bold border-2 shadow-2xl max-w-sm',
        mensagem.includes('✅')
          ? 'bg-emerald-50 text-emerald-900 border-emerald-300'
          : 'bg-red-50 text-red-900 border-red-300'
      ]"
    >
      {{ mensagem }}
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import { useRouter } from 'vue-router';
import { ENDPOINTS } from '../config/api';
import ConfigPanel from '../components/ConfigPanel.vue';

const API_KEY = import.meta.env.VITE_GCP_KEY;
const BASE_URL = import.meta.env.VITE_API_URL;
const router = useRouter();

// Estado
const selectedFiles = ref([]);
const mensagem = ref('');
const nomePlanilha = ref(''); 
const loading = ref(false);
const dragOver = ref(false);
const presetAtivo = ref('basico');
const camposSelecionados = ref([
  'numero_nf',
  'data_emissao',
  'valor_total_nf'
]);

const camposDisponiveis = {
  identificacao: [
    { id: 'numero_nf', nome: 'Número NF' },
    { id: 'data_emissao', nome: 'Data Emissão' }
  ],
  parceiros: [
    { id: 'uf_destinatario', nome: 'UF Destinatário' },
    { id: 'cidade_destinatario', nome: 'Cidade Destinatário' }
  ],
  itens: [
    { id: 'valor_desconto_item', nome: 'Desconto Item' },
    { id: 'valor_unitario', nome: 'Valor Unitário' }
  ],
  impostos: [
    { id: 'valor_icms', nome: 'ICMS' },
    { id: 'valor_pis', nome: 'PIS' }
  ]
};

// Reseta tudo ao voltar
const voltarParaInicio = () => {
  if (selectedFiles.value.length > 0) {
    if (confirm('Descartar arquivos selecionados?')) {
      selectedFiles.value = [];
      nomePlanilha.value = '';
      mensagem.value = '';
      presetAtivo.value = 'basico';
      camposSelecionados.value = ['numero_nf', 'data_emissao', 'valor_total_nf'];
      router.push('/');
    }
  } else {
    router.push('/');
  }
};

const sugerirNome = () => {
  const hoje = new Date().toISOString().slice(0, 10);

  const base = {
    basico: 'relatorio',
    completo: 'relatorio_completo',
    fiscal: 'relatorio_fiscal',
    custom: 'relatorio_personalizado'
  };

  nomePlanilha.value = `${base[presetAtivo.value] || 'relatorio'}_${hoje}`;
};

// Lógica de Presets
watch(presetAtivo, (novo) => {
  if (novo === 'custom') return;

  if (novo === 'basico') {
    camposSelecionados.value = ['numero_nf', 'data_emissao', 'valor_total_nf'];
  } else if (novo === 'completo') {
    camposSelecionados.value = [
      'numero_nf',
      'data_emissao',
      'valor_total_nf',
      'uf_destinatario',
      'valor_desconto_item',
      'valor_icms'
    ];
  } else if (novo === 'fiscal') {
    camposSelecionados.value = [
      'numero_nf',
      'data_emissao',
      'valor_desconto_item',
      'valor_icms',
      'valor_pis'
    ];
  }
});

// Arquivos
const handleFileChange = (e) => processFiles(Array.from(e.target.files));
const handleDrop = (e) => { dragOver.value = false; processFiles(Array.from(e.dataTransfer.files)); };

const processFiles = (files) => {
  const xmlFiles = files.filter(f => f.name.endsWith('.xml'));
  if (xmlFiles.length === 0) {
    mensagem.value = '❌ Selecione apenas arquivos .xml';
    setTimeout(() => mensagem.value = '', 3000);
    return;
  }
  if (selectedFiles.value.length + xmlFiles.length > 500) {
    mensagem.value = `❌ Máximo 500 arquivos. Você tem ${selectedFiles.value.length}, tentando adicionar ${xmlFiles.length}.`;
    setTimeout(() => mensagem.value = '', 3000);
    return;
  }
  selectedFiles.value.push(...xmlFiles);
};

const removeFile = (idx) => selectedFiles.value.splice(idx, 1);

const clearFiles = () => {
  if (confirm('Limpar todos os arquivos?')) {
    selectedFiles.value = [];
  }
};

// API
const enviarArquivos = async () => {
  if (!selectedFiles.value.length) {
    mensagem.value = '❌ Selecione arquivos XML primeiro';
    return;
  }
  
  if (!nomePlanilha.value.trim()) {
    mensagem.value = '❌ Defina um nome para a planilha';
    return;
  }

  const presetValido = ['basico', 'completo', 'fiscal'].includes(presetAtivo.value)
  ? presetAtivo.value
  : 'basico';
  loading.value = true;
  const formData = new FormData();
  selectedFiles.value.forEach(f => formData.append('files', f));
  formData.append('planilha', nomePlanilha.value);
  formData.append('campos_selecionados', JSON.stringify(camposSelecionados.value.filter(Boolean)));
  formData.append('preset', presetValido);
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), 60000);

  try {
    const response = await fetch(`${BASE_URL}${ENDPOINTS.PROCESSAR}`, {
      method: 'POST',
      body: formData,
      signal: controller.signal
    });

    clearTimeout(timeoutId);

    if (response.ok) {
      const blob = await response.blob();
      if (blob.size === 0) throw new Error('Resposta vazia do servidor');
      
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `${nomePlanilha.value}.xlsx`;
      a.click();
      window.URL.revokeObjectURL(url);

      mensagem.value = '✅ Arquivo baixado com sucesso!';
      setTimeout(() => {
        selectedFiles.value = [];
        nomePlanilha.value = '';
        mensagem.value = '';
      }, 2000);
    } else if (response.status === 429) {
      mensagem.value = '❌ Muitas requisições. Aguarde alguns minutos.';
    } else if (response.status === 413) {
      mensagem.value = '❌ Arquivos muito grandes. Reduza o tamanho total.';
    } else {
      mensagem.value = `❌ Erro ${response.status}. Tente novamente.`;
    }
  } catch (err) {
    if (err.name === 'AbortError') {
      mensagem.value = '❌ Requisição expirou (> 60s). Tente com menos arquivos.';
    } else {
      mensagem.value = `❌ Erro na conexão: ${err.message}`;
    }
  } finally {
    loading.value = false;
    clearTimeout(timeoutId);
  }
};
</script>

<style scoped>
/* Respeitar preferência de movimento reduzido */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}

.fade-slide-enter-active, .fade-slide-leave-active {
  transition: all 0.3s ease;
}
.fade-slide-enter-from {
  opacity: 0;
  transform: translateX(20px);
}
.fade-slide-leave-to {
  opacity: 0;
  transform: translateX(-20px);
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  .bg-white { @apply dark:bg-slate-950; }
  .text-slate-950 { @apply dark:text-white; }
  .border-slate-200 { @apply dark:border-slate-700; }
  .bg-slate-50 { @apply dark:bg-slate-900; }
}
</style>