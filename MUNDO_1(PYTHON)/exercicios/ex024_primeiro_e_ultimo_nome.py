# Exercício: Manipulação de Strings e Listas em Python
# Objetivo: Identificar o primeiro nome, último nome e total de elementos de uma lista.

# Recebe o nome completo e remove espaços desnecessários no início e no final (.strip)
nome_completo = input('Digite o nome completo: ').strip()

# Divide a string em palavras individuais usando os espaços como separador, criando uma lista (.split)
nome_fatiado = nome_completo.split()

# Exibe a lista gerada
print(f'Lista de nomes: {nome_fatiado}')

# Acessa o primeiro elemento da lista (índice 0) e o último elemento (índice -1)
print(f'O primeiro nome é: {nome_fatiado[0]}')
print(f'O último nome é: {nome_fatiado[-1]}')

# Utiliza a função len() para contar quantos itens (palavras/nomes) existem dentro da lista
total_nomes = len(nome_fatiado)
print(f'O total de nomes: {total_nomes}')