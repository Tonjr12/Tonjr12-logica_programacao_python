# Leitura inicial dos números
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

opcao = 0

# Laço principal do menu
while opcao != 5:
    print('\n' + '=' * 30)
    print('      MENU DE OPÇÕES')
    print('=' * 30)
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos números')
    print('[ 5 ] Sair do programa')

    opcao = int(input('>>>> Qual é a sua opção? '))

    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}.')
    elif opcao == 2:
        multiplicacao = n1 * n2
        print(f'O resultado de {n1} x {n2} é {multiplicacao}.')
    elif opcao == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2}, o maior valor é {n1}.')
        elif n2 > n1:
            print(f'Entre {n1} e {n2}, o maior valor é {n2}.')
        else:
            print(f'Ambos os números são iguais ({n1}).')
    elif opcao == 4:
        print('Informe os novos números:')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif opcao == 5:
        print('Finalizando o programa...')
    else:
        print('Opção inválida. Tente novamente.')

print('Fim do programa! Volte sempre.')