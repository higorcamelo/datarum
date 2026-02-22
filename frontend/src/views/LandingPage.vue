<template>
  <div class="min-h-screen bg-white">
    <!-- Header/Navigation -->
    <header class="bg-white/95 backdrop-blur fixed w-full top-0 z-50 border-b border-gray-100">
      <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center py-4">
          <div class="flex items-center gap-3">
            <span class="inline-flex items-center justify-center w-10 h-10 bg-purple-600 rounded-full text-white text-xl font-bold">D</span>
            <div class="flex flex-col">
              <span class="text-xl font-bold text-purple-700">Datarum</span>
              <span class="text-xs text-purple-600 hidden sm:block">Automação fiscal inteligente</span>
            </div>
          </div>
          <div class="flex items-center gap-4">
            <button aria-label="Ir para Recursos" @click="scrollTo('features')" class="hidden md:block text-gray-600 hover:text-purple-600 transition">Recursos</button>
            <button aria-label="Ir para Como Funciona" @click="scrollTo('how-it-works')" class="hidden md:block text-gray-600 hover:text-purple-600 transition">Como Funciona</button>
            <button aria-label="Começar" @click="goToApp" class="bg-purple-600 text-white px-6 py-2 rounded-lg hover:bg-purple-700 transition font-medium">
              Começar
            </button>
          </div>
        </div>
      </nav>
    </header>

    <!-- Hero Section -->
    <section class="pt-20 pb-16 bg-gradient-to-br from-purple-50 via-white to-purple-100">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid lg:grid-cols-2 gap-12 items-center">
          <div class="text-center lg:text-left">
            <h1 class="text-4xl sm:text-5xl lg:text-6xl font-bold text-purple-800 leading-tight mb-6">
              Datarum — converta XMLs em planilhas localmente
            </h1>
            <p class="text-xl text-gray-600 mb-8 leading-relaxed max-w-2xl mx-auto lg:mx-0">
              Processamento local no seu navegador — simples, confiável e sem instalações.
            </p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start">
              <button aria-label="Começar" @click="goToApp" class="bg-purple-700 hover:bg-purple-800 text-white font-semibold py-4 px-8 rounded-lg shadow-lg transition text-lg">
                Começar
              </button>
              <button aria-label="Ver demonstração" @click="scrollTo('demo')" class="border-2 border-purple-600 text-purple-600 px-8 py-4 rounded-lg hover:bg-purple-50 transition font-semibold text-lg">
                Ver Demonstração
              </button>
            </div>
            <p class="text-sm text-gray-600 mt-4 text-center lg:text-left">
              Uso direto • Sem cadastro • Processamento local
            </p>
            <div class="flex items-center gap-6 mt-6 justify-center lg:justify-start text-sm text-gray-500">
              <div class="flex items-center gap-2">
                <svg class="w-5 h-5 text-green-500" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
                </svg>
              </div>
              <div class="flex items-center gap-2">
                <svg class="w-5 h-5 text-green-500" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
                </svg>
                <span>Sem Cadastro</span>
              </div>
              <div class="flex items-center gap-2">
                <svg class="w-5 h-5 text-green-500" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
                </svg>
                <span>Processamento Local</span>
              </div>
              <span class="font-medium text-sm text-purple-600">Envie feedback</span>
            </div>
          </div>
          <div class="relative">
            <div class="bg-white rounded-2xl shadow-2xl p-8 border border-gray-100">
              <div class="bg-gray-50 rounded-lg p-4 mb-4">
                <div class="flex items-center gap-2 mb-2">
                  <div class="w-3 h-3 bg-red-400 rounded-full"></div>
                  <div class="w-3 h-3 bg-yellow-400 rounded-full"></div>
                  <div class="w-3 h-3 bg-green-400 rounded-full"></div>
                  <span class="text-sm text-gray-500 ml-auto">XMLs NFe → Excel</span>
                </div>
                <div class="space-y-2">
                  <div class="bg-purple-100 p-2 rounded text-sm text-purple-700">📄 nota_fiscal_001.xml</div>
                  <div class="bg-purple-100 p-2 rounded text-sm text-purple-700">📄 nota_fiscal_002.xml</div>
                  <div class="bg-purple-100 p-2 rounded text-sm text-purple-700">📄 nota_fiscal_003.xml</div>
                </div>
              </div>
              <div class="text-center py-4">
                <div class="inline-flex items-center gap-2 text-purple-600">
                  <svg class="w-6 h-6 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
                  </svg>
                  <span class="font-medium">Processando...</span>
                </div>
              </div>
              <div class="bg-green-50 p-4 rounded-lg border border-green-200">
                <div class="flex items-center gap-2 text-green-700">
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
                  </svg>
                  <span class="font-medium">📊 planilha_notas_fiscais.xlsx</span>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Quick Benefits Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-16 max-w-5xl mx-auto">
          <div class="bg-white p-6 rounded-lg shadow-lg text-center border border-gray-100">
            <svg class="w-10 h-10 text-purple-600 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M9 19l3 3m0 0l3-3m-3 3V10"/>
            </svg>
            <h3 class="text-xl font-semibold mb-2 text-gray-900">Upload em massa</h3>
            <p class="text-gray-600">Arraste vários XMLs de uma vez.</p>
          </div>
          
          <div class="bg-white p-6 rounded-lg shadow-lg text-center border border-gray-100">
            <svg class="w-10 h-10 text-purple-600 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
            </svg>
            <h3 class="text-xl font-semibold mb-2 text-gray-900">Processamento local</h3>
            <p class="text-gray-600">Conversão automática, direto no navegador.</p>
          </div>
          
          <div class="bg-white p-6 rounded-lg shadow-lg text-center border border-gray-100">
            <svg class="w-10 h-10 text-purple-600 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
            <h3 class="text-xl font-semibold mb-2 text-gray-900">100% seguro e privado</h3>
            <p class="text-gray-600">Seus dados ficam apenas no seu computador, zero uploads.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Features Section -->
    <section id="features" class="py-20 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold text-gray-900">Recursos de Especialista</h2>
        </div>
        
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <FeatureCard 
            v-for="feature in features" 
            :key="feature.title"
            :title="feature.title"
            :description="feature.desc"
          >
            <template #icon>
              <svg class="w-8 h-8 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="feature.icon"/>
              </svg>
            </template>
          </FeatureCard>
        </div>
      </div>
    </section>

    <!-- How it Works Section -->
    <section id="how-it-works" class="py-20 bg-gray-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl sm:text-4xl font-bold text-gray-900 mb-4">
            Como funciona?
          </h2>
          <p class="text-xl text-gray-600">
            Em apenas 3 passos simples você terá sua planilha pronta
          </p>
        </div>

        <div class="grid md:grid-cols-3 gap-8">
          <div class="text-center">
            <div class="w-20 h-20 bg-purple-600 text-white rounded-full flex items-center justify-center mx-auto mb-6 text-2xl font-bold">
              1
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-4">Selecione os XMLs</h3>
            <p class="text-gray-600 mb-6">
              Arraste e solte seus arquivos XML de NFe ou clique para selecioná-los. 
              Suporte para múltiplos arquivos.
            </p>
            <div class="bg-white p-4 rounded-lg border border-gray-200">
              <div class="border-2 border-dashed border-purple-300 rounded-lg p-6">
                <svg class="w-12 h-12 text-purple-400 mx-auto mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"/>
                </svg>
                <p class="text-sm text-gray-500">Arraste XMLs aqui</p>
              </div>
            </div>
          </div>

          <div class="text-center">
            <div class="w-20 h-20 bg-purple-600 text-white rounded-full flex items-center justify-center mx-auto mb-6 text-2xl font-bold">
              2
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-4">Processamento Automático</h3>
            <p class="text-gray-600 mb-6">
              O sistema analisa automaticamente todos os XMLs, extrai as informações importantes 
              e organiza tudo em uma planilha profissional.
            </p>
            <div class="bg-white p-4 rounded-lg border border-gray-200">
              <div class="space-y-2">
                <div class="flex items-center gap-2">
                  <div class="w-4 h-4 bg-purple-600 rounded animate-pulse"></div>
                  <div class="text-sm text-gray-600">Analisando XMLs...</div>
                </div>
                <div class="flex items-center gap-2">
                  <div class="w-4 h-4 bg-purple-600 rounded animate-pulse"></div>
                  <div class="text-sm text-gray-600">Extraindo dados...</div>
                </div>
                <div class="flex items-center gap-2">
                  <div class="w-4 h-4 bg-purple-600 rounded animate-pulse"></div>
                  <div class="text-sm text-gray-600">Gerando planilha...</div>
                </div>
              </div>
            </div>
          </div>

          <div class="text-center">
            <div class="w-20 h-20 bg-purple-600 text-white rounded-full flex items-center justify-center mx-auto mb-6 text-2xl font-bold">
              3
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-4">Download Automático</h3>
            <p class="text-gray-600 mb-6">
              Sua planilha Excel é gerada automaticamente e o download inicia na hora. 
              Pronta para abrir no Excel, Google Sheets ou qualquer programa de planilhas.
            </p>
            <div class="bg-white p-4 rounded-lg border border-gray-200">
              <div class="bg-green-50 border border-green-200 rounded-lg p-4">
                <div class="flex items-center gap-2 text-green-700">
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
                  </svg>
                  <span class="text-sm font-medium">planilha.xlsx baixado!</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Demo Section -->
    <section id="demo" class="py-20 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl sm:text-4xl font-bold text-gray-900 mb-4">
            Veja o que é extraído dos XMLs
          </h2>
          <p class="text-xl text-gray-600">
            Todas as informações importantes organizadas em colunas
          </p>
        </div>

        <div class="bg-white rounded-2xl shadow-2xl border border-gray-200 overflow-hidden">
          <div class="bg-gray-50 px-6 py-4 border-b border-gray-200">
            <div class="flex items-center gap-2">
              <div class="w-3 h-3 bg-red-400 rounded-full"></div>
              <div class="w-3 h-3 bg-yellow-400 rounded-full"></div>
              <div class="w-3 h-3 bg-green-400 rounded-full"></div>
              <span class="text-sm text-gray-600 ml-4">planilha_nfe_exemplo.xlsx</span>
            </div>
          </div>
          <div class="overflow-x-auto">
            <table class="w-full text-sm">
              <thead class="bg-purple-50">
                <tr>
                  <th class="px-4 py-3 text-left font-semibold text-purple-700">Nº Nota</th>
                  <th class="px-4 py-3 text-left font-semibold text-purple-700">Data Emissão</th>
                  <th class="px-4 py-3 text-left font-semibold text-purple-700">CNPJ Emitente</th>
                  <th class="px-4 py-3 text-left font-semibold text-purple-700">Razão Social</th>
                  <th class="px-4 py-3 text-left font-semibold text-purple-700">Valor Total</th>
                  <th class="px-4 py-3 text-left font-semibold text-purple-700">Série</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-200">
                <tr class="hover:bg-gray-50">
                  <td class="px-4 py-3">000000123</td>
                  <td class="px-4 py-3">15/07/2025</td>
                  <td class="px-4 py-3">12.345.678/0001-90</td>
                  <td class="px-4 py-3">Empresa Exemplo Ltda</td>
                  <td class="px-4 py-3">R$ 1.250,00</td>
                  <td class="px-4 py-3">1</td>
                </tr>
                <tr class="hover:bg-gray-50">
                  <td class="px-4 py-3">000000124</td>
                  <td class="px-4 py-3">16/07/2025</td>
                  <td class="px-4 py-3">98.765.432/0001-10</td>
                  <td class="px-4 py-3">Fornecedor ABC S.A.</td>
                  <td class="px-4 py-3">R$ 3.780,50</td>
                  <td class="px-4 py-3">1</td>
                </tr>
                <tr class="hover:bg-gray-50">
                  <td class="px-4 py-3">000000125</td>
                  <td class="px-4 py-3">17/07/2025</td>
                  <td class="px-4 py-3">11.222.333/0001-44</td>
                  <td class="px-4 py-3">Produtos XYZ Eireli</td>
                  <td class="px-4 py-3">R$ 850,25</td>
                  <td class="px-4 py-3">1</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="bg-gray-50 px-6 py-4 border-t border-gray-200">
            <p class="text-sm text-gray-600 text-center">
              E mais 15+ campos incluindo: Chave NFe, CEP, UF, Valor ICMS, Valor IPI, Produtos, etc.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Roadmap Section -->
    <section id="roadmap" class="py-20 bg-gradient-to-br from-gray-50 to-gray-100">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <div class="inline-flex items-center gap-2 bg-blue-100 text-blue-700 px-4 py-2 rounded-full text-sm font-medium mb-4">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
            </svg>
            Em desenvolvimento
          </div>
          <h2 class="text-3xl sm:text-4xl font-bold text-gray-900 mb-4">Próximas versões</h2>
          <p class="text-xl text-gray-600 max-w-3xl mx-auto">
            Baseado no seu feedback, vamos evoluir o Datarum com funcionalidades que realmente importam
          </p>
        </div>

      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
      <RoadmapCard 
        v-for="item in roadmapItems" 
        :key="item.title"
        v-bind="item" 
        class="h-full"
      />
    </div>
  </div>
