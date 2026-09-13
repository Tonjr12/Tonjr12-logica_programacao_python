# ==============================================================================
# PROJETO DATA SALES - MÓDULO DE PROCESSAMENTO DE TRANSAÇÕES (v3.0)
# Desenvolvido por: Tonjr (Tom Júnior)
# ==============================================================================

import random
from math import ceil

# 1. CABEÇALHO DO SISTEMA
print('=' * 60)
print(f'{"SISTEMA DE ANÁLISE E PROCESSAMENTO DE VENDAS v3.0":^60}')
print('=' * 60)

# 2. DEFINIÇÃO DA QUANTIDADE DE VENDAS
total_vendas = int(input('Quantidade de vendas a cadastrar hoje: '))

if total_vendas <= 0:
    print('\n[ERRO CRÍTICO]: A quantidade de vendas deve ser maior que zero!')
else:
    soma_total = 0

    # 3. LAÇO DE PROCESSAMENTO DE CADA VENDA (Módulo 7: Repetição com for)
    for c in range(1, total_vendas + 1):
        print(f'\n--- LANÇAMENTO DA VENDA #{c} ---')
        cliente = input('Nome completo do cliente: ').strip().title()
        produto = input('Nome do produto vendido: ').strip().upper()
        preco_unitario = float(input('Preço unitário do produto (R$): '))
        quantidade_itens = int(input('Quantidade de itens do produto: '))

        if preco_unitario <= 0 or quantidade_itens <= 0:
            print('[AVISO]: Venda inválida (preço/quantidade zerados). Item ignorado.')
        else:
            valor_bruto_item = preco_unitario * quantidade_itens

            # Regra Comercial: Desconto de 10% para compras acima de R$ 500,00
            if valor_bruto_item > 500:
                desconto = valor_bruto_item * 0.10
            else:
                desconto = 0.0

            valor_liquido = valor_bruto_item - desconto
            soma_total += valor_liquido

            id_transacao = random.randint(1000, 9999)
            primeiro_nome = cliente.split()[0]
            caixas_necessarias = ceil(quantidade_itens / 2)

            print(f'Status: Venda #{id_transacao} registrada para {primeiro_nome} | Valor Líquido: R$ {valor_liquido:.2f}')

    # 4. RELATÓRIO CONSOLIDADO DO DIA (FORA DO LAÇO)
    media_vendas = soma_total / total_vendas

    print('\n' + '=' * 60)
    print(f'{"RELATÓRIO CONSOLIDADO DE VENDAS DO DIA":^60}')
    print('=' * 60)
    print(f'Total de Transações Registradas: {total_vendas}')
    print(f'Faturamento Total Líquido:      R$ {soma_total:.2f}')
    print(f'Média por Venda Registrada:      R$ {media_vendas:.2f}')
    print('=' * 60)