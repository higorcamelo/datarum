import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from './views/LandingPage.vue'
import AppConverter from './views/ConversorApp.vue'
import './style.css'
const routes = [
  { path: '/', component: LandingPage },
  { path: '/conversor', component: AppConverter }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

createApp(App).use(router).mount('#app')