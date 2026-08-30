# Exercício 037 — Classificando Atletas

* **Objetivo:** Ler o ano de nascimento de um atleta e mostrar sua categoria de acordo com a idade (Mirim, Infantil, Júnior, Sênior e Master).
* **Conceito Aplicado:** Módulo `datetime` (`date.today().year`), cálculo de idade e estruturas condicionais aninhadas (`if`, `elif`, `else`).

### 💻 Código Solução

```python
from datetime import date

data_atual = date.today().year
data_nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = data_atual - data_nascimento

print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JÚNIOR')
elif idade <= 25:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')