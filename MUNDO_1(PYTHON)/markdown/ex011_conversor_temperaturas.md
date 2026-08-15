# Exercício 011 — Conversor de Temperaturas

* **Objetivo:** Ler uma temperatura em graus Celsius (°C) e convertê-la para graus Fahrenheit (°F).
* **Conceito Aplicado:** Operadores de multiplicação (`*`) e adição (`+`), tipos primitivos decimais (`float`) e formatação com f-strings (`:.2f`).

### 💻 Código Solução

```python
# Solicita a temperatura em graus Celsius e converte para número decimal (float)
celsius = float(input('Digite a temperatura em graus Celsius: '))

# Aplica a fórmula de conversão de Celsius para Fahrenheit (°F = °C * 1.8 + 32)
fahren = (celsius * 1.8) + 32

# Exibe a temperatura original em °C e o valor convertido em °F com duas casas decimais
print(f'A conversão da temperatura de Celsius {celsius}°C para Fahrenheit é {fahren:.2f}°F.')