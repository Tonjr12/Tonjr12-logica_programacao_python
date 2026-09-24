# Exercício 058 — Sequência de Fibonacci v1.0

* **Objetivo:** Ler um número inteiro $N$ e mostrar os $N$ primeiros elementos de uma Sequência de Fibonacci.
* **Conceito Aplicado:** Estrutura de repetição `while`, manipulação de variáveis encadeadas (troca de valores entre `t1`, `t2` e `t3`) e controlo de fluxo por contador de quantidade.

### 💻 Código Solução

```python
n = int(input('Quantos termos deseja mostrar: '))
t1 = 0
t2 = 1

print(f'{t1} -> {t2} -> ', end='')
cont = 3

while cont <= n:
    t3 = t1 + t2
    print(f'{t3} -> ', end='')
    t1 = t2
    t2 = t3
    cont += 1

print('FIM')