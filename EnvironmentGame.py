import pygame, sys
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Save the Planet')

display_width = 800
display_height = 600

GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
gameDisplay.fill(GREEN)


def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 90)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

message_display("Save the Planet")

def GO_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def GO_display(text):
    GOtext = pygame.font.Font("freesansbold.ttf", 30)
    TextSurf, TextRect = GO_objects(text, GOtext)
    TextRect.center = ((350, 450))
    gameDisplay.blit(TextSurf, TextRect)

GO_display("Go!")

pygame.draw.rect(gameDisplay, WHITE,(350,450,100,50))



while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
