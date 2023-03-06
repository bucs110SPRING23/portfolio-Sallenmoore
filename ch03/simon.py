## Events

## Operating system handles events
## Your program -> OS: anything happening

## OS => event
## type of event == operation
# - click
# - key_presses

# connect actions to algorithms


# Simon Says

import random

import pygame

pygame.init()
screen = pygame.display.set_mode()
colors = ["red", "green", "blue", "yellow"]
random.shuffle(colors)

for color in colors:
    screen.fill(color)
    pygame.display.flip()
    pygame.time.wait(1000)

    screen.fill("black")
    pygame.display.flip()
    pygame.time.wait(250)

message = """
    Simon says: 
    UP: RED
    DOWN: BLUE
    LEFT: GREEN
    RIGHT: YELLOW

    click on the the window, enter sequence,m then press enter
"""
response = input(message)

# pygame.EVENT_OBJECT

user_sequence = []

# respond to events in one place in program
for event in pygame.event.get():

    if event.type == pygame.KEYDOWN:
        print("colors: ", colors)
        print("user_sequence: ", user_sequence)
        if event.key == pygame.K_UP:
            screen.fill("red")
            user_sequence.append("red")
        elif event.key == pygame.K_DOWN:
            screen.fill("blue")
            user_sequence.append("blue")
        elif event.key == pygame.K_LEFT:
            screen.fill("green")
            user_sequence.append("green")
        elif event.key == pygame.K_RIGHT:
            screen.fill("yellow")
            user_sequence.append("yellow")


print("user sequence: ", user_sequence)
print("colors: ", colors)
print(print("user events: ", pygame.event.get()))

if user_sequence == colors:
    print("You win!")
else:
    print("Were you paying attention?")

pygame.quit()
