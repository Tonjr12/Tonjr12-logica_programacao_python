# Importa apenas a função 'trunc' da biblioteca matemática 'math'
from math import trunc

# Solicita ao usuário um número real (float)
numero = float(input('Digite um número real/decimal: '))

# Extrai a porção inteira do número usando a função trunc()
porcao_inteira = trunc(numero)

# Exibe na tela o número original e sua respectiva parte inteira
print(f'O valor digitado foi {numero} e a sua porção inteira é {porcao_inteira}.')