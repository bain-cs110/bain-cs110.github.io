from p1_utilities import *
import time

_ignore = setup_shapes('Lecture 19', background="white", grid=False, width=800, height=800)
ticks = 0
ticks_per_second = None
########################## YOUR CODE BELOW THIS LINE ##############################

from random import uniform

user_shapes = []
def click_handler(event):
    tag = 'circle_' + str(len(user_shapes))
    circle((event.x, event.y), uniform(10, 50), color="cyan", tag=tag)
    # add our shape to a list called user_shapes by appending
    # a tuple with its tag and a randomly generated speed to travel at
    user_shapes.append((tag, uniform(1, 5)))

def setup():
    ## Setting some listeners!
    # Notice first we define our function called do_something
    # then we tell the canvas to listen for MOUSE_CLICKs and if
    # it hears one, do_something
    setup_listener('<Button-1>', click_handler)
    setup_listener('<B1-Motion>', click_handler)

    text((500, 500), text='Click or drag to create circles', font=("Purisa", 32))

    # This is how many animations to attempt per second. If you want to slow down your
    #   animations, just decrease this number! If you want to speed up...
    global ticks_per_second
    ticks_per_second = 60


def go():
    # Here's where you'll put everything you want to control your animations
    #   EXCEPT event listeners (look higher up)
    for shape in user_shapes:

        shape_tag = shape[0] # load the shape's tag
        shape_speed = -1 * shape[1] # load the shape's speed

        # if one of our shapes reaches the bottom of the canvas
        if get_bottom(shape_tag) > 1000:
            # then calculate a new position at the "top" of the canvas
            reset_position = 1000 + get_height(shape_tag)
            # and move the shape with that tag to that "top" of the canvas
            move(shape_tag, y= -1 * reset_position)

        # regardless move the shape a little bit (determined by its speed)
        move(shape_tag, x=0, y=-1 * shape_speed)


######&&!*#################### YOUR CODE ABOVE THIS LINE ##############################

## DO NOT MODIFY THIS STUFF
setup()
while True:
    go()
    _ignore.update()
    time.sleep(1 / ticks_per_second)
    ticks = ticks + 1
