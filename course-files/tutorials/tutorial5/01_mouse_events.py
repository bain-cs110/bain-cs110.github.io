from tkinter import Canvas, Tk
from p1_utilities import *
import time
gui = Tk()
gui.title('Mouse Events')
the_canvas = Canvas(gui, width=600, height=600)
setup_shapes(the_canvas)
the_canvas.pack()
from mario_module import *
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
    # helper function that draws a grid.
    make_grid(600, 600)

    MOUSE_CLICK_MAGIC_STRING = '<Button-1>'
    MOUSE_DRAG_MAGIC_STRING = '<B1-Motion>'

    ## Listeners will go here!


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
    ticks_per_second = 30

def go():
    pass
    #print("Animating!")

########################## YOUR CODE ABOVE THIS LINE ##############################
## DO NOT MODIFY THIS STUFF
setup()
while True:
    go()
    gui.update()
    time.sleep(1 / ticks_per_second)
    ticks = ticks + 1
