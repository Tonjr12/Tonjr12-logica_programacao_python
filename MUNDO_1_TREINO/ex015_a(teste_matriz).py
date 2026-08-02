lancamento = []
while True:
    descricao = input('Digite o nome do estabelecimento: ').strip().title()
    valor = float(input('Digite o valor gasto: '))
    nota=[descricao,valor]
    lancamento.append(nota)
    continuar = ' '
    while continuar not in 'SN':
        continuar= str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if continuar == 'N':
            break

for pos,(descricao,valor) in enumerate(lancamento,start=1):
    print(f"{pos}º - Lançamento: {descricao:<15} | Valor: R$ {valor:.2f}")

