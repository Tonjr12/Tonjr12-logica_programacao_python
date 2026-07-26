from rich import print
while True:
    sexo = ' '
    while sexo not in "FM":
        sexo = input("Qual seu sexo?").upper().strip()[0]
        for c in range(1, 5):
            if sexo == "F":
                print('feminino')
            if sexo == "M":
                print('minino')

    break

if sexo == "M":
    print('você é macho')
if sexo == "F":
    print(f'[red]você é fêmea[/]')