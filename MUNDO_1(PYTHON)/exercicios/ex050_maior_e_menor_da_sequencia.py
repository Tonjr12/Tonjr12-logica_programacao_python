# Inicializa as variáveis de controle
maior = 0
menor = 0
nome_pesado = ''
nome_leve = ''

# Laço para ler os dados de 5 pessoas
for c in range(1, 6):
    nome = input(f'Digite o nome da {c}ª pessoa: ').strip()
    peso = float(input(f'Digite o peso de {nome} (kg): '))

    # Na primeira repetição, define o primeiro peso como maior e menor
    if c == 1:
        maior = peso
        menor = peso
        nome_pesado = nome
        nome_leve = nome
    else:
        # Atualiza o maior peso se a leitura atual for superior
        if peso > maior:
            maior = peso
            nome_pesado = nome
        # Atualiza o menor peso se a leitura atual for inferior
        if peso < menor:
            menor = peso
            nome_leve = nome

print('=' * 45)
print(f'Maior peso: {nome_pesado} com {maior:.1f} kg.')
print(f'Menor peso: {nome_leve} com {menor:.1f} kg.')
print('=' * 45)