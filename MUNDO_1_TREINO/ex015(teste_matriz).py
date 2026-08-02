lancamento = []
for c in range(3):
    descricao = input('Digite o nome do estabelecimento: ').strip().title()
    valor = float(input('Digite o valor gasto: '))
    nota=[descricao,valor]
    lancamento.append(nota)
for pos,(descricao,valor) in enumerate(lancamento,start=1):
    print(f"{pos}º - Lançamento: {descricao:<15} | Valor: R$ {valor:.2f}")

