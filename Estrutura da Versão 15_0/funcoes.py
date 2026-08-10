# Define a função para remover um lançamento cadastrado
def remover_transacao(lista):
    # Verifica se a lista está vazia
    if len(lista) == 0:
        print('\n⚠️ Nenhuma transação registrada para remover!')
        return  # Encerra a função mais cedo se não houver dados

    # Exibe o extrato numerado para o usuário ver quais opções existem
    mostrando_posicao(lista)

    # Loop para garantir que o usuário digite uma opção válida
    while True:
        try:
            # Pede o número do item exibido na tela e converte para número inteiro
            posicao = int(input('\nDigite o número da transação que deseja apagar: '))

            # Trava de segurança: garante que o número digitado está no intervalo válido da lista (1 até o total de itens)
            if 1 <= posicao <= len(lista):
                # Remove o item da lista ajustando o índice (o Python começa a contar do 0, por isso 'posicao - 1')
                removido = lista.pop(posicao - 1)
                # Exibe a confirmação contendo o nome e valor do item que foi apagado
                print(f"\n✅ Transação '{removido['descricao']}' no valor de R$ {removido['reais']:.2f} foi removida!")
                break  # Sai do loop de validação após remover com sucesso
            else:
                # Alerta caso o usuário digite um número fora da faixa existente
                print(f'❌ Opção inválida! Digite um número de 1 a {len(lista)}.')

        except ValueError:
            # Captura o erro caso o usuário digite texto/letras em vez de números inteiros
            print('❌ Ops! Digite apenas números inteiros.')


# Define a função para editar uma transação existente (Update do CRUD)
def editar_transacao(lista):
    # Verifica se há itens cadastrados para editar
    if len(lista) == 0:
        print('\n⚠️ Nenhuma transação registrada para editar!')
        return  # Encerra a função

    print('\n--- EDIÇÃO DE TRANSAÇÃO ---')
    # Exibe o extrato numerado
    mostrando_posicao(lista)

    # Loop para escolha do número do item a ser editado
    while True:
        try:
            # Captura a posição desejada pelo usuário
            posicao = int(input('\nDigite o número da transação que deseja alterar: '))

            # Catraca de segurança verificando se a posição existe na lista
            if 1 <= posicao <= len(lista):
                # Acessa diretamente o dicionário na posição indicada (convertendo para índice do Python)
                items = lista[posicao - 1]

                # Exibe o submenu com os dados atuais do item selecionado
                print(f"\n--- O QUE VOCÊ DESEJA ALTERAR EM '{items['descricao']}'? ---")
                print(f"[ 1 ] Descrição atual: {items['descricao']}")
                print(f"[ 2 ] Valor atual: R$ {items['reais']:.2f}")
                print(f"[ 3 ] Categoria atual: {items['categoria']}")
                print("[ 4 ] Cancelar alteração")

                # Lê a opção escolhida no submenu
                opcao_edicao = input('Digite a opção desejada (1-4): ').strip()

                # Opção 1: Alterar apenas a descrição
                if opcao_edicao == '1':
                    nova_desc = input('Digite a nova descrição: ').strip().title()
                    # Garante que não salvou um texto em branco
                    if nova_desc != '':
                        items['descricao'] = nova_desc  # Atualiza a chave 'descricao'
                        print('✅ Descrição alterada com sucesso!')

                # Opção 2: Alterar apenas o valor
                elif opcao_edicao == '2':
                    # Loop de validação para o novo valor
                    while True:
                        try:
                            novo_valor = float(input('Digite o novo valor: R$ '))
                            if novo_valor > 0:
                                items['reais'] = novo_valor  # Atualiza a chave 'reais'
                                print('✅ Valor alterado com sucesso!')
                                break  # Sai do loop do valor
                            else:
                                print('❌ O valor deve ser maior que zero.')
                        except ValueError:
                            print('❌ Digite um valor numérico válido.')

                # Opção 3: Alterar apenas a categoria
                elif opcao_edicao == '3':
                    nova_cat = input('Digite a nova categoria: ').strip().title()
                    if nova_cat != '':
                        items['categoria'] = nova_cat  # Atualiza a chave 'categoria'
                        print('✅ Categoria alterada com sucesso!')

                # Opção 4: Desistir da edição
                elif opcao_edicao == '4':
                    print('⚠️ Edição cancelada.')

                else:
                    print('❌ Opção de edição inválida!')

                break  # Sai do loop principal de seleção da posição

            else:
                print(f'❌ Opção inválida! Digite um número de 1 a {len(lista)}.')

        except ValueError:
            print('❌ Ops! Digite apenas números inteiros.')


# Define a função para calcular o total financeiro e a média dos gastos
def calcular_estatisticas(lista):
    # Soma o campo 'reais' de cada dicionário 't' contido na lista de transações
    tot = sum(t["reais"] for t in lista)
    # Calcula a média dividindo pelo total de itens (se a lista não estiver vazia)
    med = tot / len(lista) if lista else 0
    # Retorna os dois valores calculados (uma tupla com total e média)
    return tot, med


