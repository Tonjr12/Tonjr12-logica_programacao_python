altoValor = 0
totalFaturamento = 0
for c in range(1,6):
    valorVenda = float(input('Digite Valor da Venda: '))
    totalFaturamento += valorVenda
    if valorVenda > 100:
        altoValor += 1

    if c == 1:
        maiorVenda = valorVenda
        menorVenda = valorVenda
    else:
        if valorVenda > maiorVenda:
            maiorVenda = valorVenda
        elif valorVenda < menorVenda:
            menorVenda = valorVenda
print(f'Faturamento Total foi de: R$ {totalFaturamento}')
print(f'Quantidade de vendas de alto valor foram: {altoValor} venda(s)')
print(f'Valor da Maior venda registrada foi de R$ {maiorVenda} ')
print(f'Valor da Menor venda registrada foi de R$ {menorVenda} ')

