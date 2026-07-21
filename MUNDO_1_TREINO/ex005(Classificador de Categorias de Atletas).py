idade=int(input('Qual a sua idade? '))
if idade <= 11:
    print(f'Jogador com idade de {idade} anos Até 11 anos: Categoria PRÉ-MIRIM ')
elif  12 <= idade <= 14:
    print(f'Jogador com idade de {idade} anos De 12 até 14 anos: Categoria INFANTIL')
elif 15 <= idade <= 17:
    print(f'Jogador com idade de {idade} anos  De 15 até 17 anos: Categoria JUVENIL')
elif idade >= 18:
    print(f'Jogador com idade de {idade} anos A partir de 18 anos: Categoria PROFISSIONAL ')

