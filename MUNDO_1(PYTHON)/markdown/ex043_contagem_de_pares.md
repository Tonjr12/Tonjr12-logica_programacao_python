# Exercício 043 — Contagem de Pares

* **Objetivo:** Mostrar na tela todos os números pares no intervalo entre 1 e 50, aplicando tratamento de formatação na saída do terminal.
* **Conceito Aplicado:** Estrutura de repetição `for`, parâmetro de salto na função `range()`, operador resto da divisão (`%`) e controle de caracteres de término com `end`.

### 💻 Código Solução

```python
# Primeira Abordagem: Salto direto de 2 em 2 com formatação de término
for c in range(0, 52, 2):
    if c == 50:
        print(c, end='.\n')
    else:
        print(c, end=',')

# Segunda Abordagem: Verificação condicional de paridade em todo o intervalo
for c in range(0, 51):
    if c % 2 == 0:
        print(c, end=' ')