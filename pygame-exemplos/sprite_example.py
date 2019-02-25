import pygame
import random
import os

WIDTH = 800
HEIGHT = 600
FPS = 30

#Cores muito usadas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")


class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2,  HEIGHT / 2)
        self.y_speed = 5

    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed

        if self.rect.bottom > HEIGHT - 150:
            self.y_speed = -self.y_speed

        if self.rect.top < 150:
            self.y_speed = -self.y_speed

        if self.rect.left > WIDTH:
            self.rect.right = 0

    def __repr__(self):
        return f'Sprite - > x:{self.rect.x} y:{self.rect.y}'


#Inicializando pygame e criando uma janela
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My game')
clock = pygame.time.Clock()




#Lista de sprites
sp = Sprite()
all_sprites = pygame.sprite.Group()
all_sprites.add(sp)



#Loop do jogo
running = True

while running:


    clock.tick(FPS)

    #Processa as entradas (eventos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Atualiza
    all_sprites.update()


    #Desenha / renderiza
    screen.fill(BLUE)
    all_sprites.draw(screen)

    pygame.display.flip()
