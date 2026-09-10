# Exercício 045 — Tabuada v2.0

* **Objetivo:** Refazer o desafio da tabuada (Exercício 009), mostrando a tabuada de um número que o usuário escolher, mas agora utilizando um laço `for`.
* **Conceito Aplicado:** Estrutura de repetição `for`, função `range(1, 11)`, f-strings e alinhamento de texto em prints.

### 💻 Código Solução

```python
numero = int(input('Digite um número para ver sua tabuada: '))

print('-' * 18)
for c in range(1, 11):
    print(f'{numero} x {c:2d} = {numero * c}')
print('-' * 18)