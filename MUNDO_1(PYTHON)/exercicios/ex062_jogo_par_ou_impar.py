from random import randint

# Inicializa o contador de vitórias consecutivas do jogador
cont = 0

# Laço infinito para manter o jogo a correr até o jogador perder
while True:
    # Lê a escolha do utilizador (Par ou Ímpar) e formata para maiúscula ('P' ou 'I')
    jogar_escolha = input('Par ou Ímpar? [P/I] ').strip().upper()[0]

    # O computador gera um número aleatório entre 0 e 10
    computador = randint(0, 10)

    # O jogador digita o seu número
    jogar_numero = int(input('Digite um número de 0 a 10: '))

    # Soma os valores do jogador e do computador
    soma = computador + jogar_numero

    # Verifica se a soma é par ou ímpar
    if soma % 2 == 0:
        tipo = 'P'
        print(f'Deu Par! A soma foi {soma} (Computador jogou {computador} e você {jogar_numero})')
    else:
        tipo = 'I'
        print(f'Deu Ímpar! A soma foi {soma} (Computador jogou {computador} e você {jogar_numero})')

    # Compara a escolha do jogador com o resultado da ronda
    if jogar_escolha == tipo:
        print('Você VENCEU nesta ronda!\n---')
        cont += 1  # Incrementa as vitórias consecutivas
    else:
        print('Você PERDEU!')
        break  # Interrompe o laço infinito quando o jogador perde

# Exibe o resultado final com o total de vitórias
print(f'Fim do jogo! Você venceu {cont} vezes consecutivas.')