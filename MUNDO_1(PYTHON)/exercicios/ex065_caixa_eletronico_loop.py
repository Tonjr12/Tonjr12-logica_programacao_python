print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)

# Solicita o valor total a ser sacado
valor = int(input('Que valor você quer sacar? R$ '))

# Define o montante inicial igual ao valor do saque
total = valor
ced = 50
tot_ced = 0

# Laço contínuo para calcular as cédulas da maior para a menor
while True:
    if total >= ced:
        # Descobre quantas cédulas cabem no montante atual (divisão inteira)
        tot_ced = total // ced
        # Atualiza o montante com o que sobrou (operador de resto/módulo)
        total %= ced

        # Exibe a quantidade de cédulas daquele valor específico
        print(f'Total de {tot_ced} cédulas de R$ {ced}')

    # Lógica de transição para a próxima cédula menor
    if ced == 50:
        ced = 20
    elif ced == 20:
        ced = 10
    elif ced == 10:
        ced = 1   # ou ced = 1
    # Se já passou pelas cédulas de 1 e o total zerou, encerra o laço
    if total == 0:
        break

print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia.')