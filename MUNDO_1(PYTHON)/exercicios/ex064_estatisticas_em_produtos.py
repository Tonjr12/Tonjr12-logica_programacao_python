# Inicialização das variáveis
soma_total = 0
produtos_1000 = 0
cont_produtos = 0  # Contador para saber qual é o primeiro produto
menor_preco = 0  # Variável para armazenar o menor preço encontrado
produto_barato = ''  # Variável para armazenar o nome do produto mais barato

while True:
    # Lê os dados do produto
    nome = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Digite o valor do produto: R$ '))

    # 1. Soma o valor do produto ao total da compra
    soma_total += preco

    # 2. Conta se o produto custa mais de R$ 1000
    if preco > 1000:
        produtos_1000 += 1

    # Incrementa o contador de produtos cadastrados
    cont_produtos += 1

    # 3. Lógica para encontrar o produto mais barato
    if cont_produtos == 1:
        # Se for o primeiro produto, ele é o mais barato até agora
        menor_preco = preco
        produto_barato = nome
    else:
        # Se não for o primeiro, verifica se o preço atual é menor que o menor_preco guardado
        if preco < menor_preco:
            menor_preco = preco
            produto_barato = nome

    # Validação para continuar ou parar
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if continuar == 'N':
        print('\nFIM DO PROGRAMA')
        break

# Exibe os resultados formatados
print('-' * 40)
print(f'O total da compra foi R$ {soma_total:.2f}')
print(f'Temos {produtos_1000} produtos que custam mais de R$ 1000.00')
print(f'O produto mais barato foi {produto_barato} que custou R$ {menor_preco:.2f}')