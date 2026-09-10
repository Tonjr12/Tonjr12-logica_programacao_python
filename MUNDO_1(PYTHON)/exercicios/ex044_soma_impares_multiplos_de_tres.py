# Inicializa os contadores e acumuladores zerados
soma = 0
cont = 0

# Percorre o intervalo de 1 até 500 pulando de 2 em 2 (processa apenas números ímpares)
for c in range(1, 501, 2):
    # Verifica se o número ímpar também é múltiplo de 3
    if c % 3 == 0:
        cont += 1  # Incrementa a quantidade de números encontrados
        soma += c  # Acumula o valor do número na soma total

# Exibe o resultado consolidado
print(f'A soma de todos os {cont} valores solicitados é {soma}.')