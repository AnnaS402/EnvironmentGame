import pygame
from pygame.locals import *
from pygame.time import *

pygame.init()
#
# while True:
#     ms = pygame.time.get_ticks()
    # print(ms)
#---------------
# iterations = 1000
#
# timestart = pygame.time.get_ticks()
#
# for a in range(iterations):
# 	pygame.time.delay(0)
#
# timeold = pygame.time.get_ticks()
# timeperloop1 = (timeold - timestart) / float(iterations)
# print(timeperloop1)
# ---------------------
# while True:
#     pygame.time.wait(500)                # wait 500ms
#
#     print (pygame.time.get_ticks(), "ms")
# -----------------------------
# __all__ = ["Clock"]
#
# def get_ticks():
#     return pygame.time.get_ticks()
#
# def wait(milliseconds):
#     pygame.time.wait(milliseconds)
#
# def delay(milliseconds):
#     pygame.time.delay(milliseconds)
# -----------------
# start_ticks=pygame.time.get_ticks() #starter tick
# mainloop=True
# while mainloop: # mainloop
#     seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
#     if seconds>10: # if more than 10 seconds close the game
#         break
#     print (seconds) #print how many seconds
# ------------------
screen = pygame.display.set_mode((128, 128))
clock = pygame.time.Clock()

counter, text = 30, '30'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

while True:
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT:
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'boom!'
        if e.type == pygame.QUIT: break
    else:
        screen.fill((255, 255, 255))
        screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
        pygame.display.flip()
        clock.tick(60)
        continue
    break
