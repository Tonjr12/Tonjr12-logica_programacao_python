# Exercício 025 — Jogo da Adivinhação v1.0

* **Objetivo:** Escrever um programa que faça o computador "pensar" em um número inteiro entre 1 e 5 e peça para o usuário tentar adivinhar.
* **Conceito Aplicado:** Módulo `random` (`randint`), estruturas condicionais (`if` / `else`), operador relacional de diferença (`!=`) e indentação.

### 💻 Código Solução

```python
import random

numero = int(input('Digite um número entre 1 e 5: '))
computador = random.randint(1, 5)

if numero != computador:
    print(f'Você errou! Apostou no número {numero} e o sorteado foi {computador}!')
else:
    print('Você acertou! Parabéns!')