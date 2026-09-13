#tirar os espaços das pontas e deixar com letras maisculas
frase = str(input('Digite uma frase: ')).strip().upper()
#separar a frase em palvras em listas
separar_em_palvras = frase.split()
print(separar_em_palvras)
juntar_palavras = '' .join(separar_em_palvras)
print(juntar_palavras)
invertendo_palavras = juntar_palavras[::-1]
print(invertendo_palavras)
if invertendo_palavras == juntar_palavras:
    print('É palindromo')
else:
    print('Não é palindromo')