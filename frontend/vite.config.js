import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  base: '/datarum/',
  plugins: [vue()],
  build: {
    outDir: 'dist',
    sourcemap: false
  },
  server: {
    port: 5173,
    host: true
  }
})