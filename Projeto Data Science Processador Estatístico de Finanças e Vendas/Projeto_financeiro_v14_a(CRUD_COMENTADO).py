# Importa a biblioteca nativa do Python para trabalhar com arquivos no formato JSON (gravação e leitura de dados)
import json
import unicodedata
# Imprime linhas de separação e o título do programa no terminal
print('=' * 45)
print('-' * 45)
print('Processador Financeiro - Versão 14.0')

def normalizar(texto):
    # Remove acentos e converte para minúsculas
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn').lower()

# Define a função responsável por ler os dados salvos no arquivo JSON
def carregar_dados(nome_arquivo='transacoes.json'):
    try:
        # Tenta abrir o arquivo no modo de leitura ('r' = read)
        with open(nome_arquivo, 'r') as arq:
            # Converte o conteúdo do arquivo JSON de volta para uma lista de dicionários no Python
            return json.load(arq)
    except FileNotFoundError:
        # Se o arquivo ainda não existir no disco (ex: 1ª execução), retorna uma lista vazia
        return []


# Define a função responsável por gravar os dados da memória RAM no disco
def salvar_dados(lista, nome_arquivo='transacoes.json'):
    # Abre (ou cria) o arquivo no modo de escrita ('w' = write), sobrescrevendo o conteúdo anterior
    with open(nome_arquivo, 'w') as arq:
        # Converte a lista do Python para texto no formato JSON e salva no arquivo (indent=4 formata organizadamente)
        json.dump(lista, arq, indent=4)


# Define a função para remover um lançamento cadastrado
# Define a função para remover um lançamento cadastrado
def remover_transacao(lista):
    # Verifica se a lista está vazia
    if len(lista) == 0:
        print('\n⚠️ Nenhuma transação registrada para remover!')
        return  # Encerra a função mais cedo se não houver dados

    # Exibe o extrato numerado para o usuário ver quais opções existem
    mostrando_posicao(lista)
    print('[ 0 ] Cancelar exclusão')  # Opção clara de saída

    # Loop para garantir que o usuário digite uma opção válida
    while True:
        try:
            # Pede o número do item exibido na tela ou 0 para sair
            entrada = input('\nDigite o número da transação que deseja apagar (ou 0 para cancelar): ').strip()

            # Se o usuário apertar Enter ou digitar 0, cancelamos a operação
            if entrada == '' or entrada == '0':
                print('\n⚠️ Operação de exclusão cancelada.')
                return

            posicao = int(entrada)

            # Trava de segurança: garante que o número digitado está no intervalo válido da lista
            if 1 <= posicao <= len(lista):
                # Remove o item da lista ajustando o índice
                removido = lista.pop(posicao - 1)
                # Exibe a confirmação contendo o nome e valor do item que foi apagado
                print(f"\n✅ Transação '{removido['descricao']}' no valor de R$ {removido['reais']:.2f} foi removida!")
                break  # Sai do loop de validação após remover com sucesso
            else:
                # Alerta caso o usuário digite um número fora da faixa existente
                print(f'❌ Opção inválida! Digite um número de 1 a {len(lista)} (ou 0 para cancelar).')

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
        # Usamos <4 para o N° bater exatamente com a largura do "01°" (4 caracteres)
        print(f'{"N°":<4} | {"Estabelecimento":<20} | {"Categoria":<12} | {"Valor"}')
        print('-' * 56)  # Linha separadora ajustada

        # 'enumerate(..., start=1)' gera a numeração de 1 em 1 para a visualização do usuário
        for pos, ITEM in enumerate(lista, start=1):
            # Formata cada linha com alinhamentos fixos
            print(f'{pos:02d}° | {ITEM["descricao"]:<20} | {ITEM["categoria"]:<13} | R$ {ITEM["reais"]:8.2f}')


