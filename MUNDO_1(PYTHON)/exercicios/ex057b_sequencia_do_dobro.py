# Lê o número inicial da sequência
n = int(input('Digite um número inteiro: '))

# Inicializa as variáveis de controle
termo = n
cont = 1
total = 0
mais = 10  # Exibe 10 números na primeira rodada

# Laço principal: roda enquanto o usuário solicitar novos números
while mais != 0:
    # Acumula a quantidade total de termos solicitados
    total += mais

    # Laço interno: exibe a sequência dobrando a cada passo
    while cont <= total:
        print(f'{termo} -> ', end='')
        cont += 1
        termo *= 2  # Multiplica por 2 para gerar o próximo dobro da sequência

    print('PAUSA')
    # Solicita a quantidade adicional de termos
    mais = int(input('Quantos números a mais? (0 encerra): '))

# Exibe a mensagem final com o resumo e o último número da sequência
print(f'\nSequência finalizada! Você viu {total} números e o último termo foi {termo // 2}.')