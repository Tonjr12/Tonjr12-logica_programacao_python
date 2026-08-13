
numero = int(input('Digite um número: '))

antecessor = numero - 1
sucessor = numero + 1
dobro = numero * 2
triplo = numero * 3
raiz = numero ** 0.5
# aqui fiz o resultado com tuplas dentro de listas
resultado = [
    ("Antecessor", antecessor),
    ("Sucessor", sucessor),
    ("Dobro", dobro),
    ("Triplo", triplo),
    ("Raiz Quadrada", raiz)
]

for indice, (descricao, valor) in enumerate(resultado, start=1):
    print(f'{indice}. {descricao}: {valor:.2f}')