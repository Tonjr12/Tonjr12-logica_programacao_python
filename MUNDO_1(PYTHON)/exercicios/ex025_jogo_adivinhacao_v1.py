# Importa o módulo random para geração de números aleatórios
import random

# Solicita o palpite do usuário e converte para número inteiro
numero = int(input('Digite um número entre 1 e 5: '))

# Gera um número aleatório inteiro entre 1 e 5 para o computador
computador = random.randint(1, 5)

# Verifica se o palpite do usuário é diferente do número sorteado
if numero != computador:
    print(f'Você errou! Apostou no número {numero} e o sorteado foi {computador}!')
else:
    print('Você acertou! Parabéns!')