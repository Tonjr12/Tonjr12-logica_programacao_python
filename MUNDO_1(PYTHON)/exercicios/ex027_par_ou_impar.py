# Solicita um número inteiro ao usuário e converte a entrada para int
numero = int(input('Digite um número inteiro: '))

# Verifica se o resto da divisão do número por 2 é igual a zero
if numero % 2 == 0:
    print(f'O número {numero} é PAR!')
else:
    print(f'O número {numero} é ÍMPAR!')