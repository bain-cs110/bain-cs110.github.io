from MyTurtle import *
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

def draw_square():
    turtle_1.forward(100)
    turtle_1.right(90)
    turtle_1.forward(100)
    turtle_1.right(90)
    turtle_1.forward(100)
    turtle_1.right(90)
    turtle_1.forward(100)
    turtle_1.right(90)

draw_square()
turtle_1.forward(100)
draw_square()


turtle_2 = MyTurtle(x = -300, y = 100)
# A flexible function that can draw a square of any size
def draw_square_1(side_length):
    turtle_2.forward(side_length)
    turtle_2.right(90)
    turtle_2.forward(side_length)
    turtle_2.right(90)
    turtle_2.forward(side_length)
    turtle_2.right(90)
    turtle_2.forward(side_length)
    turtle_2.right(90)

draw_square_1(50)

turtle_2.forward(100)
# An even more flexible function that can draw a sqaure of any size
# and of any color, but defaults to green.
def draw_square_2(side_length, color="green"):
    turtle_2.pencolor(color)
    turtle_2.forward(side_length)
    turtle_2.right(90)
    turtle_2.forward(side_length)
    turtle_2.right(90)
    turtle_2.forward(side_length)
    turtle_2.right(90)
    turtle_2.forward(side_length)
    turtle_2.right(90)

draw_square_2(100, color="red")


turtle_3 = MyTurtle(x = -300, y = 0)
## The ultimate in flexibility, a function that can ask ANY turtle to draw a square
## of any size and color.
def draw_square_3(the_turtle, side_length, color="green"):
    the_turtle.pencolor(color)
    the_turtle.forward(side_length)
    the_turtle.right(90)
    the_turtle.forward(side_length)
    the_turtle.right(90)
    the_turtle.forward(side_length)
    the_turtle.right(90)
    the_turtle.forward(side_length)
    the_turtle.right(90)

draw_square_3(turtle_3, 100, color="red")
draw_square_3(turtle_1, 400, color="purple")
