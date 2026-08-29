# ==============================================================================
# PROJETO DATA SALES - MÓDULO DE PROCESSAMENTO DE TRANSAÇÕES (v2.0)
# Desenvolvido por: Tonjr (Tom Júnior)
# ==============================================================================

import random
from math import ceil

# 1. CABEÇALHO DO SISTEMA
print('=' * 60)
print(f'{"SISTEMA DE ANÁLISE E PROCESSAMENTO DE VENDAS":^60}')
print('=' * 60)

# 2. ENTRADA DE DADOS DA TRANSAÇÃO (Módulo 4: Limpeza de Strings)
cliente = input('Nome completo do cliente: ').strip().title()
produto = input('Nome do produto vendido: ').strip().upper()
preco_unitario = float(input('Preço unitário do produto (R$): '))
quantidade = int(input('Quantidade vendida: '))

# 3. VALIDAÇÃO DE ENTRADA (Módulo 5: Condicionais)
if preco_unitario <= 0 or quantidade <= 0:
    print('\n[ERRO CRÍTICO]: O preço e a quantidade devem ser maiores que zero!')
else:
    # 4. PROCESSAMENTO MATEMÁTICO E REGRAS DE NEGÓCIO
    valor_total_bruto = preco_unitario * quantidade
    id_transacao = random.randint(1000, 9999)
    caixas_necessarias = ceil(quantidade / 2)
    primeiro_nome_cliente = cliente.split()[0]

    # Regra Comercial: Desconto de 10% para compras acima de R$ 500,00
    if valor_total_bruto > 500:
        desconto = valor_total_bruto * 0.10
    else:
        desconto = 0.0

    valor_liquido = valor_total_bruto - desconto

    # 5. EXIBIÇÃO DO RELATÓRIO DE PROCESSAMENTO DE DADOS
    print('\n' + '-' * 60)
    print(f'{"RELATÓRIO DE RECEPTAÇÃO DA VENDA":^60}')
    print('-' * 60)
    print(f'ID da Transação:         #{id_transacao}')
    print(f'Cliente Cadastrado:      {cliente} (Primeiro Nome: {primeiro_nome_cliente})')
    print(f'Produto Processado:      {produto}')
    print(f'Quantidade Total:        {quantidade} unidade(s)')
    print(f'Estimativa de Embalagem: {caixas_necessarias} caixa(s) de transporte')

    # Alerta Logístico
    if caixas_necessarias > 5:
        print('Alerta de Transporte:    Atenção! Requer transporte de grande porte.')
    else:
        print('Alerta de Transporte:    Envio em transporte padrão.')

    print('-' * 60)
    print(f'VALOR TOTAL BRUTO:       R$ {valor_total_bruto:.2f}')
    print(f'DESCONTO APLICADO (10%): R$ {desconto:.2f}')
    print(f'VALOR LÍQUIDO FINAL:     R$ {valor_liquido:.2f}')
    print('=' * 60)
    print(f'Status: Venda registrada com sucesso para {primeiro_nome_cliente}!')
    print('=' * 60)