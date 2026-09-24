# Solicita ao utilizador quantos termos da sequência ele quer visualizar
n = int(input('Quantos termos deseja mostrar: '))

# Inicializa os dois primeiros termos da Sequência de Fibonacci
t1 = 0
t2 = 1

# Exibe os dois primeiros termos na tela sem pular linha
print(f'{t1} -> {t2} -> ', end='')

# Contador começa em 3, pois os termos 1 e 2 já foram exibidos acima
cont = 3

# Laço que executa enquanto o contador for menor ou igual ao total desejado (n)
while cont <= n:
    # O próximo termo (t3) é a soma dos dois anteriores
    t3 = t1 + t2
    print(f'{t3} -> ', end='')

    # "Troca de bastão": avança os valores das variáveis para a próxima soma
    t1 = t2
    t2 = t3

    # Incrementa o contador de termos exibidos
    cont += 1

print('FIM')