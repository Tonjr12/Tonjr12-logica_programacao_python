# Importa a classe date do módulo datetime
from datetime import date

# Solicita o ano ao usuário
ano = int(input('Que ano quer analisar? Digite 0 para analisar o ano atual: '))

# Se o usuário digitar 0, pega o ano atual configurado na máquina
if ano == 0:
    ano = date.today().year

# Regra do Ano Bissexto: divisível por 4 E não por 100, OU divisível por 400
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} NÃO é BISSEXTO!')