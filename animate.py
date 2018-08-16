import pygame, sys
from pygame.locals import *
import time
start_frame = time.time()
noi = 5
frames_per_second = .5

img5 = pygame.image.load("sprites/running/fox5running.png")
img4 = pygame.image.load("sprites/running/fox4running.png")
img3 = pygame.image.load("sprites/running/fox3running.png")
img2 = pygame.image.load("sprites/running/fox2running.png")
img1 = pygame.image.load("sprites/running/fox1running.png")

display_width = 1000
display_height = 600

sprite_image5 = pygame.image.load("sprites/running/fox5running.png")
sprite_image4 = pygame.image.load("sprites/running/fox4running.png")
sprite_image3 = pygame.image.load("sprites/running/fox3running.png")
sprite_image2 = pygame.image.load("sprites/running/fox5running.png")
sprite_image1 = pygame.image.load("sprites/running/fox1running.png")

rect = sprite_image1.get_rect()
# gameDisplay.blit(sprite_image1, rect)
# gameDisplay.blit(sprite_image2, rect)
# gameDisplay.blit(sprite_image3, rect)
# gameDisplay.blit(sprite_image4, rect)
# gameDisplay.blit(sprite_image5, rect)
#
# while True: #main game loop
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#
#     pygame.display.update()

# ---------------------------------------------------------

def load_image(name):
    image = pygame.image.load(name)
    return image

class TestSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(TestSprite, self).__init__()
        self.images = []
        self.images.append(load_image("sprites/running/fox1running.png"))
        self.images.append(load_image("sprites/running/fox2running.png"))
        self.images.append(load_image("sprites/running/fox3running.png"))
        self.images.append(load_image("sprites/running/fox4running.png"))
        self.images.append(load_image("sprites/running/fox5running.png"))



        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(5, 5, 64, 64)

    def update(self, gameDisplay):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        gameDisplay.blit

def main():
    pygame.init()
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    my_sprite = TestSprite()
    my_group = pygame.sprite.Group(my_sprite)

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        # Calling the 'my_group.update' function calls the 'update' function of all
        # its member sprites. Calling the 'my_group.draw' function uses the 'image'
        # and 'rect' attributes of its member sprites to draw the sprite.
        my_group.update(gameDisplay)
        my_group.draw(gameDisplay)
        pygame.display.flip()
        current_image = int((time.time() - start_frame) * frames_per_second % noi)
if __name__ == '__main__':
    main()
