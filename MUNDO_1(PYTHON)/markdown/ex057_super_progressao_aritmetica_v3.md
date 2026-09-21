# Exercício 057 — Super Progressão Aritmética v3.0

* **Objetivo:** Ler o primeiro termo e a razão de uma PA, mostrando inicialmente os 10 primeiros termos. O programa deve perguntar se o usuário quer mostrar mais alguns termos e encerrar somente quando for digitado 0, exibindo o total de termos mostrados.
* **Conceito Aplicado:** Laços de repetição `while` aninhados, atualização de acumulador de limites (`total += mais`) e controle de fluxo com flag de parada (`mais != 0`).

### 💻 Código Solução

```python
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))

termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print(f'Progressão finalizada com {total} termos mostrados.')

