# Exercício 024 - Analisando Primeiro e Último Nome

## 📝 Descrição
Programa em Python que recebe o nome completo de uma pessoa, higieniza a entrada removendo espaços extras, divide a string em uma lista de nomes e identifica o primeiro nome, o último nome e o total de palavras/nomes inseridos.

## 🚀 Conceitos Aplicados
* **`input().strip()`**: Leitura de dados com remoção de espaços nas extremidades da string.
* **`.split()`**: Divisão da string em uma lista baseada em espaços em branco.
* **Fatiamento de Listas (`[0]` e `[-1]`)**: Acesso ao primeiro índice e ao índice reverso (último item).
* **`len()`**: Contagem do total de elementos dentro da lista.

## 💻 Código
```python
nome_completo = input('Digite o nome completo: ').strip()
nome_fatiado = nome_completo.split()

print(f'Lista de nomes: {nome_fatiado}')
print(f'O primeiro nome é: {nome_fatiado[0]}')
print(f'O último nome é: {nome_fatiado[-1]}')

total_nomes = len(nome_fatiado)
print(f'O total de nomes: {total_nomes}')