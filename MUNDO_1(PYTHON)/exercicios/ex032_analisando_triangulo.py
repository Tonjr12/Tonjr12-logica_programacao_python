# Solicita o comprimento de três segmentos de reta
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

# Verifica se a soma de cada dois lados é maior que o terceiro
if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')