</section>

    <!-- Footer -->
    <footer class="bg-gray-900 text-white py-12">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center">
          <div class="flex items-center justify-center gap-3 mb-4">
            <span class="inline-flex items-center justify-center w-10 h-10 bg-purple-600 rounded-full text-white text-xl font-bold">D</span>
            <span class="text-2xl font-bold">Datarum</span>
          </div>
          <p class="text-gray-400 mb-6">
            Conversão de XML para planilhas
          </p>
          <div class="flex justify-center gap-8 text-sm text-gray-400 mb-8">
            <button @click="scrollTo('features')" class="hover:text-white transition">Recursos</button>
            <button @click="scrollTo('how-it-works')" class="hover:text-white transition">Como Funciona</button>
            <button @click="goToApp" class="hover:text-white transition">Abrir Aplicativo</button>
          </div>
          <div class="border-t border-gray-800 pt-8">
            <div class="flex flex-col sm:flex-row justify-center items-center gap-4 mb-4">
              <p class="text-gray-500 text-sm">
                &copy; {{ new Date().getFullYear() }} Datarum. Todos os direitos reservados.
              </p>
              <div class="flex items-center gap-2 text-blue-400 text-sm">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
                </svg>
                <span>Versão 1.0</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue';
// 1. Importe o novo componente (ajuste o caminho conforme sua pasta)
import RoadmapCard from '../components/RoadmapCard.vue';
import FeatureCard from '../components/FeatureCard.vue';

