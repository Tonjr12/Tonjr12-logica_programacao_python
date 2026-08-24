# Solicita a velocidade do veículo ao usuário e converte para número inteiro
velocidade = int(input('Qual a velocidade do carro (km/h)? '))

# Verifica se a velocidade ultrapassou o limite permitido de 80 km/h
if velocidade > 80:
    # Calcule a multa: R$ 7,00 para cada km acima dos 80 km/h
    multa = (velocidade - 80) * 7
    print(f'MULTADO! Você excedeu o limite permitido de 80 km/h.')
    print(f'O valor da sua multa é de R$ {multa:.2f}.')
else:
    print('Velocidade dentro do limite. O sistema de fiscalização deseja uma boa viagem!')