# Inicializa as variáveis de controle (contador e acumulador de soma)
num = 0
cont = 0
soma = 0

# Lê o primeiro número antes de entrar no laço
num = int(input('Digite um número [999 para parar]: '))

# O laço executa continuamente enquanto o número digitado for diferente de 999 (flag)
while num != 999:
    soma += num  # Acumula o valor digitado na soma total
    cont += 1  # Incrementa +1 a cada número válido digitado

    # Lê o próximo número (se for 999, o laço será encerrado na próxima verificação)
    num = int(input('Digite um número [999 para parar]: '))

# Exibe o resultado final com a quantidade de números e a soma acumulada
print(f'Foram digitados {cont} números e a soma entre eles foi {soma}.')