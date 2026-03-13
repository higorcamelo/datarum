<template>
    <div class="min-h-screen flex flex-col bg-gradient-to-b from-white via-orange-50 to-white">
    <header class="w-full bg-white/95 shadow-md py-4 px-8 flex items-center justify-between fixed top-0 left-0 z-10 border-b border-gray-200 backdrop-blur-sm">
      <div class="flex items-center gap-3">
        <button @click="voltarParaInicio" class="flex items-center gap-2 hover:opacity-80 transition text-left">
          <span class="inline-flex items-center justify-center w-10 h-10 bg-gradient-to-br from-orange-700 to-orange-800 rounded-lg text-white font-black text-sm shadow-lg">D</span>
          <div>
            <span class="font-black text-gray-900 text-lg" style="letter-spacing: -0.5px;">Datarum</span>
            <p class="text-xs text-gray-500 leading-none">Conversor XML</p>
          </div>
        </button>
      </div>
      
      <button @click="voltarParaInicio" class="text-gray-600 hover:text-gray-900 text-sm font-semibold transition flex items-center gap-1.5 px-3 py-2 rounded-lg hover:bg-gray-100">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/></svg>
        Voltar
      </button>
    </header>

    <div class="h-24"></div>

    <main class="flex-1 flex justify-center px-4 py-8">
      <div class="w-full max-w-2xl">
        <div class="bg-white rounded-2xl shadow-2xl p-8 border border-gray-200">
            
            <div class="mb-8">
              <h1 class="text-4xl font-black text-gray-900 mb-2" style="letter-spacing: -1px;">Converter XMLs em Excel</h1>
              <p class="text-gray-600 text-base">Selecione seus arquivos e deixe a magia acontecer</p>
            </div>

            <section class="mb-8">
              <div 
                @dragover.prevent="dragOver = true"
                @dragleave.prevent="dragOver = false"
                @drop.prevent="handleDrop"
                :class="['relative border-2 border-dashed rounded-xl p-8 transition-all text-center cursor-pointer',
                         dragOver ? 'border-orange-700 bg-orange-100 scale-105' : 'border-gray-300 hover:border-orange-400 hover:bg-orange-50']">
                <input type="file" multiple accept=".xml" @change="handleFileChange" class="absolute inset-0 w-full h-full opacity-0 cursor-pointer" />
                <div class="space-y-3">
                  <svg class="mx-auto h-12 w-12 text-orange-700" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
                  <div>
                    <p class="text-gray-900 font-bold text-lg">Arraste XMLs aqui</p>
                    <p class="text-gray-600 text-sm">ou clique para selecionar</p>
                  </div>
                  <p class="text-xs text-gray-500 font-medium">Até 50 arquivos por vez</p>
                </div>
              </div>
              
              <div v-if="selectedFiles.length" class="mt-4">
                <div class="flex justify-between items-center mb-3">
                  <div class="flex items-center gap-2">
                    <span class="inline-block w-6 h-6 bg-gradient-to-br from-amber-400 to-amber-600 rounded-full flex items-center justify-center text-white text-xs font-bold">{{ selectedFiles.length }}</span>
                    <span class="text-sm font-bold text-gray-900">arquivo(s) selecionado(s)</span>
                  </div>
                  <button @click="clearFiles" class="text-xs text-gray-500 hover:text-red-600 transition font-semibold">Limpar tudo</button>
                </div>
                <div class="max-h-28 overflow-y-auto space-y-1 bg-gradient-to-b from-orange-50 to-gray-50 p-3 rounded-lg border border-gray-200">
                  <div v-for="(file, idx) in selectedFiles" :key="idx" class="flex justify-between items-center text-sm text-gray-700 py-2 px-3 bg-white rounded border border-gray-100">
                    <span class="truncate font-medium">{{ file.name }}</span>
                    <button @click="removeFile(idx)" class="text-gray-400 hover:text-red-600 ml-2 flex-shrink-0 font-bold">✕</button>
                  </div>
                </div>
              </div>
            </section>

            <transition name="fade-slide">
              <div v-if="selectedFiles.length > 0" class="space-y-6 py-6 border-t border-gray-200 mt-6">
                
                <details class="bg-gradient-to-r from-orange-50 to-gray-50 rounded-lg p-4 border border-gray-200 cursor-pointer hover:bg-orange-100/50 transition shadow-sm">
                  <summary class="font-bold text-gray-900 select-none flex items-center gap-2 text-base">
                    <svg class="w-5 h-5 text-orange-700" fill="currentColor" viewBox="0 0 20 20">
                      <path d="M9 4.804C9 4.393 9.448 4 10 4s1 .393 1 .804v4.392h4.392c.411 0 .804.448.804 1 0 .552-.393 1-.804 1H11v4.392c0 .411-.448.804-1 .804s-1-.393-1-.804v-4.392H4.608c-.411 0-.804-.448-.804-1 0-.552.393-1 .804-1h4.392V4.804z"/>
                    </svg>
                    Opções avançadas
                  </summary>
                  <div class="mt-4 pt-4 border-t border-gray-300">
                    <ConfigPanel 
                      v-model="camposSelecionados"
                      v-model:presetAtivo="presetAtivo"
                      :camposDisponiveis="camposDisponiveis"
                    />
                  </div>
                </details>

                <div>
                  <label class="block text-sm font-bold text-gray-900 mb-3">Nome do arquivo Excel</label>
                  <div class="flex gap-2">
                    <input v-model="nomePlanilha" type="text" placeholder="Ex: NF-e_Janeiro_2025" 
                           class="flex-1 rounded-lg border border-gray-300 focus:ring-2 focus:ring-orange-500 focus:border-transparent p-3 text-sm font-medium bg-white hover:border-orange-400 transition" />
                    <button @click="usarSugestao" class="text-gray-700 border-2 border-gray-300 px-4 py-3 rounded-lg hover:bg-gray-50 hover:border-orange-400 transition text-sm font-bold bg-white">Auto</button>
                  </div>
                </div>

                <button 
                  @click="enviarArquivos" 
                  :disabled="loading"
                  class="w-full bg-gradient-to-r from-orange-700 to-orange-800 text-white py-4 rounded-lg hover:from-orange-800 hover:to-orange-900 disabled:from-gray-400 disabled:to-gray-400 disabled:cursor-not-allowed font-bold transition-all flex items-center justify-center gap-2 text-base shadow-lg hover:shadow-xl">
                  <span v-if="loading" class="animate-spin">↻</span>
                  {{ loading ? 'Processando seus XMLs...' : '⚡ Converter e Baixar' }}
                </button>
              </div>
            </transition>

            <div v-if="mensagem" :class="['mt-6 p-4 rounded-lg text-sm font-semibold border-2', mensagem.includes('✅') ? 'bg-amber-50 text-amber-900 border-amber-300' : 'bg-red-100 text-red-900 border-red-300']">
              {{ mensagem }}
            </div>

          </div>
        </div>
    </main>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import { useRouter } from 'vue-router';
