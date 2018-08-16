import pygame, sys
from pygame.locals import *
from forestInfo import forest

img = pygame.image.load("EnvironmentGameMap.png").convert()

pygame.init()

display_width = 1000
display_height = 600


BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0,0)
gameDisplay = pygame.display.set_mode((display_width, display_height))
gameDisplay.fill(BLACK)

#scales background to take up gamedisplay

background_image = pygame.image.load("EnvironmentGameMap.png").convert()

background_image = pygame.transform.scale(background_image, (1000, 600))
rect = background_image.get_rect()

gameDisplay.blit(background_image, rect)



#circle with possible play locations

def circle():
    # dot =
    pygame.draw.circle(gameDisplay,(RED),(250, 505), 6)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)

    # if (247 > mouse[0] > 253) and (502 > mouse[1] > 508):
    if (253 > mouse[0] > 247) and (508 > mouse[1] > 502):
        pygame.draw.circle(gameDisplay, (RED), (250, 505), 12)
        # pygame.draw.circle.set_alpha((5,5))
        # dotGone = dot.get_at((0,0))
        # dot.set_colorkey(dotGone)
    # else:
    #     pygame.draw.circle(gameDisplay,(RED),(250, 505), 6)
    #     print("123435236525624")
    # else:
    #     pygame.draw.circle(gameDisplay,(RED),(250, 505), 6)

    if (260 > mouse[0] > 240) and (515 > mouse[1] > 495) and click[0] == 1:
        # gameDisplay.set_colorkey(pygame.Color())
        # sfc.set_colorkey(pygame.Color(255,255,255))
        # pygame.draw.circle(gameDisplay,(RED),(250, 505), 6)
        forest()
            # import infotest.py
            # img = pygame.image.load("coastalForest.png")
            # # img.center(0,0)
            # pygame.init()
            # # pygame.font.init()
            # # myfont = pygame.font.SysFont("Comic Sans MS", 30)
            # #
            # # gameDisplay.fill(GREEN)
            #
            # # forest()
            # infobox = pygame.image.load("coastalForest.png")
            # # textsurface = myfont.render("Text color", False, (RED))
            # infobox = pygame.transform.scale(infobox, (600, 400))
            # rect = infobox.get_rect()
            # rect.center = (500, 300)
            # infobox.center(0,0)

            # gameDisplay.blit(infobox, rect)
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
