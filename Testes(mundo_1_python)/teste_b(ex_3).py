produtos = {
    'Arroz':  25.90,
    'Feijão': 8.50,
    'Café':  14.00,
    'Leite': 5.20
}

""" no for o (indice) que vai aparecer no print é guiado pelo start=1 que esta no enumerate|| a (descrição) e o (valor) do print é guiado pelo (resultado que é o nome do dicionario ) || o (.items()que acompanha o dicionario é o serve pra mostrar a descrição e volor)  """
for indice, (produto,preco) in enumerate(produtos.items(),start=1):
    print(f'{indice}. {produto} R$: {preco:.2f}')
print('='*30)
# Como só vem a chave, usamos apenas UMA variável: produto
for indice, produto in enumerate(produtos.keys(), start=1):
    print(f'{indice}. Produto: {produto}')
print('='*30)
# Como só vem o valor, usamos apenas UMA variável: preco
for indice, preco in enumerate(produtos.values(), start=1):
    print(f'{indice}. Preço: R$ {preco:.2f}')