import { ENDPOINTS } from '../config/api';
import ConfigPanel from '../components/ConfigPanel.vue';

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
    { id: 'numero_nf', nome: 'Número NF-e' },
    { id: 'serie', nome: 'Série' },
    { id: 'data_emissao', nome: 'Data Emissão' },
    { id: 'chave_nfe', nome: 'Chave NFe' },
    { id: 'valor_total_nf', nome: 'Valor Total NF' },
    { id: 'valor_produtos_total', nome: 'Total Produtos' },
    { id: 'valor_desconto_total', nome: 'Desconto Total' },
    { id: 'valor_frete_total', nome: 'Frete Total' }
  ],
  parceiros: [
    { id: 'cnpj_emitente', nome: 'CNPJ Emitente' },
    { id: 'emitente', nome: 'Razão Social Emitente' },
    { id: 'uf_emitente', nome: 'UF Emitente' },
    { id: 'cnpj_destinatario', nome: 'CNPJ Destinatário' },
    { id: 'destinatario', nome: 'Razão Social Destinatário' },
    { id: 'uf_destinatario', nome: 'UF Destinatário' }
  ],
  itens: [
    { id: 'codigo_produto', nome: 'Código Produto' },
    { id: 'descricao_produto', nome: 'Descrição Produto' },
    { id: 'ncm', nome: 'NCM' },
    { id: 'cfop', nome: 'CFOP' },
    { id: 'unidade_comercial', nome: 'Unidade' },
    { id: 'quantidade_comercial', nome: 'Quantidade' },
    { id: 'valor_unitario', nome: 'Valor Unitário' },
    { id: 'valor_total_item', nome: 'Total Item' },
    { id: 'valor_desconto_item', nome: 'Desconto Item' }
  ],
  impostos: [
    { id: 'cst_icms', nome: 'CST/CSOSN ICMS' },
    { id: 'base_icms', nome: 'Base ICMS' },
    { id: 'aliquota_icms', nome: 'Alíquota ICMS' },
    { id: 'icms_valor', nome: 'Valor ICMS' },
    { id: 'base_icms_st', nome: 'Base ICMS ST' },
    { id: 'icms_st_valor', nome: 'Valor ICMS ST' },
    { id: 'valor_ipi', nome: 'Valor IPI' },
    { id: 'pis_valor', nome: 'PIS' },
    { id: 'cofins_valor', nome: 'COFINS' }
  ]
};

