# Inicializa os acumuladores e contadores estatísticos
tot18 = 0
totH = 0
totM20 = 0

# Laço infinito para o cadastro contínuo de pessoas
while True:
    # Lê e valida o sexo do utilizador (garante apenas M ou F)
    sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        print('Sexo incorreto! Digite apenas M ou F.')
        sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()[0]

    # Lê a idade da pessoa
    idade = int(input('Digite a idade: '))

    # A) Conta pessoas com mais de 18 anos
    if idade > 18:
        tot18 += 1

    # B) Conta o total de homens cadastrados
    if sexo == 'M':
        totH += 1

    # C) Conta mulheres com menos de 20 anos
    if sexo == 'F' and idade < 20:
        totM20 += 1

    print('-' * 30)

    # Pergunta se o utilizador quer continuar e valida a resposta
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        print('Entrada inválida! Digite apenas S ou N.')
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    # Condição de parada do laço infinito
    if continuar == 'N':
        break

print('-' * 30)
# Exibe o relatório estatístico final
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de homens cadastrados: {totH}')
print(f'Total de mulheres com menos de 20 anos: {totM20}')