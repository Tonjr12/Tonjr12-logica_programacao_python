# Importa a biblioteca nativa do Python para trabalhar com arquivos no formato JSON (gravação e leitura de dados)
import json


# Define a função responsável por ler os dados salvos no arquivo JSON
def carregar_dados(nome_arquivo='transacoes.json'):
    try:
        # Tenta abrir o arquivo no modo de leitura ('r' = read)
        with open(nome_arquivo, 'r') as arq:
            # Converte o conteúdo do arquivo JSON de volta para uma lista de dicionários no Python
            return json.load(arq)
    except FileNotFoundError:
        # Se o arquivo ainda não existir no disco (ex: 1ª execução), retorna uma lista vazia
        return []


# Define a função responsável por gravar os dados da memória RAM no disco
def salvar_dados(lista, nome_arquivo='transacoes.json'):
    # Abre (ou cria) o arquivo no modo de escrita ('w' = write), sobrescrevendo o conteúdo anterior
    with open(nome_arquivo, 'w') as arq:
        # Converte a lista do Python para texto no formato JSON e salva no arquivo (indent=4 formata organizadamente)
        json.dump(lista, arq, indent=4)

