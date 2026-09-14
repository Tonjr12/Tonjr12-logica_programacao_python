# Exercício 050 — Maior e Menor da Sequência

* **Objetivo:** Ler o peso de cinco pessoas e exibir qual foi o maior e o menor peso informados, juntamente com o nome das respectivas pessoas.
* **Conceito Aplicado:** Estrutura de repetição `for`, validação de primeiro elemento no laço (`c == 1`) e atualização condicional de variáveis de extremo (`maior` e `menor`).

### 💻 Código Solução

```python
maior = 0
menor = 0
nome_pesado = ''
nome_leve = ''

for c in range(1, 6):
    nome = input(f'Digite o nome da {c}ª pessoa: ').strip()
    peso = float(input(f'Digite o peso de {nome} (kg): '))

    if c == 1:
        maior = peso
        menor = peso
        nome_pesado = nome
        nome_leve = nome
    else:
        if peso > maior:
            maior = peso
            nome_pesado = nome
        if peso < menor:
            menor = peso
            nome_leve = nome

print('=' * 45)
print(f'Maior peso: {nome_pesado} com {maior:.1f} kg.')
print(f'Menor peso: {nome_leve} com {menor:.1f} kg.')
print('=' * 45)