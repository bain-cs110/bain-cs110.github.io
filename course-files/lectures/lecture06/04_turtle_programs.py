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
