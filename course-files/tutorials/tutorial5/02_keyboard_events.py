from cs110_p1 import *
from pixel_friends import *
_ignore = setup_shapes("Tutorial 5", background="white", include_grid=True, width=1000, height=800)
########################## YOUR CODE BELOW THIS LINE ##############################

## Put your Handler Functions Here
def select_mario(event):
    tag = get_tag_from_event(event)
    print(tag)

def move_mario(event):
    print(event.keysym)
    move('mario_0', x_shift=10, y_shift=0)
##### Handler functions above here



## Anything that happens exactly once should go here!
def setup():
    print("Setup time!")
    # helper function that draws a grid.

    ## Listeners will go here!
    listen_for("KEY", move_mario)
    listen_for("LEFT-CLICK", select_mario)
    ## listeners go above here

    mario((0, 0), size=15, tag="mario_0")
    mario((150, 200), size=10, version=2, tag="mario_1")

def go():
    pass
    #print("Animating!")

# This is how many animations to attempt per second. If you want to slow down your
#   animations, just decrease this number! If you want to speed up...
ticks_per_second = 30
########################## YOUR CODE ABOVE THIS LINE ##############################
## DO NOT MODIFY THIS STUFF
clear_window() ## Nothing should be drawn outside SETUP and GO!
ticks = 0
setup()
while True:
    go()
    update() # This function draws all your stuff to the screen!
    sleep(1 / ticks_per_second)
    ticks = ticks + 1

