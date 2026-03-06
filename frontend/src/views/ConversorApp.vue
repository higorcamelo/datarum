<template>
    <div class="min-h-screen flex flex-col bg-gradient-to-br from-purple-100 via-white to-purple-200">
    <header class="w-full bg-white/80 backdrop-blur shadow-md py-3 px-8 flex items-center justify-between fixed top-0 left-0 z-10 border-b border-purple-100">
      <div class="flex items-center gap-3">
        <button @click="voltarParaInicio" class="flex items-center gap-3 hover:opacity-80 transition text-left">
          <span class="inline-flex items-center justify-center w-11 h-11 bg-purple-600 rounded-full text-white text-2xl font-bold shadow">D</span>
          <div class="flex flex-col">
            <span class="text-2xl font-extrabold text-purple-700 tracking-tight">Datarum</span>
            <span class="text-xs text-purple-600 font-medium">Automação fiscal inteligente</span>
          </div>
        </button>
      </div>
      
      <button @click="voltarParaInicio" class="text-purple-600 hover:text-purple-700 text-sm font-bold transition flex items-center gap-1">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/></svg>
        Sair
      </button>
    </header>

    <div class="h-20"></div>

    <main class="flex-1 flex justify-center px-4 py-8">
      <div class="w-full max-w-7xl flex flex-col lg:flex-row gap-6 lg:gap-8">
        
        <aside class="w-full lg:w-72 order-2 lg:order-1">
          <div class="bg-white/90 rounded-2xl shadow-lg p-6 border border-purple-100">
            <h3 class="font-bold text-purple-700 mb-4 flex items-center gap-2">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>
              Sessão Atual
            </h3>
            <div class="space-y-3 text-sm">
              <div class="flex justify-between">
                <span class="text-gray-600">Arquivos:</span>
                <span class="font-bold text-purple-600">{{ selectedFiles.length }}</span>
              </div>
              <div class="flex justify-between" v-if="selectedFiles.length > 0">
                <span class="text-gray-600">Colunas:</span>
                <span class="font-bold text-purple-600">{{ camposSelecionados.length }}</span>
              </div>
            </div>
          </div>
        </aside>

        <div class="flex-1 max-w-2xl mx-auto order-1 lg:order-2">
          <div class="bg-white/90 rounded-3xl shadow-2xl p-8 border border-purple-100">
            
            <div class="text-center mb-8">
              <h1 class="text-3xl font-extrabold text-purple-700 mb-2">Extração de Dados</h1>
              <p class="text-gray-500 text-sm">Selecione seus arquivos XML para começar.</p>
            </div>

            <section class="mb-8">
              <div 
                @dragover.prevent="dragOver = true"
                @dragleave.prevent="dragOver = false"
                @drop.prevent="handleDrop"
                :class="['relative border-2 border-dashed rounded-xl p-10 transition-all text-center cursor-pointer',
                         dragOver ? 'border-purple-500 bg-purple-50' : 'border-purple-200 hover:border-purple-300']">
                <input type="file" multiple accept=".xml" @change="handleFileChange" class="absolute inset-0 w-full h-full opacity-0 cursor-pointer" />
                <div class="space-y-3">
                  <svg class="mx-auto h-12 w-12 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
                  <p class="text-purple-600 font-bold">Clique ou arraste múltiplos XMLs aqui</p>
                  <p class="text-xs text-gray-400">Limite de 50 arquivos por vez</p>
                </div>
              </div>
              
              <div v-if="selectedFiles.length" class="mt-4">
                <div class="flex justify-between items-center mb-2">
                  <span class="text-xs font-bold text-purple-700 uppercase">Arquivos carregados</span>
                  <button @click="clearFiles" class="text-xs text-red-500 hover:underline">Remover todos</button>
                </div>
                <div class="max-h-32 overflow-y-auto space-y-2 border border-purple-50 p-2 rounded-lg">
                  <div v-for="(file, idx) in selectedFiles" :key="idx" class="flex justify-between items-center bg-white p-2 rounded border border-purple-100 text-xs shadow-sm">
                    <span class="truncate pr-4 text-gray-700">{{ file.name }}</span>
                    <button @click="removeFile(idx)" class="text-gray-400 hover:text-red-500 transition">✕</button>
                  </div>
                </div>
              </div>
            </section>

            <transition name="fade-slide">
              <div v-if="selectedFiles.length > 0" class="space-y-8 py-6 border-t border-purple-50">
                
                <ConfigPanel 
                  v-model="camposSelecionados"
                  v-model:presetAtivo="presetAtivo"
                  :camposDisponiveis="camposDisponiveis"
                />

                <section>
                  <label class="block text-sm font-bold text-purple-700 mb-2">Nome da Planilha Excel</label>
                  <div class="flex gap-2">
                    <input v-model="nomePlanilha" type="text" placeholder="Ex: Notas_Entrada_Jan" 
                           class="flex-1 rounded-lg border-purple-200 focus:ring-purple-600 focus:border-purple-600 p-2.5 text-sm" />
                    <button @click="usarSugestao" class="bg-purple-100 text-purple-700 px-4 py-2 rounded-lg text-xs font-bold hover:bg-purple-200 transition">Sugestão</button>
                  </div>
                </section>

                <button 
                  @click="enviarArquivos" 
                  :disabled="loading"
                  class="w-full bg-purple-600 text-white py-4 rounded-xl hover:bg-purple-700 disabled:bg-gray-300 font-extrabold shadow-lg transition-all flex items-center justify-center gap-3 text-lg">
                  <span v-if="loading" class="animate-spin">↻</span>
                  {{ loading ? 'Processando XMLs...' : 'Gerar e Baixar Planilha' }}
                </button>
              </div>
            </transition>

            <div v-if="mensagem" :class="['mt-4 p-4 rounded-xl text-sm font-bold shadow-inner', mensagem.includes('✅') ? 'bg-green-50 text-green-700 border border-green-200' : 'bg-red-50 text-red-700 border border-red-200']">
              {{ mensagem }}
            </div>

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