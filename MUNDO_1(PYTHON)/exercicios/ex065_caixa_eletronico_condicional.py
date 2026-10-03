nota_50 = 50
n_50 = 0
nota_20 = 20
n_20 = 0
nota_10 = 10
n_10 = 0
nota_1 = 1
n_1 = 0
contador = 0
valor_saque = int(input('Digite o valor do saque: '))
print ('valor do saque: ', valor_saque)
while True :
    if valor_saque >= nota_50 :
        valor_saque -= nota_50
        n_50 += 1

    elif valor_saque >= nota_20 :
        valor_saque -= nota_20
        n_20+= 1

    elif valor_saque >= nota_10 :
        valor_saque -= nota_10
        n_10+= 1
    elif valor_saque >= nota_1 :
        valor_saque -= nota_1
        n_1 += 1


    elif valor_saque == 0 :
            break


print(f'foram entregues {n_50} notas de R$ 50')
print(f'foram entregues {n_20} notas de R$ 20')
print(f'foram entregues {n_10} notas de R$ 10')
print(f'foram entregues {n_1} notas de R$ 1')
