# Exercício 062 — Jogo do Par ou Ímpar

* **Objetivo:** Criar um programa que jogue par ou ímpas com o computador, encerrando apenas quando o jogador perder e exibindo o total de vitórias consecutivas.
* **Conceito Aplicado:** Importação de módulos (`random.randint`), laço infinito (`while True`), interrupção de fluxo com `break`, manipulação de strings (`strip`, `upper`) e contagem de pontuação.

### 💻 Código Solução

```python
from random import randint

cont = 0

while True:
    jogar_escolha = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
    computador = randint(0, 10)
    jogar_numero = int(input('Digite um número de 0 a 10: '))

    soma = computador + jogar_numero

    if soma % 2 == 0:
        tipo = 'P'
        print('Deu Par')
    else:
        tipo = 'I'
        print('Deu Ímpar')

    if jogar_escolha == tipo:
        print('Você venceu')
        cont += 1
    else:
        print('Você perdeu')
        break

print(f'Fim do jogo! Você venceu {cont} vezes consecutivas ')