# Exercício 036 — Aquele Clássico da Média

* **Objetivo:** Ler duas notas de um aluno, calcular sua média e mostrar a mensagem correspondente (Reprovado se < 5.0, Recuperação entre 5.0 e 6.9, Aprovado se >= 7.0).
* **Conceito Aplicado:** Operadores aritméticos, tipagem `float`, estruturas condicionais aninhadas (`if`, `elif`, `else`) e encadeamento de operadores de comparação.

### 💻 Código Solução

```python
nota_1 = float(input('Qual a primeira nota do aluno: '))
nota_2 = float(input('Qual a segunda nota do aluno: '))

media = (nota_1 + nota_2) / 2

if media < 5.0:
    print(f'Sua média é de: {media:.2f}. REPROVADO!')
elif 5.0 <= media < 7.0:
    print(f'Sua média é de: {media:.2f}. RECUPERAÇÃO!')
else:
    print(f'Sua média é de: {media:.2f}. APROVADO!')