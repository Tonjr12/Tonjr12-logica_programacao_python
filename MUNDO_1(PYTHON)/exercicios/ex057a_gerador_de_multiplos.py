# Lê o número base e o valor inicial do múltiplo
n = int(input("Digite um número inteiro: "))
multiplos = int(input("Digite o múltiplo inicial: "))

# Inicializa as variáveis de controle
mult = multiplos
mais = 10
contador = 1
total = 0

# Laço principal: roda até que 'mais' seja igual a 0
while mais != 0:
    # Acumula a quantidade total de termos que o usuário solicitou
    total += mais

    # Laço interno: exibe os múltiplos até atingir o limite acumulado
    while contador <= total:
        print(f'{mult} -> ', end='')
        contador += 1
        mult += multiplos  # Soma o valor do múltiplo para gerar a sequência correta

    print('PAUSA')
    # Solicita novos termos ou 0 para encerrar
    mais = int(input("Quantos múltiplos a mais quer ver? (0 encerra): "))

# Mensagem final com o resumo
print(f'Você viu o número {n}, múltiplos de {multiplos}, total {total} vezes!.')