# Exercício 057b — Sequência do Dobro Dinâmico

* **Objetivo:** Gerar uma sequência onde cada número é o dobro do anterior (Progressão Geométrica de razão 2), permitindo expansões dinâmicas até o usuário digitar 0 e exibindo o resumo final.
* **Conceito Aplicado:** Laços `while` aninhados, multiplicação acumulativa de progressão (`termo *= 2`), controle de expansão e fechamento de laço com relatório.

### 💻 Código Solução

```python
n = int(input('Digite um número inteiro: '))

termo = n
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        cont += 1
        termo *= 2

    print('PAUSA')
    mais = int(input('Quantos números a mais? (0 encerra): '))

print(f'\nSequência finalizada! Você viu {total} números e o último termo foi {termo // 2}.')