# Exercício 048 — Números Primos

* **Objetivo:** Ler um número inteiro e dizer se ele é ou não um número primo.
* **Conceito Aplicado:** Estrutura de repetição `for`, contagem de divisores com operador `%`, validação relacional e condicionais aninhadas.

### 💻 Código Solução

```python
numero = int(input('Digite um número: '))
cont = 0

if numero > 1:
    for c in range(1, numero + 1):
        if numero % c == 0:
            cont += 1

    if cont == 2:
        print(f'O número {numero} É PRIMO!')
        print(f'Pois foi divisível exatamente {cont} vezes.')
    else:
        print(f'O número {numero} NÃO É PRIMO!')
        print(f'Pois foi divisível {cont} vezes.')
else:
    print('O número NÃO É PRIMO pois é menor ou igual a 1.')