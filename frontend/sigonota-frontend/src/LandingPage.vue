<template>
  <div class="min-h-screen bg-white pb-20 lg:pb-0">
    <!-- Header Essencial -->
    <header class="bg-white/95 backdrop-blur fixed w-full top-0 z-50 border-b border-gray-100">
      <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center py-3">
          <div class="flex items-center gap-2">
            <span class="inline-flex items-center justify-center w-8 h-8 bg-purple-600 rounded-full text-white text-lg font-bold">D</span>
            <span class="text-lg font-bold text-purple-700">Datarum</span>
          </div>
          <button @click="goToApp" class="bg-purple-600 text-white px-4 py-2 rounded-lg hover:bg-purple-700 transition text-sm font-semibold disabled:opacity-75 disabled:cursor-not-allowed flex items-center gap-2" :disabled="isLoadingApp">
            <svg v-if="isLoadingApp" class="w-4 h-4 animate-spin" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            {{ isLoadingApp ? 'Carregando...' : 'Usar Agora' }}
          </button>
        </div>
      </nav>
    </header>

    <!-- Hero Section - Responsivo -->
    <section class="pt-16 pb-8 bg-gradient-to-br from-purple-50 via-white to-purple-100 min-h-screen flex items-center">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
        <div class="grid lg:grid-cols-5 gap-6 lg:gap-8 items-start">
          
          <!-- ESQUERDA: Título + Features + CTA -->
          <div class="col-span-full lg:col-span-2 text-center lg:text-left">
            <h1 class="text-3xl sm:text-4xl lg:text-5xl font-bold text-purple-800 leading-tight mb-4 lg:mb-6">
              Transforme XMLs de NFe em Excel
            </h1>
            <p class="text-lg lg:text-xl text-gray-600 mb-6 lg:mb-8">
              Converta seus arquivos XML fiscais em planilhas organizadas automaticamente
            </p>

            <!-- Features Compactas -->
            <div class="grid sm:grid-cols-2 lg:grid-cols-1 gap-3 lg:gap-4 mb-6 lg:mb-8 text-sm lg:text-lg">
              <div class="flex items-center gap-2 lg:gap-3 justify-center lg:justify-start">
                <div class="w-5 h-5 lg:w-6 lg:h-6 bg-green-500 rounded-full flex items-center justify-center flex-shrink-0">
                  <svg class="w-3 h-3 lg:w-4 lg:h-4 text-white" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
                  </svg>
                </div>
                <span class="text-gray-700"><strong>Versão gratuita</strong> • 750 XMLs/mês</span>
              </div>
              
              <div class="flex items-center gap-2 lg:gap-3 justify-center lg:justify-start">
                <div class="w-5 h-5 lg:w-6 lg:h-6 bg-blue-500 rounded-full flex items-center justify-center flex-shrink-0">
                  <svg class="w-3 h-3 lg:w-4 lg:h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
                  </svg>
                </div>
                <span class="text-gray-700"><strong>Rápido</strong> • Centenas em segundos</span>
              </div>
              
              <div class="flex items-center gap-2 lg:gap-3 justify-center lg:justify-start">
                <div class="w-5 h-5 lg:w-6 lg:h-6 bg-purple-500 rounded-full flex items-center justify-center flex-shrink-0">
                  <svg class="w-3 h-3 lg:w-4 lg:h-4 text-white" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm6.293-6.707a1 1 0 10-1.414 1.414l3 3a1 1 0 001.414 0l3-3a1 1 0 00-1.414-1.414L12 12.586V3a1 1 0 10-2 0v9.586l-1.707-1.707z" clip-rule="evenodd"/>
                  </svg>
                </div>
                <span class="text-gray-700"><strong>Completo</strong> • Todos os dados</span>
              </div>
              
              <div class="flex items-center gap-2 lg:gap-3 justify-center lg:justify-start">
                <div class="w-5 h-5 lg:w-6 lg:h-6 bg-orange-500 rounded-full flex items-center justify-center flex-shrink-0">
                  <svg class="w-3 h-3 lg:w-4 lg:h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>
                  </svg>
                </div>
                <span class="text-gray-700"><strong>Prático</strong> • Direto no navegador</span>
              </div>
            </div>

            <!-- CTA Principal -->
            <div>
              <button @click="goToApp" class="bg-purple-600 text-white px-6 lg:px-8 py-3 lg:py-4 rounded-xl hover:bg-purple-700 transition font-bold text-base lg:text-lg shadow-lg w-full sm:w-auto disabled:opacity-75 disabled:cursor-not-allowed flex items-center justify-center gap-2" :disabled="isLoadingApp">
                <svg v-if="isLoadingApp" class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24">
                  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                  <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                {{ isLoadingApp ? 'Carregando...' : 'Começar Agora' }}
              </button>
              <p class="text-xs lg:text-sm text-gray-500 mt-2 lg:mt-3">750 XMLs grátis/mês • Processamento instantâneo</p>
            </div>
          </div>

          <!-- DIREITA: Demonstração XML → Excel -->
          <div class="col-span-full lg:col-span-3 mt-8 lg:mt-0">
            <div class="bg-white rounded-xl lg:rounded-2xl shadow-xl p-4 lg:p-8 border border-gray-200">
              <div class="text-center mb-4 lg:mb-6">
                <h3 class="text-lg lg:text-2xl font-bold text-gray-900 mb-2 lg:mb-3">Veja como funciona</h3>
                <p class="text-sm lg:text-base text-gray-600">Arquivo XML se torna planilha Excel organizada</p>
              </div>

              <!-- Demonstração Mobile/Desktop -->
              <div class="block lg:hidden">
                <!-- Layout Mobile: Vertical -->
                <div class="space-y-4">
                  <!-- XML Mobile -->
                  <div>
                    <div class="text-center mb-3">
                      <span class="text-xs font-bold text-orange-600 bg-orange-100 px-3 py-1 rounded">ARQUIVO XML</span>
                    </div>
                    <div class="bg-gray-50 rounded-lg border border-gray-300 p-3">
                      <div class="font-mono text-xs leading-relaxed">
                        <div class="text-blue-600">&lt;?xml version="1.0"?&gt;</div>
                        <div class="text-purple-600">&lt;nfeProc&gt;</div>
                        <div class="ml-2 text-green-600">&lt;emit&gt;</div>
                        <div class="ml-4 text-gray-700">&lt;CNPJ&gt;<span class="bg-yellow-200">12345678000199</span>&lt;/CNPJ&gt;</div>
                        <div class="ml-4 text-gray-700">&lt;xNome&gt;<span class="bg-yellow-200">ABC LTDA</span>&lt;/xNome&gt;</div>
                        <div class="ml-2 text-green-600">&lt;/emit&gt;</div>
                        <div class="text-center text-gray-400 py-1 text-xs">...mais 2.000 linhas...</div>
                      </div>
                    </div>
                    <div class="text-center mt-2 bg-red-50 border border-red-200 rounded p-2">
                      <p class="text-red-700 text-xs"><strong>😓 Difícil de ler</strong></p>
                    </div>
                  </div>

                  <!-- Seta Mobile -->
                  <div class="text-center py-2">
                    <svg class="w-8 h-8 text-purple-600 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M19 14l-7 7m0 0l-7-7m7 7V3"/>
                    </svg>
                  </div>

                  <!-- Excel Mobile -->
                  <div>
                    <div class="text-center mb-3">
                      <span class="text-xs font-bold text-green-600 bg-green-100 px-3 py-1 rounded">PLANILHA EXCEL</span>
                    </div>
                    <div class="bg-white rounded-lg border-2 border-green-300 overflow-hidden">
                      <div class="bg-green-100 px-3 py-2">
                        <div class="flex items-center gap-2 justify-center">
                          <svg class="w-3 h-3 text-green-700" fill="currentColor" viewBox="0 0 20 20">
                            <path fill-rule="evenodd" d="M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm6.293-6.707a1 1 0 10-1.414 1.414l3 3a1 1 0 001.414 0l3-3a1 1 0 00-1.414-1.414L12 12.586V3a1 1 0 10-2 0v9.586l-1.707-1.707z" clip-rule="evenodd"/>
                          </svg>
                          <span class="font-mono text-xs text-green-800">notas_fiscais.xlsx</span>
                        </div>
                      </div>
                      <div class="bg-green-200 px-3 py-2 text-xs font-bold text-green-900">
                        <div class="grid grid-cols-3 gap-2">
                          <div>Fornecedor</div>
                          <div>CNPJ</div>
                          <div>Valor</div>
                        </div>
                      </div>
                      <div class="text-xs">
                        <div class="grid grid-cols-3 gap-2 px-3 py-2 border-b border-green-100 bg-yellow-50">
                          <div class="font-medium">ABC LTDA</div>
                          <div>12.345.678/0001-99</div>
                          <div class="font-bold text-green-700">R$ 1.250,00</div>
                        </div>
                        <div class="grid grid-cols-3 gap-2 px-3 py-2">
                          <div class="font-medium">XYZ Corp</div>
                          <div>98.765.432/0001-11</div>
                          <div class="font-bold text-green-700">R$ 2.890,50</div>
                        </div>
                      </div>
                      <div class="bg-green-50 px-3 py-2 border-t border-green-200">
                        <div class="text-center text-green-800 text-xs">
                          <div class="font-bold">+ Produtos, CFOP, ICMS</div>
                        </div>
                      </div>
                    </div>
                    <div class="text-center mt-2 bg-green-50 border border-green-200 rounded p-2">
                      <p class="text-green-700 text-xs"><strong>😎 Organizado e pronto</strong></p>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Layout Desktop: Horizontal -->
              <div class="hidden lg:block">
                <div class="grid grid-cols-11 gap-3 items-center">
                  
                  <!-- XML (4 colunas) -->
                  <div class="col-span-4">
                    <div class="text-center mb-4">
                      <span class="text-sm font-bold text-orange-600 bg-orange-100 px-3 py-2 rounded">ARQUIVO XML</span>
                    </div>
                    
                    <div class="bg-gray-50 rounded-lg border border-gray-300 p-4">
                      <div class="font-mono text-sm leading-relaxed">
                        <div class="text-blue-600">&lt;?xml version="1.0"?&gt;</div>
                        <div class="text-purple-600">&lt;nfeProc&gt;</div>
                        <div class="ml-3 text-green-600">&lt;emit&gt;</div>
                        <div class="ml-6 text-gray-700">&lt;CNPJ&gt;<span class="bg-yellow-200 px-1">12345678000199</span>&lt;/CNPJ&gt;</div>
                        <div class="ml-6 text-gray-700">&lt;xNome&gt;<span class="bg-yellow-200 px-1">ABC LTDA</span>&lt;/xNome&gt;</div>
                        <div class="ml-3 text-green-600">&lt;/emit&gt;</div>
                        <div class="ml-3 text-green-600">&lt;ide&gt;</div>
                        <div class="ml-6 text-gray-700">&lt;nNF&gt;<span class="bg-yellow-200 px-1">123456</span>&lt;/nNF&gt;</div>
                        <div class="ml-6 text-gray-700">&lt;dEmi&gt;<span class="bg-yellow-200 px-1">2024-07-23</span>&lt;/dEmi&gt;</div>
                        <div class="ml-6 text-gray-700">&lt;vNF&gt;<span class="bg-yellow-200 px-1">1250.00</span>&lt;/vNF&gt;</div>
                        <div class="ml-3 text-green-600">&lt;/ide&gt;</div>
                        <div class="text-center text-gray-400 py-2 text-sm">...mais 2.000 linhas...</div>
                        <div class="text-purple-600">&lt;/nfeProc&gt;</div>
                      </div>
                    </div>
                    
                    <div class="text-center mt-3 bg-red-50 border border-red-200 rounded p-3">
                      <p class="text-red-700 text-sm"><strong>😓 Difícil de ler</strong></p>
                    </div>
                  </div>

                  <!-- SETA (1 coluna) -->
                  <div class="col-span-1 text-center">
                    <svg class="w-6 h-6 text-purple-600 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M13 7l5 5m0 0l-5 5m5-5H6"/>
                    </svg>
                  </div>

                  <!-- EXCEL (6 colunas) -->
                  <div class="col-span-6">
                    <div class="text-center mb-4">
                      <span class="text-sm font-bold text-green-600 bg-green-100 px-3 py-2 rounded">PLANILHA EXCEL</span>
                    </div>
                    
                    <div class="bg-white rounded-lg border-2 border-green-300 overflow-hidden">
                      <div class="bg-green-100 px-4 py-3">
                        <div class="flex items-center gap-2 justify-center">
                          <svg class="w-4 h-4 text-green-700" fill="currentColor" viewBox="0 0 20 20">
                            <path fill-rule="evenodd" d="M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm6.293-6.707a1 1 0 10-1.414 1.414l3 3a1 1 0 001.414 0l3-3a1 1 0 00-1.414-1.414L12 12.586V3a1 1 0 10-2 0v9.586l-1.707-1.707z" clip-rule="evenodd"/>
                          </svg>
                          <span class="font-mono text-sm text-green-800">notas_fiscais.xlsx</span>
                        </div>
                      </div>
                      
                      <div>
                        <div class="bg-green-200 px-4 py-3 text-sm font-bold text-green-900">
                          <div class="grid grid-cols-3 gap-4">
                            <div>Fornecedor</div>
                            <div>CNPJ</div>
                            <div>Valor</div>
                          </div>
                        </div>
                        
                        <div class="text-sm">
                          <div class="grid grid-cols-3 gap-4 px-4 py-3 border-b border-green-100 bg-yellow-50">
                            <div class="font-medium">ABC LTDA</div>
                            <div>12.345.678/0001-99</div>
                            <div class="font-bold text-green-700">R$ 1.250,00</div>
                          </div>
                          <div class="grid grid-cols-3 gap-4 px-4 py-3 border-b border-green-100">
                            <div class="font-medium">XYZ Corp</div>
                            <div>98.765.432/0001-11</div>
                            <div class="font-bold text-green-700">R$ 2.890,50</div>
                          </div>
                        </div>
                        
                        <div class="bg-green-50 px-4 py-3 border-t border-green-200">
                          <div class="text-center text-green-800 text-sm">
                            <div class="font-bold">+ Produtos, CFOP, ICMS</div>
                          </div>
                        </div>
                      </div>
                    </div>
                    
                    <div class="text-center mt-3 bg-green-50 border border-green-200 rounded p-3">
                      <p class="text-green-700 text-sm"><strong>😎 Organizado e pronto</strong></p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Benefícios Principais -->
    <section class="py-12 lg:py-16 bg-white">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-8 lg:mb-12">
          <h2 class="text-2xl lg:text-3xl font-bold text-gray-900 mb-3 lg:mb-4">
            Por que usar o Datarum?
          </h2>
          <p class="text-lg lg:text-xl text-gray-600">
            Economize tempo e tenha dados organizados
          </p>
        </div>
        
        <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6 lg:gap-8">
          <div class="text-center p-4 lg:p-6 bg-purple-50 rounded-xl border border-purple-100">
            <div class="w-10 h-10 lg:w-12 lg:h-12 bg-purple-600 rounded-xl flex items-center justify-center mx-auto mb-3 lg:mb-4">
              <svg class="w-5 h-5 lg:w-6 lg:h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
              </svg>
            </div>
            <h3 class="text-base lg:text-lg font-bold mb-2 text-purple-800">Super Rápido</h3>
            <p class="text-gray-600 text-sm">Processa <strong>200+ XMLs</strong> em menos de <strong>10 segundos</strong></p>
          </div>

          <div class="text-center p-4 lg:p-6 bg-green-50 rounded-xl border border-green-100">
            <div class="w-10 h-10 lg:w-12 lg:h-12 bg-green-600 rounded-xl flex items-center justify-center mx-auto mb-3 lg:mb-4">
              <svg class="w-5 h-5 lg:w-6 lg:h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/>
              </svg>
            </div>
            <h3 class="text-base lg:text-lg font-bold mb-2 text-green-800">Simples e Prático</h3>
            <p class="text-gray-600 text-sm"><strong>Fácil de usar</strong> • <strong>Sem instalação</strong></p>
          </div>

          <div class="text-center p-4 lg:p-6 bg-blue-50 rounded-xl border border-blue-100">
            <div class="w-10 h-10 lg:w-12 lg:h-12 bg-blue-600 rounded-xl flex items-center justify-center mx-auto mb-3 lg:mb-4">
              <svg class="w-5 h-5 lg:w-6 lg:h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
              </svg>
            </div>
            <h3 class="text-base lg:text-lg font-bold mb-2 text-blue-800">Excel Customizável</h3>
            <p class="text-gray-600 text-sm"><strong>Escolha os campos</strong> • <strong>25+ opções</strong> disponíveis</p>
          </div>

          <div class="text-center p-4 lg:p-6 bg-orange-50 rounded-xl border border-orange-100">
            <div class="w-10 h-10 lg:w-12 lg:h-12 bg-orange-600 rounded-xl flex items-center justify-center mx-auto mb-3 lg:mb-4">
              <svg class="w-5 h-5 lg:w-6 lg:h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1"/>
              </svg>
            </div>
            <h3 class="text-base lg:text-lg font-bold mb-2 text-orange-800">Versão Gratuita</h3>
            <p class="text-gray-600 text-sm"><strong>750 XMLs/mês</strong> • <strong>Relatórios básicos</strong></p>
          </div>
        </div>
      </div>
    </section>

    <!-- Roadmap Mais Sutil -->
    <section class="py-16 bg-gray-50">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="text-3xl font-bold text-gray-900 mb-4">
            Evolução do Datarum
          </h2>
          <p class="text-gray-600">
            Estamos apenas começando! Muito mais está por vir
          </p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          <!-- v1.0 -->
          <div class="bg-white p-6 rounded-xl shadow-lg border border-gray-200 relative">
            <div class="absolute -top-2 -right-2 bg-gray-500 text-white px-3 py-1 rounded-full text-xs font-bold">
              v1.0 ANTERIOR
            </div>
            <div class="w-10 h-10 bg-gray-100 rounded-lg flex items-center justify-center mb-4">
              <svg class="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-900 mb-2">Beta Inicial</h3>
            <p class="text-gray-600 text-sm mb-3">Conversor XML → Excel básico para validação do conceito.</p>
            <div class="text-xs text-gray-500">Versão de teste</div>
          </div>

          <!-- v1.1 -->
          <div class="bg-white p-6 rounded-xl shadow-lg border-2 border-blue-200 relative">
            <div class="absolute -top-2 -right-2 bg-blue-500 text-white px-3 py-1 rounded-full text-xs font-bold">
              v1.1 ATUAL
            </div>
            <div class="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center mb-4">
              <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17v4a2 2 0 002 2h4M13 13h3a2 2 0 012 2v1M13 13l-2-2H9a2 2 0 000 4v1a2 2 0 001 1z"/>
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-900 mb-2">Design Aprimorado</h3>
            <p class="text-gray-600 text-sm mb-3">Nova interface, extração melhorada, experiência otimizada.</p>
            <div class="text-xs text-blue-600 font-semibold">Acesso gratuito</div>
          </div>

          <!-- v1.2 -->
          <div class="bg-white p-6 rounded-xl shadow-lg border border-gray-200 relative">
            <div class="absolute -top-2 -right-2 bg-purple-500 text-white px-3 py-1 rounded-full text-xs font-bold">
              v1.2 PRÓXIMA
            </div>
            <div class="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center mb-4">
              <svg class="w-5 h-5 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-900 mb-2">Relatórios Automáticos</h3>
            <p class="text-gray-600 text-sm mb-3">Formulários fiscais preenchidos automaticamente. Análises por CFOP, fornecedor, período.</p>
            <div class="text-xs text-purple-600">Gratuito: limitado • Pro: sem limites</div>
          </div>

          <!-- v1.3+ -->
          <div class="bg-white p-6 rounded-xl shadow-lg border border-gray-200 relative">
            <div class="absolute -top-2 -right-2 bg-gradient-to-r from-orange-500 to-red-500 text-white px-3 py-1 rounded-full text-xs font-bold">
              v1.3+ FUTURO
            </div>
            <div class="w-10 h-10 bg-gradient-to-br from-orange-100 to-red-100 rounded-lg flex items-center justify-center mb-4">
              <svg class="w-5 h-5 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/>
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-900 mb-2">IA & Integrações</h3>
            <p class="text-gray-600 text-sm mb-3">Insights automáticos com IA, integrações avançadas, recursos colaborativos...</p>
            <div class="text-xs text-orange-600 font-semibold">Exclusivo versão Pro</div>
          </div>
        </div>

        <!-- Features Futuras -->
        <div class="mt-12 bg-gradient-to-r from-purple-600 to-purple-700 rounded-2xl p-8 text-white">
          <div class="text-center mb-8">
            <h3 class="text-2xl font-bold mb-4">Recursos em desenvolvimento</h3>
            <p class="text-purple-100">Funcionalidades básicas para todos • Recursos avançados exclusivos Pro</p>
          </div>
          
          <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div class="bg-white/10 rounded-lg p-4 backdrop-blur">
              <h4 class="font-semibold mb-2">📋 Formulários Automáticos</h4>
              <p class="text-sm text-purple-100">Relatórios fiscais preenchidos automaticamente</p>
            </div>
            <div class="bg-white/10 rounded-lg p-4 backdrop-blur">
              <h4 class="font-semibold mb-2">📈 Totais por CFOP</h4>
              <p class="text-sm text-purple-100">Análise automática por código fiscal</p>
            </div>
            <div class="bg-white/10 rounded-lg p-4 backdrop-blur">
              <h4 class="font-semibold mb-2">🏢 Análise por Fornecedor</h4>
              <p class="text-sm text-purple-100">Rankings e comparativos automáticos</p>
            </div>
            <div class="bg-white/10 rounded-lg p-4 backdrop-blur">
              <h4 class="font-semibold mb-2">🤖 Insights com IA <span class="text-xs bg-orange-500 px-2 py-1 rounded">PRO</span></h4>
              <p class="text-sm text-purple-100">IA identifica padrões e anomalias nos dados</p>
            </div>
            <div class="bg-white/10 rounded-lg p-4 backdrop-blur">
              <h4 class="font-semibold mb-2">🔗 Integrações Avançadas <span class="text-xs bg-orange-500 px-2 py-1 rounded">PRO</span></h4>
              <p class="text-sm text-purple-100">Conecte com sistemas contábeis e ERPs</p>
            </div>
            <div class="bg-white/10 rounded-lg p-4 backdrop-blur">
              <h4 class="font-semibold mb-2">👥 Recursos Colaborativos <span class="text-xs bg-orange-500 px-2 py-1 rounded">PRO</span></h4>
              <p class="text-sm text-purple-100">Compartilhamento e trabalho em equipe</p>
            </div>
          </div>
        </div>

        <div class="mt-8 text-center">
          <p class="text-sm text-gray-600 mb-4">
            Conversão sempre com mesma qualidade • Diferença apenas nos limites de uso (750 XMLs grátis/mês)
          </p>
          <button @click="goToApp" class="bg-purple-600 text-white px-6 py-3 rounded-lg hover:bg-purple-700 transition font-semibold disabled:opacity-75 disabled:cursor-not-allowed flex items-center justify-center gap-2" :disabled="isLoadingApp">
            <svg v-if="isLoadingApp" class="w-4 h-4 animate-spin" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            {{ isLoadingApp ? 'Carregando...' : 'Começar Agora' }}
          </button>
        </div>
      </div>
    </section>

    <!-- Feedback Compacto -->
    <section class="py-12 lg:py-16 bg-gradient-to-r from-purple-600 to-purple-700">
      <div class="max-w-4xl mx-auto text-center px-4 sm:px-6 lg:px-8">
        <h2 class="text-xl lg:text-2xl font-bold text-white mb-3 lg:mb-4">
          Sua opinião molda o futuro do Datarum!
        </h2>
        <p class="text-purple-100 mb-4 lg:mb-6 text-sm lg:text-base">
          Conte-nos o que você precisa e vamos construir juntos
        </p>
        <button @click="openGoogleForms()" class="border-2 border-white text-white px-4 lg:px-6 py-2 lg:py-3 rounded-lg hover:bg-white hover:text-purple-600 transition font-semibold text-sm lg:text-base disabled:opacity-75 disabled:cursor-not-allowed flex items-center justify-center gap-2 mx-auto" :disabled="isLoadingFeedback">
          <svg v-if="isLoadingFeedback" class="w-4 h-4 animate-spin" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          {{ isLoadingFeedback ? 'Abrindo...' : 'Enviar Feedback' }}
        </button>
      </div>
    </section>

    <!-- Footer Simplificado -->
    <footer class="bg-gray-900 text-white py-6 lg:py-8">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <div class="flex items-center justify-center gap-2 lg:gap-3 mb-3 lg:mb-4">
          <span class="inline-flex items-center justify-center w-8 h-8 lg:w-10 lg:h-10 bg-purple-600 rounded-full text-white text-lg lg:text-xl font-bold">D</span>
          <span class="text-lg lg:text-xl font-bold">Datarum</span>
        </div>
        <p class="text-gray-400 text-sm">
          © {{ new Date().getFullYear() }} Datarum • v1.1 • XML → Excel automatizado
        </p>
      </div>
    </footer>

    <!-- Sticky CTA Mobile -->
    <div class="lg:hidden fixed bottom-0 left-0 right-0 bg-white border-t border-gray-200 p-4 z-40 shadow-lg">
      <button @click="goToApp" class="w-full bg-purple-600 text-white py-3 rounded-xl hover:bg-purple-700 transition font-bold text-lg shadow-lg disabled:opacity-75 disabled:cursor-not-allowed flex items-center justify-center gap-2" :disabled="isLoadingApp">
        <svg v-if="isLoadingApp" class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24">
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
          <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
        </svg>
        {{ isLoadingApp ? 'Carregando...' : 'Começar Agora' }}
      </button>
      <p class="text-center text-xs text-gray-500 mt-2">750 XMLs grátis/mês</p>
    </div>

    <!-- Toast Responsivo -->
    <div v-if="showFeedbackToast" 
         class="fixed bottom-4 right-4 left-4 sm:left-auto sm:right-4 bg-purple-600 text-white px-4 lg:px-6 py-2 lg:py-3 rounded-lg shadow-lg z-50 flex items-center gap-2 max-w-sm sm:max-w-none mx-auto sm:mx-0">
      <svg class="w-4 h-4 lg:w-5 lg:h-5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
      </svg>
      <span class="text-sm lg:text-base">Abrindo formulário de feedback...</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LandingPage',
  data() {
    return {
      showFeedbackToast: false,
      isLoadingApp: false,
      isLoadingFeedback: false
    };
  },
  methods: {
    goToApp() {
      this.isLoadingApp = true;
      // Simula um pequeno delay para mostrar o loading
      setTimeout(() => {
        this.$emit('goToApp');
        this.isLoadingApp = false;
      }, 500);
    },
    openGoogleForms() {
      const formsUrl = 'https://forms.gle/w4NigAgBfVFv3saG8';
      this.isLoadingFeedback = true;
      this.showFeedbackToast = true;
      
      setTimeout(() => {
        this.showFeedbackToast = false;
        this.isLoadingFeedback = false;
      }, 2000);
      
      window.open(formsUrl, '_blank');
    }
  }
};
</script>
