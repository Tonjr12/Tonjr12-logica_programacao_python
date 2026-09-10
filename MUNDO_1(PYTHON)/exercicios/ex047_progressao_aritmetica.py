primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Qual a razao: '))
for c in range(1, 11):
    print(primeiro_termo, end=' -> ')
    primeiro_termo += razao

print('acabou')
