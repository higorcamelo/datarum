<template>
  <div class="space-y-5">
    <div>
      <label class="block text-sm font-bold text-gray-900 mb-3 flex items-center gap-2">
        <svg class="w-5 h-5 text-blue-600" fill="currentColor" viewBox="0 0 20 20">
          <path d="M5 4a2 2 0 012-2h6a2 2 0 012 2v14l-5-2.5L5 18V4z"/>
        </svg>
        Preset de colunas
      </label>
      <div class="grid grid-cols-3 gap-2">
        <button v-for="p in ['basico', 'completo', 'fiscal']" :key="p"
          @click="$emit('update:presetAtivo', p)"
          :class="['p-3 rounded-lg border-2 transition-all text-sm font-bold capitalize', 
                   presetAtivo === p ? 'bg-gradient-to-br from-orange-700 to-orange-800 text-white border-orange-800 shadow-md' : 'bg-white text-gray-700 border-gray-300 hover:border-orange-400 hover:bg-orange-50']">
          {{ p === 'basico' ? '📋' : p === 'completo' ? '📊' : '💰' }} {{ p }}
        </button>
      </div>
    </div>

    <details class="bg-gradient-to-br from-orange-50 to-gray-50 rounded-lg p-4 cursor-pointer border border-gray-200 hover:border-orange-300 transition">
      <summary class="font-bold text-sm text-gray-900 select-none flex items-center gap-2 text-base">
        <svg class="w-5 h-5 text-orange-700" fill="currentColor" viewBox="0 0 20 20">
          <path fill-rule="evenodd" d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 17v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.454z" clip-rule="evenodd"/>
        </svg>
        Personalizar colunas
      </summary>
      <div v-show="mostrarDetalhes" class="space-y-4 mt-4 pt-4 border-t border-gray-300">
        <div v-for="(campos, grupo) in camposDisponiveis" :key="grupo" class="text-sm">
          <h4 class="font-bold text-gray-900 mb-3 capitalize text-base">{{ grupo }}</h4>
          <div class="grid grid-cols-2 gap-3">
            <label v-for="campo in campos" :key="campo.id" class="flex items-center gap-3 text-sm cursor-pointer p-2 rounded-lg hover:bg-white transition">
              <input type="checkbox" 
                     :value="campo.id" 
                     :checked="modelValue.includes(campo.id)"
                     @change="toggleField(campo.id)"
                     class="w-4 h-4 rounded border-gray-300 text-orange-700 focus:ring-2 focus:ring-orange-500">
              <span class="text-gray-700 font-medium">{{ campo.nome }}</span>
            </label>
          </div>
        </div>
      </div>
    </details>
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