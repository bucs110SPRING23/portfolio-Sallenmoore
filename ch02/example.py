import math
import turtle  # 1.  import the modules

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


wn = turtle.Screen()  # 2.  Create a screen
wn.bgcolor("green")
donatello = turtle.Turtle()  # 3.  Create two turtles
donatello.shape("turtle")

colors = ["red", "purple", "yellow"]
for color in colors:
    donatello.color(color)
    for _ in range(4):
        donatello.left(90)
        donatello.forward(50)
    donatello.up()
    donatello.forward(100)
    donatello.down()

wn.exitonclick()
