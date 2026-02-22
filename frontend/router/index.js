import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '../views/LandingPage.vue'
import ConversorApp from '../views/ConversorApp.vue'

const routes = [
  { path: '/', component: LandingPage },
  { path: '/conversor', component: ConversorApp }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router