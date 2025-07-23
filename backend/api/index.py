from http.server import BaseHTTPRequestHandler
import json
import urllib.parse
import tempfile
import os
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    
    def parse_multipart(self, data, boundary):
        """Parse multipart form data para extrair arquivos XML"""
        files = []
        try:
            boundary_bytes = boundary.encode('utf-8')
            parts = data.split(b'--' + boundary_bytes)
            
            for part in parts:
                if b'Content-Disposition' in part and b'filename=' in part:
                    lines = part.split(b'\r\n')
                    filename = None
                    content_start = -1
                    
                    for i, line in enumerate(lines):
                        if b'Content-Disposition' in line:
                            line_str = line.decode('utf-8', errors='ignore')
                            if 'filename=' in line_str:
                                start = line_str.find('filename="') + 10
                                end = line_str.find('"', start)
                                filename = line_str[start:end] if start > 9 and end > start else None
                        elif line == b'' and content_start == -1:
                            content_start = i + 1
                            break
                    
                    if content_start > 0 and filename and filename.lower().endswith('.xml'):
                        content_lines = lines[content_start:]
                        if content_lines and content_lines[-1] == b'':
                            content_lines = content_lines[:-1]
                        file_content = b'\r\n'.join(content_lines)
                        if file_content:
                            files.append({'filename': filename, 'content': file_content})
        except:
            pass
        return files
    
    def processar_xml(self, content):
        """Processa um arquivo XML de NFe usando o parser do utils"""
        try:
            import sys
            import os
            # Adicionar o diretório backend ao path para importar utils
            backend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)))
            if backend_path not in sys.path:
                sys.path.append(backend_path)
            
            from utils.xml_parser import validate_nfe_version
            import xmltodict
            
            xml_dict = xmltodict.parse(content.decode('utf-8'))
            
            # Validar NFe usando a função do utils
            validacao = validate_nfe_version(xml_dict)
            if not validacao["valid"]:
                return [{
                    'numero_nf': 'ERRO',
                    'data_emissao': '2025-01-01',
                    'emitente': f'NFe inválida: {validacao["error"]}',
                    'erro': validacao["error"]
                }]
            
            # A nota pode estar aninhada de formas diferentes
            nfe_root = xml_dict.get("NFe") \
                or xml_dict.get("nfeProc", {}).get("NFe") \
                or xml_dict.get("nfeProc", {}).get("nfe:NFe")

            if not nfe_root:
                return [{
                    'numero_nf': 'ERRO',
                    'data_emissao': '2025-01-01',
                    'emitente': 'Estrutura NFe não encontrada',
                    'erro': 'Estrutura NFe não encontrada'
                }]

            inf_nfe = nfe_root.get("infNFe") or nfe_root.get("nfe:infNFe")

            # Função auxiliar para acessos seguros
            def g(dic, path, default=""):
                for p in path.split("."):
                    dic = dic.get(p, {})
                return dic or default

            # Dados do cabeçalho
            ide = inf_nfe.get("ide", {})
            emit = inf_nfe.get("emit", {})
            dest = inf_nfe.get("dest", {})
            total = inf_nfe.get("total", {}).get("ICMSTot", {})
            transp = inf_nfe.get("transp", {})

            dados_comuns = {
                "numero_nf": g(ide, "nNF"),
                "serie": g(ide, "serie"),
                "data_emissao": g(ide, "dEmi") or g(ide, "dhEmi", "")[:10],
                "modelo": g(ide, "mod"),
                "tipo_operacao": g(ide, "tpNF"),
                "finalidade": g(ide, "finNFe"),
                "natureza_operacao": g(ide, "natOp"),
                "versao_nfe": validacao["version"],

                "cnpj_emitente": g(emit, "CNPJ"),
                "emitente": g(emit, "xNome"),
                "municipio_emitente": g(emit, "enderEmit.xMun"),
                "uf_emitente": g(emit, "enderEmit.UF"),

                "cnpj_destinatario": g(dest, "CNPJ"),
                "destinatario": g(dest, "xNome"),
                "municipio_dest": g(dest, "enderDest.xMun"),
                "uf_dest": g(dest, "enderDest.UF"),

                "valor_total_nf": g(total, "vNF"),
                "valor_produtos": g(total, "vProd"),
                "valor_icms": g(total, "vICMS"),
                "valor_pis": g(total, "vPIS"),
                "valor_cofins": g(total, "vCOFINS"),

                "transportadora": g(transp, "transporta.xNome"),
                "placa_veiculo": g(transp, "veicTransp.placa"),
            }

            # Produtos
            itens = inf_nfe.get("det", [])
            if isinstance(itens, dict):  # caso haja apenas 1 item
                itens = [itens]

            resultado = []
            for item in itens:
                prod = item.get("prod", {})
                imposto = item.get("imposto", {})

                icms = next(iter(imposto.get("ICMS", {}).values()), {})
                pis = next(iter(imposto.get("PIS", {}).values()), {})
                cofins = next(iter(imposto.get("COFINS", {}).values()), {})

                item_extraido = {
                    **dados_comuns,
                    "codigo_produto": prod.get("cProd", ""),
                    "descricao_produto": prod.get("xProd", ""),
                    "cfop": prod.get("CFOP", ""),
                    "quantidade_comercial": prod.get("qCom", ""),
                    "unidade_comercial": prod.get("uCom", ""),
                    "valor_unitario": prod.get("vUnCom", ""),
                    "valor_total_item": prod.get("vProd", ""),

                    "icms_valor": icms.get("vICMS", ""),
                    "pis_valor": pis.get("vPIS", ""),
                    "cofins_valor": cofins.get("vCOFINS", "")
                }

                resultado.append(item_extraido)

            return resultado or [dados_comuns]
            
        except Exception as e:
            return [{
                'numero_nf': 'ERRO',
                'data_emissao': '2025-01-01',
                'emitente': f'Erro: {str(e)[:50]}',
                'erro': str(e)
            }]
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = {"status": "ok", "message": "Datarum API Online", "timestamp": datetime.now().isoformat()}
        self.wfile.write(json.dumps(response).encode())
    
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length) if content_length > 0 else b''
        
        if 'processar-info' in self.path:
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', '*')
            self.end_headers()
            
            try:
                # Extrair boundary do Content-Type
                content_type = self.headers.get('Content-Type', '')
                boundary = None
                if 'multipart/form-data' in content_type:
                    boundary_start = content_type.find('boundary=')
                    if boundary_start != -1:
                        boundary = content_type[boundary_start + 9:].strip()
                
                todos_dados = []
                stats = {'processados': 0, 'itens': 0, 'notas': [], 'emitentes': set(), 'valor_total': 0.0}
                
                if boundary and post_data:
                    arquivos_xml = self.parse_multipart(post_data, boundary)
                    
                    for arquivo in arquivos_xml:
                        dados_nfe = self.processar_xml(arquivo['content'])
                        if dados_nfe:
                            todos_dados.extend(dados_nfe)
                            stats['processados'] += 1
                            stats['itens'] += len(dados_nfe)
                            
                            for item in dados_nfe:
                                if item.get('numero_nf'):
                                    stats['notas'].append(item['numero_nf'])
                                if item.get('emitente'):
                                    stats['emitentes'].add(item['emitente'])
                                if item.get('valor_total_item'):
                                    try:
                                        valor = float(str(item['valor_total_item']).replace(',', '.'))
                                        stats['valor_total'] += valor
                                    except:
                                        pass
                
                # Salvar no cache global (simplificado)
                globals()['cache_dados'] = todos_dados
                
                response = {
                    'message': 'Processamento concluído!',
                    'arquivos_processados': stats['processados'],
                    'itens_processados': stats['itens'],
                    'notas_encontradas': list(stats['notas'])[:10],
                    'emitentes': list(stats['emitentes'])[:10],
                    'valor_total': round(stats['valor_total'], 2),
                    'session_id': f"session_{stats['processados']}",
                    'planilha_destino': 'datarum_processamento.xlsx'
                }
                
            except Exception as e:
                response = {'message': f'Erro: {str(e)}', 'erro': True}
            
            self.wfile.write(json.dumps(response).encode())
        
        elif 'processar' in self.path:
            self.send_response(200)
            self.send_header('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Disposition', 'attachment; filename=datarum_processamento.xlsx')
            self.end_headers()
            
            try:
                import sys
                import os
                import tempfile
                
                # Adicionar o diretório backend ao path para importar utils
                backend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)))
                if backend_path not in sys.path:
                    sys.path.append(backend_path)
                
                from utils.excel_handler import salvar_em_excel
                
                # Buscar dados do cache
                dados = globals().get('cache_dados', [])
                
                if not dados:
                    # Se não houver dados, retornar erro
                    self.send_response(400)
                    self.send_header('Content-Type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    
                    error_response = {
                        'message': 'Nenhum dado para processar. Faça upload dos XMLs primeiro.',
                        'erro': True
                    }
                    self.wfile.write(json.dumps(error_response).encode())
                    return
                
                # Criar arquivo temporário
                with tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx') as tmp_file:
                    tmp_path = tmp_file.name
                
                # Usar a função do utils para salvar em Excel
                num_linhas = salvar_em_excel(dados, tmp_path)
                
                # Ler arquivo e enviar
                with open(tmp_path, 'rb') as f:
                    excel_content = f.read()
                
                # Limpar arquivo temporário
                os.unlink(tmp_path)
                
                self.wfile.write(excel_content)
                
            except Exception as e:
                # Em caso de erro, fallback para CSV
                self.send_response(200)
                self.send_header('Content-Type', 'text/csv; charset=utf-8')
                self.send_header('Content-Disposition', 'attachment; filename=datarum_erro.csv')
                
                error_csv = f'Erro,{str(e)}\nContate o suporte,suporte@datarum.com.br'
                self.wfile.write(error_csv.encode('utf-8'))
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', '*')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.end_headers()

# Cache global simples
cache_dados = []
