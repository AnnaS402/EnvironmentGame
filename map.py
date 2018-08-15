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

def circle():
    pygame.draw.circle(gameDisplay,(RED),(250, 500), 5)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)

    if (250+5 > mouse[0] > 250) and (500+5 > mouse[1] > 500):
        if click[0] == 1:
            print("sflj ao;eijfald;kfja")
            gameDisplay.fill(RED)

intro = True

while intro: #the main loop
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            sys.exit()
    circle()



# while True: # main game loop
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()



    pygame.display.update()
