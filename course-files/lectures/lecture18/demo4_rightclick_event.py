from p1_utilities import *
import time

_ignore = setup_shapes('Lecture 18', background="white", grid=False, width=600, height=600)
ticks_per_second = None
ticks = 0
########################## YOUR CODE BELOW THIS LINE ##############################

def click_handler(event):
    circle((event.x, event.y), 20, color='hotpink')


def right_click_handler(event):
    tag = get_tag_from_event(event)
    delete(tag)


def setup():
    ## Setting some listeners!
    # Notice first we define our function called do_something
    # then we tell the canvas to listen for MOUSE_CLICKs and if
    # it hears one, do_something
    setup_listener('<Button-1>', click_handler)
    setup_listener('<Button-2>', right_click_handler)
    ## Right click not working on your computer? Change the magic string to '<Button-3>'!

    text((200, 200), text='Click anywhere add a circle. Right click on a circle to delete!', font=("Purisa", 32))

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
