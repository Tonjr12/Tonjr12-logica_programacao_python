# Exercício 014 — Catetos e Hipotenusa

* **Objetivo:** Ler o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcular e mostrar o comprimento da hipotenusa.
* **Conceito Aplicado:** Importação de funções específicas (`from math import hypot`), tipos decimais (`float`) e cálculo geométrico.

### 💻 Código Solução

```python
# Importa a função específica 'hypot' da biblioteca matemática 'math'
from math import hypot

# Solicita o comprimento do cateto oposto e converte para número decimal (float)
cateto_oposto = float(input('Digite o valor do cateto oposto: '))

# Solicita o comprimento do cateto adjacente e converte para número decimal (float)
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))

# Calcula a hipotenusa diretamente passando os dois catetos como argumentos
hipotenusa = hypot(cateto_oposto, cateto_adjacente)

# Exibe o comprimento da hipotenusa formatado com duas casas decimais
print(f'A hipotenusa vai medir {hipotenusa:.2f}.')
