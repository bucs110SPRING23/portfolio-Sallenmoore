# import math
# import turtle  # 1.  import the modules

# # simulate pen and paper
# pen = turtle.Turtle()
# pen2 = turtle.Turtle()
# pen.shape("turtle")
# pen2.shape("turtle")
# pen2.color("purple")
# pen.color("orange")
# pen.speed(1)
# pen2.speed(0)

# window = turtle.Screen()
# # variable = module.function()


# pen.forward(100)
# pen.left(90)
# pen.forward(100)
# pen.left(90)
# pen.forward(100)
# pen.left(90)
# pen.forward(100)
# pen.left(90)


# pen2.fd(50)
# pen2.left(5)
# pen2.up()
# pen2.fd(50)
# pen2.left(5)
# pen2.pendown()
# pen2.fd(50)
# pen2.left(5)
# pen2.penup()
# pen2.fd(50)
# pen2.left(5)
# pen2.down()
# pen2.fd(50)
# pen2.left(5)
# pen2.up()
# pen2.fd(50)
# pen2.left(5)
# pen2.down()
# pen2.fd(50)
# pen2.left(5)
# pen2.up()
# pen2.fd(50)
# pen2.left(5)
# pen2.down()

# var = math.pi

# pen2.home()
# pen.goto(0, 0)

# # interface: what can I tell it to do, abstract away the details
# # state: value of all its attributes
# var = [1, 2, 3, 4, 5]
# var.append(6)  # add to the end


# # Always must be the last turtle command
# window.exitonclick()


# wn = turtle.Screen()  # 2.  Create a screen
# wn.bgcolor("green")
# donatello = turtle.Turtle()  # 3.  Create two turtles
# donatello.shape("turtle")

# colors = ["red", "purple", "yellow"]
# for color in colors:
#     donatello.color(color)
#     for _ in range(4):
#         donatello.left(90)
#         donatello.forward(50)
#     donatello.up()
#     donatello.forward(100)
#     donatello.down()

# wn.exitonclick()

## Pygame
# framework

# =========================
# TOP OF THE FILE
# import pygame

# pygame.init()

# screen = pygame.display.set_mode()

# screen: variable
# pygame: modules that contain modules are called frameworks
# display: submodile of pygame
# set_mode: function of the display submodule


# screen.fill("red")
# pygame.display.flip()
# pygame.time.wait(1000)
# screen.fill("blue")
# pygame.display.flip()
# pygame.time.wait(1000)

# TOP OF THE FILE
import pygame

pygame.init()


while 1:
    pygame.event.get()

    screen.fill("green")
    pygame.display.flip()
    pygame.time.wait(1000)

    screen_size = screen.get_size()

    # [x, y, width, height]
    dimensions = [screen_size[0] / 2, screen_size[1] / 2, 250, 250]
    pygame.draw.rect(screen, "red", dimensions)

    # [x, y, width, height]
    dimensions = [300, 300, 250, 250]
    pygame.draw.rect(screen, "blue", dimensions)

    pygame.display.flip()
    input()

    break
