# Entrada do número inteiro
numero = int(input('Digite um número: '))
cont = 0

# Validação inicial: números primos devem ser maiores que 1
if numero > 1:
    # Percorre de 1 até o próprio número
    for c in range(1, numero + 1):
        if numero % c == 0:
            cont += 1

    # Se for divisível apenas 2 vezes (por 1 e por ele mesmo), é primo
    if cont == 2:
        print(f'O número {numero} É PRIMO!')
        print(f'Pois foi divisível exatamente {cont} vezes.')
    else:
        print(f'O número {numero} NÃO É PRIMO!')
        print(f'Pois foi divisível {cont} vezes.')
else:
    print('O número NÃO É PRIMO pois é menor ou igual a 1.')