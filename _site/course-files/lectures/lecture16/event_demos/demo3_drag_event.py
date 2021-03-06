'''
This demo shows you how you can create a new image by dragging across the screen.
Documentation:
  * tkinter events: https://www.python-course.eu/tkinter_events_binds.php
  * Canvas: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas.html
  * Other Canvas methods: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas-methods.html
'''
from tkinter import Canvas, Tk
import utilities

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

def make_circle(event):
    utilities.make_circle(
        canvas,
        (event.x, event.y),
        20,
        fill_color='hotpink'
    )


canvas.create_text(
    (window_width / 2, window_height / 2),
    text='Drag to create circles',
    font=("Purisa", 32)
)


canvas.bind(MOUSE_DRAG, make_circle)
canvas.bind(MOUSE_CLICK, make_circle)


########################## YOUR CODE ABOVE THIS LINE ##############################

# makes sure the canvas keeps running:
canvas.mainloop()
