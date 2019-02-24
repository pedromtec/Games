import pygame
import random

WIDTH = 680
HEIGHT = 480
FPS = 30

#Cores muito usadas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2,  HEIGHT / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0


#Inicializando pygame e criando uma janela
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My game')
clock = pygame.time.Clock()


sp = Sprite()

#Lista de sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(sp)

#Loop do jogo
running = True



print(sp.rect.x)
print(sp.rect.left)
print(sp.rect.y)

while running:


    clock.tick(FPS)

    #Processa as entradas (eventos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Atualiza
    all_sprites.update()

    #Desenha / renderiza
    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()
