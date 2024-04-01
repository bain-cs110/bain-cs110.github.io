## IGNORE ALL OF THIS STUFF AT THE TOP. SCROLL DOWN UNTIL YOU SEE THE # LINE!
from turtle import *

def raise_(ex):
    raise ex

class MyTurtle(object):
    def __new__(cls, x=-100, y=-100, pencolor="black"):
        my_turtle = Turtle()
        my_turtle.forward = lambda x : raise_(Exception("Sorry, I don't know how to do that. Did you mean to use forward(some_turtle, {})?".format(x)))
        my_turtle.right = lambda x : raise_(Exception("Sorry, I don't know how to do that. Did you mean to use right_turn(some_turtle, {})?".format(x)))
        my_turtle.left = lambda x : raise_(Exception("Sorry, I don't know how to do that. Did you mean to use left_turn(some_turtle, {})?".format(x)))
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

#############################################################################
## DO NOT MODIFY ANY LINES ABOVE THIS LINE
## DO NOT MODIFY ANY LINES THAT BEGIN WITH ## (two hashtags).
## You can add as many new lines as you'd like

## TURTLE SECTION #####!!!#####

## Exercise 1 #####!!!#####
turtle_1 = MyTurtle(x=-300, y=200)

# Your code goes here

## Exercise 2 #####!!!#####
turtle_2 = MyTurtle(x=-150, y=200)

# Your code goes here

## Exercise 3 #####!!!#####
turtle_3 = MyTurtle(x=0, y=200)

# Your code goes here

## Exercise 4 #####!!!#####
# Hint: Combine what you know from exercises 1 and 3!
turtle_4 = MyTurtle()

## Exercise 5 #####!!!#####
turtle_5 = MyTurtle(x=300, y=-300)
# Some ideas: a snowflake, a heptagon, a 2-D cube!
# Or, you could add windows or doors to your house.


## DATA SECTION #####!!!#####

## For this section, be VERY CAREFUL to save the requested data in the appropriate variable name.

## Exercise 1 #####!!!#####

# your code goes here

# Exercise 2 #####!!!#####

# your code goes here

## Exercise 3 #####!!!#####

# your code goes here

## Exercise 4 #####!!!#####
# Hint: to find the length in number of letters of a string, we can use the len function
#       like so: len("hello"). If we wanted to find the number of characters in a string
#       that's stored in a variable, we'd instead use the variable's name: len(variable)

# your code goes here
