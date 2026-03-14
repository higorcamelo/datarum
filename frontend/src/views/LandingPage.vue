<template>
  <div class="min-h-screen bg-gradient-to-b from-white via-white to-orange-50">
    <!-- Padrão de fundo -->
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
            Processamento seguro, rápido e simples. Seus arquivos não são armazenados.
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
              <span>Personalização de campos</span>
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
                <span class="font-medium"> relatorio.xlsx</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

    <section id="demo" class="py-20 bg-gradient-to-b from-white via-orange-50 to-white relative">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-5xl sm:text-6xl font-black text-gray-900 mb-4" style="letter-spacing: -1px;">
            Transformação Automática
          </h2>
          <p class="text-lg text-gray-600 max-w-2xl mx-auto">
            De XML confuso para planilhas organizadas e prontas para análise
          </p>
        </div>

        <!-- Two-column demo: XML → Spreadsheet -->
        <div class="grid lg:grid-cols-2 gap-8 mb-8">
          
          <!-- LEFT: XML Bruto (Feio) -->
          <div class="bg-gray-900 rounded-xl border-2 border-gray-700 overflow-hidden shadow-2xl">
              <div class="bg-gray-800 px-4 py-3 border-b border-gray-700 flex items-center gap-2">
                <div class="w-2 h-2 bg-red-500 rounded-full"></div>
                <div class="w-2 h-2 bg-yellow-500 rounded-full"></div>
                <div class="w-2 h-2 bg-green-500 rounded-full"></div>
                <span class="text-xs text-gray-400 ml-auto font-mono">nota_fiscal_001.xml</span>
              </div>
              <pre class="text-xs text-gray-300 p-4 overflow-x-auto font-mono leading-relaxed max-h-96 overflow-y-auto bg-gray-900" style="background: #1a1a1a;">&lt;?xml version="1.0"?&gt;
&lt;NFe xmlns="http://www.portalfiscal.inf.br/nfe"&gt;
  &lt;infNFe Id="NFe..." versao="4.00"&gt;
    &lt;ide&gt;
      &lt;cUF&gt;35&lt;/cUF&gt;
      &lt;natOp&gt;VENDA DE MERCADORIA&lt;/natOp&gt;
      &lt;serie&gt;1&lt;/serie&gt;
      &lt;n_NF&gt;123&lt;/n_NF&gt;
    &lt;/ide&gt;
    &lt;emit&gt;
      &lt;CNPJ&gt;12.345.678/0001-90&lt;/CNPJ&gt;
      &lt;xNome&gt;EMPRESA EXEMPLO&lt;/xNome&gt;
      &lt;enderEmit&gt;
        &lt;xLgr&gt;Rua Principal&lt;/xLgr&gt;
        &lt;xBairro&gt;Centro&lt;/xBairro&gt;
        &lt;UF&gt;SP&lt;/UF&gt;
      &lt;/enderEmit&gt;
    &lt;/emit&gt;
    &lt;dest&gt;
      &lt;CNPJ&gt;98.765.432/0001-10&lt;/CNPJ&gt;
      &lt;xNome&gt;CLIENTE LTDA&lt;/xNome&gt;
    &lt;/dest&gt;
    &lt;det nItem="1"&gt;
      &lt;prod&gt;
        &lt;xProd&gt;PRODUTO EXEMPLO A&lt;/xProd&gt;
        &lt;qCom&gt;10.00&lt;/qCom&gt;
        &lt;vUnCom&gt;125.00&lt;/vUnCom&gt;
        &lt;vItem&gt;1250.00&lt;/vItem&gt;
      &lt;/prod&gt;
    &lt;/det&gt;
    &lt;det nItem="2"&gt;
      &lt;prod&gt;
        &lt;xProd&gt;SERVICO DE CONSULTORIA&lt;/xProd&gt;
        &lt;qCom&gt;2.00&lt;/qCom&gt;
        &lt;vUnCom&gt;1890.25&lt;/vUnCom&gt;
        &lt;vItem&gt;3780.50&lt;/vItem&gt;
      &lt;/prod&gt;
    &lt;/det&gt;
    &lt;det nItem="3"&gt;
      &lt;prod&gt;
        &lt;xProd&gt;MATERIAL ESCRITORIO&lt;/xProd&gt;
        &lt;qCom&gt;5.00&lt;/qCom&gt;
        &lt;vUnCom&gt;170.05&lt;/vUnCom&gt;
        &lt;vItem&gt;850.25&lt;/vItem&gt;
      &lt;/prod&gt;
    &lt;/det&gt;
    &lt;det nItem="4"&gt;
      &lt;prod&gt;
        &lt;xProd&gt;LICENCA SOFTWARE&lt;/xProd&gt;
        &lt;qCom&gt;1.00&lt;/qCom&gt;
        &lt;vUnCom&gt;2450.00&lt;/vUnCom&gt;
        &lt;vItem&gt;2450.00&lt;/vItem&gt;
      &lt;/prod&gt;
    &lt;/det&gt;
    &lt;det nItem="5"&gt;
      &lt;prod&gt;
        &lt;xProd&gt;EQUIPAMENTO ELETRONICO&lt;/xProd&gt;
        &lt;qCom&gt;3.00&lt;/qCom&gt;
        &lt;vUnCom&gt;890.50&lt;/vUnCom&gt;
        &lt;vItem&gt;2671.50&lt;/vItem&gt;
      &lt;/prod&gt;
    &lt;/det&gt;
    &lt;det nItem="6"&gt;
      &lt;prod&gt;
        &lt;xProd&gt;MANUTENCAO PREVENTIVA&lt;/xProd&gt;
        &lt;qCom&gt;4.00&lt;/qCom&gt;
        &lt;vUnCom&gt;325.75&lt;/vUnCom&gt;
        &lt;vItem&gt;1303.00&lt;/vItem&gt;
      &lt;/prod&gt;
    &lt;/det&gt;
  &lt;/infNFe&gt;
