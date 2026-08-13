# Exercício 007 — Conversor de Moedas

* **Objetivo:** Ler quanto dinheiro uma pessoa tem na carteira em reais (R$) e mostrar quantos dólares (US$) ela pode comprar com base em uma cotação fixa.
* **Conceito Aplicado:** Operador aritmético de divisão (`/`), conversão de tipos com `float()` e formatação de valores monetários com f-strings (`:.2f`).

### 💻 Código Solução

```python
# Solicita o valor disponível em reais (R$) na carteira e converte para número decimal (float)
carteira = float(input('Qual o valor tem na sua carteira? R$ '))

# Define a cotação do dólar (US$) para o cálculo
dolar = 5.00

# Calcula a quantidade de dólares que podem ser comprados dividindo o saldo pela cotação
compra = carteira / dolar

# Exibe na tela o saldo e a quantidade de dólares que pode ser comprada com formatação de 2 casas decimais
print(f'Você tem R$ {carteira:.2f} na carteira e a cotação do dólar está em R$ {dolar:.2f}.')
print(f'Com esse valor, você pode comprar US$ {compra:.2f}')