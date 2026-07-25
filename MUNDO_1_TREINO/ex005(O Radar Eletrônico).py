velocidade=int(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print(f'Velocidade constatada no radar {velocidade}km/h')
    print(f'MULTADO! Você excedeu o limite permitido de 80 km/h.')
else:
    print(f'Velocidade constatada no radar {velocidade}km/h')
    print('Dirija com segurança! Tenha um bom dia.')

