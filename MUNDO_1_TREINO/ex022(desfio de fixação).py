def gerar_relatorio_sintetico(lista):
    resumo_categorias = {}

    for t in lista:
        categoria = t['categoria']
        valor = t['reais']

        if categoria in resumo_categorias:
            resumo_categorias[categoria] += valor
        else:
            resumo_categorias[categoria] = valor

    print('\n' + '=' * 45)
    print('       RELATÓRIO SINTÉTICO POR CATEGORIA      ')
    print('=' * 45)
    for cat, total in resumo_categorias.items():
        print(f'{cat:<20} | R$ {total:8.2f}')
    print('=' * 45)

# --- Lista de teste ---
minhas_transacoes = [
    {'descricao': 'Mercado', 'reais': 150.0, 'categoria': 'Alimentacao'},
    {'descricao': 'Padaria', 'reais': 25.0, 'categoria': 'Alimentacao'},
    {'descricao': 'Uber', 'reais': 30.0, 'categoria': 'Transporte'},
    {'descricao': 'Gasolina', 'reais': 100.0, 'categoria': 'Transporte'},
]

gerar_relatorio_sintetico(minhas_transacoes)