# Exercício 060 — Maior e Menor Valores

* **Objetivo:** Ler vários números inteiros pelo teclado usando a flag 999. No final, mostrar a média entre todos os valores, qual foi o maior e qual foi o menor número digitado.
* **Conceito Aplicado:** Laço `while` com flag, inicialização condicional por contagem (`cont == 1`), estruturas condicionais aninhadas para comparação e cálculo de média aritmética.

### 💻 Código Solução

```python
soma = 0
cont = 0
n = 0

n = int(input('Digite um número [999 para parar]: '))

while n != 999:
    soma += n
    cont += 1
    if cont == 1:
        menor = n
        maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    n = int(input('Digite um número [999 para parar]: '))

if cont > 0:
    media = soma / cont
    print(f'A média dos valores é {media}, e o menor valor é {menor} e o maior valor é {maior}')
else:
    print('Nenhum valor foi digitado').
