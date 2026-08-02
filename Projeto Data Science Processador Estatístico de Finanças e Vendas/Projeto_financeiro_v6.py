print('=' * 45)
print('PROCESSADOR FINACEIRO - VERSÃO 6.0')
print('Recursos: Listas compostas,unpacking e Generator Expression')
print('-'*45)

transacoes = []
while True:
    descricao = input ('Digite o nome do estabelecimento: ').strip().title()
    valor = float(input ('Digite o valor do gasto: '))
    nota = [descricao, valor]

    transacoes.append(nota)

    continuar  = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]

    if continuar == 'N':
        break

if len(transacoes) > 0:
    for pos,(descricao,valor) in enumerate(transacoes):
        print(f'{pos+1:02d}° | {descricao:<25} | {valor:8.2f}')
total = sum(valor for descricao,valor in transacoes)
media = total / len(transacoes)if transacoes else 0

print(f"TOTAL DOS LANÇAMENTOS: R$ {total:.2f}")
print(f"MÉDIA POR LANÇAMENTO: R$ {media:.2f}")
print("=" * 45)