# Exercício 016 — Sorteando um Item na Lista

* **Objetivo:** Ler o nome de quatro alunos e sortear um deles para apagar o quadro.
* **Conceito Aplicado:** Módulo `random`, criação e manipulação de listas (`[]`) e escolha aleatória com `random.choice()`.

### 💻 Código Solução

```python
# Importa o módulo random para trabalhar com sorteios e escolhas aleatórias
import random

# Solicita o nome dos quatro alunos ao usuário
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

# Cria uma lista contendo os nomes coletados
lista = [n1, n2, n3, n4]

# Sorteia um elemento de forma aleatória dentro da lista
escolhido = random.choice(lista)

# Exibe na tela o nome do aluno sorteado
print(f'O aluno escolhido foi: {escolhido}')    