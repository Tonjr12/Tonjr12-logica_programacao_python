# Exercício 049 — Detector de Palíndromo

* **Objetivo:** Ler uma frase qualquer e dizer se ela é um palíndromo, desconsiderando os espaços.
* **Conceito Aplicado:** Tratamento de strings (`.strip()`, `.upper()`, `.split()`, `''.join()`), estrutura de repetição `for` com contagem regressiva baseada no tamanho da string (`len()`) e comparação condicional.

### 💻 Código Solução

```python
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)

inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print(f'O inverso de {junto} é {inverso}')

if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada NÃO É UM PALÍNDROMO!')

