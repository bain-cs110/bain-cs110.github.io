## IGNORE ALL OF THIS STUFF AT THE TOP. SCROLL DOWN UNTIL YOU SEE THE # LINE!
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
###########################################################################
###### DO NOT WRITE ANYTHING ABOVE THIS LINE ######

# This says create a turtle at (100, 100) and who's pencolor
#   is green. Then assign it to the variable shelly
shelly = MyTurtle(x=100, y=100)

# Hint: To change the turtle's pen color, just call the pencolor function!
# change_pen_color(shelly, "green")

### Your code goes below here
forward(shelly, 100)
left_turn(shelly, 90)
forward(shelly, 100)
right_turn(shelly, 90)
