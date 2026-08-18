# Exercício 023 — Primeira e Última Ocorrência de uma String

* **Objetivo:** Ler uma frase pelo teclado e mostrar quantas vezes aparece a letra "A", em que posição ela aparece pela primeira vez e em que posição ela aparece pela última vez.
* **Conceito Aplicado:** Métodos de string (`.strip()`, `.upper()`, `.count()`, `.find()`, `.rfind()`) e ajuste de índice base 1.

### 💻 Código Solução

```python
# Solicita a frase ao usuário, remove espaços nas pontas e padroniza tudo em maiúsculas
frase = input('Digite uma frase: ').strip().upper()

# Conta quantas vezes a letra 'A' aparece na frase
quant = frase.count('A')

# Encontra a posição da primeira ocorrência da letra 'A'
posicao_p = frase.find('A')

# Encontra a posição da última ocorrência da letra 'A' (rfind busca da direita para a esquerda)
posicao_u = frase.rfind('A')

# Exibe os resultados somando 1 às posições para legibilidade humana
print(f'A letra "A" aparece {quant} vezes na frase.')
print(f'A primeira letra "A" apareceu na posição {posicao_p + 1}.')
print(f'A última letra "A" apareceu na posição {posicao_u + 1}.')