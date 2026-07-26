soma = contador = 0

while True:
    numero = int(input('Digite um número:'))
    if numero == 999:
        break

    contador += 1
    soma += numero


print(f'A soma total dos números digitados foi {soma} e foram digitados : {contador} números.')


