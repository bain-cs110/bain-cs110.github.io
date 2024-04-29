from tkinter import Canvas, Tk
from p1_utilities import *
import random
import time
gui = Tk()
gui.title('Tour of options...')

# initialize canvas:
the_canvas = Canvas(gui, width=1000, height=1000, background='white')
the_canvas.pack()
setup_shapes(the_canvas)
ticks = 0
ticks_per_second = None
########################## YOUR CODE BELOW THIS LINE ##############################

# need a global variable to store which item should be clicked:
active_tag = None
def select_circle(event):
    global active_tag

    # if something is already active, deactivate it:
    if active_tag:
        update_color(active_tag, 'hotpink')
        active_tag = None

    # get new active tag:
    active_tag = get_tag_from_event(event)
    if active_tag:
        update_color(active_tag, 'olivedrab')

active_tag = ""

def move_circle(event):
    if not active_tag:
        print('no tag selected')
        return

    # calculate the current position of the current shape:
    width = get_width(active_tag)
    height = get_height(active_tag)
    left = get_left(active_tag)
    top = get_top(active_tag)
    current_x = left + (width / 2)
    current_y = top + (height / 2)

    # calculate the delta of the current shape:
    delta_x = -1 * (current_x - event.x)
    delta_y = -1 * (current_y - event.y)

    # move the shape:
    move(active_tag, x_shift=delta_x, y_shift=delta_y)

def setup():
    ## Setting some listeners!
    # Notice first we define our function called do_something
    # then we tell the canvas to listen for MOUSE_CLICKs and if
    # it hears one, do_something
    MOUSE_CLICK = '<Button-1>'
    MOUSE_DRAG = '<B1-Motion>'

    setup_listener(MOUSE_CLICK, select_circle)
    setup_listener(MOUSE_DRAG, move_circle)

    text((500, 500), text='Click or drag to create circles', font=("Purisa", 32))
        
    # Draw some circles!
    circle_counter = 0
    for i in range(50):
        circle((random.randint(0, 1000), random.randint(0, 1000)), radius=random.randint(10, 20), tag="circle_"+str(circle_counter))
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
    gui.update()
    time.sleep(1 / ticks_per_second)
    ticks = ticks + 1