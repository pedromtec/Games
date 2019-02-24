import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

#Cores muito usadas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



#Inicializando pygame e criando uma janela
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My game')
clock = pygame.time.Clock()


#Loop do jogo
running = True

while running:


    clock.tick(FPS)

    #Processa as entradas (eventos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Atualiza

    #Desenha / renderiza
    screen.fill(BLACK)
    pygame.display.flip()
