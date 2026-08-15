# Exercício 009 — Calculando Desconto

* **Objetivo:** Ler o preço de um produto e calcular o seu novo valor com 5% de desconto.
* **Conceito Aplicado:** Operadores de divisão (`/`), multiplicação (`*`) e subtração (`-`), tipos primitivos decimais (`float`) e formatação com f-strings.

### 💻 Código Solução

```python
# Solicita o preço do produto ao usuário e converte para número decimal (float)
produto = float(input('Digite o valor do produto: R$ '))

# Define a porcentagem de desconto (5% equivale a 5/100 ou 0.05)
desconto = 5 / 100

# Calcula o preço final subtraindo a quantia do desconto do valor original
preco_final = produto - (produto * desconto)

# Exibe o valor original e o preço recalculado com 5% de desconto formatado
print(f'Um produto de R$ {produto:.2f} com 5% de desconto passa a custar R$ {preco_final:.2f}.')
