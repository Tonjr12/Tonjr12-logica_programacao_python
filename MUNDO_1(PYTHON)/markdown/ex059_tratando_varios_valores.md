# Exercício 059 — Tratando Vários Valores v1.0

* **Objetivo:** Ler vários números inteiros pelo teclado até que o utilizador digite o valor 999 (condição de parada/flag). No final, mostrar quantos números foram digitados e a soma entre eles (desconsiderando o flag).
* **Conceito Aplicado:** Laço `while` com valor de parada (*flag*), acumulador de soma (`soma += num`) e contador de ocorrências (`cont += 1`).

### 💻 Código Solução

```python
num = 0
cont = 0
soma = 0

num = int(input('Digite um número [999 para parar]: '))

while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))

print(f'Foram digitados {cont} números e a soma entre eles foi {soma}.')