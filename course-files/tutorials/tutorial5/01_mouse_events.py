from p1_utilities import *
from mario_module import *
import time

_ignore = setup_shapes('Tutorial 5', background="white", grid=True, width=1000, height=800)
ticks_per_second = None
ticks = 0
########################## YOUR CODE BELOW THIS LINE ##############################

## Put your Handler Functions Here
def add_new_goomba(event):
    print(event.x, event.y)

##### Handler functions above here


## Anything that happens exactly once should go here!
def setup():
    print("Setup time!")
    
    MOUSE_CLICK_MAGIC_STRING = '<Button-1>'
    MOUSE_DRAG_MAGIC_STRING = '<B1-Motion>'

    ## Listeners will go here!

    # YOU HAVE TO TELL PYTHON TO LISTEN FOR CLICK AND DRAG EVENTS! 

    ## listeners go above here

    # note that I'm assigning each goomba a unique tag. It's also important to note,
    # that if we go look at the mario module (which is imported above), it's using the shape
    # functions from the utilities module (also imported above). If we look at say,
    # `square`, you'll see it too takes a "tag" as input. This is important because every
    # single square in our drawing HAS TO HAVE THE SAME TAG, otherwise, Python won't know it's one
    # continuous shape.
    goomba((0, 0), size=15, tag='goomba_0')
    goomba((300, 200), size=10, tag='goomba_1')

    # This is how many animations to attempt per second. If you want to slow down your
    #   animations, just decrease this number! If you want to speed up...
    global ticks_per_second
    ticks_per_second = 10

def go():
    print("Animating!")

########################## YOUR CODE ABOVE THIS LINE ##############################
## DO NOT MODIFY THIS STUFF
setup()
while True:
    go()
    _ignore.update()
    time.sleep(1 / ticks_per_second)
    ticks = ticks + 1
