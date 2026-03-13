<template>
  <div :class="['relative pl-8', isFuture && 'opacity-60']">
    <!-- Linha vertical -->
    <div class="absolute left-0 top-3 bottom-0 w-0.5 bg-gray-300"></div>
    
    <!-- Ponto na timeline -->
    <div :class="[
      'absolute -left-2 top-1.5 w-5 h-5 rounded-full border-2 border-white',
      statusColor
    ]"></div>

    <!-- Conteúdo -->
    <div class="pb-8">
      <div class="flex items-start justify-between gap-4">
        <div>
          <h3 class="text-lg font-black text-gray-900">{{ title }}</h3>
          <p class="text-sm text-gray-600 mt-1">{{ status }}</p>
        </div>
      </div>
      
      <ul class="space-y-2 mt-3 text-sm text-gray-600">
        <slot></slot>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  title: String,
  status: String,
  type: {
    type: String,
    default: 'neutral' // success, info, warning, neutral
  }
});

const isFuture = computed(() => props.type === 'neutral');

const statusColor = computed(() => {
  const colors = {
    success: 'bg-green-500',
    info:    'bg-orange-700',
    warning: 'bg-gray-400',
    neutral: 'bg-gray-300'
  };
  return colors[props.type] || colors.neutral;
});
</script>