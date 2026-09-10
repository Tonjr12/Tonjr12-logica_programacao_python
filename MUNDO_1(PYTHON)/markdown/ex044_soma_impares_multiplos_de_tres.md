# Exercício 044 — Soma Ímpares Múltiplos de Três

* **Objetivo:** Calcular a soma entre todos os números que são ímpares, múltiplos de três e que se encontram no intervalo de 1 até 500.
* **Conceito Aplicado:** Estrutura de repetição `for`, salto no `range()` para filtragem inicial, operador resto da divisão (`%`), contadores (`cont += 1`) e acumuladores (`soma += c`).

### 💻 Código Solução

```python
soma = 0
cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c

print(f'A soma de todos os {cont} valores solicitados é {soma}.')