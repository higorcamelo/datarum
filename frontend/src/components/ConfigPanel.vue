<template>
  <div class="space-y-4">
    <!-- Seleção de Presets -->
    <div>
      <div class="mb-3">
        <p class="text-xs font-bold text-gray-700 uppercase tracking-wide">Presets padrão</p>
      </div>
      <div class="flex gap-2">
        <button v-for="p in ['basico', 'completo', 'fiscal']" :key="p"
          @click="$emit('update:presetAtivo', p)"
          :class="['px-4 py-2 rounded-lg border-2 transition-all duration-200 text-sm font-bold capitalize focus:outline-none focus:ring-2 focus:ring-orange-500', 
                   presetAtivo === p ? 'bg-orange-700 text-white border-orange-800 shadow-md' : 'bg-white text-gray-700 border-gray-300 hover:border-orange-400 hover:bg-orange-50']">
          {{ p === 'basico' ? '📋' : p === 'completo' ? '📊' : '💰' }} {{ p }}
        </button>
      </div>
    </div>

    <!-- Campos Personalizados -->
    <div v-if="mostrarCustom">
      <div class="mb-3">
        <p class="text-xs font-bold text-gray-700 uppercase tracking-wide">Personalizar colunas</p>
      </div>
      <div class="space-y-3 bg-orange-50 p-4 rounded-lg border border-orange-200">
        <div v-for="(campos, grupo) in camposDisponiveis" :key="grupo" class="text-sm">
          <h4 class="font-bold text-gray-900 mb-2 capitalize text-xs">{{ grupo }}</h4>
          <div class="grid grid-cols-2 gap-2">
            <label v-for="campo in campos" :key="campo.id" class="flex items-center gap-2 text-sm cursor-pointer">
              <input type="checkbox" 
                     :value="campo.id" 
                     :checked="modelValue.includes(campo.id)"
                     @change="toggleField(campo.id)"
                     class="w-4 h-4 rounded border-gray-300 text-orange-700 focus:ring-2 focus:ring-orange-500 cursor-pointer">
              <span class="text-gray-700 font-medium text-xs">{{ campo.nome }}</span>
            </label>
          </div>
        </div>
      </div>
    </div>

    <!-- Botão de Toggle -->
    <button 
      @click="mostrarCustom = !mostrarCustom"
      :class="['w-full py-2 text-sm font-semibold rounded-lg border-2 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-orange-500', 
               mostrarCustom ? 'border-orange-500 text-orange-700 bg-orange-50' : 'border-gray-300 text-gray-700 hover:border-orange-400']">
      {{ mostrarCustom ? '− Fechar personalização' : '+ Personalizar colunas' }}
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
const mostrarCustom = ref(false);

const toggleField = (id) => {
  const newValue = [...props.modelValue];
  const index = newValue.indexOf(id);
  if (index > -1) newValue.splice(index, 1);
  else newValue.push(id);
  emit('update:modelValue', newValue);
};
</script>