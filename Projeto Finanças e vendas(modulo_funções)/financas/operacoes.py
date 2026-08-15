from .arquivo import normalizar

def mostrando_posicao(lista):
    """Exibe o extrato detalhado em formato de tabela."""
    if len(lista) > 0:
        print(f'{"N°":<4} | {"Estabelecimento":<20} | {"Categoria":<12} | {"Valor"}')
        print('-' * 56)
        for pos, ITEM in enumerate(lista, start=1):
            print(f'{pos:02d}° | {ITEM["descricao"]:<20} | {ITEM["categoria"]:<13} | R$ {ITEM["reais"]:8.2f}')

def ler_transacao():
    """Cadastra uma nova transação validando os dados (permite cancelar digitando 0)."""
    print('\n--- CADASTRO DE TRANSAÇÃO (Digite 0 a qualquer momento para cancelar) ---')
    while True:
        descricao = input('Digite o nome do estabelecimento (ou 0 para cancelar): ').strip()
        if descricao == '0':
            print('\n⚠️ Operação de cadastro cancelada.')
            return None
        if descricao != '':
            descricao = descricao.title()
            break
        print('❌ Ops! O nome não pode ficar em branco.')

    while True:
        try:
            entrada_valor = input('Digite o valor do gasto: R$ ').strip()
            if entrada_valor == '0':
                print('\n⚠️ Operação de cadastro cancelada.')
                return None
            valor = float(entrada_valor)
            if valor <= 0:
                print('❌ Ops! O valor deve ser maior que zero.')
            else:
                print('✅ Valor registrado com sucesso!')
                break
        except ValueError:
            print('❌ Ops! Digite um valor numérico válido (ex: 25.50).')

    while True:
        categoria = input('Digite a categoria do estabelecimento (ou 0 para cancelar): ').strip()
        if categoria == '0':
            print('\n⚠️ Operação de cadastro cancelada.')
            return None
        if categoria != '':
            categoria = categoria.title()
            break
        print('❌ Ops! A categoria não pode ficar em branco.')

    return {
        'descricao': descricao,
        'reais': valor,
        'categoria': categoria
    }

def remover_transacao(lista):
    """Remove uma transação com base na posição escolhida (com opção de cancelar)."""
    if len(lista) == 0:
        print('\n⚠️ Nenhuma transação registrada para remover!')
        return

    mostrando_posicao(lista)
    print('[ 0 ] Cancelar exclusão')

    while True:
        try:
            entrada = input('\nDigite o número da transação que deseja apagar (ou 0 para cancelar): ').strip()
            if entrada == '' or entrada == '0':
                print('\n⚠️ Operação de exclusão cancelada.')
                return

            posicao = int(entrada)
            if 1 <= posicao <= len(lista):
                removido = lista.pop(posicao - 1)
                print(f"\n✅ Transação '{removido['descricao']}' no valor de R$ {removido['reais']:.2f} foi removida!")
                break
            else:
                print(f'❌ Opção inválida! Digite um número de 1 a {len(lista)} (ou 0 para cancelar).')
        except ValueError:
            print('❌ Ops! Digite apenas números inteiros.')

def editar_transacao(lista):
    """Permite editar descrição, valor ou categoria de uma transação existente."""
    if len(lista) == 0:
        print('\n⚠️ Nenhuma transação registrada para editar!')
        return

    print('\n--- EDIÇÃO DE TRANSAÇÃO ---')
    mostrando_posicao(lista)

    while True:
        try:
            posicao = int(input('\nDigite o número da transação que deseja alterar: '))
            if 1 <= posicao <= len(lista):
                items = lista[posicao - 1]
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
                break
            else:
                print(f'❌ Opção inválida! Digite um número de 1 a {len(lista)}.')
        except ValueError:
            print('❌ Ops! Digite apenas números inteiros.')

def calcular_estatisticas(lista):
    """Calcula o valor total e a média de gastos."""
    tot = sum(t["reais"] for t in lista)
    med = tot / len(lista) if lista else 0
    return tot, med

def filtrar_por_categoria(lista):
    """Filtra as transações por categoria (ignorando acentos e maiúsculas)."""
    if len(lista) == 0:
        print('\n⚠️ Nenhuma transação registrada para filtrar!')
        return

    busca = input('\nDigite a categoria que deseja buscar: ').strip()
    busca_limpa = normalizar(busca)
    filtrados = [t for t in lista if busca_limpa in normalizar(t['categoria'])]

    if len(filtrados) == 0:
        print(f'\n⚠️ Nenhuma transação encontrada para "{busca}".')
    else:
        print(f'\n--- EXTRATO FILTRADO: {busca.title()} ---')
        mostrando_posicao(filtrados)
        tot = sum(t["reais"] for t in filtrados)
        print(f'\nTOTAL DA CATEGORIA: R$ {tot:.2f}')

def gerar_relatorio_sintetico(lista):
    """Agrupa e soma todos os gastos divididos por cada categoria."""
    if len(lista) == 0:
        print('\n⚠️ Nenhuma transação registrada para gerar relatório!')
        return

    resumo_categorias = {}
    for t in lista:
        cat = t['categoria']
        valor = t['reais']
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