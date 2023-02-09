import math
import random
import turtle  # 1. import modules

import pygame

# Part A
window = turtle.Screen()  # 2.  Create a screen
window.bgcolor("lightblue")

michelangelo = turtle.Turtle()  # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color("orange")
leonardo.color("blue")
michelangelo.shape("turtle")
leonardo.shape("turtle")
michelangelo.speed(0)
leonardo.speed(0)


michelangelo.up()  # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

## 5. Your PART A code goes here

michelangelo.fd(random.randrange(0, 101))
leonardo.fd(random.randrange(0, 101))

michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

for _ in range(10):
    michelangelo.fd(random.randrange(1, 11))
    leonardo.fd(random.randrange(1, 11))

michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

window.exitonclick()

# PART B - complete part B here

pygame.init()
window = pygame.display.set_mode()

points = []
side_length = 100
xpos = 300
ypos = 180
num_sides = [3, 4, 6, 20, 100, 360]

for side in num_sides:
    window.fill("purple")
    pygame.display.flip()
    pygame.time.wait(1000)
    for i in range(side):
        angle = 360 / side
        radians = math.radians(angle * i)
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians)
        points.append([x, y])
    pygame.display.flip()
    pygame.draw.polygon(window, "orchid", points, width=0)
    pygame.display.flip()
    pygame.time.wait(1000)
    points = []
