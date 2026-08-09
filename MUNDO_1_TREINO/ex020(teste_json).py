import json

# 1. Criando uma lista simples
minha_lista = [{'item': 'Gasolina', 'valor': 50.0}]

# 2. Salvando no disco
with open('teste.json', 'w') as arq:
    json.dump(minha_lista, arq)

print("Arquivo 'teste.json' criado com sucesso!")

# 3. Lendo do disco
with open('teste.json', 'r') as arq:
    dados_lidos = json.load(arq)

print(f"Dados lidos do arquivo: {dados_lidos}")