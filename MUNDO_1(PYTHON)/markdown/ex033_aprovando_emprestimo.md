# Exercício 033 — Aprovando Empréstimo

* **Objetivo:** Escrever um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa deve calcular o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou o empréstimo será negado.
* **Conceito Aplicado:** Sanitização de strings com `.replace()`, cálculo financeiro de parcelas, validação de dados e estruturas condicionais (`if` / `else`).

### 💻 Código Solução

```python
print('Regra de Empréstimo!')
print('=' * 40)

entrada = input('Digite o valor do imóvel: R$ ').replace('.', '').replace(',', '.')
imovel = float(entrada)
salario = float(input('Digite o valor do seu salário: R$ '))
anos = int(input('Em quantos anos pretende pagar? '))

parcelas = anos * 12

if salario > 0 and parcelas > 0:
    prestacao = imovel / parcelas
    percentual_da_parcela = (prestacao / salario) * 100

    print('=' * 40)
    print(f'Prestação mensal: R$ {prestacao:.2f} ({parcelas}x)')
    print(f'Comprometimento da renda: {percentual_da_parcela:.1f}%')

    if prestacao <= salario * 0.30:
        print('Status: Empréstimo CONCEDIDO!')
    else:
        print('Status: Empréstimo NEGADO! (A parcela excede 30% da sua renda).')
else:
    print('Erro: O valor do salário e o número de anos devem ser maiores que zero.')