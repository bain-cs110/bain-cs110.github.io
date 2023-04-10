'''
This demo shows how you can move a SINGLE thing using the keyboard.
Documentation:
  * tkinter events: https://www.python-course.eu/tkinter_events_binds.php
  * Canvas: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas.html
  * Other Canvas methods: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas-methods.html
'''
from tkinter import Canvas, Tk
import project_utilities


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
    text='Click to add a circle. Right-click to select circle. Press arrow keys to move circle',
    font=("Purisa", 32)
)

# need a global variable to store which item should be clicked:
active_tag = None
def select_circle(event):
    global active_tag

    # if something is already active, deactivate it:
    if active_tag:
        project_utilities.update_fill(the_canvas, active_tag, 'hotpink')
        active_tag = None

    # get new active tag:
    active_tag = project_utilities.get_tag_from_event(
        the_canvas, event)
    if active_tag:
        project_utilities.update_fill(the_canvas, active_tag, 'yellow')

counter = 0
def handle_click(event):
    global counter
    project_utilities.make_circle(
        the_canvas,
        (event.x, event.y),
        20,
        fill_color='hotpink',
        tag='circle_' + str(counter)
    )
    counter += 1

def handle_key(event):    
    distance = 10
    if active_tag == None:
        pass
    elif event.keysym == "Up":
        project_utilities.update_position(
            the_canvas, tag=active_tag, x=0, y=-distance)
    elif event.keysym == "Down":
        project_utilities.update_position(
            the_canvas, tag=active_tag, x=0, y=distance)
    elif event.keysym == "Left":
        project_utilities.update_position(
            the_canvas, tag=active_tag, x=-distance, y=0)
    elif event.keysym == "Right":
        project_utilities.update_position(
            the_canvas, tag=active_tag, x=distance, y=0)
    else:
        print("Didn't know how to deal with:", event.keysym)


MOUSE_CLICK = '<Button-1>'
# DOUBLE_CLICK = '<Double-Button-1>' # This is sometimes difficult to time
RIGHT_CLICK = '<Button-2>'
KEY_PRESS = '<Key>'

# NOTE: canvas.focus_set() is critical to making the keyboard functions work:
the_canvas.focus_set()

the_canvas.bind(MOUSE_CLICK, handle_click)
the_canvas.bind(KEY_PRESS, handle_key)
the_canvas.bind(RIGHT_CLICK, select_circle)

########################## YOUR CODE ABOVE THIS LINE ##############################
# makes sure the canvas keeps running:
the_canvas.mainloop()
