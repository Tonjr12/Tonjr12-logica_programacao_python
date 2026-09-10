# Solicita ao usuário o número para o cálculo da tabuada
numero = int(input('Digite um número para ver sua tabuada: '))

print('-' * 18)
print(f'TABUADA DO {numero}')
print('-' * 18)

# Laço for variando de 1 a 10
for c in range(1, 11):
    # Exibe o cálculo formatando a posição do multiplicador (c:2d ajusta o alinhamento)
    print(f'{numero} x {c:2d} = {numero * c}')

print('-' * 18)