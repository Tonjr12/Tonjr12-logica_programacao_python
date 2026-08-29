# Cabeçalho do sistema bancário
print('Regra de Empréstimo!')
print('=' * 40)

# Leitura e sanitização de dados (substitui ponto por vazio e vírgula por ponto)
entrada = input('Digite o valor do imóvel: R$ ').replace('.', '').replace(',', '.')
imovel = float(entrada)
salario = float(input('Digite o valor do seu salário: R$ '))
anos = int(input('Em quantos anos pretende pagar? '))

# Converte anos para total de parcelas mensais
parcelas = anos * 12

# Validação para evitar divisão por zero ou dados inválidos
if salario > 0 and parcelas > 0:
    prestacao = imovel / parcelas
    percentual_da_parcela = (prestacao / salario) * 100

    print('=' * 40)
    print(f'Prestação mensal: R$ {prestacao:.2f} ({parcelas}x)')
    print(f'Comprometimento da renda: {percentual_da_parcela:.1f}%')

    # Regra de negócio: prestação não pode exceder 30% do salário
    if prestacao <= salario * 0.30:
        print('Status: Empréstimo CONCEDIDO!')
    else:
        print('Status: Empréstimo NEGADO! (A parcela excede 30% da sua renda).')
else:
    print('Erro: O valor do salário e o número de anos devem ser maiores que zero.')