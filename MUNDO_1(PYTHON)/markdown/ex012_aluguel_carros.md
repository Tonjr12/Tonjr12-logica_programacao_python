# Exercício 012 — Aluguel de Carros

* **Objetivo:** Calcular o preço a pagar pelo aluguel de um carro sabendo que a diária custa R$ 60.00 e cada km rodado custa R$ 0.15.
* **Conceito Aplicado:** Operadores de multiplicação (`*`) e adição (`+`), conversão de tipos (`int` e `float`) e formatação monetária com f-strings (`:.2f`).

### 💻 Código Solução

```python
# Solicita a quantidade de dias que o carro foi alugado e converte para inteiro (int)
dias = int(input('Quantos dias vai alugar o carro? '))

# Solicita a quantidade de quilômetros rodados e converte para decimal (float)
km = float(input('Quantos km rodados? '))

# Calcula o valor total somando as diárias (R$ 60/dia) e a quilometragem (R$ 0.15/km)
total = (dias * 60) + (km * 0.15)

# Exibe os dados do aluguel e o valor final a ser pago formatado em reais (R$)
print(f'O carro foi alugado por {dias} dias e rodou {km:.1f} km.')
print(f'O valor total a ser pago é de R$ {total:.2f}.')