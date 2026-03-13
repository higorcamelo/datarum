<template>
  <div class="p-6 text-center">
    <div class="w-12 h-12 bg-gray-100 rounded-lg flex items-center justify-center mx-auto mb-4 text-gray-600">
      <slot name="icon"></slot>
    </div>
    <h3 class="font-semibold text-gray-900 mb-2">{{ title }}</h3>
    <p class="text-gray-600 text-sm leading-relaxed">{{ description }}</p>
  </div>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    default: ''
  }
});
</script>