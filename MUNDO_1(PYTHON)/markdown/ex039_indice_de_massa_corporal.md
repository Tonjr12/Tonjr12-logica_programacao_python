# Exercício 039 — Índice de Massa Corporal (IMC)

* **Objetivo:** Ler o peso e a altura de uma pessoa, calcular seu IMC e mostrar sua condição de acordo com a tabela oficial.
* **Conceito Aplicado:** Operador de potenciação (`**`), cálculo de IMC e estruturas condicionais aninhadas (`if`, `elif`, `else`).

### 💻 Código Solução

```python
peso = float(input('Digite o seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))

imc = peso / (altura ** 2)

print(f'Seu IMC é de {imc:.1f}')

if imc < 18.5:
    print('Classificação: ABAIXO DO PESO')
elif 18.5 <= imc <= 25:
    print('Classificação: PESO IDEAL')
elif 25 < imc <= 30:
    print('Classificação: SOBREPESO')
elif 30 < imc <= 40:
    print('Classificação: OBESIDADE')
else:
    print('Classificação: OBESIDADE MÓRBIDA')