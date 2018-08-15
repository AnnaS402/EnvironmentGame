import pygame, sys
from pygame.locals import *
from colors import *

img = pygame.image.load("coastalForest.png")
# img.center(0,0)
pygame.init()
# pygame.font.init()
# myfont = pygame.font.SysFont("Comic Sans MS", 30)

gameDisplay.fill(GREEN)

infobox = pygame.image.load("coastalForest.png")
# textsurface = myfont.render("Text color", False, (RED))
infobox = pygame.transform.scale(infobox, (600, 400))
rect = infobox.get_rect()
rect.center = (500, 300)
# infobox.center(0,0)

gameDisplay.blit(infobox, rect)
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

intro = True

while intro: #the main loop
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            sys.exit()


    # screen.blit(textsurface, (0,0))
    # text_to_screen(screen, "please work", 100, 200)
    pygame.display.update()
