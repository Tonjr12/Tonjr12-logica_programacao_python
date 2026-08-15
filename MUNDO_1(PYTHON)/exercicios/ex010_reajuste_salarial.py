# Solicita o salário atual do funcionário e converte para número decimal (float)
salario_atual = float(input('Digite o salário atual: R$ '))

# Calcula o novo salário somando o valor atual com os 15% de aumento
novo_salario = salario_atual + (salario_atual * 0.15)

# Exibe na tela o salário antigo e o novo valor reajustado com 15% de aumento
print(f'Um funcionário que ganha R$ {salario_atual:.2f} passa a receber R$ {novo_salario:.2f} com 15% de aumento.')