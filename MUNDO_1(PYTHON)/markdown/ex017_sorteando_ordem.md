# Exercício 017 — Sorteando uma Ordem na Lista

* **Objetivo:** Ler o nome de quatro alunos, sortear e exibir a ordem de apresentação dos trabalhos.
* **Conceito Aplicado:** Módulo `random` (`random.shuffle()`), tratamento de strings (`.strip()`, `.upper()`), listas e iteração com laço `for` + `enumerate()`.

### 💻 Código Solução

```python
# Importa o módulo random para operações aleatórias
import random

# Coleta o nome de 4 alunos removendo espaços e padronizando em maiúsculas
n1 = input('Primeiro aluno: ').strip().upper()
n2 = input('Segundo aluno: ').strip().upper()
n3 = input('Terceiro aluno: ').strip().upper()
n4 = input('Quarto aluno: ').strip().upper()

# Cria a lista com os nomes digitados
lista = [n1, n2, n3, n4]

# Embaralha a ordem da lista diretamente na memória
random.shuffle(lista)

# Exibe a ordem sorteada com cabeçalho e repetição numerada
print('-' * 30)
print('ORDEM DE APRESENTAÇÃO SORTEADA:')
print('-' * 30)

for indice, aluno in enumerate(lista, start=1):
    print(f'{indice}º lugar: {aluno}')

print('-' * 30)