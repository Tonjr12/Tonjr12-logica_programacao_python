# main.py
from dados import carregar_dados, salvar_dados
from funcoes import (
    ler_transacao,
    mostrando_posicao,
    calcular_estatisticas,
    remover_transacao,
    editar_transacao,
    filtrar_por_categoria,
    gerar_relatorio_sintetico,
    exibir_menu
)

print('=' * 45)
print('-' * 45)
print('Processador Financeiro - Versão 15.0 (Arquitetura Modular)')


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
        item = ler_transacao()  # Coleta os dados digitados
        transacao.append(item)  # Insere o novo dicionário na lista da memória RAM
        salvar_dados(transacao) # Grava a lista atualizada no disco rígido (JSON)
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