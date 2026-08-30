from datetime import date

# Pega o ano atual do sistema automaticamente
data_atual = date.today().year

# Solicita o ano de nascimento do atleta
data_nascimento = int(input('Digite o ano de nascimento do atleta: '))

# Calcule a idade do atleta
idade = data_atual - data_nascimento

print(f'O atleta tem {idade} anos.')

# Classificação por faixa etária
if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JÚNIOR')
elif idade <= 25:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')