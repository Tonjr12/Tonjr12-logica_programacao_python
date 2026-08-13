## 🧪 Exercício 004 — Média Aritmética

* **Objetivo:** Ler duas notas de um aluno, calcular e exibir a sua média aritmética.
* **Conceito Aplicado:** Precedência de operadores com parênteses `(n1 + n2) / 2`, conversão com `float()` e limitação de casas decimais (`:.2f`).

### 💻 Código Solução

```python
# Solicita a primeira nota do aluno e converte a entrada para número decimal (float)
nota1 = float(input('Digite a primeira nota: '))

# Solicita a segunda nota do aluno e converte a entrada para número decimal (float)
nota2 = float(input('Digite a segunda nota: '))

# Calcula a média aritmética garantindo que a soma ocorra primeiro através dos parênteses
media = (nota1 + nota2) / 2

# Exibe na tela as notas digitadas e a média final formatada com duas casas decimais
print(f'A média entre {nota1} e {nota2} é igual a {media:.2f}')
