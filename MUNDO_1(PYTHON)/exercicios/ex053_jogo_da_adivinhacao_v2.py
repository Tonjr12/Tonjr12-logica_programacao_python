# Importa a função randint para gerar números inteiros aleatórios
from random import randint

# Importa a função colored para aplicar cores aos textos do terminal
from termcolor import colored

# Importa o módulo time para controlar pausas e tempo de execução
import time

# O computador sorteia um número secreto entre 0 e 100
computador = randint(0, 100)

# Variável de controle (flag): define se o jogador acertou o palpite
acertou = False

# Acumulador: conta quantas tentativas o jogador utilizou
palpites = 0

# Laço principal: executa continuamente enquanto a variável 'acertou' for False
while not acertou:
    # Solicita o palpite do jogador imprimindo o texto da pergunta em azul
    jogador = int(input(colored('Qual o seu palpite entre 0 e 100: ', 'blue')))

    # Soma +1 ao contador de palpites a cada nova tentativa enviada
    palpites += 1

    # Verifica se o palpite do jogador é idêntico ao número sorteado
    if jogador == computador:
        # Altera a flag para True, o que quebrará a condição do laço while
        acertou = True
    else:
        # Se o palpite foi MAIOR que o número do computador
        if jogador > computador:
            # Exibe a dica "Menos..." na cor vermelha
            print(colored('Menos... Tente mais uma vez', 'red'))
        # Se o palpite foi MENOR que o número do computador
        elif jogador < computador:
            # Exibe a dica "Mais..." na cor amarela
            print(colored('Mais... Tente mais uma vez', 'yellow'))

# Guarda a mensagem de vitória final em uma variável de texto (f-string)
mensagem = f'Você acertou com {palpites} palpites.'

# Laço para criar o efeito visual de texto piscando 5 vezes no terminal
for _ in range(5):
    # Imprime a mensagem em verde e negrito sem pular linha (end=''), forçando a saída imediata (flush=True)
    print(colored(f'\r{mensagem}', 'green', attrs=['bold']), end='', flush=True)

    # Pausa a execução do programa por 0.4 segundos com o texto visível
    time.sleep(0.4)

    # Sobrescreve a linha do terminal com espaços em branco (\r volta o cursor ao início da linha)
    print('\r' + ' ' * len(mensagem), end='', flush=True)

    # Pausa a execução por 0.3 segundos com a linha "invisível"
    time.sleep(0.3)

# Imprime a mensagem final fixa em verde e negrito para encerrar o programa
print(colored(f'\r{mensagem}', 'green', attrs=['bold']))