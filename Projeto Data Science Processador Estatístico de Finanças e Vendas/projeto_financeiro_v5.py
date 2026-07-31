vendas = []

print("=" * 45)
print("   PROCESSADOR FINANCEIRO - VERSÃO 5.0   ")
print("=" * 45)

while True:
    # 1. VALIDAÇÃO DE ENTRADA
    while True:
        valor = float(input('Digite o valor da venda: R$ '))
        if valor > 0:
            break
        print('❌ Valor inválido! Digite um valor maior que zero.')

    # 2. ARMAZENAMENTO
    vendas.append(valor)

    # 3. VALIDAÇÃO DE CONTINUIDADE
    continuar = ' '
    while continuar not in "SN":
        continuar = input('Deseja cadastrar outra venda? [S/N]: ').strip().upper()[0]

    if continuar == 'N':
        break

print("\n" + "=" * 45)
print("          RELATÓRIO ESTATÍSTICO          ")
print("=" * 45)

# 4. EXIBIÇÃO SEGURA DOS RESULTADOS
if len(vendas) > 0:
    ticket_medio = sum(vendas) / len(vendas)
    vendas_altas = [v for v in vendas if v > 100]

    print(f'Total de Transações: {len(vendas)}')
    print(f'Faturamento Total: R$ {sum(vendas):.2f}')
    print(f'Menor Venda: R$ {min(vendas):.2f}')
    print(f'Maior Venda: R$ {max(vendas):.2f}')
    print(f'Ticket Médio: R$ {ticket_medio:.2f}')
    print(f'Vendas acima de R$ 100.00: {len(vendas_altas)} -> {vendas_altas}')

    # Historico cronológico
    print("\n--- HISTÓRICO DE ENTRADAS ---")
    for i, valor in enumerate(vendas, start=1):
        print(f'{i}ª Venda: R$ {valor:.2f}')

    # Ranking ordenado
    print('\n' + '=' * 45)
    print('          RANKING DAS VENDAS (MAIOR -> MENOR)          ')
    print("=" * 45)

    vendas_decrescente = sorted(vendas, reverse=True)
    for i, valor in enumerate(vendas_decrescente, start=1):
        print(f'{i}º Lugar: R$ {valor:.2f}')
else:
    print('⚠️ Nenhuma venda foi registrada.')