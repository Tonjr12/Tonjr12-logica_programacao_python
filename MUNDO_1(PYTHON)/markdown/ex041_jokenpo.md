# Exercício 041 — GAME: Jokenpô (Pedra, Papel e Tesoura)

* **Objetivo:** Criar um jogo de Jokenpô contra o computador utilizando apenas condicionais aninhadas.
* **Conceito Aplicado:** Módulo `random` (`randint`), módulo `time` (`sleep`) e estruturas condicionais aninhadas (`if`, `elif`, `else`).

### 💻 Código Solução

```python
from random import randint
from time import sleep

print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')

jogador = int(input('Qual é a sua jogada? '))
computador = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

if computador == 0:
    comp_str = 'PEDRA'
elif computador == 1:
    comp_str = 'PAPEL'
else:
    comp_str = 'TESOURA'

if jogador == 0:
    jog_str = 'PEDRA'
elif jogador == 1:
    jog_str = 'PAPEL'
elif jogador == 2:
    jog_str = 'TESOURA'
else:
    jog_str = 'INVÁLIDO'

if jog_str == 'INVÁLIDO':
    print('JOGADA INVÁLIDA!')
else:
    print(f'Computador jogou: {comp_str}')
    print(f'Jogador jogou: {jog_str}')

    if computador == jogador:
        print('EMPATE!')
    elif jogador == 0 and computador == 2:
        print('JOGADOR VENCEU!')
    elif jogador == 1 and computador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 2 and computador == 1:
        print('JOGADOR VENCEU!')
    else:
        print('COMPUTADOR VENCEU!') 