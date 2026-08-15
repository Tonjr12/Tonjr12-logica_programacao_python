# Solicita um número inteiro ao usuário e converte o texto para o tipo inteiros (int)
numero = int(input('Digite um número: '))

# Calcula o antecessor subtraindo 1 do número digitado
antecessor = numero - 1

# Calcula o sucessor somando 1 ao número digitado
sucessor = numero + 1

# Calcula o dobro multiplicando o número por 2
dobro = numero * 2

# Calcula o triplo multiplicando o número por 3
triplo = numero * 3

# Calcula a raiz quadrada elevando o número a 0.5
raiz = numero ** 0.5

# Exibe na tela todos os resultados organizados e formatados
print(f'Analisando o valor {numero}:')
print(f'O antecessor é: {antecessor}')
print(f'O sucessor é: {sucessor}')
print(f'O dobro é: {dobro}')
print(f'O triplo é: {triplo}')
print(f'A raiz quadrada é: {raiz:.2f}')