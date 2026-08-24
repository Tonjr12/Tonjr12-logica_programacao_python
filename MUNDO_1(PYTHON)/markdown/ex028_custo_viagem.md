# Exercício 028 — Custo da Viagem

* **Objetivo:** Calcular o preço da passagem cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.
* **Conceito Aplicado:** Tipagem `float`, estruturas condicionais (`if` / `else`), operador de comparação (`<=`) e regras tarifárias.

### 💻 Código Solução

```python
distancia = float(input('Qual a distância da viagem em km? '))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f'O valor cobrado pelo frete/passagem será de R$ {preco:.2f}')