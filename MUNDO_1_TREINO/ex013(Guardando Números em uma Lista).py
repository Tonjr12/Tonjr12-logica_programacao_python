numeros = []
for c in range(1, 6):
    numeros.append(int(input('digite um numero:')))

media = sum(numeros)/len(numeros)
#A lista completa digitada.
print(numeros)
print(f'O maior valor da lista usando max() é: {max(numeros)}')

print(f'O menor valor da lista usando min() é : {min(numeros)}')

print(f'A média de todos os valores (dica: sum() / len() é  {sum(numeros):.2f}')

print(f'A média de todos os valores é {sum(numeros) / len(numeros):.2f}')
print(f'A média de todos os valores é {media:.2f}')