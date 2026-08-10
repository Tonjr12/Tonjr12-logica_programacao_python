import json

print('=' * 45)
print('-' * 45)
print('Processador Financeiro - Versão 14.0')


def carregar_dados(nome_arquivo='transacoes.json'):
    try:
        with open(nome_arquivo, 'r') as arq:
            return json.load(arq)
    except FileNotFoundError:
        return []


def salvar_dados(lista, nome_arquivo='transacoes.json'):
    with open(nome_arquivo, 'w') as arq:
        json.dump(lista, arq, indent=4)


def remover_transacao(lista):
    if len(lista) == 0:
        print('\n⚠️ Nenhuma transação registrada para remover!')
        return

    mostrando_posicao(lista)

    while True:
        try:
            posicao = int(input('\nDigite o número da transação que deseja apagar: '))

            if 1 <= posicao <= len(lista):
                removido = lista.pop(posicao - 1)
                print(f"\n✅ Transação '{removido['descricao']}' no valor de R$ {removido['reais']:.2f} foi removida!")
                break
            else:
                print(f'❌ Opção inválida! Digite um número de 1 a {len(lista)}.')

        except ValueError:
            print('❌ Ops! Digite apenas números inteiros.')


def editar_transacao(lista):
    if len(lista) == 0:
        print('\n⚠️ Nenhuma transação registrada para editar!')
        return

    print('\n--- EDIÇÃO DE TRANSAÇÃO ---')
    mostrando_posicao(lista)

    while True:
        try:
            posicao = int(input('\nDigite o número da transação que deseja alterar: '))

            if 1 <= posicao <= len(lista):
                items = lista[posicao - 1]  # Acessa o dicionário escolhido

                print(f"\n--- O QUE VOCÊ DESEJA ALTERAR EM '{items['descricao']}'? ---")
                print(f"[ 1 ] Descrição atual: {items['descricao']}")
                print(f"[ 2 ] Valor atual: R$ {items['reais']:.2f}")
                print(f"[ 3 ] Categoria atual: {items['categoria']}")
                print("[ 4 ] Cancelar alteração")

                opcao_edicao = input('Digite a opção desejada (1-4): ').strip()

                if opcao_edicao == '1':
                    nova_desc = input('Digite a nova descrição: ').strip().title()
                    if nova_desc != '':
                        items['descricao'] = nova_desc
                        print('✅ Descrição alterada com sucesso!')

                elif opcao_edicao == '2':
                    while True:
                        try:
                            novo_valor = float(input('Digite o novo valor: R$ '))
                            if novo_valor > 0:
                                items['reais'] = novo_valor
                                print('✅ Valor alterado com sucesso!')
                                break
                            else:
                                print('❌ O valor deve ser maior que zero.')
                        except ValueError:
                            print('❌ Digite um valor numérico válido.')

                elif opcao_edicao == '3':
                    nova_cat = input('Digite a nova categoria: ').strip().title()
                    if nova_cat != '':
                        items['categoria'] = nova_cat
                        print('✅ Categoria alterada com sucesso!')

                elif opcao_edicao == '4':
                    print('⚠️ Edição cancelada.')

                else:
                    print('❌ Opção de edição inválida!')

                break  # Sai do 'loop' de posição

            else:
                print(f'❌ Opção inválida! Digite um número de 1 a {len(lista)}.')

        except ValueError:
            print('❌ Ops! Digite apenas números inteiros.')

def calcular_estatisticas(lista):
    tot = sum(t["reais"] for t in lista)
    med = tot / len(lista) if lista else 0
    return tot, med


def mostrando_posicao(lista):
    if len(lista) > 0:
        for pos, ITEM in enumerate(lista, start=1):
            print(f'{pos:02d}° | {ITEM["descricao"]:<20} | {ITEM["categoria"]:<12} | R$ {ITEM["reais"]:8.2f}')


def ler_transacao():
    while True:
        descricao = input('Digite o nome do estabelecimento: ').strip().title()
        if descricao != '':
            break
        print('❌ Ops! O nome não pode ficar em branco.')

    while True:
        try:
            valor = float(input('Digite o valor do gasto: R$ '))
            if valor <= 0:
                print('❌ Ops! O valor deve ser maior que zero.')
            else:
                print('✅ Valor registrado com sucesso!')
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


