arquivo = open("jogadores.txt", "a")
usuario = input("Digite o seu nome aqui: ")
email = input("Digite o seu e-mail aqui: ")
arquivo.write("\nUsuario: "+ usuario+ "\nE-mail: "+ email+ "\n")

import pygame, random
from pygame.locals import *

def caixas(caixax, caixay, caixaw, caixah): #Posição do y e x da caixa e altura e largura dela 
    caixa = (caixax, caixay)
    caixa_skin = pygame.Surface((caixaw, caixah))
    caixa_skin = pygame.image.load('midia/imagemalvo.jpg')
    screen.blit(caixa_skin, caixa)

def click(caixax, caixay, caixaw, caixah):
    mouse = pygame.mouse.get_pos()
    if caixax < mouse[0] < caixax + caixaw and caixay < mouse[1] < caixay + caixah:
        print("Clique dentro do alvo")
        status = (STOP) and  (caixax < -60 or caixax > 610)
              
    else:
        print("Clique fora do alvo !!!")
        status = MOVE 
    return caixax, status

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tiro ao alvo')

clock = pygame.time.Clock()

RIGHT = 1
LEFT = 0
MOVE = 1
STOP = 0

white = (255,255,255)
my_direction = RIGHT
status = MOVE
caixax = 0
caixay = random.randint(0, 550)
caixaw, caixah = 50, 50
 
caixas(caixax, caixay, caixaw, caixah)


while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            caixax, status = click(caixax, caixay, caixaw, caixah)

    if my_direction == RIGHT and status == MOVE:
        caixax = caixax + 30
    if my_direction == LEFT and status == MOVE:
        caixax = caixax - 30

    if caixax < -80 or caixax > 620: #Define a posição em que a caixa vai voltar quando sair da tela
        my_direction = random.randint(0, 2)
        if my_direction == 0:
            my_direction = LEFT
            caixax = 610
        if my_direction == 1:
            my_direction = RIGHT
            caixax = -60
        caixay = random.randint(0, 550)


    screen.fill((white))

    caixas(caixax, caixay, caixaw, caixah)

    pygame.display.update()
    