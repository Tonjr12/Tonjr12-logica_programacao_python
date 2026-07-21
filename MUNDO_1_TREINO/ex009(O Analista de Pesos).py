for c in range(1,6):
    nome = input('Qual seu nome? ')
    peso = float(input('qual o seu peso: '))
    if c == 1:
        pessoaPesado = nome
        pessoaLeve = nome
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
            pessoaPesado = nome
        elif peso < menorPeso:
            menorPeso = peso
            pessoaLeve = nome
print(f'A pessoa mais Pesada é: {pessoaPesado}, com :{maiorPeso} kilos')
print(f'A pessoa mais Leve é: {pessoaLeve}, com :{menorPeso} kilos')