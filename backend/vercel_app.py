def handler(event, context):
    """Handler simples que funciona no Vercel"""
    
    # Importar aqui dentro para evitar problemas de inicialização
    import json
    from urllib.parse import parse_qs
    
    # Verificar se é POST para processar-info
    method = event.get('httpMethod', event.get('requestContext', {}).get('http', {}).get('method', 'GET'))
    path = event.get('path', event.get('rawPath', ''))
    
    if method == 'POST' and 'processar-info' in path:
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
                'Access-Control-Allow-Headers': '*'
            },
            'body': json.dumps({
                'message': 'API funcionando!',
                'endpoint': 'processar-info',
                'method': method,
                'path': path
            })
        }
    
    # Endpoint raiz
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'message': 'Datarum API está funcionando!',
            'status': 'online'
        })
    }