# Define a função para cadastrar e validar uma nova transação individual
def ler_transacao():
    print('\n--- CADASTRO DE TRANSAÇÃO (Digite 0 a qualquer momento para cancelar) ---')

    # Loop de validação do nome do estabelecimento
    while True:
        descricao = input('Digite o nome do estabelecimento (ou 0 para cancelar): ').strip()
        if descricao == '0':
            print('\n⚠️ Operação de cadastro cancelada.')
            return None  # Retorna 'None' indicando que foi cancelado
        if descricao != '':
            descricao = descricao.title()
            break  # Nome válido aceito
        print('❌ Ops! O nome não pode ficar em branco.')

    # Loop de validação do valor do gasto
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
                break  # Valor válido aceito
        except ValueError:
            print('❌ Ops! Digite um valor numérico válido (ex: 25.50).')

    # Loop de validação da categoria
    while True:
        categoria = input('Digite a categoria do estabelecimento (ou 0 para cancelar): ').strip()
        if categoria == '0':
            print('\n⚠️ Operação de cadastro cancelada.')
            return None

        if categoria != '':
            categoria = categoria.title()
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

    # Captura o termo de busca digitado pelo usuário
    busca = input('\nDigite a categoria que deseja buscar: ').strip()
    busca_limpa = normalizar(busca)

    # Filtra comparando os textos normalizados (sem acento, tudo minúsculo e aceitando pedaços da palavra)
    filtrados = [t for t in lista if busca_limpa in normalizar(t['categoria'])]

    # Se a lista filtrada estiver vazia
    if len(filtrados) == 0:
        print(f'\n⚠️ Nenhuma transação encontrada para "{busca}".')
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


# ==============================================================================
# --- PROGRAMA PRINCIPAL ---
# ==============================================================================

# Executa o carregamento inicial dos dados salvos do disco para a memória RAM
transacao = carregar_dados()

# Loop principal de funcionamento do programa financeiro
while True:
    # Exibe o menu e aguarda a escolha válida do usuário
    opcao = exibir_menu()

    # Opção 1: Cadastrar
    if opcao == '1':
        item = ler_transacao()  # Coleta os dados digitados ou retorna None se cancelado

        # Só salva se o usuário não tiver cancelado (ou seja, se 'item' não for None)
        if item is not None:
            transacao.append(item)  # Insere o novo dicionário na lista da memória RAM
            salvar_dados(transacao)  # Grava a lista atualizada no disco rígido (JSON)
            print('💾 Transação salva com sucesso no disco!')

        input('\nPressione ENTER para voltar ao menu...')

    # Opção 2: Extrato Detalhado
    elif opcao == '2':
        if len(transacao) == 0:
            print('\n⚠️ Nenhuma Transação registrada!')
        else:
            mostrando_posicao(transacao)  # Exibe todos os lançamentos
        input('\nPressione ENTER para voltar ao menu...')

    # Opção 3: Estatísticas Gerais
    elif opcao == '3':
        if len(transacao) == 0:
            print('\n⚠️ Nenhuma Transação registrada!')
        else:
            total, media = calcular_estatisticas(transacao)  # Calcula total e média
            print('\n' + '=' * 45)
            print(f'TOTAL DOS LANÇAMENTOS: R$ {total:.2f}')
            print(f'MÉDIA POR LANÇAMENTO:  R$ {media:.2f}')
            print('-' * 45)
        input('\nPressione ENTER para voltar ao menu...')

    # Opção 4: Excluir
    elif opcao == '4':
        remover_transacao(transacao)  # Apaga da lista na memória RAM
        salvar_dados(transacao)       # Atualiza o arquivo no disco rígido
        input('\nPressione ENTER para voltar ao menu...')

    # Opção 5: Filtrar por Categoria
    elif opcao == '5':
        filtrar_por_categoria(transacao)  # Busca e exibe apenas a categoria desejada
        input('\nPressione ENTER para voltar ao menu...')

    # Opção 6: Relatório Sintético
    elif opcao == '6':
        gerar_relatorio_sintetico(transacao)  # Exibe os totais agrupados
        input('\nPressione ENTER para voltar ao menu...')

    # Opção 7: Editar Transação
    elif opcao == '7':
        editar_transacao(transacao)   # Atualiza os campos do lançamento selecionado
        salvar_dados(transacao)       # Grava as alterações permanentemente no JSON
        input('\nPressione ENTER para voltar ao menu...')

    # Opção 8: Sair
    elif opcao == '8':
        print('\nSaindo do Sistema... Até logo!')
        break  # Interrompe o loop principal e finaliza o programa