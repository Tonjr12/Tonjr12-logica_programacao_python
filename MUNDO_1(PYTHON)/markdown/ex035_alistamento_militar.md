# Exercício 035 — Alistamento Militar

* **Objetivo:** Ler o ano de nascimento de um jovem e informar a sua situação em relação ao alistamento militar (se ainda vai se alistar, se é a hora exata ou se já passou do prazo).
* **Conceito Aplicado:** Módulo `datetime` (`date.today().year`), cálculo de saldo de anos e condicionais aninhadas (`if`, `elif`, `else`).

### 💻 Código Solução

```python
from datetime import date

ano_atual = date.today().year
ano_nasc = int(input('Digite o ano de nascimento: '))
idade = ano_atual - ano_nasc

if idade < 18:
    print(f'Ainda vai se alistar! Faltam {18 - idade} ano(s) para o alistamento.')
elif idade == 18:
    print(f'Você tem {idade} anos. É a hora exata de se alistar!')
else:
    print(f'Já passou do tempo de alistamento! Já se passaram {idade - 18} ano(s).')