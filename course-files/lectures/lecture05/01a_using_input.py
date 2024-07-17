## Ignore everything before the line of all # symbols!
from turtle import *


def raise_(ex):
    raise ex


class MyTurtle(object):
    def __new__(cls, x=-100, y=-100, pencolor="black"):
        my_turtle = Turtle()
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


#####################################################################
### TURTLE CHEATSHEET ###############################################
# Pretend we have a turtle named: turtle_0

# If we want turtle_0 to go forward 100 steps we just say:
# forward(turtle_0, 100)

# If we want turtle_0 to turn left or right 90 degrees, we just say:
# left_turn(turtle_0, 90)
# right_turn(turtle_0, 90)

# If we want to turn turtle_0 around, we'd just turn 180 degrees!
# right_turn(turtle_0, 180)

# If we want turtle_0 to change the color of its pen:
# change_pen_color(turtle_0, "green")

# If we want to make a new turtle at a specific x, y coordinate, we use the optional
# arguments to the MyTurtle Function like so:
# turtle_0 = MyTurtle(x = 100, y = 100)
# (If you leave those out, it will default to 0, 0)

#####################################################################
fred = MyTurtle(x=-250, y=200)

left_turn(fred, 45)
forward(fred, 100)
left_turn(fred, 90)
forward(fred, 100)
left_turn(fred, 90)
forward(fred, 100)
left_turn(fred, 90)
forward(fred, 100)