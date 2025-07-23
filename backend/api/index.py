from http.server import BaseHTTPRequestHandler
import json
import urllib.parse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = {"status": "ok", "message": "API funcionando"}
        self.wfile.write(json.dumps(response).encode())
    
    def do_POST(self):
        if 'processar-info' in self.path:
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {
                "message": "Processamento OK",
                "arquivos_processados": 1,
                "itens_processados": 5,
                "notas_encontradas": ["NF000001"],
                "emitentes": ["Empresa Teste"],
                "valor_total": 1000.0
            }
            self.wfile.write(json.dumps(response).encode())
        
        elif 'processar' in self.path:
            self.send_response(200)
            self.send_header('Content-Type', 'text/csv')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Disposition', 'attachment; filename=resultado.csv')
            self.end_headers()
            
            csv_content = "Numero NF,Serie,Data,Emitente,Valor\n123456,1,2025-07-23,Empresa Teste,1000.00\n"
            self.wfile.write(csv_content.encode())
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', '*')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.end_headers()
