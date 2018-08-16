import pygame, sys
from pygame.locals import *

img5 = pygame.image.load("sprites/running/fox5running.png")
img4 = pygame.image.load("sprites/running/fox4running.png")
img3 = pygame.image.load("sprites/running/fox3running.png")
img2 = pygame.image.load("sprites/running/fox2running.png")
img1 = pygame.image.load("sprites/running/fox1running.png")

display_width = 1000
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))

sprite_image5 = pygame.image.load("sprites/running/fox5running.png")
sprite_image4 = pygame.image.load("sprites/running/fox4running.png")
sprite_image3 = pygame.image.load("sprites/running/fox3running.png")
sprite_image2 = pygame.image.load("sprites/running/fox2running.png")
sprite_image1 = pygame.image.load("sprites/running/fox1running.png")

rect = sprite_image1.get_rect()
gameDisplay.blit(sprite_image1, rect)
gameDisplay.blit(sprite_image2, rect)
gameDisplay.blit(sprite_image3, rect)
gameDisplay.blit(sprite_image4, rect)
gameDisplay.blit(sprite_image5, rect)

while True: #main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
