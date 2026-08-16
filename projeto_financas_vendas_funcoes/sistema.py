# Importa as funções modulares do pacote financas
from financas.arquivo import carregar_dados, salvar_dados
from financas.interface import exibir_menu
from financas.operacoes import (
    mostrando_posicao, ler_transacao, remover_transacao,
    editar_transacao, calcular_estatisticas, filtrar_por_categoria,
    gerar_relatorio_sintetico
)

print('=' * 45)
print('-' * 45)
print('Processador Financeiro - Versão 14.0')

# Carrega os dados salvos no arquivo JSON para a memória RAM
transacao = carregar_dados()

# Loop principal de funcionamento do programa
while True:
    opcao = exibir_menu()

    # Opção 1: Cadastrar Nova Transação
    if opcao == '1':
        item = ler_transacao()
        if item is not None:
            transacao.append(item)
            salvar_dados(transacao)
            print('💾 Transação salva com sucesso no disco!')
        input('\nPressione ENTER para voltar ao menu...')

    # Opção 2: Exibir Extrato Detalhado
    elif opcao == '2':
        if len(transacao) == 0:
            print('\n⚠️ Nenhuma Transação registrada!')
        else:
            mostrando_posicao(transacao)
        input('\nPressione ENTER para voltar ao menu...')

    # Opção 3: Exibir Estatísticas Gerais (Total e Média)
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

    # Opção 4: Excluir uma Transação
    elif opcao == '4':
        remover_transacao(transacao)
        salvar_dados(transacao)
        input('\nPressione ENTER para voltar ao menu...')

    # Opção 5: Filtrar por Categoria
    elif opcao == '5':
        filtrar_por_categoria(transacao)
        input('\nPressione ENTER para voltar ao menu...')

    # Opção 6: Relatório Sintético por Categoria
    elif opcao == '6':
        gerar_relatorio_sintetico(transacao)
        input('\nPressione ENTER para voltar ao menu...')

    # Opção 7: Editar Transação Existente
    elif opcao == '7':
        editar_transacao(transacao)
        salvar_dados(transacao)
        input('\nPressione ENTER para voltar ao menu...')

    # Opção 8: Sair do Sistema
    elif opcao == '8':
        print('\nSaindo do Sistema... Até logo!')
        break