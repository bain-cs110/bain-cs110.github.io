from p1_utilities import *
import time
from random import uniform, choice

_ignore = setup_shapes('Lecture 16', background="white", grid=False, width=600, height=600)
ticks_per_second = None
ticks = 0
########################## YOUR CODE BELOW THIS LINE ##############################

square_counter = 0
def make_square_from_click(event):

    # use the random module to pick a random number between 40 and 150
    a_width = uniform(40, 150)

    # use the random module to pick a random color from a list of colors
    a_color = choice(['black', 'yellow', 'blue', 'pink'])

    # Tell Python we're using the GLOBAL version of this variable
    global square_counter
    # generate a new tag for this shape based on how many there are on the screen
    my_tag = "square" + str(square_counter)
    square_counter += 1

    # create a creature at the place the person clicked with
    square(top_left=(event.x, event.y), size=a_width, color=a_color, tag=my_tag)


def setup():
    ## Setting some listeners!
    # Notice first we define our function called do_something
    # then we tell the canvas to listen for MOUSE_CLICKs and if
    # it hears one, do_something
    setup_listener('<Button-1>', make_square_from_click)

    text((200, 200), text='Click anywhere add a square', font=("Purisa", 32))

    # This is how many animations to attempt per second. If you want to slow down your
    #   animations, just decrease this number! If you want to speed up...
    global ticks_per_second
    ticks_per_second = 30


def go():
    # Here's where you'll put everything you want to control your animations
    #   EXCEPT event listeners (look higher up)
    pass


######&&!*#################### YOUR CODE ABOVE THIS LINE ##############################

## DO NOT MODIFY THIS STUFF
setup()
while True:
    go()
    _ignore.update()
    time.sleep(1 / ticks_per_second)
    ticks = ticks + 1