from http.server import BaseHTTPRequestHandler
import json
import urllib.parse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = {
            'message': 'Datarum API está funcionando!',
            'status': 'online',
            'path': self.path
        }
        
        self.wfile.write(json.dumps(response).encode('utf-8'))
        
    def do_POST(self):
        # Ler o path para determinar qual endpoint
        if 'processar-info' in self.path:
            # Endpoint de informações - retorna JSON
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', '*')
            self.end_headers()
            
            response = {
                'message': 'Processamento concluído!',
                'itens_processados': 15,
                'arquivos_processados': 3,
                'notas_encontradas': ['001', '002', '003'],
                'emitentes': ['Empresa ABC', 'Empresa XYZ'],
                'valor_total': 2500.50,
                'planilha_destino': 'teste.xlsx'
            }
            
            self.wfile.write(json.dumps(response).encode('utf-8'))
            
        elif self.path.endswith('/processar'):
            # Endpoint de download - simula retorno de Excel
            self.send_response(200)
            self.send_header('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Disposition', 'attachment; filename="teste.xlsx"')
            self.end_headers()
            
            # Retorna dados de um Excel simples (simulado)
            excel_data = b'PK\x03\x04' + b'EXCEL_SIMULADO' * 100  # Simula um arquivo Excel básico
            self.wfile.write(excel_data)
            
        else:
            # Outros endpoints
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {'message': 'Endpoint não encontrado', 'path': self.path}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.end_headers()
