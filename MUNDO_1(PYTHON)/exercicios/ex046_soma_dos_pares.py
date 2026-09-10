# Inicializa o acumulador da soma e o contador de pares
soma = 0
cont = 0

# Repete a leitura 6 vezes
for c in range(1, 7):
    numero = int(input(f'Digite o {c}º número inteiro: '))
    # Filtra apenas os números pares
    if numero % 2 == 0:
        soma += numero
        cont += 1

# Exibe o relatório final com os totais contabilizados
print(f'Você informou {cont} número(s) PAR(ES) e a soma foi {soma}.')