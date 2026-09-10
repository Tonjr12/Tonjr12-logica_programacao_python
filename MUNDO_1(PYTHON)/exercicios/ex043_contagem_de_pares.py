# Abordagem 1: Usando o passo do range() para saltar de 2 em 2
# Trata o último número (50) separadamente para formatar com ponto final e quebra de linha
for c in range(0, 52, 2):
    if c == 50:
        print(c, end='.\n')  # Imprime o 50 com ponto e pula de linha
    else:
        print(c, end=',')    # Imprime os demais valores separados por vírgula

# Abordagem 2: Varrendo todos os números do intervalo (0 a 50)
# e filtrando apenas os pares com o operador de resto da divisão (%)
for c in range(0, 51):
    if c % 2 == 0:
        print(c, end=' ')    # Imprime apenas os pares separados por espaço