#import the pygame module, so you can use it
import pygame

#define a main function
def main():

    #initialize the pygame module
    pygame.init()
    #load and set the logo
    pygame.display.set_caption("minimal program")

    #create a surface on the screen that has the size of 240 x 180
    screen = pygame.display.set_mode((1000,800))
    #define a variable to control the main loop
    running = True

    #main loop
    while running:
        #event handling, gets all even from the eventqueue
        for event in pygame.event.get():
            #only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                #change the value to False, to exit the main loop
                running = False

        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30,30,60,60))


        pygame.display.flip()

#run the main funiton only if this module is executed as the main script
#if you import this as a module then nothing is executed)
if __name__=="__main__":
    #call the main function
    main()
