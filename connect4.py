import pygame
import sys

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)

NUM_LIN = 6
NUM_COL = 7

def cria_board():
    '''
    Cria tabuleiro
    '''
    board = [[0] * NUM_COL for i in range(NUM_LIN)]
    return board

board = cria_board()

def isValid(coluna):
    '''
    Verifica se a coluna escolhida é válida.
    '''
    return coluna >= 0 and coluna < NUM_COL and board[0][coluna] == 0

def solta_bolinha(bolinha, coluna):
    '''
    Solta a bolinha até chegar ao seu destino
    '''
    linha = 0
    while linha < NUM_LIN and board[linha][coluna] == 0:
        linha+=1
    board[linha-1][coluna] = bolinha

def movimento_vencedor(bolinha):
    '''
    Verifica se um determinado jogador fez um movimento vencedor
    '''
    for i in range(NUM_LIN):
        for j in range(NUM_COL-3):
            if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == bolinha:
                return True

    for j in range(NUM_COL):
        for i in range(NUM_LIN-3):
            if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == bolinha:
                return True

    for i in range(NUM_LIN-3):
        for j in range(NUM_COL-3):
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == bolinha:
                return True

    for i in range(NUM_LIN-3):
        for j in range(NUM_COL-3):
            if board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3] == bolinha:
                return True

    return False


def draw_board():
    for i in range(1, NUM_LIN+1):
        for j in range(NUM_COL):
            cor = BLACK
            if board[i-1][j] == 1:
                cor = VERDE
            elif board[i-1][j] == 2:
                cor = VERMELHO
            pygame.draw.rect(screen, BLUE, (j*TILE_SIZE, i*TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.circle(screen, cor, (j*TILE_SIZE + TILE_SIZE//2, i*TILE_SIZE + TILE_SIZE//2), raio)
    pygame.display.update()


TILE_SIZE = 95
ALTURA = TILE_SIZE * (NUM_LIN+1)
LARGURA = TILE_SIZE * NUM_COL
raio = (TILE_SIZE//2 - 5)


pygame.init()
screen = pygame.display.set_mode((LARGURA, ALTURA))
myfont = pygame.font.SysFont("monospace", 75)

turn = 0
game_over = False

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_x = event.pos[0]
            col = int(pos_x / TILE_SIZE)
            bolinha = turn + 1
            if isValid(col):
                solta_bolinha(bolinha, col)
                if movimento_vencedor(bolinha):
                    cor = VERDE
                    if bolinha == 2:
                        cor = VERMELHO
                    label = myfont.render(f"Player {bolinha} vence!!", 1, cor)
                    screen.blit(label, (30,10))
                    game_over = True
                turn = (turn+1) % 2

    draw_board()
    if game_over:
        pygame.time.wait(3000)
