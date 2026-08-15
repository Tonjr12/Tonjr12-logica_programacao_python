# Solicita a distância em metros ao usuário e converte para número decimal (float)
distancia_metros = float(input('Qual a distancia em metros que deseja converter?: '))

# Converte metros para centímetros multiplicando por 100
centimetro = distancia_metros * 100

# Converte metros para milímetros multiplicando por 1000
milimetro = distancia_metros * 1000

# Exibe os resultados formatados na tela (usando :.0f para mostrar sem casas decimais)
print(f'A medida de {distancia_metros}m corresponde a {centimetro:.0f}cm e {milimetro:.0f}mm')