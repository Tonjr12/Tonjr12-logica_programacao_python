# Exercício 061 — Tabuada v3.0

* **Objetivo:** Calcular a tabuada de vários números, um de cada vez, de acordo com o valor digitado pelo usuário. O programa é interrompido quando o número digitado for negativo.
* **Conceito Aplicado:** Laço infinito controlado (`while True`), instrução de interrupção (`break`), laço de contagem (`for in range`) e formatação de saídas tabulares.

### 💻 Código Solução

```python
while True:
    n = int(input('Quer ver a tabuada de qual valor? (Negativo para encerrar): '))
    
    if n < 0:
        print('Programa encerrado. Volte sempre!')
        break
        
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 30)

print('FIM')
