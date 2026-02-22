<template>
  <div class="bg-gradient-to-r from-purple-50 to-purple-100 rounded-xl p-6 border border-purple-200">
    <div class="flex items-center gap-3 mb-4">
      <div class="w-10 h-10 bg-purple-600 rounded-lg flex items-center justify-center">
        <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 100 4m0-4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 100 4m0-4v2m0-6V4"/>
        </svg>
      </div>
      <h3 class="text-lg font-bold text-purple-700">Personalizar Extração</h3>
    </div>

    <div class="mb-6">
      <label class="block text-sm font-semibold text-purple-700 mb-3">Presets de Colunas</label>
      <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
        <button v-for="p in ['basico', 'completo', 'fiscal']" :key="p"
          @click="$emit('update:presetAtivo', p)"
          :class="['p-3 rounded-lg border transition-all text-sm capitalize font-medium', 
                   presetAtivo === p ? 'bg-purple-600 text-white shadow-md border-purple-600' : 'bg-white text-purple-700 border-purple-200 hover:border-purple-400']">
          {{ p }}
        </button>
      </div>
    </div>

    <div v-show="mostrarDetalhes" class="space-y-4">
      <div v-for="(campos, grupo) in camposDisponiveis" :key="grupo" class="bg-white rounded-lg p-4 border border-purple-100 shadow-sm">
        <h4 class="text-sm font-bold text-purple-700 mb-3 capitalize border-b border-purple-50 pb-1">{{ grupo }}</h4>
        <div class="grid grid-cols-2 gap-3">
          <label v-for="campo in campos" :key="campo.id" class="flex items-center gap-2 text-sm cursor-pointer hover:text-purple-600 transition-colors">
            <input type="checkbox" 
                   :value="campo.id" 
                   :checked="modelValue.includes(campo.id)"
                   @change="toggleField(campo.id)"
                   class="rounded border-purple-300 text-purple-600 focus:ring-purple-500">
            <span class="text-gray-700">{{ campo.nome }}</span>
          </label>
        </div>
      </div>
    </div>
    
    <button @click="mostrarDetalhes = !mostrarDetalhes" class="mt-4 text-xs text-purple-600 font-bold hover:text-purple-800 underline w-full text-center uppercase tracking-wider">
      {{ mostrarDetalhes ? '↑ Ocultar Seleção Manual' : '↓ Ver Todos os Campos (Seleção Manual)' }}
    </button>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const props = defineProps({
  modelValue: { type: Array, default: () => [] },
  presetAtivo: { type: String, default: 'basico' },
  camposDisponiveis: { type: Object, required: true }
});

const emit = defineEmits(['update:modelValue', 'update:presetAtivo']);
const mostrarDetalhes = ref(false);

const toggleField = (id) => {
  const newValue = [...props.modelValue];
  const index = newValue.indexOf(id);
  if (index > -1) newValue.splice(index, 1);
  else newValue.push(id);
  emit('update:modelValue', newValue);
};
</script>