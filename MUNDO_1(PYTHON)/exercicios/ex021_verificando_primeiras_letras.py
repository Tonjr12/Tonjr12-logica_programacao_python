# Solicita o nome da cidade e remove espaços antes e depois do texto
cidade = input('Em que cidade você nasceu? ').strip()

# Pega os 5 primeiros caracteres ([:5]), converte para maiúsculas (.upper()) e compara com 'SANTO'
resultado = cidade[:5].upper() == 'SANTO'

# Exibe True se a cidade começar com 'SANTO' ou False se não começar
print(f'A cidade começa com "SANTO"? {resultado}')