// Reseta tudo ao voltar
const voltarParaInicio = () => {
  if (selectedFiles.value.length > 0) {
    if (confirm('Deseja sair? Os arquivos serão perdidos.')) {
      router.push('/');
    }
  } else {
    router.push('/');
  }
};

// Lógica de Presets
watch(presetAtivo, (novo) => {
  if (novo === 'basico')
    camposSelecionados.value = ['numero_nf', 'data_emissao', 'valor_total_nf'];

  else if (novo === 'completo')
    camposSelecionados.value = Object.values(camposDisponiveis)
      .flat()
      .map(c => c.id);

  else if (novo === 'fiscal')
    camposSelecionados.value = [
      'numero_nf',
      'data_emissao',
      'cnpj_emitente',
      'emitente',
      'valor_unitario'
    ];
});

// Arquivos
const handleFileChange = (e) => processFiles(Array.from(e.target.files));
const handleDrop = (e) => { dragOver.value = false; processFiles(Array.from(e.dataTransfer.files)); };
const processFiles = (files) => {
  const xmls = files.filter(f => f.name.toLowerCase().endsWith('.xml'));
  selectedFiles.value = [...selectedFiles.value, ...xmls].slice(0, 50);
  mensagem.value = '';
};
const removeFile = (idx) => selectedFiles.value.splice(idx, 1);
const clearFiles = () => { 
  selectedFiles.value = []; 
  mensagem.value = ''; 
  nomePlanilha.value = '';
};
const usarSugestao = () => {
  const data = new Date().toLocaleDateString('pt-BR').replace(/\//g, '_');
  nomePlanilha.value = `Relatorio_Datarum_${data}`;
};

// API
const enviarArquivos = async () => {
  if (!selectedFiles.value.length) {
    mensagem.value = '❌ Selecione pelo menos um XML.';
    return;
  }

  try {
    loading.value = true;
    mensagem.value = '';

    const formData = new FormData();

    // Nome correto do parâmetro
    formData.append('planilha', nomePlanilha.value || 'extracao_datarum');

    // Arquivos (nome correto: files)
    selectedFiles.value.forEach(f => formData.append('files', f));

    // Preset
    formData.append('preset', presetAtivo.value);

    // Campos personalizados
    formData.append(
      'campos_selecionados',
      JSON.stringify(camposSelecionados.value)
    );

    const response = await fetch(ENDPOINTS.PROCESSAR_EXCEL, {
      method: 'POST',
      body: formData
    })

    if (!response.ok) {
      const erro = await response.json()
      throw new Error(erro.detail || "Erro ao processar")
    }

    const blob = await response.blob()
    const url = window.URL.createObjectURL(blob);

    const a = document.createElement('a');
    a.href = url;
    a.download = `${nomePlanilha.value || 'relatorio'}.xlsx`;
    document.body.appendChild(a);
    a.click();
    a.remove();

    mensagem.value = '✅ Planilha gerada com sucesso!';
  } catch (err) {
    mensagem.value = `❌ ${err.message}`;
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
.fade-slide-enter-active, .fade-slide-leave-active {
  transition: all 0.4s ease;
}
.fade-slide-enter-from {
  opacity: 0;
  transform: translateY(-20px);
}
.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>