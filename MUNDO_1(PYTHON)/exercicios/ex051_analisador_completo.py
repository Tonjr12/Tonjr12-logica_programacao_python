idade_total = 0
idade_velho = 0
nome_velho = ''
mulher_nova = 0
for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = str(input('Digite seu nome: ')).strip().upper()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
    idade_total += idade

    if c == 1 and sexo == 'M':
        idade_velho = idade
        nome_velho = nome
    elif sexo == 'M' and idade > idade_velho:
        idade_velho = idade
        nome_velho = nome


    if sexo == 'F' and idade < 20:
        mulher_nova += 1
media = idade_total / 4
print('=' * 30)
print(f'O homem mais velho é o {nome_velho} com {idade_velho} anos.')
print(f'Existem {mulher_nova} mulheres com menos de 20 anos.')
print(f'A média do grupo é: {media}')