
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
    to_draw_alt()
