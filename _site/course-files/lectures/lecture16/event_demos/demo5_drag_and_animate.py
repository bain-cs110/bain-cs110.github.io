'''
Documentation:
  * tkinter events: https://www.python-course.eu/tkinter_events_binds.php
  * Canvas: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas.html
  * Other Canvas methods: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas-methods.html
'''
from tkinter import Canvas, Tk
import utilities
import time
import random

gui = Tk()
gui.title('Tour of options...')

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
canvas = Canvas(gui, width=window_width, height=window_height, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################
MOUSE_DRAG = '<B1-Motion>'
MOUSE_CLICK = '<Button-1>'
user_shapes = []

def make_circle(event):
    tag = 'circle_' + str(len(user_shapes))
    utilities.make_circle(
        canvas,
        (event.x, event.y),
        random.uniform(10, 50),
        fill_color=None,
        tag=tag
    )
    # add our shape to a list called user_shapes by appending
    # a tuple with its tag and a randomly generated speed to travel at
    user_shapes.append((tag, random.uniform(1, 5)))


canvas.create_text(
    (window_width / 2, window_height / 2),
    text='Click or drag to create circles',
    font=("Purisa", 32)
)

canvas.bind(MOUSE_DRAG, make_circle)
canvas.bind(MOUSE_CLICK, make_circle)

# animation loop should come after everything else
# (because while loop never terminates, and therefore nothing
# below the while loop will ever run):
while True:
    # for every shape in user_shapes
    for shape in user_shapes:

        shape_tag = shape[0] # load the shape's tag
        shape_speed = -1 * shape[1] # load the shape's speed

        # if one of our shapes reaches the "bottom" of the canvas
        if utilities.get_bottom(canvas, shape_tag) < 0:
            # then calculate a new position at the "top" of the canvas
            reset_position = window_height + utilities.get_width(canvas, shape_tag)
            # and move the shape with that tag to that "top" of the canvas
            utilities.update_position_by_tag(canvas, tag=shape_tag, y=reset_position)

        # regardless move the shape a little bit (determined by its speed)
        utilities.update_position_by_tag(canvas, tag=shape_tag, x=0, y=shape_speed)
    gui.update()
    time.sleep(0.002)
