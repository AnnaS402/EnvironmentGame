import pygame, sys
from pygame.locals import *
from colors import *
# from EnvironmentGame import button

def forest():
    img = pygame.image.load("coastalForest.png")
    # img.center(0,0)
    pygame.init()
    # pygame.font.init()
    # myfont = pygame.font.SysFont("Comic Sans MS", 30)
    #
    # gameDisplay.fill(GREEN)

    # forest()
    infobox = pygame.image.load("coastalForest.png")
    # textsurface = myfont.render("Text color", False, (RED))
    infobox = pygame.transform.scale(infobox, (600, 400))
    rect = infobox.get_rect()
    rect.center = (500, 300)
    # infobox.center(0,0)

    gameDisplay.blit(infobox, rect)

    #
    # button("EASY", 270, 415, 110, 50, GREY_DARK, GREY_LIGHT, "easy")
    # pygame.draw.rect(gameDisplay, BLACK, (270, 415, 110, 50), 2)
    # button("NORMAL", 445, 415, 110, 50, GREY_DARK, GREY_LIGHT, action = None)
    # pygame.draw.rect(gameDisplay, BLACK, (445, 415, 110, 50), 2)
    # button("HARD", 620, 415, 110, 50, GREY_DARK, GREY_LIGHT, action = None)
    # pygame.draw.rect(gameDisplay, BLACK, (620, 415, 110, 50), 2)

    # forestTextBox = True

def button(msg,x,y,w,h,ic,ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)

    if (x+w > mouse[0] > x) and (y+h > mouse[1] > y):
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            # blackground = background + 1

            if action == "easy":
                print("asdlfj aopw;e jfa;lkdsfaj;lkdsf")
                import game.py

            #     background = background + 1
                # print("ASDF AWRFASDFA DS")
                # map.circle()
            # if background > 0:

                # img = pygame.image.load("EnvironmentGameMap.png").convert()
                #
                # pygame.init()
                #
                # gameDisplay.fill(BLACK)
                #
                # #scales background to take up gamedisplay
                #
                # background_image = pygame.image.load("EnvironmentGameMap.png").convert()
                #
                # background_image = pygame.transform.scale(background_image, (1000, 600))
                # rect = background_image.get_rect()
                #
                # gameDisplay.blit(background_image, rect)

            #
            # elif action == "easy":
            #     gameDisplay.fill(BLACK)
                # map.newMap()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurface = smallText.render(msg, True, BLACK)
    textSurf, textRect = textSurface, textSurface.get_rect()
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
# def text_to_screen(screen, text, x, y, size = 50, color = (200, 0, 0), font_type = "data/fonts/orecrusherexpand.ttf"):
#     # try:
#     text = str(text)
#     font = pygame.font.Font(font_type, size)
#     text = font.render(text, True, color)
#     screen.blit(Text, (x,y))
    # except Exception, e:
    #     print "Font Error, saw it coming"
    #     raise e

# Surface((width, height), flags=0, Surface)
#
# intro = True
#
# while intro: #the main loop
#     for event in pygame.event.get():
#         #print(event)
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#             sys.exit()
#
#
#     # screen.blit(textsurface, (0,0))
#     # text_to_screen(screen, "please work", 100, 200)
#     pygame.display.update()
