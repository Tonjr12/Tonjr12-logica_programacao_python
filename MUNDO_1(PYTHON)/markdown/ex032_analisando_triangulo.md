# Exercício 032 — Analisando Triângulo v1.0

* **Objetivo:** Ler o comprimento de três retas e dizer ao usuário se elas podem ou não formar um triângulo.
* **Conceito Aplicado:** Condição de existência de um triângulo, operador lógico `and`, operadores de comparação (`>`) e condicionais (`if` / `else`).

### 💻 Código Solução

```python
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')