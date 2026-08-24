    # Exercício 027 — Par ou Ímpar?

* **Objetivo:** Ler um número inteiro e mostrar na tela se ele é PAR ou ÍMPAR.
* **Conceito Aplicado:** Operador aritmético módulo/resto (`%`), operador relacional de igualdade (`==`) e estruturas condicionais (`if` / `else`).

### 💻 Código Solução

```python
numero = int(input('Digite um número inteiro: '))

if numero % 2 == 0:
    print(f'O número {numero} é PAR!')
else:
    print(f'O número {numero} é ÍMPAR!')