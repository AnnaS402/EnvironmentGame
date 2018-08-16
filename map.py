import pygame, sys
from pygame.locals import *
from forestInfo import forest
from colors import *



img = pygame.image.load("EnvironmentGameMap.png").convert()

pygame.init()

gameDisplay.fill(BLACK)

#scales background to take up gamedisplay

background_image = pygame.image.load("EnvironmentGameMap.png").convert()

background_image = pygame.transform.scale(background_image, (1000, 600))
rect = background_image.get_rect()

gameDisplay.blit(background_image, rect)

#circle with possible play locations
forestTextBox = False
def circle(forestTextBox):
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
        forestTextBox = True
    if forestTextBox == True:
        return forestTextBox
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



sideScrollGame1 = False
sideScrollGame2 = False
sideScrollGame3 = False
def button(sideScrollGame1, sideScrollGame2, sideScrollGame3, forestTextBox, msg,x,y,w,h,ic,ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)

    if (x+w > mouse[0] > x) and (y+h > mouse[1] > y):
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            # blackground = background + 1

            if action == "easy":
                gameDisplay.fill(WHITE)
                pygame.display.update()

                print("asdlfj aopw;e jfa;lkdsfaj;lkdsf")
                sideScrollGame1 = True
                # forestTextBox = False
                return sideScrollGame1
                # theGame()
                # pygame.display.update()
                # import game.py
                # pygame.display.update()
            elif action == "normal":
                gameDisplay.fill(WHITE)
                pygame.display.update()

                print("asdlfj aopw;e jfa;lkdsfaj;lkdsf")
                sideScrollGame2 = True
                # forestTextBox = False
                return sideScrollGame2

            elif action == "hard":
                gameDisplay.fill(WHITE)
                pygame.display.update()

                print("asdlfj aopw;e jfa;lkdsfaj;lkdsf")
                sideScrollGame3 = True
                # forestTextBox = False
                return sideScrollGame3

    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurface = smallText.render(msg, True, BLACK)
    textSurf, textRect = textSurface, textSurface.get_rect()
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

intro = True



while intro: #the main loop
    print(forestTextBox)
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            sys.exit()

    forestTextBox = circle(forestTextBox)

    # sideScrollGame1 = sideScrollGame
    # sideScrollGame2 = sideScrollGame
    # sideScrollGame3 = sideScrollGame

    if forestTextBox == True:
        print("10192837904879135098619845")
        sideScrollGame1 = button(sideScrollGame1, sideScrollGame2, sideScrollGame3, forestTextBox, "EASY", 270, 415, 110, 50, GREY_DARK, GREY_LIGHT, "easy")
        pygame.draw.rect(gameDisplay, BLACK, (270, 415, 110, 50), 2)
        sideScrollGame2 = button(sideScrollGame1, sideScrollGame2, sideScrollGame3, forestTextBox, "NORMAL", 445, 415, 110, 50, GREY_DARK, GREY_LIGHT, "normal")
        pygame.draw.rect(gameDisplay, BLACK, (445, 415, 110, 50), 2)
        sideScrollGame3 = button(sideScrollGame1, sideScrollGame2, sideScrollGame3, forestTextBox, "HARD", 620, 415, 110, 50, GREY_DARK, GREY_LIGHT, "hard")
        pygame.draw.rect(gameDisplay, BLACK, (620, 415, 110, 50), 2)



        # gameDisplay.fill(WHITE)
    if sideScrollGame1 == True or sideScrollGame2 == True or sideScrollGame3 == True:
        forestTextBox = False
        background_image2 = pygame.image.load("background1.png").convert()

        background_image2 = pygame.transform.scale(background_image2, (1000, 600))
        rect = background_image2.get_rect()

        gameDisplay.blit(background_image2, rect)

    # else:
    # gameDisplay.blit(infobox, (0,0)
    # gameDisplay.blit(background_image, (0,0))




# while True: # main game loop
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()



    pygame.display.update()
