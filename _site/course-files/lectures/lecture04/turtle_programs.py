from turtle import *

class MyTurtle(object):
    def __new__(cls, x=-100, y=-100, pencolor="black"):
        my_turtle = Turtle()
        Screen().tracer(0)
        my_turtle.pencolor(pencolor)
        my_turtle.penup()
        my_turtle.goto(x, y)
        my_turtle.pendown()
        Screen().tracer(1)
        return my_turtle

### TURTLE CHEATSHEET ###############################################
# Pretend we have a turtle named: turtle_0

# If we want turtle_0 to go forward 100 steps we just say:
# turtle_0.forward(100)

# If we want turtle_0 to turn left or right 90 degrees, we just say:
# turtle_0.left(90)
# turtle_0.right(90)

# If we want to turn turtle_0 around, we'd just turn 180 degrees!
# turtle_0.left(180)

# If we want turtle_0 to change the color of its pen:
# turtle_0.pencolor("green")

# If we want to make a new turtle at a specific x, y coordinate, we use the optional
# arguments to the MyTurtle Function like so:
# turtle_0 = MyTurtle(x = 100, y = 100)
# (If you leave those out, it will default to 0, 0)

#####################################################################
turtle_1 = MyTurtle(x = -300, y = 200)

turtle_1.forward(200)
turtle_1.right(90)
turtle_1.forward(100)

turtle_1.pencolor("yellow")

turtle_1.right(90)
turtle_1.forward(200)
turtle_1.right(90)
turtle_1.forward(100)
