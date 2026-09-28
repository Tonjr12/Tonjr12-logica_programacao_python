# Laço infinito para continuar pedindo números até que uma condição de parada ocorra
while True:
    n = int(input('Quer ver a tabuada de qual valor? (Digite um valor negativo para encerrar): '))

    # Condição de parada (flag): se o número for negativo, interrompe o laço com break
    if n < 0:
        print('Programa encerrado. Volte sempre!')
        break

    print('-' * 30)
    # Laço for para calcular e exibir a tabuada de 1 a 10 do número informado
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 30)

print('FIM')