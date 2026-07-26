venda = []
maior_venda = []

while True:
    valor = float(input('Digite o valor do produto: '))
    while valor <= 0:
        valor = float(input('(ERRO!) Digite o valor do produto: '))
        
    if valor > 0:
        venda.append(valor)

    if valor > 100:
        maior_venda.append(valor)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja cadastrar outra transação? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break

if len(venda) > 0:
    media = sum(venda) / len(venda)
    print(f'Total de transações: {len(venda)} venda(s)')
    print(f'Faturamento total: {sum(venda):.2f} ')
    print(f'Maior venda: {max(venda):.2f} ')
    print(f'Menor venda: {min(venda):.2f} ')
    print(f'O ticket médio foi: {media:} ')
    print(f'Vendas de alto valor: {len(maior_venda)} venda(s) e os valores foram: {maior_venda} ')
else:
    print('Nenhum Transação cadastrada')


