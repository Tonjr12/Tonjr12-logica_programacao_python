print('=' * 45)
print('PROCESSADOR FINANCEIRO - VERSÃO 9.0')
print('Recursos: Modularização, Validação de Dados e Try/Except')
print('-' * 45)


def calcular_estatisticas(lista):
    total = sum(t["reais"] for t in lista)
    media = total / len(lista) if lista else 0
    return total, media


def mostrando_posicao(lista):
    if len(lista) > 0:
        for pos, item in enumerate(lista, start=1):
            print(f'{pos:02d}° | {item["descricao"]:<20} | {item["categoria"]:<12} | R$ {item["reais"]:8.2f}')


def ler_transacao():
    # Exemplo de validação para não aceitar texto em branco:
    while True:
        descricao = input('Digite o nome do estabelecimento: ').strip().title()
        if descricao != '':
            break
        print('❌ Ops! O nome não pode ficar em branco.')

    while True:
        try:
            valor = float(input('Digite o valor do gasto: '))
            if valor <= 0:
                print('❌ Ops! O valor deve ser maior que zero')
            else:
                print('Valor registrado com sucesso!')
                break
        except ValueError:
            print('❌ Ops! Digite um valor numérico válido (ex: 25.50).')

    while True:
        categoria = input('Digite a categoria do estabelecimento: ').strip().title()
        if categoria != '':
            break
        print('❌ Ops! A categoria não pode ficar em branco.')   
    return {
        'descricao': descricao,
        'reais': valor,
        'categoria': categoria
    }


transacoes = []

while True:

    item = ler_transacao()  # A função faz as perguntas e devolve o dicionário
    transacoes.append(item)  # Adiciona na lista principal

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]

    if continuar == 'N':
        break

print('\n' + '=' * 55)
print('                 EXTRATO DETALHADO                  ')
print('=' * 55)

mostrando_posicao(transacoes)

tot, media = calcular_estatisticas(transacoes)
# Imprime o resumo final UMA ÚNICA VEZ (sem o loop 'for')
print('-' * 55)
print(f'TOTAL DOS LANÇAMENTOS: R$ {tot:.2f}')
print(f'MÉDIA POR LANÇAMENTO:  R$ {media:.2f}')
print('=' * 55)



















