import sys
sys.path.append('.')
from utils.xml_parser import parse_nfe
import tempfile

xml = """<?xml version="1.0" encoding="UTF-8"?>
<nfeProc>
    <NFe>
        <infNFe>
            <ide><nNF>123</nNF></ide>
            <emit><xNome>Teste</xNome></emit>
            <dest><xNome>Dest</xNome></dest>
            <det><prod><xProd>Prod</xProd></prod></det>
        </infNFe>
    </NFe>
</nfeProc>"""

with tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False) as f:
    f.write(xml)
    temp_path = f.name

dados = parse_nfe(temp_path)
if dados:
    print("Campos disponíveis:")
    for key in sorted(dados[0].keys()):
        print(f"  {key}: {dados[0][key]}")
else:
    print("Nenhum dado retornado")
