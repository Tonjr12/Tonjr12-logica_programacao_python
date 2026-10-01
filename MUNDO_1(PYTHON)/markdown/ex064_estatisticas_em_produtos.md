# Exercício 064 — Estatísticas em Produtos

* **Objetivo:** Ler o nome e o preço de vários produtos, permitindo continuar ou parar. No final, mostrar o total gasto, quantos produtos custam mais de R$ 1000 e o nome do produto mais barato.
* **Conceito Aplicado:** Laço `while True` com `break`, acumuladores de soma (`soma_total`), contadores condicionais (`produtos_1000`) e lógica de identificação do menor valor com rastreamento de nome.

### 💻 Código Solução

```python
soma_total = 0
produtos_1000 = 0
cont_produtos = 0
menor_preco = 0
produto_barato = ''

while True:
    nome = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$ '))
    
    soma_total += preco
    if preco > 1000:
        produtos_1000 += 1
        
    cont_produtos += 1
    if cont_produtos == 1 or preco < menor_preco:
        menor_preco = preco
        produto_barato = nome

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        
    if continuar == 'N':
        break

print(f'O total da compra foi R$ {soma_total:.2f}')
print(f'Temos {produtos_1000} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {produto_barato} que custou R$ {menor_preco:.2f}')