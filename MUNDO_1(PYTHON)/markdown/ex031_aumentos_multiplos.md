# Exercício 031 — Aumentos Múltiplos

* **Objetivo:** Calcular o reajuste salarial de um funcionário cobrando 10% de aumento para salários superiores a R$ 1.250,00 e 15% para salários inferiores ou iguais.
* **Conceito Aplicado:** Tipagem `float`, estruturas condicionais (`if` / `else`), operador relacional (`>`), cálculo de porcentagem e formatação monetária.

### 💻 Código Solução

```python
salario = float(input('Qual o seu salário: R$ '))

if salario > 1250:
    novo_salario = salario + (salario * 0.10)
else:
    novo_salario = salario + (salario * 0.15)

print(f'Seu salário atual é de R$ {salario:.2f} e com o aumento seu novo salário é de R$ {novo_salario:.2f}')