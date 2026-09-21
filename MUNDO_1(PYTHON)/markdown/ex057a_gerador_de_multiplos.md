# Exercício 057a — Gerador de Sequência de Múltiplos

* **Objetivo:** Exercício de fixação para gerar uma sequência de múltiplos a partir de um número base e valor inicial, permitindo expansões dinâmicas até o usuário digitar 0.
* **Conceito Aplicado:** Laços `while` aninhados, acumulador de exibição (`total += mais`), controle de incremento progressivo e tratamento de saída com flag de parada (`mais != 0`).

### 💻 Código Solução

```python
n = int(input("Digite um número inteiro: "))
multiplos = int(input("Digite o múltiplo inicial: "))

mult = multiplos
mais = 10
contador = 1
total = 0

while mais != 0:
    total += mais
    while contador <= total:
        print(f'{mult} -> ', end='')
        contador += 1
        mult += multiplos

    print('PAUSA')
    mais = int(input("Quantos múltiplos a mais quer ver? (0 encerra): "))

print(f'Você viu o número {n}, múltiplos de {multiplos}, total {total} vezes!.')    