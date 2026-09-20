# Exercício 056 — Progressão Aritmética v2.0

* **Objetivo:** Ler o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos utilizando a estrutura de repetição `while`.
* **Conceito Aplicado:** Laço `while` com contador de controle (`cont <= 10`), atualização de variáveis acumuladoras (`termo += razao`) e formatação de saída em linha.

### 💻 Código Solução

```python
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))

termo = primeiro
cont = 1

while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1

print('FIM')