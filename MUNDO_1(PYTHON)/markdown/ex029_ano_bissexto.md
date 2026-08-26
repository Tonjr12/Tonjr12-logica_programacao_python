# Exercício 029 — Ano Bissexto

* **Objetivo:** Ler um ano qualquer e mostrar se ele é bissexto. Se for digitado 0, o programa deve analisar o ano atual da máquina.
* **Conceito Aplicado:** Módulo `datetime` (`date.today().year`), operadores lógicos (`and`, `or`), operador de resto da divisão (`%`) e condicionais.

### 💻 Código Solução

```python
from datetime import date

ano = int(input('Que ano quer analisar? Digite 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} NÃO é BISSEXTO!')