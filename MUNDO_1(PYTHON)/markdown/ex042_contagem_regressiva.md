# Exercício 042 — Contagem Regressiva

* **Objetivo:** Mostrar na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
* **Conceito Aplicado:** Estrutura de repetição `for`, função `range()` com passo negativo (`range(10, -1, -1)`) e módulo `time` (`sleep`).

### 💻 Código Solução

```python
from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)

print('BUM! BUM! POOW! 🎆')