# Exercício 008 — Pintando Parede

* **Objetivo:** Ler a largura e a altura de uma parede em metros, calcular a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
* **Conceito Aplicado:** Operadores de multiplicação (`*`) e divisão (`/`), tipos primitivos decimais (`float`) e formatação com f-strings.

### 💻 Código Solução

```python
# Solicita a altura da parede em metros e converte para decimal (float)
altura = float(input('Qual a altura da parede em metros? '))

# Solicita a largura da parede em metros e converte para decimal (float)
largura = float(input('Qual a largura da parede em metros? '))

# Calcula a área total da parede multiplicando largura por altura
area = largura * altura

# Calcula a quantidade de tinta necessária em litros (cada litro pinta 2m²)
tinta = area / 2

# Exibe na tela as dimensões, a área total e a quantidade de tinta necessária
print(f'Sua parede tem a dimensão de {largura}x{altura}m e sua área é de {area:.2f}m².')
print(f'Para pintar essa parede, você precisará de {tinta:.2f}l de tinta.')