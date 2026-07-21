ano_atual=int(input('digite em que ano nós estamos?'))
ano_nascimento=int(input('digite o ano de nascimento?'))
idade=ano_atual-ano_nascimento

print(f'sua idade é {idade}. Maior de idade {idade>=18}:')
