<template>
  <div v-if="currentView === 'landing'">
    <LandingPage @goToApp="currentView = 'app'" />
  </div>
  <div v-else class="min-h-screen flex flex-col bg-gradient-to-br from-purple-100 via-white to-purple-200">
    <!-- Header -->
    <header class="w-full bg-white/80 backdrop-blur shadow-md py-3 px-8 flex items-center justify-between fixed top-0 left-0 z-10 border-b border-purple-100">
      <div class="flex items-center gap-3">
        <button @click="currentView = 'landing'" class="flex items-center gap-3 hover:opacity-80 transition">
          <span class="inline-flex items-center justify-center w-11 h-11 bg-purple-600 rounded-full text-white text-2xl font-bold shadow">D</span>
          <div class="flex flex-col">
            <span class="text-2xl font-extrabold text-purple-700 tracking-tight">Datarum</span>
            <span class="text-xs text-purple-600 font-medium">XML → Excel automatizado</span>
          </div>
        </button>
      </div>
      <div class="flex items-center gap-4">
        <!-- Indicador de versão -->
        <div class="hidden md:flex items-center gap-2 bg-purple-50 px-3 py-1 rounded-full">
          <span class="text-xs font-medium text-purple-600">v1.0</span>
        </div>
        <button @click="currentView = 'landing'" class="text-purple-600 hover:text-purple-700 text-sm font-medium transition">
          ← Voltar ao início
        </button>
      </div>
    </header>

    <div class="h-20"></div>

    <!-- Conteúdo principal -->
    <main class="flex-1 flex justify-center px-4 py-8">
      <div class="w-full max-w-7xl flex flex-col lg:flex-row gap-6 lg:gap-8">
        
        <!-- Sidebar Esquerda -->
        <aside class="w-full lg:w-72 order-2 lg:order-1">
          <div class="flex lg:flex-col gap-4 lg:gap-6 overflow-x-auto lg:overflow-x-visible">
          <!-- Stats Card -->
          <div class="bg-white/90 rounded-2xl shadow-lg p-4 lg:p-6 border border-purple-100 flex-shrink-0 w-64 lg:w-full">
            <div class="flex items-center gap-3 mb-4">
              <div class="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center">
                <svg class="w-5 h-5 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
                </svg>
              </div>
              <h3 class="font-bold text-purple-700">Estatísticas</h3>
            </div>
            <div class="space-y-3">
              <div class="flex justify-between">
                <span class="text-sm text-gray-600">Sessão atual</span>
                <span class="font-semibold text-purple-600">{{ selectedFiles.length }} arquivos</span>
              </div>
              <div class="flex justify-between">
                <span class="text-sm text-gray-600">Suporte NFe</span>
                <span class="font-semibold text-purple-600">v1.10 - v4.00</span>
              </div>
              <div class="flex justify-between">
                <span class="text-sm text-gray-600">Formato saída</span>
                <span class="font-semibold text-purple-600">Excel (.xlsx)</span>
              </div>
            </div>
          </div>

          <!-- Dicas Card -->
          <div class="bg-gradient-to-br from-purple-50 to-purple-100 rounded-2xl shadow-lg p-4 lg:p-6 border border-purple-200 flex-shrink-0 w-64 lg:w-full">
            <div class="flex items-center gap-3 mb-4">
              <div class="w-10 h-10 bg-purple-200 rounded-lg flex items-center justify-center">
                <svg class="w-5 h-5 text-purple-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/>
                </svg>
              </div>
              <h3 class="font-bold text-purple-700">Dicas de Uso</h3>
            </div>
            <div class="space-y-3 text-sm text-purple-600">
              <div class="flex items-start gap-2">
                <span class="text-purple-400 mt-0.5">•</span>
                <span>Arraste múltiplos XMLs de uma vez</span>
              </div>
              <div class="flex items-start gap-2">
                <span class="text-purple-400 mt-0.5">•</span>
                <span>Máximo 200 arquivos por conversão</span>
              </div>
              <div class="flex items-start gap-2">
                <span class="text-purple-400 mt-0.5">•</span>
                <span>750 XMLs gratuitos por mês</span>
              </div>
              <div class="flex items-start gap-2">
                <span class="text-purple-400 mt-0.5">•</span>
                <span>Nome da planilha será o nome do arquivo</span>
              </div>
            </div>
          </div>

          <!-- Versões NFe -->
          <div class="bg-white/90 rounded-2xl shadow-lg p-6 border border-purple-100 flex-shrink-0 w-64 lg:w-full">
            <div class="flex items-center gap-3 mb-4">
              <div class="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center">
                <svg class="w-5 h-5 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
                </svg>
              </div>
              <h3 class="font-bold text-purple-700">Compatibilidade</h3>
            </div>
            <div class="grid grid-cols-2 gap-2">
              <div class="text-center p-2 bg-purple-50 rounded-lg">
                <div class="text-xs text-purple-600 font-semibold">NFe 1.10</div>
                <div class="text-xs text-green-600">✓ Suportado</div>
              </div>
              <div class="text-center p-2 bg-purple-50 rounded-lg">
                <div class="text-xs text-purple-600 font-semibold">NFe 2.00</div>
                <div class="text-xs text-green-600">✓ Suportado</div>
              </div>
              <div class="text-center p-2 bg-purple-50 rounded-lg">
                <div class="text-xs text-purple-600 font-semibold">NFe 3.10</div>
                <div class="text-xs text-green-600">✓ Suportado</div>
              </div>
              <div class="text-center p-2 bg-purple-50 rounded-lg">
                <div class="text-xs text-purple-600 font-semibold">NFe 4.00</div>
                <div class="text-xs text-green-600">✓ Suportado</div>
              </div>
            </div>
          </div>
          </div>
        </aside>

        <!-- Conteúdo Principal -->
        <div class="flex-1 max-w-2xl mx-auto order-1 lg:order-2">
          <div class="bg-white/90 rounded-3xl shadow-2xl p-10 border border-purple-100">
        <div class="flex flex-col items-center mb-8">
          <div class="bg-gradient-to-br from-purple-200 to-purple-400 rounded-full p-4 shadow-lg mb-4">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-purple-700" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" /></svg>
          </div>
          <h1 class="text-3xl font-extrabold text-purple-700 mb-1 text-center">Extrator de XMLs NFe</h1>
          <p class="text-gray-500 mb-2 text-center">Converta arquivos XML de NFe em planilhas Excel organizadas e inteligentes.</p>
        </div>

        <!-- Área de upload com drag & drop -->
        <section class="mb-8">
          <label class="block text-sm font-semibold text-purple-700 mb-2">
            Selecione arquivos XML (máx. 200 por conversão • 750/mês grátis)
          </label>
          <div 
            @dragover.prevent="dragOver = true"
            @dragleave.prevent="dragOver = false"
            @drop.prevent="handleDrop"
            :class="[
              'relative border-2 border-dashed rounded-lg p-8 transition-all duration-200 cursor-pointer',
              dragOver ? 'border-purple-400 bg-purple-50 scale-105' : 'border-purple-200 hover:border-purple-300'
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
              <svg class="mx-auto h-12 w-12 text-purple-400 mb-4" stroke="currentColor" fill="none" viewBox="0 0 48 48">
                <path d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <p class="text-lg font-medium text-purple-600 mb-1">
                <span class="underline">Clique para selecionar</span> ou arraste arquivos XML aqui
              </p>
              <p class="text-sm text-gray-500">Máximo 200 por vez, 5MB cada • 750 XMLs grátis/mês</p>
            </div>
          </div>
          
          <!-- Lista de arquivos selecionados -->
          <div v-if="selectedFiles.length" class="mt-4 space-y-2">
            <div class="flex items-center justify-between text-sm text-purple-700 font-medium">
              <span>{{ selectedFiles.length }} arquivo(s) selecionado(s)</span>
              <button @click="clearFiles" class="text-red-500 hover:text-red-700 transition-colors">
                Limpar tudo
              </button>
            </div>
            <ul class="space-y-2 max-h-32 overflow-y-auto">
              <li v-for="(file, index) in selectedFiles" :key="index" 
                  :class="[
                    'flex items-center justify-between p-2 rounded border text-sm',
                    getFileStatus(file).valid ? 'bg-emerald-50 border-emerald-200' : 'bg-red-50 border-red-200'
                  ]">
                <div class="flex items-center gap-2 flex-1 min-w-0">
                  <svg :class="[
                    'h-4 w-4 flex-shrink-0',
                    getFileStatus(file).valid ? 'text-emerald-500' : 'text-red-500'
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

        <!-- Customização da Extração -->
        <section v-if="selectedFiles.length" class="mb-8">
          <div class="bg-gradient-to-r from-purple-50 to-purple-100 rounded-xl p-6 border border-purple-200">
            <div class="flex items-center gap-3 mb-4">
              <div class="w-10 h-10 bg-purple-600 rounded-lg flex items-center justify-center">
                <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 100 4m0-4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 100 4m0-4v2m0-6V4"/>
                </svg>
              </div>
              <h3 class="text-lg font-bold text-purple-700">Customizar Extração</h3>
              <span class="text-xs bg-purple-600 text-white px-2 py-1 rounded-full font-semibold">NOVO v1.1</span>
            </div>

            <!-- Aviso sobre compatibilidade -->
            <div class="mb-6 bg-blue-50 border border-blue-200 rounded-lg p-4">
              <div class="flex items-start gap-3">
                <svg class="w-5 h-5 text-blue-600 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
                <div class="text-sm">
                  <p class="font-medium text-blue-800 mb-1">📋 Compatibilidade e Tratamento de Erros</p>
                  <ul class="text-blue-700 space-y-1 text-xs">
                    <li>• <strong>Aceitos:</strong> XMLs de NFe (versões 1.10 a 4.00)</li>
                    <li>• <strong>Campos ausentes:</strong> Serão deixados em branco na planilha</li>
                    <li>• <strong>XMLs inválidos:</strong> Relatório detalhado de erros será gerado</li>
                    <li>• <strong>Processamento flexível:</strong> Extração continua mesmo com alguns arquivos com erro</li>
                  </ul>
                </div>
              </div>
            </div>
            
            <!-- Presets Rápidos -->
            <div class="mb-6">
              <label class="block text-sm font-semibold text-purple-700 mb-3">Configurações Pré-definidas</label>
              <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
                <button @click="aplicarPreset('basico')" 
                        :class="['p-3 rounded-lg border transition-all text-sm font-medium', presetAtivo === 'basico' ? 'bg-purple-600 text-white border-purple-600' : 'bg-white border-purple-200 text-purple-700 hover:bg-purple-50']">
                  <div class="flex items-center gap-2">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
                    </svg>
                    <span>Básico</span>
                  </div>
                  <div class="text-xs mt-1 opacity-90">Dados essenciais</div>
                </button>
                
                <button @click="aplicarPreset('completo')" 
                        :class="['p-3 rounded-lg border transition-all text-sm font-medium', presetAtivo === 'completo' ? 'bg-purple-600 text-white border-purple-600' : 'bg-white border-purple-200 text-purple-700 hover:bg-purple-50']">
                  <div class="flex items-center gap-2">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/>
                    </svg>
                    <span>Completo</span>
                  </div>
                  <div class="text-xs mt-1 opacity-90">Todos os campos</div>
                </button>
                
                <button @click="aplicarPreset('fiscal')" 
                        :class="['p-3 rounded-lg border transition-all text-sm font-medium', presetAtivo === 'fiscal' ? 'bg-purple-600 text-white border-purple-600' : 'bg-white border-purple-200 text-purple-700 hover:bg-purple-50']">
                  <div class="flex items-center gap-2">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1"/>
                    </svg>
                    <span>Fiscal</span>
                  </div>
                  <div class="text-xs mt-1 opacity-90">Impostos + CFOP</div>
                </button>
              </div>
            </div>

            <!-- Campos Personalizados -->
            <div class="mb-6">
              <div class="flex items-center justify-between mb-3">
                <label class="text-sm font-semibold text-purple-700">Campos Personalizados</label>
                <button @click="mostrarCamposPersonalizados = !mostrarCamposPersonalizados" 
                        class="text-xs text-purple-600 hover:text-purple-700 font-medium underline">
                  {{ mostrarCamposPersonalizados ? 'Ocultar' : 'Personalizar' }}
                </button>
              </div>
              
              <div v-show="mostrarCamposPersonalizados" class="space-y-4">
                <!-- Dados da Nota -->
                <div class="bg-white rounded-lg p-4 border border-purple-100">
                  <h4 class="text-sm font-semibold text-purple-700 mb-3 flex items-center gap-2">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
                    </svg>
                    Dados da Nota
                  </h4>
                  <div class="grid grid-cols-2 sm:grid-cols-3 gap-2">
                    <label v-for="campo in camposDisponiveis.nota" :key="campo.id" class="flex items-center gap-2 text-sm">
                      <input type="checkbox" v-model="camposSelecionados" :value="campo.id" class="rounded border-purple-300 text-purple-600 focus:ring-purple-500">
                      <span class="text-gray-700">{{ campo.nome }}</span>
                    </label>
                  </div>
                </div>

                <!-- Dados do Emitente -->
                <div class="bg-white rounded-lg p-4 border border-purple-100">
                  <h4 class="text-sm font-semibold text-purple-700 mb-3 flex items-center gap-2">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/>
                    </svg>
                    Dados do Emitente
                  </h4>
                  <div class="grid grid-cols-2 sm:grid-cols-3 gap-2">
                    <label v-for="campo in camposDisponiveis.emitente" :key="campo.id" class="flex items-center gap-2 text-sm">
                      <input type="checkbox" v-model="camposSelecionados" :value="campo.id" class="rounded border-purple-300 text-purple-600 focus:ring-purple-500">
                      <span class="text-gray-700">{{ campo.nome }}</span>
                    </label>
                  </div>
                </div>

                <!-- Dados do Destinatário -->
                <div class="bg-white rounded-lg p-4 border border-purple-100">
                  <h4 class="text-sm font-semibold text-purple-700 mb-3 flex items-center gap-2">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
                    </svg>
                    Dados do Destinatário
                  </h4>
                  <div class="grid grid-cols-2 sm:grid-cols-3 gap-2">
                    <label v-for="campo in camposDisponiveis.destinatario" :key="campo.id" class="flex items-center gap-2 text-sm">
                      <input type="checkbox" v-model="camposSelecionados" :value="campo.id" class="rounded border-purple-300 text-purple-600 focus:ring-purple-500">
                      <span class="text-gray-700">{{ campo.nome }}</span>
                    </label>
                  </div>
                </div>

                <!-- Produtos -->
                <div class="bg-white rounded-lg p-4 border border-purple-100">
                  <h4 class="text-sm font-semibold text-purple-700 mb-3 flex items-center gap-2">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/>
                    </svg>
                    Produtos
                  </h4>
                  <div class="grid grid-cols-2 sm:grid-cols-3 gap-2">
                    <label v-for="campo in camposDisponiveis.produtos" :key="campo.id" class="flex items-center gap-2 text-sm">
                      <input type="checkbox" v-model="camposSelecionados" :value="campo.id" class="rounded border-purple-300 text-purple-600 focus:ring-purple-500">
                      <span class="text-gray-700">{{ campo.nome }}</span>
                    </label>
                  </div>
                </div>

                <!-- Impostos -->
                <div class="bg-white rounded-lg p-4 border border-purple-100">
                  <h4 class="text-sm font-semibold text-purple-700 mb-3 flex items-center gap-2">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1"/>
                    </svg>
                    Impostos
                  </h4>
                  <div class="grid grid-cols-2 sm:grid-cols-3 gap-2">
                    <label v-for="campo in camposDisponiveis.impostos" :key="campo.id" class="flex items-center gap-2 text-sm">
                      <input type="checkbox" v-model="camposSelecionados" :value="campo.id" class="rounded border-purple-300 text-purple-600 focus:ring-purple-500">
                      <span class="text-gray-700">{{ campo.nome }}</span>
                    </label>
                  </div>
                </div>
              </div>
            </div>

            <!-- Opções Adicionais -->
            <div class="mb-4">
              <label class="text-sm font-semibold text-purple-700 mb-3 block">Opções Adicionais</label>
              <div class="space-y-2">
                <label class="flex items-center gap-3 p-2 rounded bg-white border border-purple-100">
                  <input type="checkbox" v-model="opcoes.incluirTotais" class="rounded border-purple-300 text-purple-600 focus:ring-purple-500">
                  <div class="flex-1">
                    <span class="text-sm font-medium text-gray-700">Incluir linha de totais</span>
                    <p class="text-xs text-gray-500">Adiciona uma linha final com soma dos valores</p>
                  </div>
                </label>
                
                <label class="flex items-center gap-3 p-2 rounded bg-white border border-purple-100">
                  <input type="checkbox" v-model="opcoes.agruparPorEmitente" class="rounded border-purple-300 text-purple-600 focus:ring-purple-500">
                  <div class="flex-1">
                    <span class="text-sm font-medium text-gray-700">Agrupar por emitente</span>
                    <p class="text-xs text-gray-500">Organiza dados por fornecedor com subtotais</p>
                  </div>
                </label>
                
                <label class="flex items-center gap-3 p-2 rounded bg-white border border-purple-100">
                  <input type="checkbox" v-model="opcoes.incluirResumo" class="rounded border-purple-300 text-purple-600 focus:ring-purple-500">
                  <div class="flex-1">
                    <span class="text-sm font-medium text-gray-700">Aba de resumo</span>
                    <p class="text-xs text-gray-500">Cria aba adicional com estatísticas gerais</p>
                  </div>
                </label>
              </div>
            </div>

            <!-- Contador de Campos -->
            <div class="text-center p-2 bg-white rounded border border-purple-200">
              <span class="text-sm text-purple-600">
                <strong>{{ camposSelecionados.length }}</strong> campos selecionados
                <span v-if="opcoes.incluirTotais || opcoes.agruparPorEmitente || opcoes.incluirResumo"> + opções adicionais</span>
              </span>
            </div>
          </div>
        </section>

        <!-- Criar nova planilha -->
        <section class="mb-8">
          <label for="nomePlanilha" class="block text-sm font-semibold text-purple-700 mb-2">
            Nome da nova planilha
          </label>
          <div class="relative rounded-lg shadow-sm">
            <input 
              type="text" 
              id="nomePlanilha"
              v-model="nomePlanilha"
              placeholder="ex: Notas Recebidas"
              class="block w-full rounded-lg border border-purple-300 focus:border-purple-500 focus:ring-1 focus:ring-purple-500 text-sm p-3 pr-36 transition"
              aria-describedby="sugestaoPlanilha"
            />
            <button 
              v-if="!nomePlanilha"
              @click="usarSugestao"
              type="button"
              class="absolute right-2 top-1/2 -translate-y-1/2 bg-purple-50 text-purple-600 px-3 py-1 text-xs rounded-md hover:bg-purple-100 transition"
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
            class="w-full bg-purple-600 text-white py-3 px-4 rounded-lg hover:bg-purple-700 disabled:bg-gray-300 disabled:cursor-not-allowed transition-all font-bold shadow-md flex items-center justify-center gap-2 text-lg"
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
         :class="mensagem.includes('✅') ? 'bg-emerald-50 text-emerald-800' : 'bg-red-50 text-red-800'">
          {{ mensagem }}
        </section>

          </div>
        </div>

      </div>
    </main>

    <!-- Footer -->
    <footer class="w-full text-center text-purple-400 text-xs py-4 mt-8">
      &copy; {{ new Date().getFullYear() }} Datarum. Todos os direitos reservados.
    </footer>
  </div>
