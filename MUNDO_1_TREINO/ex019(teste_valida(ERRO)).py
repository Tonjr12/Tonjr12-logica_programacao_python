while True:
    try:
        idade= int(input('Qual a sua idade : '))
        if idade < 0 :
            print('Idade deve ser maior que zero')

        else:
            print('Idade registrada com sucesso')
            break
    except ValueError:
        print('❌ Ops! Digite apenas números inteiros.')

