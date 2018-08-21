import pygame
from pygame.locals import *
import os
import sys
import math
import random as rand
from colors import *
from random import *
# img = pygame.image.load("sprites/running/")
pygame.init()

W, H = 1000, 600
win = pygame.display.set_mode((W,H))
pygame.display.set_caption('Side Scroller')

bg = pygame.image.load(os.path.join("backgrounds/background1.png")).convert()
bgX = 0
bgX2 = bg.get_width()

clock = pygame.time.Clock()

class player(object):
    run = [pygame.image.load(os.path.join("sprites/running/" + 'fox'+ str(x) + 'running' + '.png')) for x in range(1,9)]
    jump = [pygame.image.load(os.path.join("sprites/jumping/" + 'fox' + 'jump' + str(x) + '.png')) for x in range(0,8)]
    # for img in jump:
    #     print("jumping")
    slide = [pygame.image.load(os.path.join("sprites/crouch/crouch0.png")),pygame.image.load(os.path.join("sprites/crouch/crouch1.png")),pygame.image.load(os.path.join("sprites/crouch/crouch2.png")),pygame.image.load(os.path.join("sprites/crouch/crouch2.png")), pygame.image.load(os.path.join("sprites/crouch/crouch2.png")),pygame.image.load(os.path.join("sprites/crouch/crouch2.png")), pygame.image.load(os.path.join("sprites/crouch/crouch2.png")), pygame.image.load(os.path.join("sprites/crouch/crouch2.png")), pygame.image.load(os.path.join("sprites/crouch/crouch2.png")), pygame.image.load(os.path.join("sprites/crouch/crouch2.png")), pygame.image.load(os.path.join("sprites/crouch/crouch2.png")), pygame.image.load(os.path.join("sprites/crouch/crouch2.png")), pygame.image.load(os.path.join("sprites/crouch/crouch2.png")),pygame.image.load(os.path.join("sprites/crouch/crouch2.png")),pygame.image.load(os.path.join("sprites/crouch/crouch2.png")),pygame.image.load(os.path.join("sprites/crouch/crouch2.png")),pygame.image.load(os.path.join("sprites/crouch/crouch2.png")),pygame.image.load(os.path.join("sprites/crouch/crouch2.png")),pygame.image.load(os.path.join("sprites/crouch/crouch2.png")),pygame.image.load(os.path.join("sprites/crouch/crouch2.png")),pygame.image.load(os.path.join("sprites/crouch/crouch2.png")),pygame.image.load(os.path.join("sprites/crouch/crouch2.png"))]
    fall = pygame.image.load(os.path.join("sprites/stop/foxstop.png"))
    jumpList = [1,1,1,1,1,1,1,1,1,
    2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
    3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
    4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    -1,-1,-1,-1,-1,-1,-1,-1,-1,
    -2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,
    -3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,
    -4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4]
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.sliding = False
        self.slideCount = 0
        self.jumpCount = 0
        self.runCount = 0
        self.slideUp = False
        self.falling = False

    def draw(self, win):
        if self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.2
            win.blit(self.jump[self.jumpCount//17], (self.x,self.y))
            self.jumpCount += 1
            if self.jumpCount > 135:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
            self.hitbox = (100, 215, 85, 100)
        elif self.sliding or self.slideUp:
            # if self.slideCount < 20:
            #     print("hello")
                # self.y += 1
            if self.slideCount == 80:
                # self.y -= 19
                self.sliding = False
                self.slideUp = True
            elif self.slideCount >20 and self.slideCount <80:
                self.hitbox = (103, 422, 135, 80)
                self.slideUp = True
            if self.slideCount >= 220:
                self.slideCount = 0
                self.slideUp = False
                self.runCount = 0
                self.hitbox = (94, 381, 165, 100)
            # print(self.slideCount//10)
            win.blit(self.slide[self.slideCount//10], (self.x,self.y))
            self.slideCount += 1

        elif self.falling:
            win.blit(self.fall, (self.x, self.y))

        else:
            if self.runCount > 42:
                self.runCount = 0
            win.blit(self.run[self.runCount//6], (self.x,self.y))
            self.runCount += 1
            self.hitbox = (140, 379, 110, 100)
        # pygame.draw.rect(win, (255, 0,0), self.hitbox, 2)

class trap(object):
    img = [pygame.image.load(os.path.join("obstacles/trap1.png")),pygame.image.load(os.path.join("obstacles/trap2.png")),pygame.image.load(os.path.join("obstacles/trap3.png")),pygame.image.load(os.path.join("obstacles/trap4.png"))]
    def __init__ (self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (x,y,width,height)
        self.count = 0

    def draw(self, win):
        self.hitbox = (self.x + 60, 430, self.width, self.height)
        if self.count >= 8:
            self.count = 0
        win.blit(self.img [self.count//2], (self.x, self.y))
        self.count += 1
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
# collision detection stuff
    def collide(self, rect):
        # print("hitbox 0:", self.hitbox[0])
        # print("hitbox 1:", self.hitbox[1])
        # print("hitbox 2:", self.hitbox[2])
        # print("hitbox 3:", self.hitbox[3])
        if rect[0] + rect [2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False

class sandBlock(trap):
    img = pygame.image.load(os.path.join("obstacles/sandblock.png"))
    def draw(self, win):
        self.hitbox = (self.x + 47, 379, self.width, self.height - 20)
        if self.count >= 8:
            self.count = 0
        win.blit(self.img, (self.x, self.y))
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox,2)

    def collide(self, rect):
        # print("hitbox 0:", rect[0])
        # print("hitbox 1:", rect[1])
        # print("hitbox 2:", rect[2])
        # print("hitbox 3:", rect[3])
        # # print("hitbox 3:", self.hitbox[3])
        # print("hitbox 0:", self.hitbox[0])
        # print("hitbox 1:", self.hitbox[1])
        # print("hitbox 2:", self.hitbox[2])
        # print("hitbox 3:", self.hitbox[3])
        # print(rect)

        if rect[0] + rect [2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[0] > self.hitbox[2]:
                return True
        return False

class flag(trap):
    img = pygame.image.load(os.path.join("obstacles/checkpoint.png"))
    def draw(self, win):
        self.hitbox = (self.x + 50, 350, self.width + 30, 100)
        win.blit(self.img, (self.x, self.y))
        # pygame.draw.rect(win, (255, 0, 00), self.hitbox, 2)
# collision detection stuff
    def collide1(self, rect):
        if rect[0] + rect [2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False
        #
        # if rect[0] + rect [2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
        #     if rect[1] < self.hitbox[3]:
        #         return True
        # return False


def redrawWindow():
    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX2, 0))
    runner.draw(win)
    for x in objects:
        x.draw(win)
    for x in checkpoints:
        x.draw(win)
    pygame.display.update()

#definitions for questiontab
def question_PopUp():

    question = questionBank[randint(0,len(questionBank)-1)]
    questionBank.remove(question)
    done.append(question)
    # Qnum = int(question[21:22])
    if question == "coastalForestQuestion1A.png":
        questionBank.append("coastalForestQuestion4A.png")
    if len(questionBank) == 0:
        questionBank.append("coastalForestQuestion6A.png")
    # print(Qnum)
    # return Qnum

    # print("")
    # print(questionBank)
    # print("")
    # print(done)
    # print("")
    # print("-----------------------------------")

    # questionPop = pygame.image.load(question).convert()
    # questionPop = pygame.transform.scale(questionPop, (600, 400))
    # rect3 = questionPop.get_rect()
    # rect3.center= (500, 300)
    #
    # gameDisplay.blit(questionPop, rect3)
    # checkFlag = False
    return(question)

def whichQuestion(Qnum):
    ansOptions = []
    ansOptions.append(ChoiceA[Qnum-1])
    ansOptions.append(ChoiceB[Qnum-1])
    ansOptions.append(ChoiceC[Qnum-1])
    ansOptions.append(ChoiceD[Qnum-1])
    return ansOptions

def answer(Qnum):
    # print("HEY!!!!!!!!!!!")
    # Qnum = question_PopUp(Qnum)

    if Qnum == 4 or Qnum == 6:
        Letter = "C"
        # if key[pygame.K_c]:
        #     print("correct")
        #     # return
        # else:
        #     print("wrong")
        return Letter

    if Qnum == 1 or Qnum == 2:
        Letter = "A"
        # if key[pygame.K_a]:
        #     print("correct")
        # else:
        #     print("wrong")
        return Letter

    if Qnum == 3 or Qnum == 5:
        Letter = "B"
        # if key[pygame.K_b]:
        #     print("correct")
        # else:
        #     print("wrong")
        return Letter

def Qbutton(msg,x,y,w,h,ic,ac, CorrectColor, action = None, Hilit = RED):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)

    # if ON:
    pygame.draw.rect(gameDisplay, BLACK, (x,y,w,h), 2)
    if (x+w > mouse[0] > x) and (y+h > mouse[1] > y):
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))


        if click[0] == 1 and action != None:
            pygame.draw.rect(gameDisplay, Hilit, (x,y,w,h))
            CorrectColor = True
            # print(CorrectColor)
            return CorrectColor
            # if action == "map":
            #     import map.py
    # elif permenantColor:
        # pygame.draw.rect(gameDisplay, Hilit, (x,y,w,h))

    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))


    # if permenantColor:
        # pygame.draw.rect(gameDisplay, Hilit ,(x,y,w,h))


    smallText = pygame.font.Font("PlayfairDisplay-Regular.otf", 15)
    textSurface = smallText.render(msg, True, BLACK)
    textSurf, textRect = textSurface, textSurface.get_rect()
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()

    CorrectColor = False
    return CorrectColor

def OtherButton(msg,x,y,w,h,Hilit):
    pygame.draw.rect(gameDisplay, BLACK, (x,y,w,h), 2)
    pygame.draw.rect(gameDisplay, Hilit ,(x,y,w,h))


    smallText = pygame.font.Font("PlayfairDisplay-Regular.otf", 15)
    textSurface = smallText.render(msg, True, BLACK)
    textSurf, textRect = textSurface, textSurface.get_rect()
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()


runner = player(90, 375, 16, 16)
pygame.time.set_timer(USEREVENT+1, 500)
pygame.time.set_timer(USEREVENT+2, rand.randrange(3000,5000))
pygame.time.set_timer(USEREVENT+3, 30000)
speed = 80
run = True

objects = []
checkpoints = []
checkFlag = False
questionPause = False

while run:
    if questionPause == False:
        redrawWindow()
    for objectt in objects:
        if objectt.collide(runner.hitbox):
            # runner.falling = True
            pygame.time.delay(2000)
            objects.pop(objects.index(objectt))
        if checkFlag != True or questionPause != True:
            objectt.x -= 1.4
        else:
            objectt.x = 0

    for checkpointss in checkpoints:
        # checkpointss.x -= 1.4
        # if flag == (150, 390):
        #     pygame.time.delay(3000)
        # if self.hitbox == (94, 430, self.width, self.height):
        #     pygame.time.delay(3000)
        if checkpointss.collide1(runner.hitbox):
            # pygame.time.delay(3000)
            checkpoints.pop(checkpoints.index(checkpointss))
            checkFlag = True
        # print(checkFlag)
        if checkFlag:

            question = question_PopUp()
            Qnum = int(question[21:22])

            ansOptions = whichQuestion(Qnum)

            ansAs = "A. " + ansOptions[0]
            ansBs = "B. " + ansOptions[1]
            ansCs = "C. " + str(ansOptions[2])
            ansDs = "D. " + str(ansOptions[3])
            questionPause = True
            checkFlag = False

        if questionPause:
            questionPop = pygame.image.load(question).convert()
            questionPop = pygame.transform.scale(questionPop, (600, 400))
            rect3 = questionPop.get_rect()
            rect3.center= (500, 300)

            gameDisplay.blit(questionPop, rect3)
            pygame.display.update()
            # checkFlag = False


            correctLetter = answer(Qnum)

            if CorrectColor == False:
                isitclicked = []
                if correctLetter == "A":
                    CorrectColor = Qbutton(ansAs, 220, 300, 560, 30, WHITE, GREY_DARK, CorrectColor,  "answerA", GREEN)
                    CorrectColorA = CorrectColor
                    isitclicked.append(CorrectColorA)
                else:
                    CorrectColor = Qbutton(ansAs, 220, 300, 560, 30, WHITE, GREY_DARK, CorrectColor,  "answerA")
                    WrongColorA = CorrectColor
                    isitclicked.append(WrongColorA)

                if correctLetter == "B":
                    CorrectColor = Qbutton(ansBs, 220, 345, 560, 30, WHITE, GREY_DARK, CorrectColor,  "answerA", GREEN)
                    CorrectColorB = CorrectColor
                    isitclicked.append(CorrectColorB)
                else:
                    CorrectColor = Qbutton(ansBs, 220, 345, 560, 30, WHITE, GREY_DARK, CorrectColor,  "answerA")
                    WrongColorB = CorrectColor
                    isitclicked.append(WrongColorB)

                if Qnum != 2 and Qnum != 5:
                    if correctLetter == "C":
                        CorrectColor = Qbutton(ansCs, 220, 390, 560, 30, WHITE, GREY_DARK, CorrectColor,  "answerA", GREEN)
                        CorrectColorC = CorrectColor
                        isitclicked.append(CorrectColorC)
                    else:
                        CorrectColor = Qbutton(ansCs, 220, 390, 560, 30, WHITE, GREY_DARK, CorrectColor,  "answerA")
                        WrongColorC = CorrectColor
                        isitclicked.append(WrongColorC)

                    if correctLetter == "D":
                        CorrectColor = Qbutton(ansDs, 220, 435, 560, 30, WHITE, GREY_DARK, CorrectColor,  "answerA", GREEN)
                        CorrectColorD = CorrectColor
                        isitclicked.append(CorrectColorD)
                    else:
                        WrongColorD = Qbutton(ansDs, 220, 435, 560, 30, WHITE, GREY_DARK, CorrectColor,  "answerA")
                        isitclicked.append(WrongColorD)

                if True in isitclicked:
                    # questionPause = False
                    CorrectColor = True
                    anyClicked = True
            if CorrectColorB:
                OtherButton(ansBs, 220, 345, 560, 30, GREEN)
            if CorrectColorC:
                OtherButton(ansCs, 220, 390, 560, 30, GREEN)
            if CorrectColorA:
                OtherButton(ansAs, 220, 300, 560, 30, GREEN)


            if WrongColorB:
                OtherButton(ansBs, 220, 345, 560, 30, RED)
            if WrongColorC:
                OtherButton(ansCs, 220, 390, 560, 30, RED)
            if WrongColorD:
                OtherButton(ansDs, 220, 435, 560, 30, RED)
            if WrongColorA:
                OtherButton(ansAs, 220, 300, 560, 30, RED)


            if anyClicked:
                timer = timer - .01
                # print(timer)
                pygame.time.delay(10)
                if timer <= 0:
                    anyClicked = False
                    theactualend = True
            if theactualend:
                questionPause = False



        checkpointss.x -= 1.4


    bgX -= 1.4
    bgX2 -= 1.4
    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        if event.type == USEREVENT+1:
            speed += 1

        if event.type == USEREVENT+2:

            r = rand.randrange(0,2)
            if r == 0:
                objects.append(trap(1000, 390, 40, 40))
            else:
                objects.append(sandBlock(1000, 335, 110, 35))
        if event.type == USEREVENT+3:
            checkpoints.append(flag(1000, 390, 40, 100))
            # if objectt.collide():
            #     pygame.time.delay(1000)



    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        if not(runner.jumping):
            runner.jumping = True

    if keys[pygame.K_DOWN]:
        if not(runner.sliding):
            runner.sliding = True
    clock.tick(speed)
