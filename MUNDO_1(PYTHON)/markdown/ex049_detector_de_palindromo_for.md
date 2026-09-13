# Exercício 049 — Detector de Palíndromo (usando laço for)

* **Objetivo:** Ler uma frase e identificar se ela é um palíndromo (lida da mesma forma de trás para frente, ignorando espaços) utilizando a estrutura de repetição `for`.
* **Conceito Aplicado:** Manipulação de strings (`.strip()`, `.upper()`, `.split()`, `''.join()`), iteração regressiva com `range(len - 1, -1, -1)` e validação condicional.

### 💻 Código Solução

```python
frase = str(input('Digite uma frase: ')).strip().upper()
separar_em_palavras = frase.split()
juntar_palavras = ''.join(separar_em_palavras)

inverso_palavras = ''

for letra in range(len(juntar_palavras) - 1, -1, -1):
    inverso_palavras += juntar_palavras[letra]

print(f'O inverso de {juntar_palavras} é {inverso_palavras}')

if juntar_palavras == inverso_palavras:
    print('A frase é um PALÍNDROMO!')
else:
    print('A frase NÃO é um palíndromo!')