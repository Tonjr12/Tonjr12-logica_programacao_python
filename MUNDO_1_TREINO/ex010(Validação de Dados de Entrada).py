# Pedimos a entrada, limpamos espaços, deixamos em maiúsculas e pegamos só a PRIMEIRA letra ([0])
sexo = input("Qual seu sexo?").upper().strip()[0]

# Enquanto a primeira letra NÃO for 'M' e NÃO for 'F', ele repete
while sexo not in "FM":
    print('seu sexo invalido digite novamente')
    sexo = input("Qual seu sexo?").upper().strip()[0]
print('sexo cadastrado com sucesso')