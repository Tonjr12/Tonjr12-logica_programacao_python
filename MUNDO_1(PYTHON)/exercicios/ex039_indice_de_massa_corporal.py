# Recebe o peso e a altura do usuário
peso = float(input('Digite o seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))

# Calcule o Índice de Massa Corporal (IMC)
imc = peso / (altura ** 2)

print(f'Seu IMC é de {imc:.1f}')

# Classificação das faixas de IMC
if imc < 18.5:
    print('Classificação: ABAIXO DO PESO')
elif 18.5 <= imc <= 25:
    print('Classificação: PESO IDEAL')
elif 25 < imc <= 30:
    print('Classificação: SOBREPESO')
elif 30 < imc <= 40:
    print('Classificação: OBESIDADE')
else:
    print('Classificação: OBESIDADE MÓRBIDA')