import pygame, sys
from pygame.locals import *
img = pygame.image.load("EnvironmentGameMap.png")

pygame.init()

display_width = 1000
display_height = 600

BLACK = (255, 255, 255)
RED = (255, 0, 0)

#background is map

gameDisplay = pygame.display.set_mode((display_width, display_height))
gameDisplay.fill(BLACK)

#scales background to take up gamedisplay

background_image = pygame.image.load("EnvironmentGameMap.png")

background_image = pygame.transform.scale(background_image, (1000, 600))
rect = background_image.get_rect()

gameDisplay.blit(background_image, rect)



#circle with possible play locations

pygame.draw.circle(gameDisplay,(RED),(250, 500), 5)

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
