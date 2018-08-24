import pygame, sys
from pygame.locals import *

display_width = 1000
display_height = 600

GREEN = (0, 128, 0)
GREEN2 = (0, 80, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY_LIGHT = (224, 224, 224)
GREY_DARK = (192, 192, 192)

gameDisplay = pygame.display.set_mode((display_width, display_height))

forestTextBox = False
permenantColor = False
RedorGreen = RED

ChoiceA = ["Charles Darwin", "True", "Argentina", "They had the fox as a pet once", "True", "Wolves, racoons, bears"]
ChoiceB = ["Anne Darwin", "False", "Chile", "They were their favorite animal", "False", "Owls, eagles, hawks"]
ChoiceC = ["Emma Darwin", 0, "North America", "They discovered, collected, and observed them", 0, "Domestic dogs, pumas, large raptors"]
ChoiceD = ["Carl Linnaeus", 0, "Canada", "They looked like a fox", 0, "Coyotes, bobcats, hyenas"]

Qnum = 0
CorrectColor = False
CorrectColorA = False
CorrectColorB = False
CorrectColorC = False

WrongColorA = False
WrongColorB = False
WrongColorC = False
WrongColorD = False

checkFlag = False
questionPause = False
anyClicked = False
theactualend = False
first6 = True
firstflag = True
timer = .5
