# Solicita três números inteiros ao usuário
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

# Assume inicialmente que 'a' é o maior
maior = a
# Testa se 'b' é maior que os outros dois
if b > a and b > c:
    maior = b
# Testa se 'c' é maior que os outros dois
if c > a and c > b:
    maior = c

# Assume inicialmente que 'a' é o menor
menor = a
# Testa se 'b' é menor que os outros dois
if b < a and b < c:
    menor = b
# Testa se 'c' é menor que os outros dois
if c < a and c < b:
    menor = c

# Exibe os resultados na tela
print(f'O maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')