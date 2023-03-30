
## Import some libraries so we don't have to start from scratch
from turtle import *
from random import randint

# This creates a special turtle called "MyTurtle" that allows
# us to create turltes anywhere on the screen
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


################################
# Example 1
################################

# Make a turtle called turtle_1 for us to draw with
turtle_1 = MyTurtle(x = -300, y = 150)


# Create a new function called to_draw that explains to our turtle
# how they should move across the screen
def to_draw():
    turtle_1.speed(0)
    turtle_1.left(54)
    turtle_1.forward(100)

    # This is "short" for "repeat 20 times"
    for i in range(20):
        turtle_1.forward(150)
        turtle_1.right(75)
        turtle_1.pencolor("blue")

    for i in range(1):
        turtle_1.forward(350)
        turtle_1.right(90)
        turtle_1.pencolor("red")


################################
# Example 2
################################

# Create a second turtle called turtle_2 and start it at a different place
turtle_2 = MyTurtle(x = -50, y = 50)
x = 1

# Explain how that turtle will draw
def to_draw_alt():
    bgcolor('black') 

    global x
    
    turtle_2.speed(0)
        
    r = randint(0,255) 
    g = randint(0,255)  
    b = randint(0,255) 

    colormode(255)  
    turtle_2.pencolor(r,g,b) 
    turtle_2.forward(50 + x) 
    turtle_2.right(90.991) 
    x = x + 1 



# Actually ask the turtle to draw
while True:
    to_draw()
