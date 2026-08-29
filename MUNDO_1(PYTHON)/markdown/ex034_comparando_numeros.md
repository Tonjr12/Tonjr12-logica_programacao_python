    # Exercício 034 — Comparando Números

* **Objetivo:** Escrever um programa que leia dois números inteiros e compare-os, mostrando uma mensagem informando qual deles é maior ou se são iguais.
* **Conceito Aplicado:** Estruturas condicionais aninhadas (`if`, `elif`, `else`) e operadores relacionais (`>`, `<`).

### 💻 Código Solução

```python
num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))

if num1 > num2:
    print('O PRIMEIRO valor é maior!')
elif num2 > num1:
    print('O SEGUNDO valor é maior!')
else:
    print('Não existe valor maior, os dois são IGUAIS!')