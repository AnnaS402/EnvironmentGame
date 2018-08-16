import pygame, sys
from pygame.locals import *
from colors import *


pygame.init()

#scales background to take up gamedisplay
def desert():
    background_image2 = pygame.image.load("background1.png").convert()

    background_image2 = pygame.transform.scale(background_image2, (1000, 600))
    rect = background_image2.get_rect()

    gameDisplay.blit(background_image2, rect)

while True: #the main loop
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            sys.exit()
    desert()
