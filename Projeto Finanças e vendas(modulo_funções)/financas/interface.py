def exibir_menu():
    """Exibe o menu principal de opções e valida a escolha do usuário."""
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
        if opc in ['1', '2', '3', '4', '5', '6', '7', '8']:
            return opc

        input('\n❌ Opção inválida! Pressione ENTER para ver o menu novamente...')