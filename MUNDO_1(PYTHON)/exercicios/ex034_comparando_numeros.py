# Solicita dois números inteiros ao usuário
num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))

# Compara os dois valores usando a estrutura if / elif / else
if num1 > num2:
    print('O PRIMEIRO valor é maior!')
elif num2 > num1:
    print('O SEGUNDO valor é maior!')
else:
    print('Não existe valor maior, os dois são IGUAIS!')