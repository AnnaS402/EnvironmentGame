import pygame, sys
from pygame.locals import *

img = pygame.image.load("running/fox1running.png")
display_width = 1000
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
sprite_image = pygame.image.load("running/fox1running.png")
rect = sprite_image.get_rect()
gameDisplay.blit(sprite_image, rect)

while True: #main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
