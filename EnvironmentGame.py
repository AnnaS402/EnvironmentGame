import pygame, sys
from pygame.locals import *

# import map.py

pygame.init()
# pygame.display.set_caption('Save the Planet')

display_width = 1000
display_height = 600

GREEN = (0, 128, 0)
GREEN2 = (0, 80, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
# gameDisplay.fill(GREEN)


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

def button(msg,x,y,w,h,ic,ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)

    if (x+w > mouse[0] > x) and (y+h > mouse[1] > y):
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
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

    gameDisplay.fill(GREEN)
    largeText = pygame.font.SysFont('freesansbold.ttf', 175)
    TextSurf, TextRect = text_objects("Save the World", largeText)
    TextRect.center = ((display_width/2),(display_height/2)- 75)
    gameDisplay.blit(TextSurf, TextRect)

    button("GO!", 450, 400, 100, 50, WHITE, GREEN2)

    pygame.display.update()





#
# while True: # main game loop
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.display.update()