const emit = defineEmits(['goToApp']);

const showFeedbackToast = ref(false);
const FORMS_URL = import.meta.env.VITE_FORMS_URL;

// Dados das Features (Mantidos)
const features = [
  { title: "Super Rápido", desc: "Suporta múltiplos arquivos localmente.", icon: "M13 10V3L4 14h7v7l9-11h-7z" },
  { title: "Compatibilidade", desc: "Formatos NFe comuns (v4.00).", icon: "M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" },
  { title: "100% Seguro", desc: "Dados nunca saem do seu computador.", icon: "M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" }
];

// 2. Adicione o Array do Roadmap (Secando o HTML anterior)
const roadmapItems = [
  { 
    title: "Datarum v1.0", 
    description: "Conversão XML para Excel com seleção de colunas, ordenação personalizada e sumário de totais.", 
    status: "DISPONÍVEL", 
    type: "success", 
    icon: "M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" 
  },
  { 
    title: "Relatórios Básicos", 
    description: "Totais por CFOP, fornecedor e resumo fiscal inteligente.", 
    status: "PLANEJADO", 
    type: "warning", 
    icon: "M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" 
  },
  { 
    title: "Insights Automáticos", 
    description: "Análise de padrões de compra e detecção de ICMS ST.", 
    status: "FUTURO", 
    type: "neutral", 
    icon: "M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" 
  },
  { 
    title: "Recursos Colaborativos", 
    description: "Upload por pasta e histórico de exportações.", 
    status: "FUTURO", 
    type: "neutral", 
    icon: "M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" 
  },
  { 
    title: "Integrações", 
    description: "APIs e conectores com ERPs conforme a demanda.", 
    status: "FUTURO", 
    type: "neutral", 
    icon: "M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v14a2 2 0 002 2z" 
  }
];

// Métodos
const scrollTo = (id) => {
  document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' });
};

const goToApp = () => emit('goToApp');
</script>

<style scoped>
/* Animações e estilos adicionais se necessário */
.animate-pulse {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}

/* Respeitar preferência de movimento reduzido */
@media (prefers-reduced-motion: reduce) {
  .animate-pulse,
  .animate-spin {
    animation: none !important;
  }
}
</style>
