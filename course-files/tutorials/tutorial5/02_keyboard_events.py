from p1_utilities import *
from mario_module import *
import time

_ignore = setup_shapes('Tutorial 5', background="white", grid=True, width=1000, height=800)
ticks_per_second = None
ticks = 0
########################## YOUR CODE BELOW THIS LINE ##############################

## Put your Handler Functions Here
def select_mario(event):
    tag = get_tag_from_event(event)
    print(tag)

def move_mario(event):
    print(event.keysym)
    move('mario_0', x=10, y=0)
##### Handler functions above here



## Anything that happens exactly once should go here!
def setup():
    print("Setup time!")
    # helper function that draws a grid.

    ## Listeners will go here!
    setup_listener('<Key>', move_mario)
    setup_listener('<Button-1>', select_mario)
    ## listeners go above here

    mario((0, 0), size=15, tag='mario_0')
    mario((150, 200), size=10, version=2, tag='mario_1')

    # This is how many animations to attempt per second. If you want to slow down your
    #   animations, just decrease this number! If you want to speed up...
    global ticks_per_second
    ticks_per_second = 30

def go():
    pass
    #print("Animating!")

########################## YOUR CODE ABOVE THIS LINE ##############################
## DO NOT MODIFY THIS STUFF
setup()
while True:
    go()
    _ignore.update()
    time.sleep(1 / ticks_per_second)
    ticks = ticks + 1
