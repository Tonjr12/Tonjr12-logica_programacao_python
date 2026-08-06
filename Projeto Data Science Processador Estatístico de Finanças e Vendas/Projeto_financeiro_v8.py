print('=' * 45)
print('PROCESSADOR FINACEIRO - VERSÃO 8.0')
print('Recursos: Listas compostas,unpacking e Generator Expression')
print('-'*45)
def calcular_estatisticas(lista):
    total = sum(t["reais"] for t in lista)
    media = total / len(lista) if lista else 0
    return total, media
def mostrando_posicao(lista):
    if len(lista) > 0:
        for pos, item in enumerate(lista, start=1):
            print(f'{pos:02d}° | {item["descricao"]:<20} | {item["categoria"]:<12} | R$ {item["reais"]:8.2f}')

def ler_transacao():
    descricao = input('Digite o nome do estabelecimento: ').strip().title()
    valor = float(input('Digite o valor do gasto: '))
    categoria = input('Digite o categoria do estabelecimento: ')
    return{
        'descricao': descricao,
        'reais': valor,
        'categoria': categoria
    }

transacoes = []

while True:

    item = ler_transacao()  # A função faz as perguntas e devolve o dicionário
    transacoes.append(item)  # Adiciona na lista principal

    continuar  = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]

    if continuar == 'N':
        break

print('\n' + '=' * 55)
print('                 EXTRATO DETALHADO                  ')
print('=' * 55)

mostrando_posicao(transacoes)


tot,media = calcular_estatisticas(transacoes)
# Imprime o resumo final UMA ÚNICA VEZ (sem o loop 'for')
print('-' * 55)
print(f'TOTAL DOS LANÇAMENTOS: R$ {tot:.2f}')
print(f'MÉDIA POR LANÇAMENTO:  R$ {media:.2f}')
print('=' * 55)



'''# Exibição dos dados acessando as chaves do dicionário
if len(transacoes) > 0:
    for pos, item in enumerate(transacoes, start=1):
        print(f'{pos:02d}° | {item["descricao"]:<20} | {item["categoria"]:<12} | R$ {item["reais"]:8.2f}')


# Generator Expression extraindo o 'valor' de cada dicionário 't'
total = sum(t["reais"] for t in transacoes)
media = total / len(transacoes) if transacoes else 0

print('-' * 55)
print(f"TOTAL DOS LANÇAMENTOS: R$ {total:.2f}")
print(f"MÉDIA POR LANÇAMENTO:  R$ {media:.2f}")
print("=" * 55)'''