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
            <button @click="scrollTo('features')" class="hidden md:block text-gray-600 hover:text-purple-600 transition">Recursos</button>
            <button @click="scrollTo('how-it-works')" class="hidden md:block text-gray-600 hover:text-purple-600 transition">Como Funciona</button>
            <button @click="goToApp" class="bg-purple-600 text-white px-6 py-2 rounded-lg hover:bg-purple-700 transition font-medium">
              Começar Agora
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
            <h1 class="text-4xl sm:text-5xl lg:text-6xl font-bold text-gray-900 leading-tight mb-6">
              Converta XMLs de NFe em 
              <span class="text-purple-600 bg-gradient-to-r from-purple-600 to-purple-700 bg-clip-text text-transparent">
                planilhas Excel
              </span>
              automaticamente
            </h1>
            <p class="text-xl text-gray-600 mb-8 leading-relaxed">
              Transforme centenas de XMLs de Nota Fiscal Eletrônica em planilhas organizadas e profissionais em segundos. 
              Suporte completo para todas as versões NFe (1.10 a 4.00).
            </p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start">
              <button @click="goToApp" class="bg-purple-600 text-white px-8 py-4 rounded-lg hover:bg-purple-700 transition font-semibold text-lg shadow-lg">
                Começar Agora - Grátis
              </button>
              <button @click="scrollTo('demo')" class="border-2 border-purple-600 text-purple-600 px-8 py-4 rounded-lg hover:bg-purple-50 transition font-semibold text-lg">
                Ver Demonstração
              </button>
            </div>
            <div class="flex items-center gap-6 mt-8 justify-center lg:justify-start text-sm text-gray-500">
              <div class="flex items-center gap-2">
                <svg class="w-5 h-5 text-green-500" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
                </svg>
                <span>100% Gratuito</span>
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
            </div>
            <div class="mt-6 p-4 bg-gradient-to-r from-blue-50 to-purple-50 rounded-lg border border-blue-200">
              <div class="flex items-center gap-2 text-blue-700 mb-2">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
                <span class="font-semibold text-sm">Versão 1.0 - Lançamento Beta</span>
              </div>
              <p class="text-blue-600 text-sm">
                Esta versão está disponível gratuitamente por tempo limitado durante nosso período de testes. 
                <span class="font-medium">Ajude-nos com seu feedback para melhorar!</span>
              </p>
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
      </div>
    </section>

    <!-- Features Section -->
    <section id="features" class="py-20 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl sm:text-4xl font-bold text-gray-900 mb-4">
            Por que escolher o Datarum?
          </h2>
          <p class="text-xl text-gray-600 max-w-3xl mx-auto">
            A solução mais simples e eficiente para converter XMLs de NFe em planilhas organizadas
          </p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div class="text-center p-6">
            <div class="w-16 h-16 bg-purple-100 rounded-2xl flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-2">Super Rápido</h3>
            <p class="text-gray-600">Processe até 50 XMLs simultaneamente em segundos. Não perca mais tempo com conversões manuais.</p>
          </div>

          <div class="text-center p-6">
            <div class="w-16 h-16 bg-purple-100 rounded-2xl flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-2">Todas as Versões NFe</h3>
            <p class="text-gray-600">Suporte completo para NFe versões 1.10, 2.00, 3.10 e 4.00. Funciona com qualquer XML válido.</p>
          </div>

          <div class="text-center p-6">
            <div class="w-16 h-16 bg-purple-100 rounded-2xl flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-2">100% Seguro</h3>
            <p class="text-gray-600">Processamento local no seu navegador. Seus dados nunca saem do seu computador.</p>
          </div>

          <div class="text-center p-6">
            <div class="w-16 h-16 bg-purple-100 rounded-2xl flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-2">Excel Profissional</h3>
            <p class="text-gray-600">Planilhas bem formatadas com todas as informações importantes organizadas e prontas para uso.</p>
          </div>

          <div class="text-center p-6">
            <div class="w-16 h-16 bg-purple-100 rounded-2xl flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-2">Totalmente Gratuito*</h3>
            <p class="text-gray-600">Durante o período beta! Sem custos, sem cadastros, sem limitações. Ajude-nos com feedback.</p>
          </div>

          <div class="text-center p-6">
            <div class="w-16 h-16 bg-purple-100 rounded-2xl flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M9 19l3 3m0 0l3-3m-3 3V10"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-2">Arrastar e Soltar</h3>
            <p class="text-gray-600">Interface super simples. Basta arrastar seus XMLs e pronto! Download automático da planilha.</p>
          </div>
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
              Suporte para até 50 arquivos de uma vez.
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
    <section class="py-20 bg-gradient-to-br from-gray-50 to-gray-100">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <div class="inline-flex items-center gap-2 bg-blue-100 text-blue-700 px-4 py-2 rounded-full text-sm font-medium mb-4">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
            </svg>
            Em desenvolvimento
          </div>
          <h2 class="text-3xl sm:text-4xl font-bold text-gray-900 mb-4">
            Próximas versões
          </h2>
          <p class="text-xl text-gray-600 max-w-3xl mx-auto">
            Baseado no seu feedback, vamos evoluir o Datarum com funcionalidades que realmente importam
          </p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div class="bg-white p-6 rounded-2xl shadow-lg border border-gray-200 relative">
            <div class="absolute -top-2 -right-2 bg-green-500 text-white px-2 py-1 rounded-full text-xs font-bold">
              DISPONÍVEL
            </div>
            <div class="w-12 h-12 bg-green-100 rounded-xl flex items-center justify-center mb-4">
              <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-900 mb-2">v1.0 - Beta Público</h3>
            <p class="text-gray-600 text-sm">Conversor XML → Excel básico. Versão gratuita para testes e validação com usuários reais.</p>
          </div>

          <div class="bg-white p-6 rounded-2xl shadow-lg border border-gray-200 relative">
            <div class="absolute -top-2 -right-2 bg-blue-500 text-white px-2 py-1 rounded-full text-xs font-bold">
              v1.1
            </div>
            <div class="w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center mb-4">
              <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 100 4m0-4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 100 4m0-4v2m0-6V4"/>
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-900 mb-2">Primeira versão SaaS</h3>
            <p class="text-gray-600 text-sm">Escolher colunas específicas, linha de soma, melhor resumo. Freemium: 5 arquivos/mês grátis.</p>
          </div>

          <div class="bg-white p-6 rounded-2xl shadow-lg border border-gray-200 relative">
            <div class="absolute -top-2 -right-2 bg-purple-500 text-white px-2 py-1 rounded-full text-xs font-bold">
              v1.2
            </div>
            <div class="w-12 h-12 bg-purple-100 rounded-xl flex items-center justify-center mb-4">
              <svg class="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-900 mb-2">Relatórios Básicos</h3>
            <p class="text-gray-600 text-sm">Totais por CFOP, por fornecedor, períodos. Aba extra na planilha com resumo fiscal inteligente.</p>
          </div>

          <div class="bg-white p-6 rounded-2xl shadow-lg border border-gray-200 relative opacity-75">
            <div class="absolute -top-2 -right-2 bg-gray-400 text-white px-2 py-1 rounded-full text-xs font-bold">
              FUTURO
            </div>
            <div class="w-12 h-12 bg-gray-100 rounded-xl flex items-center justify-center mb-4">
              <svg class="w-6 h-6 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-700 mb-2">Insights Automáticos</h3>
            <p class="text-gray-500 text-sm">Análises de padrões de compra, detecção de ICMS ST, sugestões baseadas nos dados.</p>
          </div>

          <div class="bg-white p-6 rounded-2xl shadow-lg border border-gray-200 relative opacity-75">
            <div class="absolute -top-2 -right-2 bg-gray-400 text-white px-2 py-1 rounded-full text-xs font-bold">
              FUTURO
            </div>
            <div class="w-12 h-12 bg-gray-100 rounded-xl flex items-center justify-center mb-4">
              <svg class="w-6 h-6 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/>
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-700 mb-2">Recursos Colaborativos</h3>
            <p class="text-gray-500 text-sm">Upload por pasta, histórico de exportações, compartilhamento de relatórios.</p>
          </div>

          <div class="bg-white p-6 rounded-2xl shadow-lg border border-gray-200 relative opacity-75">
            <div class="absolute -top-2 -right-2 bg-gray-400 text-white px-2 py-1 rounded-full text-xs font-bold">
              FUTURO
            </div>
            <div class="w-12 h-12 bg-gray-100 rounded-xl flex items-center justify-center mb-4">
              <svg class="w-6 h-6 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v14a2 2 0 002 2z"/>
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-700 mb-2">Integrações</h3>
            <p class="text-gray-500 text-sm">Baseado na demanda: APIs, conectores com ERPs, sistemas contábeis.</p>
          </div>
        </div>

        <div class="mt-12 text-center">
          <div class="bg-gradient-to-r from-purple-600 to-blue-600 text-white p-6 rounded-2xl max-w-2xl mx-auto">
            <h3 class="text-xl font-bold mb-2">🧪 Ajude-nos a melhorar!</h3>
            <p class="mb-4">
              Use a v1.0 gratuitamente e nos diga o que funciona, o que não funciona e o que falta. 
              Seu feedback define as próximas versões.
            </p>
            <button @click="goToApp" class="bg-white text-purple-600 px-6 py-3 rounded-lg hover:bg-gray-50 transition font-semibold">
              Testar Agora - v1.0 Beta
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Feedback Section -->
    <section class="py-16 bg-gradient-to-r from-green-50 to-blue-50">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <div class="bg-white rounded-2xl shadow-xl p-8 border border-gray-200">
          <div class="flex items-center justify-center gap-3 mb-6">
            <div class="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center">
              <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z"/>
              </svg>
            </div>
            <h3 class="text-2xl font-bold text-gray-900">Seu feedback é fundamental!</h3>
          </div>
          <p class="text-gray-600 mb-6 max-w-2xl mx-auto">
            Esta versão está disponível <strong>gratuitamente por tempo limitado</strong> durante nosso período de testes. 
            Clique no botão abaixo para acessar nosso formulário de feedback e nos ajudar a melhorar o Datarum.
          </p>
          <div class="mb-6">
            <button @click="openGoogleForms()" 
                    class="bg-purple-600 text-white px-8 py-4 rounded-lg hover:bg-purple-700 transition font-semibold text-lg flex items-center justify-center gap-3 mx-auto shadow-lg">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z"/>
              </svg>
              Enviar Feedback
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
              </svg>
            </button>
          </div>
          <p class="text-sm text-gray-500">
            💡 <strong>Dica:</strong> O formulário possui seções diferentes para sugestões e problemas - você escolhe no primeiro campo
          </p>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="py-20 bg-gradient-to-br from-purple-600 to-purple-700">
      <div class="max-w-4xl mx-auto text-center px-4 sm:px-6 lg:px-8">
        <h2 class="text-3xl sm:text-4xl font-bold text-white mb-4">
          Pronto para simplificar seu trabalho?
        </h2>
        <p class="text-xl text-purple-100 mb-8">
          Comece agora e transforme seus XMLs em planilhas organizadas em segundos
        </p>
        <button @click="goToApp" class="bg-white text-purple-600 px-8 py-4 rounded-lg hover:bg-gray-50 transition font-semibold text-lg shadow-lg">
          Começar Agora - Beta Gratuito!
        </button>
        <p class="text-purple-200 text-sm mt-4">
          Versão beta • Sem cadastro • Sem custos • Acesso antecipado garantido
        </p>
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
            Automação fiscal com inteligência e clareza
          </p>
          <div class="flex justify-center gap-8 text-sm text-gray-400 mb-8">
            <button @click="scrollTo('features')" class="hover:text-white transition">Recursos</button>
            <button @click="scrollTo('how-it-works')" class="hover:text-white transition">Como Funciona</button>
            <button @click="goToApp" class="hover:text-white transition">Aplicativo Beta</button>
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
                <span>Versão 1.0 Beta</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </footer>

    <!-- Toast de Confirmação -->
    <div v-if="showFeedbackToast" 
         class="fixed bottom-4 right-4 bg-purple-600 text-white px-6 py-3 rounded-lg shadow-lg z-50 flex items-center gap-2">
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
      </svg>
      Redirecionando para o formulário...
    </div>
  </div>
</template>

<script>
export default {
  name: 'LandingPage',
  data() {
    return {
      showFeedbackToast: false
    };
  },
  methods: {
    scrollTo(elementId) {
      const element = document.getElementById(elementId);
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
      }
    },
    goToApp() {
      this.$emit('goToApp');
    },
    openGoogleForms() {
      // URL do seu Google Forms
      const formsUrl = 'https://forms.gle/w4NigAgBfVFv3saG8';
      
      // Mostrar feedback visual
      this.showFeedbackToast = true;
      
      // Auto-ocultar toast
      setTimeout(() => {
        this.showFeedbackToast = false;
      }, 2000);
      
      // Abrir o Google Forms em nova aba
      window.open(formsUrl, '_blank');
      
      // Log para desenvolvimento
      console.log('📝 Redirecionando para formulário de feedback');
    }
  }
};
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
</style>
