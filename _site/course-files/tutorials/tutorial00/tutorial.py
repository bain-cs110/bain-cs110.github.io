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

###### DO NOT WRITE ANYTHING ABOVE THIS LINE ###### 

# This says create a turtle at (100, 100) and who's pencolor
#   is green. Then assign it to the variable shelly
shelly = MyTurtle(x = 100, y = 100, pencolor="green")

# Hint: To change the turtle's pen color, just call the pencolor function!
# shelly.pencolor("green")

### Your code goes below here
shelly.forward(100)
shelly.left(90)
