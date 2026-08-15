import pygame

# 1. Inicializa o Pygame e o sistema de áudio
pygame.init()
pygame.mixer.init()

# 2. Carrega e toca o arquivo MP3
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()

# 3. Mantém o script aberto até você dar ENTER
input('Tocando áudio... Pressione ENTER para encerrar.')