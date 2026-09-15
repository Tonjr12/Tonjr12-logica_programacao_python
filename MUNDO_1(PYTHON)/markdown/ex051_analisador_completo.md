# Exercício 051 — Analisador Completo

* **Objetivo:** Ler nome, idade e sexo de 4 pessoas e exibir a média de idade do grupo, o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
* **Conceito Aplicado:** Estrutura de repetição `for`, acumuladores de soma, filtros condicionais com operadores lógicos (`and`) e formatação de texto.

### 💻 Código Solução

```python
idade_total = 0
idade_velho = 0
nome_velho = ''
mulher_nova = 0

for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = str(input('Digite seu nome: ')).strip().upper()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

    idade_total += idade

    if c == 1 and sexo == 'M':
        idade_velho = idade
        nome_velho = nome
    elif sexo == 'M' and idade > idade_velho:
        idade_velho = idade
        nome_velho = nome

    if sexo == 'F' and idade < 20:
        mulher_nova += 1

media = idade_total / 4

print('=' * 30)
if nome_velho != '':
    print(f'O homem mais velho é {nome_velho} com {idade_velho} anos.')
else:
    print('Não há homens cadastrados no grupo.')
print(f'Existem {mulher_nova} mulheres com menos de 20 anos.')
print(f'A média de idade do grupo é: {media:.1f} anos.')