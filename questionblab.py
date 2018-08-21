import pygame, sys
from pygame.locals import *
from colors import *
from random import *

pygame.init()

questionBank = ["coastalForestQuestion1A.png", "coastalForestQuestion2A.png", "coastalForestQuestion3A.png", "coastalForestQuestion5A.png"]
done = []

# key = pygame.key.get_pressed()

Qnum = 0
CorrectColor = False

CorrectColorA = False
CorrectColorB = False
CorrectColorC = False

WrongColorA = False
WrongColorB = False
WrongColorC = False
WrongColorD = False
# print (CorrectColor)
# ON = True

# print(questionBank)
# print(done)
#in other code, just make it run the code.
def question_PopUp():

    question = questionBank[randint(0,len(questionBank)-1)]
    # if question == "coastalForestQuestion4.png":
    #     if "coastalForestQuestion1.png" not in done:
    #         print(";sadjf a;lkdsjf a;lkdsjf a;lkfdja")
    #         question = questionBank[randint(0,len(questionBank)-1)]
    # if question == "coastalForestQuestion6.png":
    #     if len(done) != 5:
    #         print(";sadjf a;lkdsjf a;lkdsjf a;lkfdja")
    #         question = questionBank[randint(0,len(questionBank)-1)]
    # if checkFlag:
    questionBank.remove(question)
    done.append(question)
    Qnum = int(question[21:22])

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

    questionPop = pygame.image.load(question).convert()
    questionPop = pygame.transform.scale(questionPop, (600, 400))
    rect3 = questionPop.get_rect()
    rect3.center= (500, 300)

    gameDisplay.blit(questionPop, rect3)
    # checkFlag = False
    return(Qnum)

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

    CorrectColor = False
    return CorrectColor

def OtherButton(msg,x,y,w,h, Hilit):
    pygame.draw.rect(gameDisplay, BLACK, (x,y,w,h), 2)
    pygame.draw.rect(gameDisplay, Hilit ,(x,y,w,h))


    smallText = pygame.font.Font("PlayfairDisplay-Regular.otf", 15)
    textSurface = smallText.render(msg, True, BLACK)
    textSurf, textRect = textSurface, textSurface.get_rect()
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

# def End():
    # pygame.time.delay(3000)
    # print("you should now blank out")


# for i in range(6):
    # question_PopUp(Qnum)
checkFlag = True
timer = 30

# print ("CorrectColor before loop: ")
# print (CorrectColor)

while True: # main game loop
    # print ("CorrectColor inside loop: ")
    # print (CorrectColor)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #when checkpoint condition is met
    # checkFlag = True
    #make sure to move the flag after so after checkFlag is set as true, it no longer applies
    if checkFlag:
        # question_PopUp()
        Qnum = question_PopUp()
        print(Qnum)
        # whichQuestion(Qnum)
        ansOptions = whichQuestion(Qnum)

        ansAs = "A. " + ansOptions[0]
        ansBs = "B. " + ansOptions[1]
        ansCs = "C. " + str(ansOptions[2])
        ansDs = "D. " + str(ansOptions[3])

        # print("1")
        questionPause = True
        checkFlag = False
        # print("This should only show up once")

    # print ("CorrectColor before questionpause if: ")
    # print (CorrectColor)

    if questionPause:
        # print(whichQuestion(Qnum))
        # print(ansAs, ansBs, ansCs, ansDs)
        correctLetter = answer(Qnum)

        # print(correctLetter)
        # print(CorrectColor)
        if CorrectColor == False:
            if correctLetter == "A":
                CorrectColor = Qbutton(ansAs, 220, 300, 560, 30, WHITE, GREY_DARK, CorrectColor,  "answerA", GREEN)
                CorrectColorA = CorrectColor
                # EndWorldCounter += 1
            #     if colorCorrectA:
            #         print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAaaa")
            else:
                CorrectColor = Qbutton(ansAs, 220, 300, 560, 30, WHITE, GREY_DARK, CorrectColor,  "answerA")
                WrongColorA = CorrectColor

            if correctLetter == "B":
                CorrectColor = Qbutton(ansBs, 220, 345, 560, 30, WHITE, GREY_DARK, CorrectColor,  "answerA", GREEN)
                CorrectColorB = CorrectColor
                # EndWorldCounter += 1

            else:
                CorrectColor = Qbutton(ansBs, 220, 345, 560, 30, WHITE, GREY_DARK, CorrectColor,  "answerA")
                WrongColorB = CorrectColor

            if Qnum != 2 and Qnum != 5:
                if correctLetter == "C":
                    CorrectColor = Qbutton(ansCs, 220, 390, 560, 30, WHITE, GREY_DARK, CorrectColor,  "answerA", GREEN)
                    CorrectColorC = CorrectColor
                    # EndWorldCounter += 1

                else:
                    CorrectColor = Qbutton(ansCs, 220, 390, 560, 30, WHITE, GREY_DARK, CorrectColor,  "answerA")
                    WrongColorC = CorrectColor

                CorrectColor = Qbutton(ansDs, 220, 435, 560, 30, WHITE, GREY_DARK, CorrectColor,  "answerA")
                WrongColorD = CorrectColor
        if CorrectColorA or CorrectColorB or CorrectColorC:
            print("Correct!")
            if CorrectColorA:
                OtherButton(ansAs, 220, 300, 560, 30, GREEN)
                # EndWorldCounter += 1

            elif CorrectColorB:
                OtherButton(ansBs, 220, 345, 560, 30, GREEN)
                # EndWorldCounter += 1

            if Qnum != 2 and Qnum != 5:
                if CorrectColorC:
                    OtherButton(ansCs, 220, 390, 560, 30, GREEN)
                    # EndWorldCounter += 1

        if WrongColorA or WrongColorB or WrongColorC or WrongColorD:
            print("Incorrect")
            if WrongColorA:
                OtherButton(ansAs, 220, 300, 560, 30, RED)
            elif WrongColorB:
                OtherButton(ansBs, 220, 345, 560, 30, RED)
            if Qnum != 2 and Qnum != 5:
                if WrongColorC:
                    OtherButton(ansCs, 220, 390, 560, 30, RED)
                elif WrongColorD:
                    OtherButton(ansDs, 220, 435, 560, 30,)


            # CorrectColor = True
            # print("yes, thank you so much")
        # else:
            # print("Ah sh*t")
        # if ON != True:
            # print("asdfa sdf asdjfal;ksdjf;;a")

        # key = pygame.key.get_pressed()
        # Qnum = question_PopUp()
        # print(Qnum)
        # print("You are now in questionPause")
        #also start pseudo timer for 30 seconds
        # if timer == 0 or key[pygame.K_a] or key[pygame.K_b] or key[pygame.K_c] or key[pygame.K_d]:
            # answer(Qnum)
        # if key[pygame.K_SPACE]:
            # print("SF ARG AFGA SDF a")
        # else:
            # print("346579623574878")
        # question_PopUp(Qnum)
# print(EndWorldCounter)
    pygame.display.update()
