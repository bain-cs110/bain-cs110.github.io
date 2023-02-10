'''
Documentation:
  * tkinter events: https://www.python-course.eu/tkinter_events_binds.php
  * Canvas: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas.html
  * Other Canvas methods: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas-methods.html
'''
from tkinter import Canvas, Tk
import project_utilities
import random
import time

gui = Tk()
gui.title('Tour of options...')

# initialize canvas:
window_width = 1000
window_height = 1000
the_canvas = Canvas(gui, width=window_width,
                    height=window_height, background='white')
the_canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################
MOUSE_DRAG = '<B1-Motion>'
MOUSE_CLICK = '<Button-1>'

user_shapes = []
def click_handler(event):
    tag = 'circle_' + str(len(user_shapes))
    project_utilities.make_circle(
        the_canvas,
        (event.x, event.y),
        random.uniform(10, 50),
        fill_color="cyan",
        tag=tag
    )
    # add our shape to a list called user_shapes by appending
    # a tuple with its tag and a randomly generated speed to travel at
    user_shapes.append((tag, random.uniform(1, 5)))

shape_id = the_canvas.create_text(
    (window_width / 2, window_height / 2),
    text='Click or drag to create circles',
    font=("Purisa", 32)
)

the_canvas.bind(MOUSE_DRAG, click_handler)
the_canvas.bind(MOUSE_CLICK, click_handler)

# animation loop should come after everything else
# (because while loop never terminates, and therefore nothing
# below the while loop will ever run):
while True:
    # for every shape in user_shapes
    for shape in user_shapes:

        shape_tag = shape[0] # load the shape's tag
        shape_speed = -1 * shape[1] # load the shape's speed

        # if one of our shapes reaches the bottom of the canvas
        if project_utilities.get_bottom(the_canvas, shape_tag) > 1000:
            # then calculate a new position at the "top" of the canvas
            reset_position = window_height + project_utilities.get_height(the_canvas, shape_tag)
            # and move the shape with that tag to that "top" of the canvas
            project_utilities.update_position(
                the_canvas, tag=shape_tag, y= -1 * reset_position)

        # regardless move the shape a little bit (determined by its speed)
        project_utilities.update_position(
            the_canvas, tag=shape_tag, x=0, y=-1 * shape_speed)
    gui.update()
    time.sleep(0.002)
