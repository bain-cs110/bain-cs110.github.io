'''
This demo shows you how you can create a new image by clicking the screen.
Documentation:
  * tkinter events: https://www.python-course.eu/tkinter_events_binds.php
  * Canvas: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas.html
  * Other Canvas methods: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas-methods.html
'''
from tkinter import Canvas, Tk
import p1_utilities
import random

gui = Tk()
gui.title('Tour of options...')

# initialize canvas:
window_width = 1000
window_height = 1000
the_canvas = Canvas(gui, width=window_width,
                    height=window_height, background='white')
the_canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

the_canvas.create_text(
    (window_width / 2, window_height / 2),
    text='Click circle to select it. Drag selected circle to move it.',
    font=("Purisa", 32)
)

# need a global variable to store which item should be clicked:
active_tag = None

def select_circle(event):
    global active_tag

    # if something is already active, deactivate it:
    if active_tag:
        p1_utilities.update_fill(the_canvas, active_tag, 'hotpink')
        active_tag = None

    # get new active tag:
    active_tag = p1_utilities.get_tag_from_event(
        the_canvas, event)
    if active_tag:
        p1_utilities.update_fill(the_canvas, active_tag, 'yellow')


def move_circle(event):
    if not active_tag:
        print('no tag selected')
        return

    # calculate the current position of the current shape:
    width = p1_utilities.get_width(the_canvas, active_tag)
    height = p1_utilities.get_height(the_canvas, active_tag)
    left = p1_utilities.get_left(the_canvas, active_tag)
    top = p1_utilities.get_top(the_canvas, active_tag)
    current_x = left + (width / 2)
    current_y = top + (height / 2)

    # calculate the delta of the current shape:
    delta_x = -1 * (current_x - event.x)
    delta_y = -1 * (current_y - event.y)

    # move the shape:
    p1_utilities.update_position(
        the_canvas, active_tag, x=delta_x, y=delta_y)

counter = 1
def make_circle(x, y):
    global counter
    p1_utilities.make_circle(
        the_canvas,
        (x, y),
        20,
        fill_color='hotpink',
        tag='circle_' + str(counter)
    )
    counter += 1
    
MOUSE_CLICK = '<Button-1>'
MOUSE_DRAG = '<B1-Motion>'
RIGHT_CLICK = '<Button-2>'
KEY_PRESS = '<Key>'

the_canvas.bind(MOUSE_CLICK, select_circle)
the_canvas.bind(MOUSE_DRAG, move_circle)

for i in range(50):
    make_circle(random.randint(0, window_width), random.randint(0, window_height))

the_canvas.focus_set()
########################## YOUR CODE ABOVE THIS LINE ##############################
# makes sure the canvas keeps running:
the_canvas.mainloop()
