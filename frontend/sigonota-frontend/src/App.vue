<template>
  <main class="container">
    <h1>Sigonota 📄</h1>

    <!-- Área de upload -->
    <section class="upload-section">
      <label for="xmlUpload">Selecione arquivos XML:</label>
      <input type="file" id="xmlUpload" multiple accept=".xml" @change="handleFileChange" />
      <ul>
        <li v-for="(file, index) in selectedFiles" :key="index">{{ file.name }}</li>
      </ul>
    </section>

    <!-- Botão de envio -->
    <section class="actions">
      <button @click="enviarArquivos" :disabled="!selectedFiles.length">Enviar para processamento</button>
    </section>

    <!-- Mensagem -->
    <section v-if="mensagem" class="mensagem">{{ mensagem }}</section>
  </main>
</template>

<script>
export default {
  data() {
    return {
      selectedFiles: [],
      mensagem: ''
    };
  },
  methods: {
    handleFileChange(event) {
      this.selectedFiles = Array.from(event.target.files);
    },
    async enviarArquivos() {
      if (!this.selectedFiles.length) return;

      const formData = new FormData();
      this.selectedFiles.forEach(file => formData.append('xmls', file));

      try {
        const response = await fetch('http://localhost:8000/processar', {
          method: 'POST',
          body: formData
        });

        if (!response.ok) throw new Error('Falha ao enviar arquivos');
        const resultado = await response.json();
        this.mensagem = `✅ ${resultado.qtd} itens processados com sucesso!`;

      } catch (err) {
        this.mensagem = `❌ Erro: ${err.message}`;
      }
    }
  }
}
</script>

<style>
body {
  font-family: Arial, sans-serif;
  background-color: #f4f6fb;
  margin: 0;
  padding: 2rem;
}
.container {
  max-width: 600px;
  margin: auto;
  background: white;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 0 10px #ccc;
}
.upload-section {
  margin-bottom: 1.5rem;
}
.actions {
  margin-top: 1rem;
}
.mensagem {
  margin-top: 1.5rem;
  font-weight: bold;
  color: #1976d2;
}
</style>
