from p1_utilities import *
import time

_ignore = setup_shapes('Lecture 16', background="white", grid=False, width=600, height=600)
ticks_per_second = None
ticks = 0
########################## YOUR CODE BELOW THIS LINE ##############################

circle_counter = 0
def make_a_circle(event):
    global circle_counter
    circle(center=(event.x, event.y), radius=20, color='hotpink', tag="circle_" + str(circle_counter))
    circle_counter += 1

def setup():
    ## Setting some listeners!
    # Notice first we define our function called do_something
    # then we tell the canvas to listen for MOUSE_CLICKs and if
    # it hears one, make_a_circle
    setup_listener('<B1-Motion>', make_a_circle)

    text((200, 200), text='Drag to make circles!', font=("Purisa", 32))

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