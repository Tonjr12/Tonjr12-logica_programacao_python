minhas_transacoes = [
    {'descricao':'mercado','valor':100},
    {'descricao':'padaria','valor':50}
]
outras_transacoes = [
    {'descricao':'mao de obra','valor':50},
    {'descricao':'peças','valor':40},
]

def calcular_trasacoes(lista):
    total = 0
    for t in lista:
        total += t['valor']
    #total = sum(t["valor"] for t in lista)
    media = total / len(lista) if lista else 0
    return total, media
tot, med = calcular_trasacoes(minhas_transacoes)
print(f'{tot:.2f}')
print(f'{med:.2f}')

print('='*30)

tot, med = calcular_trasacoes(outras_transacoes)
print(f'{tot:.2f}')
print(f'{med:.2f}')