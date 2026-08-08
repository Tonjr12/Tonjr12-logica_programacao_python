print('=' * 45)
print('-' * 45)
print ('Processador Financeiro - Versão 10.0')

import json

def carregar_dados(nome_arquivo='transacoes.json'):
    try:
        with open(nome_arquivo, 'r') as arq:
            return json.load(arq)
    except FileNotFoundError:
        # Se o arquivo não existir ainda (1ª execução), retorna uma lista vazia
        return []

def salvar_dados(lista, nome_arquivo='transacoes.json'):
    with open(nome_arquivo, 'w') as arq:
        json.dump(lista, arq, indent=4)

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

def exibir_menu():
    print('=' * 45)
    print('-' * 45)
    print('          Processador Financeiro      ')
    print('='*45)
    print('[ 1 ] Cadastrar Nova Transação')
    print('[ 2 ] Exibir Extrato Detalhado')
    print('[ 3 ] Exibir Estatística (Total,Média)')
    print('[ 4 ] Sair do Sistema')
    print('='*45)
    print('-' * 45)
    while True:
        opcao =input('Digite uma Opção (1-4): ').strip()
        if opcao in ['1','2','3','4']:
            return opcao

        print('Opção invalida!')

#---Programa Principal---
transacao = carregar_dados()
while True:
    opcao = exibir_menu()
    if opcao == '1':
        item = ler_transacao()
        transacao.append(item)
        # Salva imediatamente no arquivo após adicionar
        salvar_dados(transacao)
        print('💾 Transação salva com sucesso no disco!')
        input('\nPressione ENTER para voltar ao menu...')  # 👈 Pausa para você ver o extrato com calma!
    elif opcao == '2':
        if len(transacao) == 0:
            print('\n⚠️ Nenhuma Transação registrada!')
        else:
            mostrando_posicao(transacao)
        input('\nPressione ENTER para voltar ao menu...')  # 👈 Pausa para você ver o extrato com calma!

    elif opcao == '3':
        if len(transacao) == 0:
            print('Nenhuma Transação registrada!')
        else:
            total, media = calcular_estatisticas(transacao)
            print('\n' + '='*45)
            print(f'TOTAL DOS LANÇAMENTOS: R$ {total:.2f}')
            print(f'MÉDIA POR LANÇAMENTO:  R$ {media:.2f}')
            print('-' * 45)
        input('\nPressione ENTER para voltar ao menu...')  # 👈 Pausa para você ver o extrato com calma!
    elif opcao == '4':
        print('Saindo do Sistema')
        break







