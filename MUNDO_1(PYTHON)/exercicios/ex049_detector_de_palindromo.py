# Entrada de dados tratando espaços nas pontas e padronizando em maiúsculas
frase = str(input('Digite uma frase: ')).strip().upper()

# Divide a frase em palavras e junta tudo sem espaços internos
palavras = frase.split()
junto = ''.join(palavras)

inverso = ''

# Percorre a string junta de trás para frente usando o índice dos caracteres
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print(f'O inverso de {junto} é {inverso}')

# Verificação se a frase original sem espaços é igual ao seu inverso
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada NÃO É UM PALÍNDROMO!')