&lt;/NFe&gt;</pre>
            </div>

          <!-- RIGHT: Planilha Formatada (Bonita) -->
          <div class="bg-white rounded-xl border-2 border-gray-200 overflow-hidden shadow-2xl">
              <div class="bg-gradient-to-r from-orange-50 to-amber-100 px-4 py-3 border-b border-gray-200">
                <span class="text-xs font-bold text-orange-900">relatorio_nfe.xlsx</span>
              </div>
              <div class="overflow-x-auto">
                <table class="w-full text-xs">
                  <thead class="bg-orange-100 border-b border-gray-300">
                    <tr>
                      <th class="px-3 py-2 text-left font-bold text-orange-900">Nº NF</th>
                      <th class="px-3 py-2 text-left font-bold text-orange-900">Data</th>
                      <th class="px-3 py-2 text-left font-bold text-orange-900">CNPJ Emitente</th>
                      <th class="px-3 py-2 text-left font-bold text-orange-900">Emitente</th>
                      <th class="px-3 py-2 text-left font-bold text-orange-900">Produto</th>
                      <th class="px-3 py-2 text-left font-bold text-orange-900">Qtd</th>
                      <th class="px-3 py-2 text-right font-bold text-orange-900">Valor</th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-gray-100 text-gray-700">
                    <tr class="hover:bg-orange-50 transition-colors">
                      <td class="px-3 py-2 font-semibold">123</td>
                      <td class="px-3 py-2">15/07/2025</td>
                      <td class="px-3 py-2 font-mono text-xs">12.345.678/0001-90</td>
                      <td class="px-3 py-2 whitespace-nowrap">Empresa Exemplo</td>
                      <td class="px-3 py-2 truncate">Produto Exemplo A</td>
                      <td class="px-3 py-2 text-center">10.00</td>
                      <td class="px-3 py-2 text-right font-semibold text-orange-700">R$ 1.250,00</td>
                    </tr>
                    <tr class="bg-gray-50 hover:bg-orange-50 transition-colors">
                      <td class="px-3 py-2 font-semibold">123</td>
                      <td class="px-3 py-2">15/07/2025</td>
                      <td class="px-3 py-2 font-mono text-xs">12.345.678/0001-90</td>
                      <td class="px-3 py-2 whitespace-nowrap">Empresa Exemplo</td>
                      <td class="px-3 py-2 truncate">Serviço de Consultoria</td>
                      <td class="px-3 py-2 text-center">2.00</td>
                      <td class="px-3 py-2 text-right font-semibold text-orange-700">R$ 3.780,50</td>
                    </tr>
                    <tr class="hover:bg-orange-50 transition-colors">
                      <td class="px-3 py-2 font-semibold">123</td>
                      <td class="px-3 py-2">15/07/2025</td>
                      <td class="px-3 py-2 font-mono text-xs">12.345.678/0001-90</td>
                      <td class="px-3 py-2 whitespace-nowrap">Empresa Exemplo</td>
                      <td class="px-3 py-2 truncate">Material Escritório</td>
                      <td class="px-3 py-2 text-center">5.00</td>
                      <td class="px-3 py-2 text-right font-semibold text-orange-700">R$ 850,25</td>
                    </tr>
                    <tr class="bg-gray-50 hover:bg-orange-50 transition-colors">
                      <td class="px-3 py-2 font-semibold">123</td>
                      <td class="px-3 py-2">15/07/2025</td>
                      <td class="px-3 py-2 font-mono text-xs">12.345.678/0001-90</td>
                      <td class="px-3 py-2 whitespace-nowrap">Empresa Exemplo</td>
                      <td class="px-3 py-2 truncate">Licença Software</td>
                      <td class="px-3 py-2 text-center">1.00</td>
                      <td class="px-3 py-2 text-right font-semibold text-orange-700">R$ 2.450,00</td>
                    </tr>
                    <tr class="hover:bg-orange-50 transition-colors">
                      <td class="px-3 py-2 font-semibold">123</td>
                      <td class="px-3 py-2">15/07/2025</td>
                      <td class="px-3 py-2 font-mono text-xs">12.345.678/0001-90</td>
                      <td class="px-3 py-2 whitespace-nowrap">Empresa Exemplo</td>
                      <td class="px-3 py-2 truncate">Equipamento Eletrônico</td>
                      <td class="px-3 py-2 text-center">3.00</td>
                      <td class="px-3 py-2 text-right font-semibold text-orange-700">R$ 2.671,50</td>
                    </tr>
                    <tr class="bg-gray-50 hover:bg-orange-50 transition-colors">
                      <td class="px-3 py-2 font-semibold">123</td>
                      <td class="px-3 py-2">15/07/2025</td>
                      <td class="px-3 py-2 font-mono text-xs">12.345.678/0001-90</td>
                      <td class="px-3 py-2 whitespace-nowrap">Empresa Exemplo</td>
                      <td class="px-3 py-2 truncate">Manutenção Preventiva</td>
                      <td class="px-3 py-2 text-center">4.00</td>
                      <td class="px-3 py-2 text-right font-semibold text-orange-700">R$ 1.303,00</td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <div class="bg-gray-50 px-4 py-3 border-t border-gray-200 text-xs text-gray-600">
                <span class="font-semibold">Total:</span> 3 notas | <span class="font-semibold text-orange-700">R$ 5.880,75</span>
              </div>
          </div>

        </div>

        <!-- Bottom CTA -->
        <div class="text-center pt-8">
          <p class="text-lg text-gray-600 mb-4">
           Processa múltiplos XMLs em segundos. Personalize quais campos extrair.
          </p>
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
          <!-- v1.0 -->
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

          <!-- v1.1 - -->
          <RoadmapCard title="v1.1" status="→ Em desenvolvimento" type="info">
            <li class="flex items-center gap-2">
              <span class="w-1 h-1 bg-gray-600 rounded-full"></span>
              <span>Mais personalizações de planilhas</span>
            </li>
            <li class="flex items-center gap-2">
              <span class="w-1 h-1 bg-gray-600 rounded-full"></span>
              <span>Geração de relatórios baseado nas notas fiscais</span>
            </li>
          </RoadmapCard>

          <!-- v2.0+ - -->
          <RoadmapCard title="v2.0+" status="◯ Futuro" type="neutral">
            <li class="flex items-center gap-2">
              <span class="w-1 h-1 bg-gray-600 rounded-full"></span>
              <span>Processamento de notas fiscais em imagens ou PDFs</span>
            </li>
            <li class="flex items-center gap-2">
              <span class="w-1 h-1 bg-gray-600 rounded-full"></span>
              <span>API para integrações</span>
            </li>
            <li class="flex items-center gap-2">
              <span class="w-1 h-1 bg-gray-600 rounded-full"></span>
              <span>Análise de dados avançada com IA</span>
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
</style> 