# Define a função responsável por formatar e exibir as transações na tela
def mostrando_posicao(lista):
    if len(lista) > 0:
        # 'enumerate(..., start=1)' gera a numeração de 1 em 1 para a visualização do usuário
        for pos, ITEM in enumerate(lista, start=1):
            # Formata cada linha com alinhamentos fixos (<20 alinha a esquerda com 20 espaços, :8.2f formata moeda)
            print(f'{pos:02d}° | {ITEM["descricao"]:<20} | {ITEM["categoria"]:<12} | R$ {ITEM["reais"]:8.2f}')


# Define a função para cadastrar e validar uma nova transação individual
def ler_transacao():
    # Loop de validação do nome do estabelecimento (não aceita texto em branco)
    while True:
        descricao = input('Digite o nome do estabelecimento: ').strip().title()
        if descricao != '':
            break  # Nome válido aceito
        print('❌ Ops! O nome não pode ficar em branco.')

    # Loop de validação do valor do gasto
    while True:
        try:
            valor = float(input('Digite o valor do gasto: R$ '))
            if valor <= 0:
                print('❌ Ops! O valor deve ser maior que zero.')
            else:
                print('✅ Valor registrado com sucesso!')
                break  # Valor válido aceito
        except ValueError:
            print('❌ Ops! Digite um valor numérico válido (ex: 25.50).')

    # Loop de validação da categoria
    while True:
        categoria = input('Digite a categoria do estabelecimento: ').strip().title()
        if categoria != '':
            break  # Categoria válida aceita
        print('❌ Ops! A categoria não pode ficar em branco.')

    # Retorna a transação estruturada como um dicionário Python
    return {
        'descricao': descricao,
        'reais': valor,
        'categoria': categoria
    }


# Define a função para filtrar transações por uma categoria específica
def filtrar_por_categoria(lista):
    if len(lista) == 0:
        print('\n⚠️ Nenhuma transação registrada para filtrar!')
        return

    # Captura o termo de busca convertendo para minúsculas para ignorar maiúsculas/minúsculas
    busca = input('\nDigite a categoria que deseja buscar: ').strip().lower()

    # Cria uma nova lista contendo apenas os itens cuja categoria seja igual ao termo buscado
    filtrados = [t for t in lista if t['categoria'].lower() == busca]

    # Se a lista filtrada estiver vazia
    if len(filtrados) == 0:
        print(f'\n⚠️ Nenhuma transação encontrada para a categoria "{busca.title()}".')
    else:
        # Exibe o cabeçalho do filtro e reutiliza a função mostrando_posicao para a sublista
        print(f'\n--- EXTRATO FILTRADO: {busca.title()} ---')
        mostrando_posicao(filtrados)

        # Soma e exibe o gasto total específico dessa categoria
        tot = sum(t["reais"] for t in filtrados)
        print(f'\nTOTAL DA CATEGORIA: R$ {tot:.2f}')


# Define a função para agrupar e somar todos os gastos por categoria cadastrada
def gerar_relatorio_sintetico(lista):
    """Agrupa e soma todos os gastos divididos por cada categoria cadastrada."""
    if len(lista) == 0:
        print('\n⚠️ Nenhuma transação registrada para gerar relatório!')
        return

    # Dicionário acumulador (conceito das "caixas" por categoria)
    resumo_categorias = {}

    # Varre cada transação salva na lista principal
    for t in lista:
        cat = t['categoria']
        valor = t['reais']

        # Se a categoria já é uma chave no dicionário, soma o valor. Se não, cria a chave com o valor inicial.
        if cat in resumo_categorias:
            resumo_categorias[cat] += valor
        else:
            resumo_categorias[cat] = valor

    # Exibe a tabela consolidada
    print('\n' + '=' * 45)
    print('       RELATÓRIO SINTÉTICO POR CATEGORIA      ')
    print('=' * 45)
    # Percorre o dicionário acumulador exibindo a chave (cat) e a soma total acumulada (tot)
    for cat, tot in resumo_categorias.items():
        print(f'{cat:<20} | R$ {tot:8.2f}')
    print('=' * 45)


# Define a função que exibe o menu principal de navegação
def exibir_menu():
    # Loop contínuo para reexibir o menu caso haja erro de digitação
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

        # Captura a opção do usuário limpando espaços nas pontas
        opc = input('Digite uma Opção (1-8): ').strip()
        # Valida se a opção digitada é uma das permitidas
        if opc in ['1', '2', '3', '4', '5', '6', '7', '8']:
            return opc  # Retorna a opção escolhida e encerra o menu

        # Mensagem de erro e pausa para o usuário ler antes de redesenhar o menu
        input('\n❌ Opção inválida! Pressione ENTER para ver o menu novamente...')

