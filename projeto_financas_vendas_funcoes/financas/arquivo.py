import json
import unicodedata

def normalizar(texto):
    """Remove acentos e converte o texto para minúsculas para facilitar buscas."""
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn').lower()

def carregar_dados(nome_arquivo='transacoes.json'):
    """Lê os dados salvos no arquivo JSON. Se não existir, retorna uma lista vazia."""
    try:
        with open(nome_arquivo, 'r') as arq:
            return json.load(arq)
    except FileNotFoundError:
        return []

def salvar_dados(lista, nome_arquivo='transacoes.json'):
    """Salva a lista atualizada de transações em formato JSON no disco."""
    with open(nome_arquivo, 'w') as arq:
        json.dump(lista, arq, indent=4)