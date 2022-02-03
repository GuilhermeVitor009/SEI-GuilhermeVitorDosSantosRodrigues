import pygame
from pygame.locals import *

import sys

pygame.init()

img_fundo = pygame.image.load('fundor.jpg')

img_drone = pygame.image.load('drone-removebg-preview.png')

larg_bk = img_fundo.get_rect().width
altura_bk = img_fundo.get_rect().height

render_tela = 10

tela = pygame.display.set_mode((larg_bk, altura_bk))

pygame.display.set_caption('Teste de movimento do drone')

angulo = 0

running = True

pos = [0, 0]
rpos = [0, 0]

clock = pygame.time.Clock()

while running:

    clock.tick(30)

    tela.fill([0, 0, 0])

    tela.blit(img_fundo, (0, 0))

    #tela.blit(img_drone, pos)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    comando = pygame.key.get_pressed()
    if comando[pygame.K_LEFT]:
        pos[0] -= render_tela
    if comando[pygame.K_RIGHT]:
        pos[0] += render_tela
    if comando[pygame.K_UP]:
        pos[1] -= render_tela
    if comando[pygame.K_DOWN]:
        pos[1] += render_tela
    if comando[pygame.K_a]:
        angulo += 10
    if comando[pygame.K_z]:
        angulo -= 10

    drone_rodado = pygame.transform.rotate(img_drone, angulo)

    pos_rotacao = (pos[0]-drone_rodado.get_width()/2,  pos[1] - drone_rodado.get_height()/2)

    tela.blit(drone_rodado, pos_rotacao)
    pygame.time.delay(10)
    
    pygame.display.update()
