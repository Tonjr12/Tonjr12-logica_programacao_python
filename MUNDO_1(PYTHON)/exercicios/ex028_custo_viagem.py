# Recebe a distância da viagem em km e converte para número decimal (float)
distancia = float(input('Qual a distância da viagem em km? '))

# Verifica se a viagem é curta (até 200 km) ou longa (acima de 200 km)
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

# Exibe o valor final cobrado formatado com duas casas decimais
print(f'O valor cobrado pelo frete/passagem será de R$ {preco:.2f}')