import pygame, sys
from pygame.locals import *
from colors import *
from random import *

pygame.init()

questionBank = ["coastalForestQuestion1.png", "coastalForestQuestion2.png", "coastalForestQuestion3.png", "coastalForestQuestion5.png"]
done = []

key=pygame.key.get_pressed()
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
        Qnum = int(question[21:22])
    if question == "coastalForestQuestion1.png":
        questionBank.append("coastalForestQuestion4.png")
    if len(questionBank) == 0:
        questionBank.append("coastalForestQuestion6.png")
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
    return(Qnum)

#in other code, have line:
##Qnum = question_PopUp(Qnum)
def answer(Qnum):
    if Qnum == 4 or Qnum == 6:
        if pygame.key.get_pressed()[pygame.K_c]:
            print("correct")
        else:
            print("wrong")
    elif Qnum == 1 or Qnum == 2:
        if pygame.key.get_pressed()[pygame.K_a]:
            print("correct")
        else:
            print("wrong")
    elif Qnum == 3 or Qnum == 5:
        if pygame.key.get_pressed()[pygame.K_b]:
            print("correct")
        else:
            print("wrong")

# def multiple choice(x):




# for i in range(1):
    # question_PopUp()
    # answer(Qnum)
flag = True

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # if event.type == pygame.KEYDOWN:
            # if event.key == key[pygame.K_a]:
                # print("1234646784526246")
            # if event.key == key[pygame.K_b]:
                # print("asdf arga sfasf")
            # if event.key == key[pygame.K_c]:
                # print("asgfak jshfkajsdhlfa")
            # if event.key == key[pygame.K_d]:
                # print("ast arg sdgndfgas")
    if flag:
        question_PopUp(Qnum)
        Qnum = question_PopUp(Qnum)
    # print(Qnum)
        answer(Qnum)
    if answered:
        flag == False
    # if pygame.key.get_pressed()[pygame.K_c]:
    #     print("correct")
    # else:
    #     print("wrong")


    pygame.display.update()
