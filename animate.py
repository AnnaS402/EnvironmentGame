import pygame
from pygame.locals import *
from pygame.time import *

pygame.init()

screen = pygame.display.set_mode((128, 128))
clock = pygame.time.Clock()

counter, text = 30, '30'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

while True:
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT:
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'START!'
        if e.type == pygame.QUIT: break
    else:
        screen.fill((255, 255, 255))
        screen.blit(font.render(text, True, (0, 0, 0)), (18, 48))
        pygame.display.flip()
        clock.tick(60)
        continue
    break
