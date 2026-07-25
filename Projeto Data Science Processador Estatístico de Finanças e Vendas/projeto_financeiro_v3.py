tototalFaturamento = 0
totalTransacao = 0
menorVenda = 0
maiorVenda = 0
altoValor = 0
cadastrar = input("Deseja cadastrar uma venda? [S/N]: ").upper().strip()[0]
if cadastrar == "S":

    while cadastrar not in "N":
        venda = float(input("Digite o valor da venda:"))
        while venda <= 0:
            print('Digite um valor valido!')
            venda = float(input("Digite o valor da venda:"))
        if totalTransacao == 0:
            maiorVenda = venda
            menorVenda = venda
        else:
            if venda > maiorVenda:
                maiorVenda = venda
            elif venda < menorVenda:
                menorVenda = venda

        if venda > 100:
            altoValor +=1

        tototalFaturamento += venda
        totalTransacao += 1
        cadastrar = input("Deseja cadastrar uma nova venda? [S/N]").upper().strip()[0]

else:
    print('Cadastro não realizado!')

print(f'O faturamento total foi {tototalFaturamento}')
print(f'O total de vendas em faturamento foi {totalTransacao}')
print(f'O menor venda foi {menorVenda:,.2f}')
print(f'O maior venda foi {maiorVenda:,.2f}')
print(f'Vendas de Alto Valor (> R$ 100) = {altoValor} transações.')




