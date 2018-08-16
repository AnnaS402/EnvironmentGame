import pygame, sys
from pygame.locals import *
from colors import *


pygame.init()

#scales background to take up gamedisplay

background_image = pygame.image.load("background1.png").convert()

background_image = pygame.transform.scale(background_image, (1000, 600))
rect = background_image.get_rect()

gameDisplay.blit(background_image, rect)

while intro: #the main loop
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            sys.exit()
