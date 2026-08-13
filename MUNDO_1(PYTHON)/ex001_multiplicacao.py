# Solicita o primeiro número ao usuário e converte o texto digitado para inteiro (int)
n1 = int(input('digite um numero: '))

# Solicita o segundo número ao usuário e converte o texto digitado para inteiro (int)
n2 = int(input('digite outro numero: '))

# Realiza a multiplicação entre n1 e n2 e guarda o valor na variável 'multiplicacao'
multiplicacao = n1 * n2

# Exibe na tela uma mensagem formatada (f-string) mostrando a conta e o resultado
print(f'A multiplicação entre {n1} e {n2} resulta em {multiplicacao}')

# Exibe na tela qual é a classe/tipo primitivo dos dados armazenados na variável 'multiplicacao'
print(f'O tipo primitivo desse resultado é {type(multiplicacao)}')