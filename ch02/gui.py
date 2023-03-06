import pygame

# intialize game data
pygame.init()


# mainloop - while loop
# event loop - for loop
# update data
# redraw screen
# update display

screen = pygame.display.set_mode((100, 100))
screen.fill("red")
pygame.display.flip()
input("Press Enter to continue...")
screen.fill("green")
pygame.display.flip()
input("Press Enter to continue...")
# keeps track of display image and next image
