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
    jump = [pygame.image.load(os.path.join("sprites/jumping/" + 'fox' + 'jump' + str(x) + '.png')) for x in range(0,7)]
    slide = [pygame.image.load(os.path.join("sprites/crouch/crouch0.png")),pygame.image.load(os.path.join("sprites/crouch/crouch1.png")),pygame.image.load(os.path.join("sprites/crouch/crouch2.png")),pygame.image.load(os.path.join("sprites/crouch/crouch2.png")), pygame.image.load(os.path.join("sprites/crouch/crouch2.png")),pygame.image.load(os.path.join("sprites/crouch/crouch2.png")), pygame.image.load(os.path.join("sprites/crouch/crouch2.png")), pygame.image.load(os.path.join("sprites/crouch/crouch2.png")), pygame.image.load(os.path.join("sprites/crouch/crouch2.png")), pygame.image.load(os.path.join("sprites/crouch/crouch1.png")), pygame.image.load(os.path.join("sprites/crouch/crouch2.png"))]
    jumpList = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4]
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

    def draw(self, win):
        if self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.2
            win.blit(self.jump[self.jumpCount//18], (self.x,self.y))
            self.jumpCount += 1
            if self.jumpCount > 108:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
        elif self.sliding or self.slideUp:
            if self.slideCount < 20:
                self.y += 1
            elif self.slideCount == 80:
                self.y -= 19
                self.sliding = False
                self.slideUp = True
            if self.slideCount >= 110:
                self.slideCount = 0
                self.slideUp = False
                self.runCount = 0
            win.blit(self.slide[self.slideCount//10], (self.x,self.y))
            self.slideCount += 1

        else:
            if self.runCount > 42:
                self.runCount = 0
            win.blit(self.run[self.runCount//6], (self.x,self.y))
            self.runCount += 1

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


class sandBlock(trap):
    img = pygame.image.load(os.path.join("obstacles/sandblock.png"))
    def draw(self, win):
        self.hitbox = (self.x + 47, 331, self.width, self.height)
        win.blit(self.img, (self.x, self.y))
        pygame.draw.rect(win, (255, 0, 0), self.hitbox,2)


def redrawWindow():
    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX2, 0))
    runner.draw(win)
    for x in objects:
        x.draw(win)
    pygame.display.update()



runner = player(90, 375, 16, 16)
pygame.time.set_timer(USEREVENT+1, 500)
pygame.time.set_timer(USEREVENT+2, random.randrange(3000,5000))
speed = 50
run = True

objects = []

while run:
    redrawWindow()

    for objectt in objects:
        objectt.x -= 1.4
        if objectt.x < -objectt.width * -1:
            objects.pop(objects.index(objectt))

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
                objects.append(sandBlock(1000, 300, 110, 35))



    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        if not(runner.jumping):
            runner.jumping = True

    if keys[pygame.K_DOWN]:
        if not(runner.sliding):
            runner.sliding = True
    clock.tick(speed)
