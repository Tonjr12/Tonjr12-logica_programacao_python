# Inicializa a variável com valor neutro para garantir a entrada no laço
sexo = ''

# Repete o pedido enquanto a entrada for diferente de 'M' e 'F'
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()

    # Valida e exibe mensagem de erro caso o valor seja inválido
    if sexo != 'M' and sexo != 'F':
        print('Dados inválidos. Por favor, informe seu sexo com M ou F.')

print(f'Sexo {sexo} registrado com sucesso!')