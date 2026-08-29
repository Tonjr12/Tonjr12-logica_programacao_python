# Importa a classe date do módulo datetime
from datetime import date

# Pega o ano atual configurado no sistema
ano_atual = date.today().year

# Solicita o ano de nascimento do usuário
ano_nasc = int(input('Digite o ano de nascimento: '))

# Calcule a idade do jovem
idade = ano_atual - ano_nasc

# Estrutura condicional aninhada para verificar a situação do alistamento
if idade < 18:
    saldo = 18 - idade
    print(f'Ainda vai se alistar! Faltam {saldo} ano(s) para o seu alistamento.')
elif idade == 18:
    print(f'Você tem {idade} anos. É a HORA EXATA de se alistar no serviço militar!')
else:
    saldo = idade - 18
    print(f'Já passou do tempo de alistamento! Já se passaram {saldo} ano(s) do prazo.')