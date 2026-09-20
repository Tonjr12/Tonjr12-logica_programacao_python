# Solicita um número inteiro ao utilizador e converte a entrada para int
n = int(input('Digite um número para calcular seu Fatorial: '))

# Inicializa o contador 'c' com o mesmo valor do número digitado
c = n

# Inicializa a variável 'f' com 1 (elemento neutro da multiplicação)
f = 1

# Exibe o texto inicial do cálculo sem pular de linha (end='')
print(f'Calculando {n}! = ', end='')

# Laço que executa enquanto o contador for maior que zero
while c > 0:
    # Exibe o valor atual do contador na tela sem pular de linha
    print(f'{c}', end='')

    # Operador ternário: imprime ' x ' se c > 1, ou ' = ' quando chega ao último número (1)
    print(' x ' if c > 1 else ' = ', end='')

    # Multiplica e acumula o valor atual do contador na variável 'f' (f = f * c)
    f *= c

    # Decrementa o contador em 1 a cada iteração para avançar até ao final
    c -= 1

# Exibe o resultado final acumulado do fatorial
print(f'{f}')