'''
This demo shows you how you can create a new image by dragging across the screen.
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
    text='Drag to create circles',
    font=("Purisa", 32))

# Here's our handler function
def handle_clicks(event):
    project_utilities.make_circle(
        the_canvas,
        (event.x, event.y),
        20,
        fill_color='hotpink'
    )

MOUSE_DRAG = '<B1-Motion>'
MOUSE_CLICK = '<Button-1>'
the_canvas.bind(MOUSE_DRAG, handle_clicks)
the_canvas.bind(MOUSE_CLICK, handle_clicks)

########################## YOUR CODE ABOVE THIS LINE ##############################

# makes sure the canvas keeps running:
the_canvas.mainloop()
