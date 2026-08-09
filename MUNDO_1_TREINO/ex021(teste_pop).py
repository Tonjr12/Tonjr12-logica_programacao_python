compras = ['mercado', 'padaria', 'farmácia']

# 1. Exibe a lista
for i, comp in enumerate(compras, start=1):
    print(f'{i}° | {comp}')

# 2. Loop de validação para remoção
while True:
    try:
        apagar = int(input('\nQual item deseja apagar?: '))

        # Trava para garantir que o número está dentro do tamanho da lista
        if 1 <= apagar <= len(compras):
            removido = compras.pop(apagar - 1)
            print(f'✅ O item "{removido}" foi removido com sucesso!')
            print(f'Ficaram estes itens: {compras}')
            break  # Sai do loop se deu tudo certo
        else:
            print(f'❌ Opção inválida! Digite um número de 1 a {len(compras)}.')

    except ValueError:
        print('❌ Ops! Digite apenas números inteiros.')