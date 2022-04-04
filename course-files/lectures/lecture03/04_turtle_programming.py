# --------------------------------------------------------------------------------
# ## Using Python to control text
# --------------------------------------------------------------------------------

from turtle import *

### Turtle functions are special in that they can be applied to SPECIFIC turtles
# using a special notation specifically: turtle_name.function_name(...).
# Check out the CHEATSHEET below where we have a turtle with the name my_turtle

### TURTLE CHEATSHEET ###############################################
# Pretend we have a turtle setup like this
# my_turtle = Turtle()

# If we want turtle_0 to go forward 100 steps we just say:
# my_turtle.forward(100)

# If we want turtle_0 to turn left or right 90 degrees, we just say:
# my_turtle.left(90)
# my_turtle.right(90)

# If we want to turn turtle_0 around, we'd just turn 180 degrees!
# my_turtle.left(180)

# If we want turtle_0 to change the color of its pen:
# my_turtle.pencolor("green")
#####################################################################

my_turtle = Turtle()

### Let's draw a green square!
my_turtle.forward(100)
my_turtle.left(90)
