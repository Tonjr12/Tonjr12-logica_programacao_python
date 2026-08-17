# Solicita o nome completo do usuário e remove espaços extras no início e no fim (.strip())
nome = input('Digite seu nome completo: ').strip()

# Converte todo o texto para letras maiúsculas
print(f'Seu nome em maiúsculas é {nome.upper()}')

# Converte todo o texto para letras minúsculas
print(f'Seu nome em minúsculas é {nome.lower()}')

# Calcula o total de letras subtraindo a quantidade de espaços em branco do tamanho total da string
tot_letras = len(nome) - nome.count(' ')
print(f'Seu nome tem ao todo {tot_letras} letras')

# Divide o nome completo em uma lista de palavras com base nos espaços
lista = nome.split()

# Exibe o primeiro nome e calcula a quantidade de letras dele usando len()
print(f'Seu primeiro nome é {lista[0]} e ele tem {len(lista[0])} letras')