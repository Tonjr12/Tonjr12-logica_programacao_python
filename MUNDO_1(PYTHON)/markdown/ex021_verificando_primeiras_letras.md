# Exercício 021 — Verificando as Primeiras Letras de um Texto

* **Objetivo:** Ler o nome de uma cidade e dizer se ela começa ou não com o nome "SANTO".
* **Conceito Aplicado:** Fatiamento de strings (`[:5]`), método de padronização (`.upper()`), remoção de espaços (`.strip()`) e operadores relacionais (`==`).

### 💻 Código Solução

```python
# Solicita o nome da cidade e remove espaços antes e depois do texto
cidade = input('Em que cidade você nasceu? ').strip()

# Pega os 5 primeiros caracteres ([:5]), converte para maiúsculas (.upper()) e compara com 'SANTO'
resultado = cidade[:5].upper() == 'SANTO'

# Exibe True se a cidade começar com "SANTO" ou False se não começar
print(f'A cidade começa com "SANTO"? {resultado}')