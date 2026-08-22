# ==============================================================================
# PROJETO DATA SALES - MÓDULO DE PROCESSAMENTO DE TRANSAÇÕES (v1.0)
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

# 3. PROCESSAMENTO MATEMÁTICO E REGRAS DE NEGÓCIO (Módulo 1, 2 e 3)
valor_total_bruto = preco_unitario * quantidade

# Gerando um ID aleatório de transação de 4 dígitos usando 'random'
id_transacao = random.randint(1000, 9999)

# Calculando estimativa de caixas/pacotes para transporte (2 itens por caixa)
caixas_necessarias = ceil(quantidade / 2)

# Fatiamento do primeiro nome do cliente para mensagem personalizada
primeiro_nome_cliente = cliente.split()[0]

# 4. EXIBIÇÃO DO RELATÓRIO DE PROCESSAMENTO DE DADOS
print('\n' + '-' * 60)
print(f'{"RELATÓRIO DE RECEPTAÇÃO DA VENDA":^60}')
print('-' * 60)
print(f'ID da Transação:        #{id_transacao}')
print(f'Cliente Cadastrado:     {cliente} (Primeiro Nome: {primeiro_nome_cliente})')
print(f'Produto Processado:     {produto}')
print(f'Preço Unitário:         R$ {preco_unitario:.2f}')
print(f'Quantidade Total:       {quantidade} unidade(s)')
print(f'Estimativa de Embalagem: {caixas_necessarias} caixa(s) de transporte')
print('-' * 60)
print(f'VALOR TOTAL BRUTO:      R$ {valor_total_bruto:.2f}')
print('=' * 60)
print(f'Status: Venda registrada com sucesso para {primeiro_nome_cliente}!')
print('=' * 60)