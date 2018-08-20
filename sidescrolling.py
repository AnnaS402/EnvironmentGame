import pygame
from pygame.locals import *
import os
import sys
import math
import random
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
    slide = [pygame.image.load(os.path.join("sprites/crouch/crouch0.png")),pygame.image.load(os.path.join("sprites/crouch/crouch1.png")),pygame.image.load(os.path.join("sprites/crouch/crouch2.png")),pygame.image.load(os.path.join("sprites/crouch/crouch2.png")), pygame.image.load(os.path.join("sprites/crouch/crouch2.png")),pygame.image.load(os.path.join("sprites/crouch/crouch2.png")), pygame.image.load(os.path.join("sprites/crouch/crouch2.png")), pygame.image.load(os.path.join("sprites/crouch/crouch2.png")), pygame.image.load(os.path.join("sprites/crouch/crouch2.png")), pygame.image.load(os.path.join("sprites/crouch/crouch2.png")), pygame.image.load(os.path.join("sprites/crouch/crouch2.png")), pygame.image.load(os.path.join("sprites/crouch/crouch2.png")), pygame.image.load(os.path.join("sprites/crouch/crouch2.png")),pygame.image.load(os.path.join("sprites/crouch/crouch2.png")),pygame.image.load(os.path.join("sprites/crouch/crouch2.png")),pygame.image.load(os.path.join("sprites/crouch/crouch2.png")),pygame.image.load(os.path.join("sprites/crouch/crouch2.png")),pygame.image.load(os.path.join("sprites/crouch/crouch2.png")),pygame.image.load(os.path.join("sprites/crouch/crouch2.png")),pygame.image.load(os.path.join("sprites/crouch/crouch2.png"))]
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
            if self.slideCount < 20:
                print("hello")
                # self.y += 1
            elif self.slideCount == 80:
                # self.y -= 19
                self.sliding = False
                self.slideUp = True
            elif self.slideCount >20 and self.slideCount <80:
                self.hitbox = (103, 422, 135, 80)
                self.slideUp = True
            if self.slideCount >= 200:
                self.slideCount = 0
                self.slideUp = False
                self.runCount = 0
                self.hitbox = (94, 381, 165, 100)
            print(self.slideCount//10)
            win.blit(self.slide[self.slideCount//10], (self.x,self.y))
            self.slideCount += 1

        elif self.falling:
            win.blit(self.fall, (self.x, self.y))

        else:
            if self.runCount > 42:
                self.runCount = 0
            win.blit(self.run[self.runCount//6], (self.x,self.y))
            self.runCount += 1
            self.hitbox = (130, 379, 120, 100)
        pygame.draw.rect(win, (255, 0,0), self.hitbox, 2)

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
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
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
        self.hitbox = (self.x + 47, 366, self.width, self.height)
        if self.count >= 8:
            self.count = 0
        win.blit(self.img, (self.x, self.y))
        pygame.draw.rect(win, (255, 0, 0), self.hitbox,2)

    def collide(self, rect):
        print("hitbox 0:", rect[0])
        print("hitbox 1:", rect[1])
        print("hitbox 2:", rect[2])
        print("hitbox 3:", rect[3])
        # print("hitbox 3:", self.hitbox[3])
        print("hitbox 0:", self.hitbox[0])
        print("hitbox 1:", self.hitbox[1])
        print("hitbox 2:", self.hitbox[2])
        print("hitbox 3:", self.hitbox[3])
        print(rect)

        if rect[0] + rect [2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] > self.hitbox[3]:
                return True
        return False

class flag(trap):
    img = pygame.image.load(os.path.join("obstacles/checkpoint.png"))
    def draw(self, win):
        self.hitbox = (self.x, 430, self.width, self.height)
        win.blit(self.img, (self.x, self.y))
# collision detection stuff
    def collide(self, rect):
        # if rect[0] + rect [2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
        #     if rect[1] + rect[3] > self.hitbox[1]:
        #         return True
        # return False

        if rect[0] + rect [2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] < self.hitbox[3]:
                return True
        return False


def redrawWindow():
    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX2, 0))
    runner.draw(win)
    for x in objects:
        x.draw(win)
    for x in checkpoints:
        x.draw(win)
    pygame.display.update()



runner = player(90, 375, 16, 16)
pygame.time.set_timer(USEREVENT+1, 500)
pygame.time.set_timer(USEREVENT+2, random.randrange(3000,5000))
pygame.time.set_timer(USEREVENT+3, 5000)
speed = 80
run = True

objects = []
checkpoints = []

while run:
    redrawWindow()


    for objectt in objects:
        if objectt.collide(runner.hitbox):
            # runner.falling = True
            pygame.time.delay(2000)
            objects.pop(objects.index(objectt))
        objectt.x -= 1.4


    for checkpointss in checkpoints:
        checkpointss.x -= 1.4
        if flag == (150, 390):
            pygame.time.delay(3000)
        # if self.hitbox == (94, 430, self.width, self.height):
        #     pygame.time.delay(3000)

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

            r = random.randrange(0,2)
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
