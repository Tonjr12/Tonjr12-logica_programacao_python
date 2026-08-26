# Exercício 030 — Maior e Menor Valores

* **Objetivo:** Ler três números inteiros e mostrar qual é o maior e qual é o menor.
* **Conceito Aplicado:** Testes condicionais sucessivos (`if`), operadores de comparação (`>`, `<`) e operador lógico `and`.

### 💻 Código Solução

```python
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

print(f'O maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')