from random import randint
from time import sleep

print('-=-' * 20)
print('GAME: JOKENPÔ')
print('-=-' * 20)
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
print('-=-' * 20)

jogador = int(input('Qual é a sua jogada? '))
computador = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 20)

# Estrutura usando APENAS condicionais para exibir a jogada do computador
if computador == 0:
    comp_str = 'PEDRA'
elif computador == 1:
    comp_str = 'PAPEL'
else:
    comp_str = 'TESOURA'

# Estrutura usando APENAS condicionais para exibir a jogada do jogador
if jogador == 0:
    jog_str = 'PEDRA'
elif jogador == 1:
    jog_str = 'PAPEL'
elif jogador == 2:
    jog_str = 'TESOURA'
else:
    jog_str = 'INVÁLIDO'

if jog_str == 'INVÁLIDO':
    print('JOGADA INVÁLIDA! Escolha 0, 1 ou 2.')
else:
    print(f'Computador jogou: {comp_str}')
    print(f'Jogador jogou:    {jog_str}')
    print('-=' * 20)

    # Lógica de vitória, empate e derrota usando apenas if / elif / else
    if computador == jogador:
        print('RESULTADO: EMPATE!')
    elif jogador == 0 and computador == 2:
        print('RESULTADO: JOGADOR VENCEU! (Pedra esmaga Tesoura)')
    elif jogador == 1 and computador == 0:
        print('RESULTADO: JOGADOR VENCEU! (Papel cobre Pedra)')
    elif jogador == 2 and computador == 1:
        print('RESULTADO: JOGADOR VENCEU! (Tesoura corta Papel)')
    else:
        print('RESULTADO: COMPUTADOR VENCEU!')