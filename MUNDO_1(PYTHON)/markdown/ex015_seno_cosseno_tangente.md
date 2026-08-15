# Exercício 015 — Seno, Cosseno e Tangente

* **Objetivo:** Ler um ângulo qualquer em graus e mostrar na tela o valor do seno, cosseno e tangente desse ângulo.
* **Conceito Aplicado:** Módulo `math`, conversão de graus para radianos (`math.radians`) e funções trigonométricas (`math.sin`, `math.cos`, `math.tan`).

### 💻 Código Solução

```python
# Importa o módulo 'math' para utilizar funções matemáticas e trigonométricas
import math

# Solicita ao usuário o ângulo em graus e converte para número decimal (float)
graus = float(input('Digite o valor do ângulo em graus: '))

# Converte o ângulo de graus para radianos (exigido pelas funções trigonométricas)
radiano = math.radians(graus)

# Calcula o seno, cosseno e tangente a partir do valor em radianos
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

# Exibe os resultados formatados com duas casas decimais
print(f'O ângulo de {graus}° tem o Seno de {seno:.2f}, Cosseno de {cosseno:.2f} e Tangente de {tangente:.2f}.')