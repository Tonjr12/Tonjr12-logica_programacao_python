# Exercício 052 — Validação de Dados

* **Objetivo:** Ler o sexo de uma pessoa aceitando apenas os valores 'M' ou 'F'. Caso esteja errado, pedir a digitação novamente até ter um valor correto.
* **Conceito Aplicado:** Estrutura de repetição `while` para validação de entrada, operadores lógicos (`and`, `!=`) e sanitização de strings (`.strip()`, `.upper()`).

### 💻 Código Solução

```python
sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('Dados inválidos. Por favor, informe seu sexo com M ou F.')

print(f'Sexo {sexo} registrado com sucesso!')