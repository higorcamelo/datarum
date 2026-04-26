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
     <div v-if="erroConfig" class="text-red-600 text-sm font-bold">
      Erro ao carregar configurações. Tente recarregar a página.
    </div>
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
                  v-model="selected"
                  class="w-5 h-5 rounded border-2 border-orange-200 text-orange-800 focus:ring-2 focus:ring-orange-800"
                />
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
import { ref, watch, computed, onMounted } from 'vue';

const props = defineProps({
  modelValue: {
    type: Array,
    default: () => []
  },
  presetAtivo: {
    type: String,
    default: 'basico'
  }
});

const emit = defineEmits(['update:modelValue', 'update:presetAtivo']);

const mostrarCustom = ref(false);

const presets = ref({});
const camposDisponiveis = ref({});
const loading = ref(true);
const erroConfig = ref(false);

onMounted(async () => {
  try {
    const res = await fetch(`${import.meta.env.VITE_API_URL}/config`);

    if (!res.ok) throw new Error(`HTTP ${res.status}`);

    const config = await res.json();

    presets.value = config?.presets ?? {};
    camposDisponiveis.value = config?.campos ?? {};

  } catch (e) {
    console.error('Erro ao carregar /config:', e);
    erroConfig.value = true;

    // fallback seguro pra não quebrar UI
    camposDisponiveis.value = {};
    presets.value = {};
  } finally {
    loading.value = false;
  }
});

const selected = computed({
  get: () => props.modelValue,
  set: (val) => emit('update:modelValue', val)
});


watch(() => props.presetAtivo, (preset) => {
  if (!preset || preset === 'custom') return;
  if (!presets.value[preset]) return;

  const campos = presets.value[preset]?.campos;

  if (Array.isArray(campos)) {
    emit('update:modelValue', [...campos]);
  }
});

watch(() => props.modelValue, (val = []) => {
  const isSameSet = (a, b) => {
    if (!Array.isArray(a) || !Array.isArray(b)) return false;
    if (a.length !== b.length) return false;

    const setB = new Set(b);
    return a.every(x => setB.has(x));
  };

  const isPreset = Object.values(presets.value || {}).some(
    p => isSameSet(p?.campos || [], val)
  );

  if (!isPreset && props.presetAtivo !== 'custom') {
    emit('update:presetAtivo', 'custom');
  }
}, { deep: true });

const toggleField = (id) => {
  const current = Array.isArray(props.modelValue)
    ? props.modelValue
    : [];

  const set = new Set(current);

  if (set.has(id)) set.delete(id);
  else set.add(id);

  emit('update:modelValue', [...set]);
};

const totalSelecionados = computed(() =>
  Array.isArray(props.modelValue) ? props.modelValue.length : 0
);
</script>