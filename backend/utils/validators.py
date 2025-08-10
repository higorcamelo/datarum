"""
Funções utilitárias de validação para o sistema Sigonota
"""

import xml.etree.ElementTree as ET
from typing import Dict, Any


def validar_xml_nfe(xml_content: bytes, detalhado: bool = False) -> Dict[str, Any]:
    """
    Valida se o conteúdo XML é uma NFe válida
    
    Args:
        xml_content: Conteúdo do XML em bytes
        detalhado: Se deve retornar informações detalhadas
        
    Returns:
        Dict com status da validação e informações
    """
    try:
        # Tentar fazer parse do XML
        root = ET.fromstring(xml_content)
        
        # Verificar se é NFe
        if 'nfe' in root.tag.lower() or 'infnfe' in root.tag.lower():
            return {
                'valido': True,
                'tipo': 'NFe',
                'detalhes': 'XML NFe válido' if detalhado else None
            }
        
        # Buscar por elementos NFe nos filhos
        for child in root.iter():
            if 'nfe' in child.tag.lower() or 'infnfe' in child.tag.lower():
                return {
                    'valido': True,
                    'tipo': 'NFe',
                    'detalhes': 'XML NFe válido encontrado' if detalhado else None
                }
        
        return {
            'valido': False,
            'erro': 'XML não é uma NFe válida',
            'detalhes': f'Root tag: {root.tag}' if detalhado else None
        }
        
    except ET.ParseError as e:
        return {
            'valido': False,
            'erro': f'XML malformado: {str(e)}',
            'detalhes': str(e) if detalhado else None
        }
    except Exception as e:
        return {
            'valido': False,
            'erro': f'Erro na validação: {str(e)}',
            'detalhes': str(e) if detalhado else None
        }


def validar_tamanho_arquivo(tamanho: int, limite_mb: int = 5) -> Dict[str, Any]:
    """
    Valida se o tamanho do arquivo está dentro do limite
    
    Args:
        tamanho: Tamanho do arquivo em bytes
        limite_mb: Limite em MB (padrão: 5MB)
        
    Returns:
        Dict com status da validação
    """
    limite_bytes = limite_mb * 1024 * 1024
    
    if tamanho <= limite_bytes:
        return {
            'valido': True,
            'tamanho_mb': round(tamanho / (1024 * 1024), 2)
        }
    else:
        return {
            'valido': False,
            'erro': f'Arquivo muito grande. Limite: {limite_mb}MB',
            'tamanho_mb': round(tamanho / (1024 * 1024), 2)
        }


def contar_itens_xml(xml_content: bytes) -> int:
    """
    Conta o número de itens/produtos no XML da NFe
    
    Args:
        xml_content: Conteúdo do XML em bytes
        
    Returns:
        Número de itens encontrados
    """
    try:
        root = ET.fromstring(xml_content)
        
        # Buscar por elementos de itens (det, detalhamento, etc.)
        itens = []
        
        # Padrões comuns para itens em NFe
        patterns = ['det', 'detalhamento', 'item', 'produto']
        
        for pattern in patterns:
            elements = root.findall(f".//{pattern}")
            if elements:
                itens.extend(elements)
        
        # Se não encontrou nada, tentar busca mais ampla
        if not itens:
            for elem in root.iter():
                if 'det' in elem.tag.lower() and elem.attrib:
                    itens.append(elem)
        
        return len(itens)
        
    except Exception:
        return 0
