import pygame, sys
from pygame.locals import *


display_width = 1000
display_height = 600

GREEN = (0, 128, 0)
GREEN2 = (0, 80, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


gameDisplay = pygame.display.set_mode((display_width, display_height))

game = True
def black():
    gameDisplay.fill(BLACK)
    pygame.display.update()
