# Solicita ao usuário um número inteiro de 0 a 9999 e converte para int
num = int(input('Digite um número de 0 a 9999: '))

# Extrai a unidade, dezena, centena e milhar utilizando divisão inteira (//) e módulo (%)
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

# Exibe na tela os dígitos separados e identificados
print(f'Analisando o número {num}:')
print(f'Unidade: {unidade}')
print(f'Dezena:  {dezena}')
print(f'Centena: {centena}')
print(f'Milhar:  {milhar}')
print('-'*40)
unidade = num // 1
dezena = num // 10
centena = num // 100
milhar = num // 1000
print(f'Unidade: {unidade}')
print(f'Dezena:  {dezena}')
print(f'Centena:  {centena}')
print(f'Milhar:  {milhar}')

