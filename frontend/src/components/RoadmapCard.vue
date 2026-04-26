<template>
  <div :class="['relative pl-8', isFuture && 'opacity-60']">

    <!-- linha vertical -->
    <div class="absolute left-0 top-3 bottom-0 w-0.5 bg-slate-200"></div>

    <!-- ponto -->
    <div :class="[
      'absolute -left-2 top-1.5 w-5 h-5 rounded-full border-2 border-white',
      statusColor
    ]"></div>

    <!-- conteúdo -->
    <div class="pb-8">

      <div>
        <h3 class="text-lg font-black text-slate-900">
          {{ title }}
        </h3>

        <p class="text-sm text-slate-500 mt-1">
          {{ status }}
        </p>
      </div>

      <ul class="space-y-2 mt-3 text-sm text-slate-600">
        <slot />
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
    default: 'idea' // stable | evolving | exploring | idea
  }
});

const isFuture = computed(() => props.type !== 'stable');

const statusColor = computed(() => {
  const colors = {
    stable: 'bg-emerald-500',
    evolving: 'bg-orange-600',
    exploring: 'bg-slate-400',
    idea: 'bg-slate-300'
  };

  return colors[props.type] || colors.idea;
});
</script>