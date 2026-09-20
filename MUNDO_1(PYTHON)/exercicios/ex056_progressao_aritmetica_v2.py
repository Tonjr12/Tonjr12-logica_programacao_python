# Lê o primeiro termo da Progressão Aritmética
primeiro = int(input('Digite o primeiro termo: '))

# Lê a razão da PA
razao = int(input('Digite a razão da PA: '))

# Inicializa o termo atual com o primeiro valor digitado
termo = primeiro

# Contador para controlar a quantidade de termos exibidos (começa no 1)
cont = 1

# Laço que executa enquanto o contador for menor ou igual a 10
while cont <= 10:
    # Exibe o termo atual seguido de uma seta sem pular linha
    print(f'{termo} -> ', end='')

    # Atualiza o termo somando a razão para o próximo passo
    termo += razao

    # Incrementa o contador de termos exibidos
    cont += 1

# Exibe a mensagem de fim após exibir os 10 termos
print('FIM')