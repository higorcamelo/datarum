import { ENDPOINTS } from '../config/api';

export const xmlService = {
  async processarDocumentos(arquivos, nomePlanilha, camposSelecionados) {
    const formData = new FormData();

    // Arquivos
    arquivos.forEach(file => formData.append('xmls', file));

    // Nome da planilha
    formData.append('planilha', nomePlanilha);

    // Campos selecionados
    camposSelecionados.forEach(campo => {
      formData.append('campos', campo);
    });

    // Chamada de Info
    const infoRes = await fetch(ENDPOINTS.PROCESSAR_INFO, {
      method: 'POST',
      body: formData
    });

    if (!infoRes.ok) {
      throw new Error('Falha ao obter informações dos XMLs');
    }

    const info = await infoRes.json();

    // Chamada de Excel
    const excelRes = await fetch(ENDPOINTS.PROCESSAR_EXCEL, {
      method: 'POST',
      body: formData
    });

    if (!excelRes.ok) {
      throw new Error('Falha ao gerar o Excel');
    }

    const blob = await excelRes.blob();

    return { info, blob };
  }
};