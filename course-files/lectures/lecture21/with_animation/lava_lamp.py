from p1_utilities import *
import time

_ignore = setup_shapes('Lecture 21', background="white", grid=False, width=1000, height=1000)
ticks = 0
ticks_per_second = None
########################## YOUR CODE BELOW THIS LINE ##############################

from random import uniform, choice

# Change bubbles to dictionaries!
#   Add colors!
#   Add directions!
user_shapes = []
def click_handler(event):
    global user_shapes

    tag = 'circle_' + str(len(user_shapes))
    the_circle = {
        "tag": tag,
        "speed": uniform(1, 5),
        "direction": choice([-1, 1]),
        "color": random_color(),
        "size": uniform(10, 50)
    }
    circle((event.x, event.y),
           radius=the_circle['size'],
           color=the_circle['color'],
           tag=the_circle['tag'])
    
    # add our shape to a list called user_shapes by appending
    # the dictionary to our global list!
    user_shapes.append(the_circle)
    
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

        shape_tag = shape['tag'] # load the shape's tag

        # if one of our shapes reaches the bottom of the canvas
        if get_top(shape_tag) > 1000:
            # then calculate a new position at the "top" of the canvas
            reset_position = -1000 - get_height(shape_tag)
            # and move the shape with that tag to that "top" of the canvas
            move(shape_tag, y=reset_position)

        # if one of our shapes reaches the top of the canvas
        if get_bottom(shape_tag) < 0:
            # then calculate a new position at the "top" of the canvas
            reset_position = 1000 + get_height(shape_tag)
            # and move the shape with that tag to that "top" of the canvas
            move(shape_tag, y=reset_position)

        # regardless move the shape a little bit (determined by its speed)
        move(shape_tag, x=0, y=shape['direction'] * shape['speed'])


######&&!*#################### YOUR CODE ABOVE THIS LINE ##############################

setup()
while True:
    go()
    _ignore.update()
    time.sleep(1 / ticks_per_second)
    ticks = ticks + 1
