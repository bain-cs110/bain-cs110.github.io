## Import some libraries so we don't have to start from scratch
from turtle import *

def raise_(ex):
    raise ex
class MyTurtle(object):
    def __new__(cls, x=-100, y=-100, pencolor="black"):
        my_turtle = Turtle()
        my_turtle.speed(0)
        my_turtle.forward = lambda x: raise_(
            Exception(
                "Sorry, I don't know how to do that. Did you mean to use forward(some_turtle, {})?".format(
                    x
                )
            )
        )
        my_turtle.right = lambda x: raise_(
            Exception(
                "Sorry, I don't know how to do that. Did you mean to use right_turn(some_turtle, {})?".format(
                    x
                )
            )
        )
        my_turtle.left = lambda x: raise_(
            Exception(
                "Sorry, I don't know how to do that. Did you mean to use left_turn(some_turtle, {})?".format(
                    x
                )
            )
        )
        my_turtle.lt = my_turtle.left
        my_turtle.rt = my_turtle.right
        my_turtle.fd = my_turtle.forward
        Screen().tracer(0)
        my_turtle.pencolor(pencolor)
        my_turtle.pencolor = None
        my_turtle.penup()
        my_turtle.goto(x, y)
        my_turtle.pendown()
        Screen().tracer(1)
        return my_turtle

def forward(a_turtle, dist):
    a_turtle._go(dist)

def right_turn(a_turtle, angle):
    a_turtle._rotate(-angle)

def left_turn(a_turtle, angle):
    a_turtle._rotate(angle)

def change_pen_color(a_turtle, color):
    a_turtle.pen(pencolor=color)

################################
# Example
################################

# Make a turtle called turtle_1 for us to draw with
turtle_1 = MyTurtle(x=-300, y=150)

# Create a new function called to_draw that explains to our turtle
# how they should move across the screen
def to_draw():
    left_turn(turtle_1, 54)
    forward(turtle_1, 50)

    # This is "short" for "repeat 20 times"
    for i in range(20):
        forward(turtle_1, 150)
        right_turn(turtle_1, 75)
        change_pen_color(turtle_1, "blue")

    for i in range(1):
        forward(turtle_1, 350)
        right_turn(turtle_1, 90)
        change_pen_color(turtle_1, "red")

# Actually ask the turtle to draw
while True:
    to_draw()
