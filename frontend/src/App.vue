<template>
  <div class="font-sans antialiased text-gray-900">
    <LandingPage 
      v-if="currentView === 'landing'" 
      @goToApp="currentView = 'app'" 
    />
    <ConversorApp v-else @back="currentView = 'landing'" />
    
  </div>
</template>

<script setup>
import { ref } from 'vue';
import LandingPage from './views/LandingPage.vue';
import ConversorApp from './views/ConversorApp.vue';

const currentView = ref('landing');
</script>