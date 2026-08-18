# Solicita o nome completo e remove espaços desnecessários nas pontas
nome = input('Digite seu nome completo: ').strip()

# Converte o nome para maiúsculas e verifica se a palavra 'SILVA' está contida nele
resultado = 'SILVA' in nome.upper()

# Exibe True se o nome contiver 'SILVA' ou False se não contiver
print(f'Seu nome tem "SILVA"? {resultado}')