</template>

<script>
import LandingPage from './LandingPage.vue';

export default {
  components: {
    LandingPage
  },
  data() {
    return {
      currentView: 'landing', // 'landing' ou 'app'
      selectedFiles: [],
      mensagem: '',
      nomePlanilha: '',
      loading: false,
      progress: 0,
      dragOver: false,
      validationMessage: null,
      
      // Customização da extração
      mostrarCamposPersonalizados: false,
      presetAtivo: 'basico',
      camposSelecionados: [
        'numero_nf', 'data_emissao', 'emitente', 'cnpj_emitente', 
        'valor_total_nf', 'descricao_produto', 'valor_total_item'
      ],
      opcoes: {
        incluirTotais: true,
        agruparPorEmitente: false,
        incluirResumo: false
      },
      camposDisponiveis: {
        nota: [
          { id: 'numero_nf', nome: 'Número da NFe' },
          { id: 'data_emissao', nome: 'Data de Emissão' },
          { id: 'serie', nome: 'Série' },
          { id: 'natureza_operacao', nome: 'Natureza da Operação' },
          { id: 'valor_total_nf', nome: 'Valor Total da NFe' },
          { id: 'chave_nfe', nome: 'Chave de Acesso' },
          { id: 'versao_nfe', nome: 'Versão da NFe' },
          { id: 'modelo', nome: 'Modelo' },
          { id: 'tipo_operacao', nome: 'Tipo de Operação' }
        ],
        emitente: [
          { id: 'emitente', nome: 'Razão Social' },
          { id: 'cnpj_emitente', nome: 'CNPJ' },
          { id: 'municipio_emitente', nome: 'Cidade' },
          { id: 'uf_emitente', nome: 'UF' },
          { id: 'regime_tributario', nome: 'Regime Tributário' }
        ],
        destinatario: [
          { id: 'destinatario', nome: 'Nome/Razão Social' },
          { id: 'cnpj_destinatario', nome: 'CPF/CNPJ' },
          { id: 'municipio_dest', nome: 'Cidade' },
          { id: 'uf_dest', nome: 'UF' }
        ],
        produtos: [
          { id: 'descricao_produto', nome: 'Descrição do Produto' },
          { id: 'codigo_produto', nome: 'Código do Produto' },
          { id: 'ncm', nome: 'NCM' },
          { id: 'cfop', nome: 'CFOP' },
          { id: 'quantidade_comercial', nome: 'Quantidade' },
          { id: 'unidade_comercial', nome: 'Unidade' },
          { id: 'valor_unitario', nome: 'Valor Unitário' },
          { id: 'valor_total_item', nome: 'Valor Total do Item' }
        ],
        impostos: [
          { id: 'cst_icms', nome: 'CST ICMS' },
          { id: 'base_icms', nome: 'Base ICMS' },
          { id: 'aliquota_icms', nome: 'Alíquota ICMS' },
          { id: 'icms_valor', nome: 'Valor ICMS' },
          { id: 'aliquota_ipi', nome: 'Alíquota IPI' },
          { id: 'valor_ipi', nome: 'Valor IPI' },
          { id: 'aliquota_pis', nome: 'Alíquota PIS' },
          { id: 'pis_valor', nome: 'Valor PIS' },
          { id: 'aliquota_cofins', nome: 'Alíquota COFINS' },
          { id: 'cofins_valor', nome: 'Valor COFINS' }
        ]
      }
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
      
      // Limitar a 200 arquivos
      if (xmlFiles.length > 200) {
        this.showValidation('error', 'Máximo 200 arquivos permitidos. Alguns foram removidos.');
        this.selectedFiles = xmlFiles.slice(0, 200);
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
      const sugestao = `datarum_${agora.getFullYear()}-${pad(agora.getMonth()+1)}-${pad(agora.getDate())}_${pad(agora.getHours())}${pad(agora.getMinutes())}`;
      this.nomePlanilha = sugestao;
    },
    aplicarPreset(tipo) {
      this.presetAtivo = tipo;
      
      switch(tipo) {
        case 'basico':
          this.camposSelecionados = [
            'numero_nf', 'data_emissao', 'emitente', 'cnpj_emitente', 
            'valor_total_nf', 'descricao_produto', 'valor_total_item'
          ];
          this.opcoes = { 
            incluirTotais: true, 
            agruparPorEmitente: false, 
            incluirResumo: false
          };
          break;
          
        case 'completo':
          this.camposSelecionados = [
            // Dados da NFe
            'numero_nf', 'data_emissao', 'serie', 'natureza_operacao', 'valor_total_nf', 'chave_nfe', 'modelo',
            // Dados do emitente
            'emitente', 'cnpj_emitente', 'municipio_emitente', 'uf_emitente', 'regime_tributario',
            // Dados do destinatário
            'destinatario', 'cnpj_destinatario', 'municipio_dest', 'uf_dest',
            // Produtos completos
            'descricao_produto', 'codigo_produto', 'ncm', 'cfop', 'quantidade_comercial', 'unidade_comercial', 'valor_unitario', 'valor_total_item',
            // Impostos principais
            'icms_valor', 'pis_valor', 'cofins_valor'
          ];
          this.opcoes = { 
            incluirTotais: true, 
            agruparPorEmitente: true, 
            incluirResumo: true
          };
          break;
          
        case 'fiscal':
          this.camposSelecionados = [
            // Dados básicos da NFe
            'numero_nf', 'data_emissao', 'emitente', 'cnpj_emitente', 'valor_total_nf',
            // Dados fiscais dos produtos
            'descricao_produto', 'cfop', 'ncm', 'valor_total_item', 
            // Impostos detalhados
            'cst_icms', 'base_icms', 'aliquota_icms', 'icms_valor',
            'aliquota_ipi', 'valor_ipi',
            'aliquota_pis', 'pis_valor',
            'aliquota_cofins', 'cofins_valor'
          ];
          this.opcoes = { 
            incluirTotais: true, 
            agruparPorEmitente: true, 
            incluirResumo: false
          };
          break;
      }
    },
    isPresetMatch() {
      // Verifica se a seleção atual corresponde a algum preset
      const presets = {
        basico: [
          'numero_nf', 'data_emissao', 'emitente', 'cnpj_emitente', 
          'valor_total_nf', 'descricao_produto', 'valor_total_item'
        ],
        completo: [
          'numero_nf', 'data_emissao', 'serie', 'natureza_operacao', 'valor_total_nf', 'chave_nfe', 'modelo',
          'cnpj_emitente', 'emitente', 'municipio_emitente', 'uf_emitente', 'regime_tributario',
          'cnpj_destinatario', 'destinatario', 'municipio_dest', 'uf_dest',
          'codigo_produto', 'descricao_produto', 'ncm', 'cfop', 'quantidade_comercial', 'unidade_comercial', 'valor_unitario', 'valor_total_item',
          'cst_icms', 'base_icms', 'aliquota_icms', 'icms_valor',
          'aliquota_ipi', 'valor_ipi',
          'aliquota_pis', 'pis_valor',
          'aliquota_cofins', 'cofins_valor'
        ],
        fiscal: [
          'numero_nf', 'data_emissao', 'emitente', 'cnpj_emitente',
          'codigo_produto', 'descricao_produto', 'ncm', 'cfop', 'quantidade_comercial', 'valor_unitario', 'valor_total_item',
          'cst_icms', 'base_icms', 'aliquota_icms', 'icms_valor',
          'aliquota_ipi', 'valor_ipi',
          'aliquota_pis', 'pis_valor',
          'aliquota_cofins', 'cofins_valor'
        ]
      };
      
      const sorted = (arr) => [...arr].sort();
      const currentSorted = sorted(this.camposSelecionados);
      
      return Object.values(presets).some(preset => 
        JSON.stringify(sorted(preset)) === JSON.stringify(currentSorted)
      );
    },
    async enviarArquivos() {
      if (!this.selectedFiles.length || !this.nomePlanilha.trim()) return;

      this.loading = true;
      this.mensagem = '';
      this.validationMessage = null;

      const formData = new FormData();
      
      // ✅ Adicionar arquivos
      this.selectedFiles.forEach(file => formData.append('xmls', file));
      
      // ✅ Adicionar nome da planilha (OBRIGATÓRIO!)
      formData.append('planilha', this.nomePlanilha);
      
      // ✅ NOVO: Adicionar configurações de extração
      formData.append('campos_selecionados', JSON.stringify(this.camposSelecionados));
      formData.append('opcoes', JSON.stringify(this.opcoes));
      formData.append('preset', this.presetAtivo);

      // URL correta do backend
      const API_URL = 'http://127.0.0.1:8000';

      try {
        // Primeiro: obter informações
        const responseInfo = await fetch(`${API_URL}/processar-info`, {
          method: 'POST',
          body: formData
        });
        
        if (!responseInfo.ok) {
          const errorText = await responseInfo.text();
          throw new Error(`Erro ${responseInfo.status}: ${errorText}`);
        }
        
        const info = await responseInfo.json();
        
        // ✅ Mostrar resultados com informações sobre customização
        let camposInfo = this.camposSelecionados.length === 7 ? 'campos básicos' : 
                        this.camposSelecionados.length > 15 ? 'extração completa' : 
                        `${this.camposSelecionados.length} campos personalizados`;
        
        let opcoesInfo = [];
        if (this.opcoes.incluirTotais) opcoesInfo.push('totais');
        if (this.opcoes.agruparPorEmitente) opcoesInfo.push('agrupamento');
        if (this.opcoes.incluirResumo) opcoesInfo.push('resumo');
        
        this.mensagem = `✅ Processamento concluído!\n` +
          `📁 Arquivos: ${info.arquivos_processados}\n` +
          `📄 Itens: ${info.itens_processados}\n` +
          `💰 Valor total: R$ ${info.valor_total.toLocaleString('pt-BR', {minimumFractionDigits: 2})}\n` +
          `🎛️ Extração: ${camposInfo}${opcoesInfo.length ? ' + ' + opcoesInfo.join(', ') : ''}\n` +
          `📋 NFes: ${info.notas_encontradas.slice(0, 3).join(', ')}${info.notas_encontradas.length > 3 ? '...' : ''}\n` +
          `🏢 Emitentes: ${info.emitentes.slice(0, 2).join(', ')}${info.emitentes.length > 2 ? '...' : ''}`;
        
        // Depois: baixar Excel usando o MESMO formData (agora com configurações!)
        const responseExcel = await fetch(`${API_URL}/processar`, {
          method: 'POST', 
          body: formData
        });
        
        if (!responseExcel.ok) {
          const errorText = await responseExcel.text();
          throw new Error(`Erro ${responseExcel.status}: ${errorText}`);
        }
        
        // ✅ Download do arquivo Excel
        const blob = await responseExcel.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `${this.nomePlanilha}.xlsx`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        window.URL.revokeObjectURL(url);
        
        // ✅ Mostrar sucesso no download
        this.mensagem += '\n📥 Download iniciado automaticamente!';
        
      } catch (error) {
        this.mensagem = `❌ Erro: ${error.message}`;
        console.error('Erro no processamento:', error);
      } finally {
        this.loading = false;
      }
    }
  },
  watch: {
    // Detecta mudanças manuais nos campos para resetar preset
    camposSelecionados: {
      handler(newVal, oldVal) {
        if (oldVal && newVal && JSON.stringify(newVal) !== JSON.stringify(oldVal)) {
          // Verifica se não corresponde a nenhum preset
          if (this.presetAtivo !== 'personalizado' && !this.isPresetMatch()) {
            this.presetAtivo = 'personalizado';
          }
        }
      },
      deep: true
    }
  },
  methods: {
    isPresetMatch() {
      // Verifica se a seleção atual corresponde a algum preset
      const presets = {
        basico: [
          'numero_nf', 'data_emissao', 'emitente', 'cnpj_emitente', 
          'valor_total_nf', 'descricao_produto', 'valor_total_item'
        ],
        completo: [
          // Dados da NFe
          'numero_nf', 'data_emissao', 'serie', 'natureza_operacao', 'valor_total_nf', 'chave_nfe', 'modelo',
          // Dados do emitente
          'emitente', 'cnpj_emitente', 'municipio_emitente', 'uf_emitente', 'regime_tributario',
          // Dados do destinatário
          'destinatario', 'cnpj_destinatario', 'municipio_dest', 'uf_dest',
          // Produtos completos
          'descricao_produto', 'codigo_produto', 'ncm', 'cfop', 'quantidade_comercial', 'unidade_comercial', 'valor_unitario', 'valor_total_item',
          // Impostos principais
          'icms_valor', 'pis_valor', 'cofins_valor'
        ],
        fiscal: [
          // Dados básicos da NFe
          'numero_nf', 'data_emissao', 'emitente', 'cnpj_emitente', 'valor_total_nf',
          // Dados fiscais dos produtos
          'descricao_produto', 'cfop', 'ncm', 'valor_total_item', 
          // Impostos detalhados
          'cst_icms', 'base_icms', 'aliquota_icms', 'icms_valor',
          'aliquota_ipi', 'valor_ipi',
          'aliquota_pis', 'pis_valor',
          'aliquota_cofins', 'cofins_valor'
        ]
      };
      
      const sorted = (arr) => [...arr].sort();
      const currentSorted = sorted(this.camposSelecionados);
      
      return Object.values(presets).some(preset => 
        JSON.stringify(sorted(preset)) === JSON.stringify(currentSorted)
      );
    },
    
    aplicarPreset(tipo) {
      const presets = {
        basico: [
          'numero_nf', 'data_emissao', 'emitente', 'cnpj_emitente', 
          'valor_total_nf', 'descricao_produto', 'valor_total_item'
        ],
        completo: [
          // Dados da NFe
          'numero_nf', 'data_emissao', 'serie', 'natureza_operacao', 'valor_total_nf', 'chave_nfe', 'modelo',
          // Dados do emitente
          'emitente', 'cnpj_emitente', 'municipio_emitente', 'uf_emitente', 'regime_tributario',
          // Dados do destinatário
          'destinatario', 'cnpj_destinatario', 'municipio_dest', 'uf_dest',
          // Produtos completos
          'descricao_produto', 'codigo_produto', 'ncm', 'cfop', 'quantidade_comercial', 'unidade_comercial', 'valor_unitario', 'valor_total_item',
          // Impostos principais
          'icms_valor', 'pis_valor', 'cofins_valor'
        ],
        fiscal: [
          // Dados básicos da NFe
          'numero_nf', 'data_emissao', 'emitente', 'cnpj_emitente', 'valor_total_nf',
          // Dados fiscais dos produtos
          'descricao_produto', 'cfop', 'ncm', 'valor_total_item', 
          // Impostos detalhados
          'cst_icms', 'base_icms', 'aliquota_icms', 'icms_valor',
          'aliquota_ipi', 'valor_ipi',
          'aliquota_pis', 'pis_valor',
          'aliquota_cofins', 'cofins_valor'
        ]
      };
      
      if (presets[tipo]) {
        this.camposSelecionados = [...presets[tipo]];
        this.presetAtivo = tipo;
      }
    },
    
    // ... outros métodos serão mantidos ...
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
        this.showValidation('warning', `${files.length - xmlFiles.length} arquivo(s) não XML foram ignorados`);
      }
      
      // Limitar a 200 arquivos
      if (xmlFiles.length > 200) {
        this.selectedFiles = xmlFiles.slice(0, 200);
        this.showValidation('warning', `Apenas os primeiros 200 arquivos foram selecionados (${xmlFiles.length} total)`);
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
        this.showValidation('success', `${this.selectedFiles.length} arquivo(s) XML válido(s) selecionado(s)`);
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
        error: !isXml ? 'Não é XML' : !isValidSize ? 'Muito grande' : null
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
      const sugestao = `datarum_${agora.getFullYear()}-${pad(agora.getMonth()+1)}-${pad(agora.getDate())}_${pad(agora.getHours())}${pad(agora.getMinutes())}`;
      this.nomePlanilha = sugestao;
    },
    
    async enviarArquivos() {
      if (!this.selectedFiles.length || !this.nomePlanilha.trim()) return;

      this.loading = true;
      this.mensagem = '';
      this.validationMessage = null;

      const formData = new FormData();
      
      // ✅ Adicionar arquivos
      this.selectedFiles.forEach(file => formData.append('xmls', file));
      
      // ✅ Adicionar nome da planilha (OBRIGATÓRIO!)
      formData.append('planilha', this.nomePlanilha);
      
      // ✅ NOVO: Adicionar configurações de extração
      formData.append('campos_selecionados', JSON.stringify(this.camposSelecionados));
      formData.append('opcoes', JSON.stringify(this.opcoes));
      formData.append('preset', this.presetAtivo);

      // URL correta do backend LOCAL para desenvolvimento  
      const API_URL = 'http://127.0.0.1:8000';

      // Declarar progressInterval fora do try para acessar no catch
      let progressInterval;

      try {
        // Primeiro: obter informações
        const responseInfo = await fetch(`${API_URL}/processar-info`, {
          method: 'POST',
          body: formData
        });
        
        if (!responseInfo.ok) {
          const errorText = await responseInfo.text();
          throw new Error(`Erro ${responseInfo.status}: ${errorText}`);
        }
        
        const info = await responseInfo.json();
        
        // Mostrar resumo otimista
        this.mensagem = `Processando ${info.itens_processados} itens de ${info.arquivos_processados} arquivo(s)...`;
        
        // Simular progresso (visual feedback)
        let progress = 0;
        progressInterval = setInterval(() => {
          progress += Math.random() * 10;
          this.progress = Math.min(progress, 90);
        }, 200);

        // Segundo: processar e baixar
        const formDataDownload = new FormData();
        this.selectedFiles.forEach(file => formDataDownload.append('xmls', file));
        formDataDownload.append('planilha', this.nomePlanilha);
        formDataDownload.append('campos_selecionados', JSON.stringify(this.camposSelecionados));
        formDataDownload.append('opcoes', JSON.stringify(this.opcoes));
        formDataDownload.append('preset', this.presetAtivo);

        const responseExcel = await fetch(`${API_URL}/processar`, {
          method: 'POST',
          body: formDataDownload
        });
        
        if (progressInterval) {
          clearInterval(progressInterval);
        }
        this.progress = 100;
        
        if (!responseExcel.ok) {
          const errorText = await responseExcel.text();
          throw new Error(`Erro ${responseExcel.status}: ${errorText}`);
        }
        
        // Download do arquivo
        const blob = await responseExcel.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `${this.nomePlanilha}.xlsx`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        window.URL.revokeObjectURL(url);
        
        // Sucesso
        this.mensagem = `✅ Sucesso! ${info.itens_processados} itens processados em ${info.arquivos_processados} arquivo(s)`;
        
        if (info.arquivos_com_erro > 0) {
          this.mensagem += ` (${info.arquivos_com_erro} com erro)`;
        }
        
        setTimeout(() => {
          this.progress = 0;
        }, 3000);
        
      } catch (error) {
        if (progressInterval) {
          clearInterval(progressInterval);
        }
        this.progress = 0;
        this.mensagem = `❌ Erro: ${error.message}`;
        console.error('Erro no processamento:', error);
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>

<style>
</style>
