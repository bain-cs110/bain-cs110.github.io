from p1_utilities import *
import time
from random import randint

_ignore = setup_shapes('Lecture 18', background="white", grid=False, width=600, height=600)
ticks_per_second = None
ticks = 0
########################## YOUR CODE BELOW THIS LINE ##############################
def move_circle(event):
    selected_tag = get_tag_from_event(event)
    
    # check to see if this thing is a circle
    if "circle" not in selected_tag:
        selected_tag = None # If it's not a circle let's not mess with it

    # as long as we have something selected, move it!
    if selected_tag != None:
        move_to(selected_tag, (event.x, event.y))
        update_color(selected_tag, "yellow")

circle_counter = 0
def setup():
    ## Setting some listeners!
    MOUSE_DRAG = '<B1-Motion>'
    
    setup_listener(MOUSE_DRAG, move_circle)

    text((300, 200), text='Drag a circle around!', font=("Purisa", 32), tag="instructions")

    # Draw some circles!
    global circle_counter
    circle_counter = 0
    for i in range(50):
        circle((randint(0, 1000), randint(0, 1000)), radius=randint(10, 20), tag="circle_"+str(circle_counter))
        circle_counter += 1

    # This is how many animations to attempt per second. If you want to slow down your
    #   animations, just decrease this number! If you want to speed up...
    global ticks_per_second
    ticks_per_second = 60


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
