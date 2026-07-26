from rich import print
maior = homem = mulher = 0
while True:
    sexo = ' '
    while sexo not in "FM":
        sexo = input('digite qual seu sexo:').upper().strip()[0]

    idade = int(input('digite sua idade:'))
    if idade >= 18:
        maior += 1

    if sexo == 'M':
        homem += 1

    if sexo == 'F' and idade < 20:
        mulher += 1

    continuar = ' '
    while continuar  not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]

    if continuar == 'N':
        break

print(f'Maior de idade: [red]{maior}[/] pessoas')
print(f'foram cadastradas [red]{homem}[/] homem(s)')
print(f'foram cadastradas [red]{mulher}[/] mulher(s) com menor de 20 anos')
