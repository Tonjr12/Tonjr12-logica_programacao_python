# Exercício 018 — Tocando um Áudio MP3

* **Objetivo:** Abrir e reproduzir o áudio de um arquivo MP3 utilizando uma biblioteca externa.
* **Conceito Aplicado:** Instalação de pacotes com `pip`, biblioteca `pygame` (`pygame.mixer.init()`, `load()`, `play()`) e pausa de execução com `input()`.

### 💻 Código Solução

```python
import pygame

# Inicializa o mixer do pygame para permitir a execução de áudios
pygame.mixer.init()

# Carrega o arquivo MP3 localizado na mesma pasta do script
pygame.mixer.music.load('musica.mp3')

# Inicia a reprodução do áudio carregado
pygame.mixer.music.play()

# Mantém o programa em execução enquanto a música toca
input('Aperte ENTER para encerrar a música...')