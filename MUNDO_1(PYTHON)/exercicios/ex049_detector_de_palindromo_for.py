# Remove os espaços do início/fim e converte a frase para maiúsculas
frase = str(input('Digite uma frase: ')).strip().upper()

# Divide a frase em uma lista de palavras para isolar os espaços internos
separar_em_palavras = frase.split()

# Junta todas as palavras sem nenhum espaço entre elas
juntar_palavras = ''.join(separar_em_palavras)

# Variável acumuladora para guardar o texto invertido
inverso_palavras = ''

# Percorre a string junta do último índice (len - 1) até o primeiro (0)
for letra in range(len(juntar_palavras) - 1, -1, -1):
    inverso_palavras += juntar_palavras[letra]

print(f'O inverso de {juntar_palavras} é {inverso_palavras}')

# Compara a palavra junta original com a sua versão invertida
if juntar_palavras == inverso_palavras:
    print('A frase é um PALÍNDROMO!')
else:
    print('A frase NÃO é um palíndromo!')