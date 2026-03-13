<template>
  <div class="min-h-screen bg-gradient-to-b from-white via-white to-orange-50">
    <!-- Padrão subtle de fundo -->
    <div class="absolute inset-0 opacity-[0.02] pointer-events-none" style="background-image: radial-gradient(circle at 1px 1px, currentColor 0.5px, transparent 0.5px); background-size: 40px 40px;"></div>
    
      <header class="bg-white/95 fixed w-full top-0 z-50 border-b border-gray-200 backdrop-blur-sm">
    <nav class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center py-3">
        
        <router-link to="/" class="flex items-center gap-2 group">
          <span class="inline-flex items-center justify-center w-10 h-10 bg-gradient-to-br from-orange-700 to-orange-800 rounded-lg text-white font-black text-base group-hover:shadow-lg transition-all duration-200">D</span>
          <div>
            <span class="text-lg font-black text-gray-900" style="letter-spacing: -0.5px;">Datarum</span>
          </div>
        </router-link>

        <button 
          aria-label="Começar" 
          @click="$router.push('/conversor')" 
          class="bg-gradient-to-r from-orange-700 to-orange-800 text-white px-6 py-2.5 rounded-lg hover:shadow-lg hover:from-orange-800 hover:to-orange-900 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-700 transition-all duration-200 font-semibold text-sm"
        >
          Abrir Aplicativo
        </button>
      </div>
    </nav>
  </header>

  <section class="relative pt-28 pb-20 bg-white overflow-hidden">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid lg:grid-cols-2 gap-12 items-center">
        <div class="z-10">
          <div class="inline-block mb-6 px-3 py-1.5 bg-orange-100 text-orange-700 rounded-full text-xs font-bold tracking-wide">
            ⚡ Sem complicações
          </div>
          
          <h1 class="text-6xl sm:text-7xl font-black text-gray-900 leading-tight mb-6" style="letter-spacing: -1px;">
            Converta XMLs em segundos
          </h1>

          <p class="text-xl text-gray-600 mb-10 leading-relaxed max-w-lg">
            Processamento 100% local. Seus dados nunca saem do PC. Rápido, seguro, simples.
          </p>

          <div class="flex flex-col sm:flex-row gap-4 mb-10">
            <button
              aria-label="Começar"
              @click="$router.push('/conversor')"
              class="inline-flex items-center justify-center bg-gradient-to-r from-orange-700 to-orange-800 hover:from-orange-800 hover:to-orange-900 text-white font-bold py-4 px-8 rounded-lg focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-700 transition-all duration-200 shadow-lg hover:shadow-xl text-lg"
            >
              Abrir Aplicativo →
            </button>
            <button
              @click="scrollTo('demo')"
              class="inline-flex items-center justify-center border-2 border-gray-300 text-gray-700 hover:border-gray-400 hover:bg-gray-50 px-8 py-4 rounded-lg focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-700 transition-all duration-200 font-semibold"
            >
              Ver Demo
            </button>
          </div>

          <div class="flex flex-col gap-3 text-sm">
            <div class="flex items-center gap-2 text-gray-600">
              <svg class="w-5 h-5 text-orange-700 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
              </svg>
              <span>Nenhum cadastro obrigatório</span>
            </div>
            <div class="flex items-center gap-2 text-gray-600">
              <svg class="w-5 h-5 text-orange-700 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
              </svg>
              <span>Processamento local (dados no seu PC)</span>
            </div>
            <div class="flex items-center gap-2 text-gray-600">
              <svg class="w-5 h-5 text-orange-700 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
              </svg>
              <span>Compatível com NF-e v4.00</span>
            </div>
          </div>
        </div>
        
        <!-- Visual lado direito -->
        <div class="relative hidden lg:block">
          <div class="absolute -inset-4 bg-gradient-to-br from-orange-100 to-amber-50 rounded-2xl blur-2xl opacity-40"></div>
          <div class="relative bg-white rounded-2xl shadow-2xl p-8 border border-gray-200">
            <div class="bg-gray-50 rounded-lg p-4 mb-4 border border-gray-100">
              <div class="flex items-center gap-2 mb-3">
                <div class="w-3 h-3 bg-red-400 rounded-full"></div>
                <div class="w-3 h-3 bg-yellow-400 rounded-full"></div>
                <div class="w-3 h-3 bg-green-400 rounded-full"></div>
                <span class="text-xs text-gray-500 ml-auto">XMLs → Excel</span>
              </div>
              <div class="space-y-2">
                <div class="bg-orange-50 px-3 py-2 rounded text-xs text-orange-700 font-medium">📄 nota_001.xml</div>
                <div class="bg-orange-50 px-3 py-2 rounded text-xs text-orange-700 font-medium">📄 nota_002.xml</div>
                <div class="bg-orange-50 px-3 py-2 rounded text-xs text-orange-700 font-medium">📄 nota_003.xml</div>
              </div>
            </div>
            <div class="text-center py-6">
              <div class="inline-flex items-center gap-2 text-orange-700">
                <svg class="w-6 h-6 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
                </svg>
                <span class="font-semibold text-sm">Convertendo...</span>
              </div>
            </div>
            <div class="bg-amber-50 px-4 py-3 rounded-lg border border-amber-200">
              <div class="flex items-center gap-2 text-amber-700 text-sm font-semibold">
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                </svg>
                ✓ relatorio.xlsx
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

    <section id="demo" class="py-20 bg-gradient-to-b from-white via-orange-50 to-white relative">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-14">
          <h2 class="text-5xl sm:text-6xl font-black text-gray-900 mb-4" style="letter-spacing: -1px;">
            Veja exatamente o que é extraído
          </h2>
          <p class="text-lg text-gray-600 max-w-2xl mx-auto">
            Suas planilhas organizadas, limpas e prontas para análise ou importação em qualquer sistema
          </p>
        </div>

        <div class="bg-white rounded-2xl shadow-2xl border border-gray-200 overflow-hidden hover:shadow-3xl transition">
          <div class="overflow-x-auto">
            <table class="w-full text-sm">
              <thead class="bg-gradient-to-r from-orange-50 to-amber-100 border-b border-gray-200">
                <tr>
                  <th class="px-6 py-4 text-left font-bold text-orange-900">Nº Nota</th>
                  <th class="px-6 py-4 text-left font-bold text-orange-900">Data Emissão</th>
                  <th class="px-6 py-4 text-left font-bold text-orange-900">CNPJ Emitente</th>
                  <th class="px-6 py-4 text-left font-bold text-orange-900">Razão Social</th>
                  <th class="px-6 py-4 text-left font-bold text-orange-900">Valor Total</th>
                  <th class="px-6 py-4 text-left font-bold text-orange-900">Série</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-100">
                <tr class="hover:bg-orange-50 transition">
                  <td class="px-6 py-4 font-semibold text-gray-900">000000123</td>
                  <td class="px-6 py-4 text-gray-600">15/07/2025</td>
                  <td class="px-6 py-4 text-gray-600 font-mono text-xs">12.345.678/0001-90</td>
                  <td class="px-6 py-4 text-gray-700">Empresa Exemplo Ltda</td>
                  <td class="px-6 py-4 font-semibold text-gray-900">R$ 1.250,00</td>
                  <td class="px-6 py-4 text-gray-600">1</td>
                </tr>
                <tr class="hover:bg-orange-50 transition">
                  <td class="px-6 py-4 font-semibold text-gray-900">000000124</td>
                  <td class="px-6 py-4 text-gray-600">16/07/2025</td>
                  <td class="px-6 py-4 text-gray-600 font-mono text-xs">98.765.432/0001-10</td>
                  <td class="px-6 py-4 text-gray-700">Fornecedor ABC S.A.</td>
                  <td class="px-6 py-4 font-semibold text-gray-900">R$ 3.780,50</td>
                  <td class="px-6 py-4 text-gray-600">1</td>
                </tr>
                <tr class="hover:bg-orange-50 transition">
                  <td class="px-6 py-4 font-semibold text-gray-900">000000125</td>
                  <td class="px-6 py-4 text-gray-600">17/07/2025</td>
                  <td class="px-6 py-4 text-gray-600 font-mono text-xs">11.222.333/0001-44</td>
                  <td class="px-6 py-4 text-gray-700">Produtos XYZ Eireli</td>
                  <td class="px-6 py-4 font-semibold text-gray-900">R$ 850,25</td>
                  <td class="px-6 py-4 text-gray-600">1</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>

    <section id="roadmap" class="py-16 bg-gradient-to-b from-white to-gray-50 border-t border-gray-200">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-20">
          <h2 class="text-5xl sm:text-6xl font-black text-gray-900 mb-4" style="letter-spacing: -1px;">
            Roadmap
          </h2>
          <p class="text-xl text-gray-600">
            Acompanhe o desenvolvimento
          </p>
        </div>

        <div class="max-w-2xl">
          <!-- v1.0 - Released -->
          <RoadmapCard title="v1.0" status="✓ Disponível" type="success">
            <li class="flex items-center gap-2">
              <span class="w-1 h-1 bg-gray-600 rounded-full"></span>
              <span>Extração de XML em Excel</span>
            </li>
            <li class="flex items-center gap-2">
              <span class="w-1 h-1 bg-gray-600 rounded-full"></span>
              <span>Interface simples</span>
            </li>
            <li class="flex items-center gap-2">
              <span class="w-1 h-1 bg-gray-600 rounded-full"></span>
              <span>Sem necessidade de login</span>
            </li>
          </RoadmapCard>

          <!-- v1.1 - Soon -->
          <RoadmapCard title="v1.1" status="→ Em desenvolvimento" type="info">
            <li class="flex items-center gap-2">
              <span class="w-1 h-1 bg-gray-600 rounded-full"></span>
              <span>Histórico de conversões</span>
            </li>
            <li class="flex items-center gap-2">
              <span class="w-1 h-1 bg-gray-600 rounded-full"></span>
              <span>Presets personalizados</span>
            </li>
            <li class="flex items-center gap-2">
              <span class="w-1 h-1 bg-gray-600 rounded-full"></span>
              <span>Template customizado</span>
            </li>
          </RoadmapCard>

          <!-- v2.0+ - Future -->
          <RoadmapCard title="v2.0+" status="◯ Futuro" type="neutral">
            <li class="flex items-center gap-2">
              <span class="w-1 h-1 bg-gray-600 rounded-full"></span>
              <span>Processamento em lote</span>
            </li>
            <li class="flex items-center gap-2">
              <span class="w-1 h-1 bg-gray-600 rounded-full"></span>
              <span>API para integrações</span>
            </li>
            <li class="flex items-center gap-2">
              <span class="w-1 h-1 bg-gray-600 rounded-full"></span>
              <span>Análise de dados avançada</span>
            </li>
          </RoadmapCard>
        </div>
      </div>
    </section>

    <footer class="bg-gradient-to-b from-gray-900 to-gray-950 text-white py-12 border-t border-gray-800">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid md:grid-cols-3 gap-12 mb-12">
          <div>
            <div class="flex items-center gap-2 mb-4">
            <span class="inline-flex items-center justify-center w-8 h-8 bg-gradient-to-br from-orange-700 to-orange-800 rounded-lg text-white font-black text-xs">D</span>
              <span class="text-sm font-bold">Datarum</span>
            </div>
            <p class="text-gray-400 text-sm">
              Converta XMLs em planilhas com velocidade e segurança. 100% local.
            </p>
          </div>
          <div>
            <h4 class="font-bold text-sm mb-4 text-orange-700">Produto</h4>
            <ul class="space-y-2 text-sm">
              <li><button @click="$router.push('/conversor')" class="text-gray-400 hover:text-white focus:outline-none focus:ring-1 focus:ring-orange-500 rounded px-1 transition-colors duration-200">Abrir Aplicativo</button></li>
              <li><a href="#demo" @click="scrollTo('demo')" class="text-gray-400 hover:text-white focus:outline-none focus:ring-1 focus:ring-orange-500 rounded px-1 transition-colors duration-200">Ver Demo</a></li>
              <li><a href="#roadmap" @click="scrollTo('roadmap')" class="text-gray-400 hover:text-white focus:outline-none focus:ring-1 focus:ring-orange-500 rounded px-1 transition-colors duration-200">Roadmap</a></li>
            </ul>
          </div>
          <div>
            <h4 class="font-bold text-sm mb-4 text-orange-700">Sobre</h4>
            <ul class="space-y-2 text-sm">
              <li><a href="#" class="text-gray-400 hover:text-white focus:outline-none focus:ring-1 focus:ring-orange-500 rounded px-1 transition-colors duration-200">GitHub</a></li>
              <li><a href="#" class="text-gray-400 hover:text-white focus:outline-none focus:ring-1 focus:ring-orange-500 rounded px-1 transition-colors duration-200">Contato</a></li>
              <li><a href="#" class="text-gray-400 hover:text-white focus:outline-none focus:ring-1 focus:ring-orange-500 rounded px-1 transition-colors duration-200">Documentação</a></li>
            </ul>
          </div>
        </div>
        <div class="border-t border-gray-800 pt-8 flex flex-col sm:flex-row items-center justify-between">
          <p class="text-gray-500 text-sm">© 2025 Datarum. Feito com ❤️ por Higor Camelo.</p>
          <button @click="$router.push('/conversor')" class="mt-4 sm:mt-0 inline-flex items-center gap-2 bg-gradient-to-r from-orange-700 to-orange-800 hover:from-orange-800 hover:to-orange-900 focus:outline-none focus:ring-2 focus:ring-orange-500 text-white px-6 py-2.5 rounded-lg transition-all duration-200 font-semibold text-sm">
            Começar Agora →
          </button>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import RoadmapCard from '../components/RoadmapCard.vue';

const router = useRouter();

const scrollTo = (id) => {
  const element = document.getElementById(id);
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' });
  }
};
</script>

<style scoped>
/* Estilos mínimos para landing simples */
</style> 
