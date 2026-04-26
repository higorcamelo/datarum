<template>
  <div class="space-y-6">
    <!-- Seleção de Presets -->
    <div>
      <div class="mb-4">
        <p class="text-base font-black text-orange-800 uppercase tracking-widest">
          Formato do relatório
        </p>
      </div>

      <div class="grid grid-cols-3 gap-2">
        <button
          v-for="p in ['basico', 'completo', 'fiscal']"
          :key="p"
          @click="$emit('update:presetAtivo', p)"
          :class="[
            'px-3 py-3 rounded-lg border-2 transition-all duration-200 text-xs font-black capitalize focus:outline-none focus:ring-2 focus:ring-orange-800',
            presetAtivo === p
              ? 'bg-orange-800 text-white border-orange-800 shadow-md'
              : 'bg-white text-orange-700 border-orange-200 hover:border-orange-800 hover:bg-orange-50'
          ]"
        >
          {{ p === 'basico' ? 'Básico' : p === 'completo' ? 'Completo' : 'Fiscal' }}
        </button>
      </div>
    </div>

    <!-- Campos Personalizados -->
    <div v-if="mostrarCustom">
      <div class="mb-3">
        <p class="text-xs font-black text-orange-800 uppercase tracking-widest">Colunas</p>
      </div>

      <div class="space-y-4 bg-orange-50 p-4 rounded-xl border-2 border-orange-200">
        <div v-for="(campos, grupo) in camposDisponiveis" :key="grupo" class="text-sm">
          <h4 class="font-black text-orange-800 mb-2 capitalize text-xs uppercase tracking-wide">
            {{ grupo }}
          </h4>

          <div class="grid grid-cols-1 gap-2">
            <label
              v-for="campo in campos"
              :key="campo.id"
              class="flex items-center gap-2 text-sm cursor-pointer"
            >
              <input
                type="checkbox"
                :value="campo.id"
                :checked="modelValue.includes(campo.id)"
                @change="toggleField(campo.id)"
                class="w-5 h-5 rounded border-2 border-orange-200 text-orange-800 focus:ring-2 focus:ring-orange-800 cursor-pointer"
              >
              <span class="text-orange-700 font-semibold text-xs">{{ campo.nome }}</span>
            </label>
          </div>
        </div>
      </div>
    </div>

    <!-- Botão de Toggle -->
    <button
      @click="mostrarCustom = !mostrarCustom"
      :class="[
        'w-full py-3 text-sm font-black rounded-lg border-2 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-orange-800 uppercase tracking-wide',
        mostrarCustom
          ? 'border-orange-800 text-orange-800 bg-orange-100'
          : 'border-orange-200 text-orange-700 hover:border-orange-800 hover:bg-orange-50'
      ]"
    >
      {{ mostrarCustom ? '− Fechar' : '+ Personalizar' }}
    </button>
  </div>
</template>

<script setup>
import { ref, watch, computed } from 'vue';

const props = defineProps({
  modelValue: { type: Array, default: () => [] },
  presetAtivo: { type: String, default: 'basico' },
  camposDisponiveis: { type: Object, required: true }
});

const emit = defineEmits(['update:modelValue', 'update:presetAtivo']);

const mostrarCustom = ref(false);

const PRESETS = {
  basico: ['id', 'data', 'valor'],
  completo: ['id', 'data', 'valor', 'cliente', 'descricao'],
  fiscal: ['id', 'cnpj', 'imposto']
};

watch(() => props.presetAtivo, (novo) => {
  if (novo !== 'custom') {
    emit('update:modelValue', PRESETS[novo] || []);
  }
});

watch(() => props.modelValue, (val) => {
  const isPreset = Object.entries(PRESETS).some(
    ([_, campos]) =>
      campos.length === val.length &&
      campos.every(c => val.includes(c))
  );

  if (!isPreset && props.presetAtivo !== 'custom') {
    emit('update:presetAtivo', 'custom');
  }
}, { deep: true });

const toggleField = (id) => {
  const set = new Set(props.modelValue);

  if (set.has(id)) set.delete(id);
  else set.add(id);

  emit('update:modelValue', [...set]);
};

const totalSelecionados = computed(() => props.modelValue.length);
</script>