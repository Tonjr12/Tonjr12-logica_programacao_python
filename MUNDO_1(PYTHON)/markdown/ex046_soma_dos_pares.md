# Exercício 046 — Soma dos Pares

* **Objetivo:** Ler seis números inteiros e mostrar a soma apenas daqueles que forem pares, desconsiderando os ímpares.
* **Conceito Aplicado:** Estrutura de repetição `for`, entrada de dados em laço, operador módulo (`%`), contador (`cont += 1`) e acumulador (`soma += numero`).

### 💻 Código Solução

```python
soma = 0
cont = 0

for c in range(1, 7):
    numero = int(input(f'Digite o {c}º número inteiro: '))
    if numero % 2 == 0:
        soma += numero
        cont += 1

print(f'Você informou {cont} número(s) PAR(ES) e a soma foi {soma}.')