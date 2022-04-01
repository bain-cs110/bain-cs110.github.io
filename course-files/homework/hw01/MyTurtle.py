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
