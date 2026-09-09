from time import sleep

# Laço for contando de 10 até 0 de trás para frente (passo -1)
for c in range(10, -1, -1):
    print(c)
    sleep(1) # Pausa de 1 segundo entre cada número

# Mensagem final executada após o término do laço
print('BUM! BUM! POOW! 🎆')