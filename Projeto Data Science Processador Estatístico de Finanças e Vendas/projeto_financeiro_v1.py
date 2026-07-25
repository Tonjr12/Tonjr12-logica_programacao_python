from rich import print
altoValor = 0
totalFaturamento = 0
for c in range(1,6):
    valorVenda = int(input('Qual o valor da venda:'))
    totalFaturamento += valorVenda
    if valorVenda > 100:
        altoValor += 1
print(f'Faturamento Total Bruto: A soma de todas as vendas válidas [red]R${totalFaturamento}[/red].')
print(f'Quantidade de Vendas de Alto Valor: O número de transações que foram acima de R$ 100: {altoValor} venda(s). ')
