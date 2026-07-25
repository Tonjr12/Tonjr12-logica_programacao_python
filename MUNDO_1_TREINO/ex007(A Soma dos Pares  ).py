soma = 0
for c in range(1,7):
    numero=int(input('Digite um numero: '))
    if numero % 2 == 0:
        soma+=numero

print(f' A soma dos números par è {soma}')