import pygame, sys
from pygame.locals import *
from colors import *
# import map



pygame.init()

# pygame.display.set_caption('Save the Planet')

gameDisplay.fill(GREEN)


def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

# def message_display(text):
#     largeText = pygame.font.Font('freesansbold.ttf', 90)
#     TextSurf, TextRect = text_objects(text, largeText)
#     TextRect.center = ((display_width/2), (display_height/2))
#     gameDisplay.blit(TextSurf, TextRect)
#
# message_display("Save the Planet")

# def GO_objects(text, font):
#     textSurface = font.render(text, True, BLACK)
#     return textSurface, textSurface.get_rect()
#
# pygame.draw.rect(gameDisplay, WHITE,(350, 450, 100,50))
#
# def GO_display(text):
#     GOtext = pygame.font.Font("freesansbold.ttf", 30)
#     TextSurf, TextRect = GO_objects(text, GOtext)
#     TextRect.center = ((400, 475))
#     gameDisplay.blit(TextSurf, TextRect)
#
# GO_display("Go!")
# background = 0

def button(msg,x,y,w,h,ic,ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)

    if (x+w > mouse[0] > x) and (y+h > mouse[1] > y):
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            # blackground = background + 1

            if action == "map":
                import map.py
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

    smallText = pygame.font.Font("OstrichSans-Bold.otf", 40)
    textSurface = smallText.render(msg, True, BLACK)
    textSurf, textRect = textSurface, textSurface.get_rect()
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)



intro = True

while intro: #the main loop
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            sys.exit()

    # if background < 0:
    #     gameDisplay.fill(BLACK)
    # else:
    # gameDisplay.fill(GREEN)


    largeText = pygame.font.Font("OstrichSans-Bold.otf", 150)
    TextSurf, TextRect = text_objects("Save the World", largeText)
    TextRect.center = ((display_width/2),(display_height/2)- 75)
    gameDisplay.blit(TextSurf, TextRect)

    button("G O !", 450, 400, 100, 50, WHITE, GREY_DARK, "map")

    # if background > 0:
    #     gameDisplay.fill(BLACK)

    pygame.display.update()





#
# while True: # main game loop
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.display.update()
