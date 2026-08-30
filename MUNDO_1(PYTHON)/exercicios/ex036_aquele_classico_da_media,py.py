# Solicita as duas notas do aluno e converte para decimal (float)
nota_1 = float(input('Qual a primeira nota do aluno: '))
nota_2 = float(input('Qual a segunda nota do aluno: '))

# Calcule a média aritmética entre as notas
media = (nota_1 + nota_2) / 2

# Exibe a situação com base nas faixas de notas
if media < 5.0:
    print(f'Sua média é de: {media:.2f}. REPROVADO!')
elif 5.0 <= media < 7.0 and 9 <= media <= 10.0:
    print(f'Sua média é de: {media:.2f}. RECUPERAÇÃO!')
else:
    print(f'Sua média é de: {media:.2f}. APROVADO!')