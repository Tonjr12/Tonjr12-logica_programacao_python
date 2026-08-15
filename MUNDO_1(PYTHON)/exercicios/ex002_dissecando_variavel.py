# Solicita qualquer entrada ao usuário e armazena na variável 'lendo_tipo'
lendo_tipo = input('Digite algo: ')

# Exibe o tipo primitivo da variável (como vem de um input simples, será <class 'str'>)
print(f'O tipo primitivo desse valor é: {type(lendo_tipo)}')

# Testa se a entrada é composta exclusivamente por espaços
print(f'Só tem espaços? {lendo_tipo.isspace()}')

# Testa se a entrada é composta apenas por números
print(f'É um número? {lendo_tipo.isnumeric()}')

# Testa se a entrada é composta apenas por letras
print(f'É alfabético? {lendo_tipo.isalpha()}')

# Testa se a entrada é alfanumérica (contém letras e/ou números)
print(f'É alfanumérico? {lendo_tipo.isalnum()}')

# Testa se todas as letras digitadas estão em maiúsculas
print(f'Está em maiúsculas? {lendo_tipo.isupper()}')

# Testa se todas as letras digitadas estão em minúsculas
print(f'Está em minúsculas? {lendo_tipo.islower()}')

# Testa se o texto está capitalizado (primeira letra maiúscula e o restante minúscula)
print(f'Está capitalizado? {lendo_tipo.istitle()}')