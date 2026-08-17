# Exercício 013 — Quebrando um Número

* **Objetivo:** Ler um número real qualquer pelo teclado e mostrar na tela a sua porção inteira.
* **Conceito Aplicado:** Importação de módulos (`from math import trunc`), conversão para float e interpolação com f-strings.

### 💻 Código Solução

```python
# Importa apenas a função 'trunc' da biblioteca matemática 'math'
from math import trunc

# Solicita ao usuário um número real (float)
numero = float(input('Digite um número real/decimal: '))

# Extrai a porção inteira do número usando a função trunc()
porcao_inteira = trunc(numero)

# Exibe na tela o número original e sua respectiva parte inteira
print(f'O valor digitado foi {numero} e a sua porção inteira é {porcao_inteira}.')