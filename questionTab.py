import pygame, sys
from pygame.locals import *
from colors import *
from random import *

questionBank = ["coastalForestQuestion1.png", "coastalForestQuestion2.png", "coastalForestQuestion3.png", "coastalForestQuestion5.png"]
done = []

Qnum = 0

# print(questionBank)
# print(done)
#in other code, just make it run the code.
def question_PopUp(Qnum):

    order = True
    question = questionBank[randint(0,len(questionBank)-1)]
    # if question == "coastalForestQuestion4.png":
    #     if "coastalForestQuestion1.png" not in done:
    #         print(";sadjf a;lkdsjf a;lkdsjf a;lkfdja")
    #         question = questionBank[randint(0,len(questionBank)-1)]
    # if question == "coastalForestQuestion6.png":
    #     if len(done) != 5:
    #         print(";sadjf a;lkdsjf a;lkdsjf a;lkfdja")
    #         question = questionBank[randint(0,len(questionBank)-1)]
    if order == True:
        questionBank.remove(question)
        done.append(question)
        Qnum = question[21:22]
    if question == "coastalForestQuestion1.png":
        questionBank.append("coastalForestQuestion4.png")
    if len(questionBank) == 0:
        questionBank.append("coastalForestQuestion6.png")
    print(Qnum)
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
    return(Qnum)

# def answer(Qnum):
#     if



for i in range(6):
    question_PopUp(Qnum)

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # question_PopUp(Qnum)

    pygame.display.update()
