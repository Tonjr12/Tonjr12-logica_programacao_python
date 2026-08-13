
numero = int(input('Digite um número: '))

antecessor = numero - 1
sucessor = numero + 1
dobro = numero * 2
triplo = numero * 3
raiz = numero ** 0.5
# aqui fiz o resultado com dicionário
resultado = {
    "Antecessor": antecessor,
    "Sucessor": sucessor,
    "Dobro": dobro,
    "Triplo": triplo,
    "Raiz Quadrada": raiz
}
""" no for o (indice) que vai aparecer no print é guiado pelo start=1 que esta no enumerate|| a (descrição) e o (valor) do print é guiado pelo (resultado que é o nome do dicionario ) || o (.items()que acompanha o dicionario é o serve pra mostrar a descrição e volor)  """
print(resultado)

for indice, (descricao, valor) in enumerate(resultado.items(), start=1):
    print(f'{indice}. {descricao}: {valor:.2f}')