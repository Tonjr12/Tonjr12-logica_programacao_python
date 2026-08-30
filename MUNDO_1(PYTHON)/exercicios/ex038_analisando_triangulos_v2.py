# Exercício: Classificação de Triângulos
# Objetivo: Identificar se três lados formam um triângulo Equilátero, Escaleno ou Isósceles.

# Entrada dos três lados do triângulo
a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))

# Checa se os três lados são iguais (pode usar a comparação encadeada a == b == c)
if a == b == c:
    print('Tipo de triângulo: EQUILÁTERO')

# Checa se todos os lados são totalmente diferentes entre si
elif a != b and b != c and c != a:
    print('Tipo de triângulo: ESCALENO')

# Caso não seja nem equilátero nem escaleno, sobra exatamente a opção de 2 lados iguais
else:
    print('Tipo de triângulo: ISÓSCELES')