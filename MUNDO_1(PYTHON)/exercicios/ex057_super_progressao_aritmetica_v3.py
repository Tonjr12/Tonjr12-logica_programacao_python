# Leitura dos dados iniciais da PA
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))

# Variáveis de controle
termo = primeiro
cont = 1
total = 0
mais = 10  # Começa pedindo os 10 primeiros termos

# Laço principal: roda enquanto 'mais' for diferente de 0
while mais != 0:
    # Acumula a quantidade de termos que o usuário quer ver
    total += mais

    # Exibe os termos solicitados na rodada atual
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1

    print('PAUSA')
    # Pergunta quantos termos a mais o usuário quer ver
    mais = int(input('Quantos termos você quer mostrar a mais? '))

# Mensagem final com o totalizador de termos exibidos
print(f'Progressão finalizada com {total} termos mostrados.')