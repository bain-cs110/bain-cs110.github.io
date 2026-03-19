from cs110_p1 import *
from pixel_friends import *
_ignore = setup_shapes("Tutorial 5", background="white", include_grid=True, width=1000, height=800)
########################## YOUR CODE BELOW THIS LINE ##############################


## Put your Handler Functions Here
def add_new_goomba(event):
    print(event.x, event.y)

##### Handler functions above here

## Anything that happens exactly once should go here!
def setup():
    print("Setup time!")

    ## Listeners will go here!

    # YOU HAVE TO TELL PYTHON TO LISTEN FOR CLICK AND DRAG EVENTS! 

    ## listeners go above here

    # note that I'm assigning each goomba a unique tag. It's also important to note,
    # that if we go look at the mario module (which is imported above), it's using the shape
    # functions from the utilities module (also imported above). If we look at say,
    # `square`, you'll see it too takes a "tag" as input. This is important because every
    # single square in our drawing HAS TO HAVE THE SAME TAG, otherwise, Python won't know it's one
    # continuous shape.
    goomba((0, 0), size=15, tag="goomba_0")
    goomba((300, 200), size=10, tag="goomba_1")

def go():
    # print("Animating!")
    pass

# This is how many animations to attempt per second. If you want to slow down your
#   animations, just decrease this number! If you want to speed up...
ticks_per_second = 10

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
