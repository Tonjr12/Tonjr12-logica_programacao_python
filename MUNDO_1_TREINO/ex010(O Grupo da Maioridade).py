anoatual = 2026
maior = 0
menor = 0
for c in range(1,8):
    anoNascimento = int(input('Qual ano você nasceu? '))
    idade = anoatual - anoNascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'{maior} Pessoas são maiores de 18 anos')
print(f'{menor} Pesooas são menores de 18 anos')


