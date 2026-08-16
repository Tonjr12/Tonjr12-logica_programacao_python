import pygame

# Inicializa o mixer do pygame para permitir a execução de áudios
pygame.mixer.init()

# Carrega o arquivo MP3 localizado na mesma pasta do script
pygame.mixer.music.load('ex018ton.mp3')

# Inicia a reprodução do áudio carregado
pygame.mixer.music.play()

# Mantém o programa em execução enquanto a música toca (sem o input, o script encerra imediatamente)
input('Aperte ENTER para encerrar a música...')