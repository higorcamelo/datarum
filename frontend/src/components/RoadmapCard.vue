<template>
  <div 
    :class="[
      'bg-white p-6 rounded-2xl shadow-lg border relative transition-all duration-300',
      isFuture ? 'opacity-75 grayscale-[0.5]' : 'hover:shadow-xl hover:-translate-y-1'
    ]"
  >
    <div 
      :class="[
        'absolute -top-2 -right-2 text-white px-2 py-1 rounded-full text-xs font-bold shadow-sm',
        config.badge
      ]"
    >
      {{ status }}
    </div>

    <div :class="['w-12 h-12 rounded-xl flex items-center justify-center mb-4', config.bg]">
      <svg class="w-6 h-6" :class="config.text" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="icon" />
      </svg>
    </div>

    <h3 class="text-lg font-semibold text-gray-900 mb-2">{{ title }}</h3>
    <p class="text-gray-600 text-sm leading-relaxed">{{ description }}</p>
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  title: String,
  description: String,
  status: String,
  icon: String,
  type: {
    type: String,
    default: 'neutral' // success, info, warning, neutral
  }
});

const isFuture = computed(() => props.type === 'neutral');

// Mapeamento de estilos centralizado
const config = computed(() => {
  const styles = {
    success: { badge: 'bg-green-500', bg: 'bg-green-100', text: 'text-green-600' },
    info:    { badge: 'bg-blue-500',  bg: 'bg-blue-100',  text: 'text-blue-600' },
    warning: { badge: 'bg-purple-500',bg: 'bg-purple-100',text: 'text-purple-600' },
    neutral: { badge: 'bg-gray-400',  bg: 'bg-gray-100',  text: 'text-gray-500' }
  };
  return styles[props.type] || styles.neutral;
});
</script>