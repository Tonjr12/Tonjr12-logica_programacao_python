# Inicializa as variáveis de controle (soma, contador e os números)
soma = 0
cont = 0
n = 0

# Lê o primeiro número antes de entrar no laço (condição de parada / flag)
n = int(input('Digite um número [999 para parar]: '))

# Laço principal executado enquanto o número digitado for diferente de 999
while n != 999:
    soma += n  # Acumula a soma dos valores
    cont += 1  # Incrementa o contador de números válidos

    # Se for o primeiro número digitado, ele é automaticamente o maior e o menor
    if cont == 1:
        menor = n
        maior = n
    else:
        # A partir do segundo número, compara para atualizar o maior ou o menor
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    # Solicita o próximo número
    n = int(input('Digite um número [999 para parar]: '))

# Valida se pelo menos um número foi digitado para calcular a média
if cont > 0:
    media = soma / cont
    print(f'A média dos valores é {media}, o menor valor é {menor} e o maior valor é {maior}.')
else:
    print('Nenhum valor válido foi digitado.')