def filtrar_por_categoria(lista):
    if len(lista) == 0:
        print('\n⚠️ Nenhuma transação registrada para filtrar!')
        return

    busca = input('\nDigite a categoria que deseja buscar: ').strip().lower()

    filtrados = [t for t in lista if t['categoria'].lower() == busca]

    if len(filtrados) == 0:
        print(f'\n⚠️ Nenhuma transação encontrada para a categoria "{busca.title()}".')
    else:
        print(f'\n--- EXTRATO FILTRADO: {busca.title()} ---')
        mostrando_posicao(filtrados)

        tot = sum(t["reais"] for t in filtrados)
        print(f'\nTOTAL DA CATEGORIA: R$ {tot:.2f}')


def gerar_relatorio_sintetico(lista):
    """Agrupa e soma todos os gastos divididos por cada categoria cadastrada."""
    if len(lista) == 0:
        print('\n⚠️ Nenhuma transação registrada para gerar relatório!')
        return

    resumo_categorias = {}

    for t in lista:
        cat = t['categoria']
        valor = t['reais']

        # Aplica a lógica das caixas acumuladoras
        if cat in resumo_categorias:
            resumo_categorias[cat] += valor
        else:
            resumo_categorias[cat] = valor

    print('\n' + '=' * 45)
    print('       RELATÓRIO SINTÉTICO POR CATEGORIA      ')
    print('=' * 45)
    for cat, tot in resumo_categorias.items():
        print(f'{cat:<20} | R$ {tot:8.2f}')
    print('=' * 45)


def exibir_menu():
    while True:
        print('\n' + '=' * 45)
        print('          Processador Financeiro      ')
        print('=' * 45)
        print('[ 1 ] Cadastrar Nova Transação')
        print('[ 2 ] Exibir Extrato Detalhado')
        print('[ 3 ] Exibir Estatística (Total, Média)')
        print('[ 4 ] Excluir uma Transação')
        print('[ 5 ] Filtrar por Categoria')
        print('[ 6 ] Relatório Sintético por Categoria')
        print('[ 7 ] Editar transação')
        print('[ 8 ] Sair do Sistema')
        print('=' * 45)

        opc = input('Digite uma Opção (1-8): ').strip()
        if opc in ['1', '2', '3', '4', '5', '6', '7','8']:
            return opc

        input('\n❌ Opção inválida! Pressione ENTER para ver o menu novamente...')


# --- Programa Principal ---
transacao = carregar_dados()

while True:
    opcao = exibir_menu()

    if opcao == '1':
        item = ler_transacao()
        transacao.append(item)
        salvar_dados(transacao)
        print('💾 Transação salva com sucesso no disco!')
        input('\nPressione ENTER para voltar ao menu...')

    elif opcao == '2':
        if len(transacao) == 0:
            print('\n⚠️ Nenhuma Transação registrada!')
        else:
            mostrando_posicao(transacao)
        input('\nPressione ENTER para voltar ao menu...')

    elif opcao == '3':
        if len(transacao) == 0:
            print('\n⚠️ Nenhuma Transação registrada!')
        else:
            total, media = calcular_estatisticas(transacao)
            print('\n' + '=' * 45)
            print(f'TOTAL DOS LANÇAMENTOS: R$ {total:.2f}')
            print(f'MÉDIA POR LANÇAMENTO:  R$ {media:.2f}')
            print('-' * 45)
        input('\nPressione ENTER para voltar ao menu...')

    elif opcao == '4':
        remover_transacao(transacao)
        salvar_dados(transacao)
        input('\nPressione ENTER para voltar ao menu...')

    elif opcao == '5':
        filtrar_por_categoria(transacao)
        input('\nPressione ENTER para voltar ao menu...')

    elif opcao == '6':
        gerar_relatorio_sintetico(transacao)
        input('\nPressione ENTER para voltar ao menu...')


    elif opcao == '7':

        editar_transacao(transacao)

        salvar_dados(transacao)  # 💾 OBRIGATÓRIO: salva as alterações no JSON!

        input('\nPressione ENTER para voltar ao menu...')

    elif opcao == '8':
        print('\nSaindo do Sistema... Até logo!')
        break