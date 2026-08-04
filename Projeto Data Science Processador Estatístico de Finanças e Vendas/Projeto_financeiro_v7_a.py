print('=' * 45)
print('PROCESSADOR FINACEIRO - VERSÃO 7.0_a')
print('Recursos: Listas compostas,unpacking e Generator Expression')
print('-'*45)

transacoes = []
while True:
    descricao = input ('Digite o nome do estabelecimento: ').strip().title()
    valor = float(input ('Digite o valor do gasto: '))
    produto = input('Digite a descrição do produto: ').strip().title()
    nota = {
        'descricao': descricao,
        'valor': valor,
        'produto': produto
    }

    transacoes.append(nota)

    continuar  = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]

    if continuar == 'N':
        break

if len(transacoes) > 0:
    for pos,nota in enumerate(transacoes):
        print(f'{pos+1:02d}° | {nota["descricao"]:<20} |{nota["produto"]:<15} | {nota["valor"]:8.2f}')
total = sum(t["valor"] for t in transacoes)
media = total / len(transacoes)if transacoes else 0

print(f"TOTAL DOS LANÇAMENTOS: R$ {total:.2f}")
print(f"MÉDIA POR LANÇAMENTO: R$ {media:.2f}")
print("=" * 45)