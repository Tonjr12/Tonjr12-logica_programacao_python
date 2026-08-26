# Recebe o salário atual do funcionário e converte para decimal (float)
salario = float(input('Qual o seu salário: R$ '))

# Verifica se o salário é superior a R$ 1.250,00 para aplicar 10% ou 15% de aumento
if salario > 1250:
    novo_salario = salario + (salario * 0.10)
else:
    novo_salario = salario + (salario * 0.15)

# Exibe o salário antigo e o novo valor reajustado
print(f'Seu salário atual é de R$ {salario:.2f} e com o aumento seu novo salário é de R$ {novo_salario:.2f}')       