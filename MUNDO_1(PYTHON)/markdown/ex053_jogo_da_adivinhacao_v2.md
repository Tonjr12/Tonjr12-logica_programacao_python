# Exercício 053 — Jogo da Adivinhação v2.0

* **Objetivo:** Criar um jogo onde o computador pensa em um número entre 0 e 100 e o jogador tenta adivinhar até acertar, com dicas de "mais" ou "menos" coloridas e efeito animado ao vencer.
* **Conceito Aplicado:** Biblioteca `random`, repetição com `while`, cores no terminal via `termcolor`, manipulação de tempo com `time` e efeito de texto piscante com retornos de carro (`\r`).

### 💻 Código Solução

```python
from random import randint
from termcolor import colored
import time

computador = randint(0, 100)
acertou = False
palpites = 0

while not acertou:
    jogador = int(input(colored('Qual o seu palpite entre 0 e 100: ', 'blue')))
    palpites += 1

    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print(colored('Menos... Tente mais uma vez', 'red'))
        elif jogador < computador:
            print(colored('Mais... Tente mais uma vez', 'yellow'))

mensagem = f'Você acertou com {palpites} palpites.'
for _ in range(5):
    print(colored(f'\r{mensagem}', 'green', attrs=['bold']), end='', flush=True)
    time.sleep(0.4)
    print('\r' + ' ' * len(mensagem), end='', flush=True)
    time.sleep(0.3)

print(colored(f'\r{mensagem}', 'green', attrs=['bold']))