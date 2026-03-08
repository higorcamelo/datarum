import { createRouter, createWebHashHistory } from 'vue-router'
import LandingPage from '../views/LandingPage.vue'
import ConversorApp from '../views/ConversorApp.vue'

const routes = [
  { path: '/', component: LandingPage },
  { path: '/conversor', component: ConversorApp }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router