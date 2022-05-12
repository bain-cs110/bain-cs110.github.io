'''
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

canvas.focus_set()
########################## YOUR CODE BELOW THIS LINE ##############################
MOUSE_CLICK = '<Button-1>'
RIGHT_CLICK = '<Button-2>'

### NOTE: If you're RIGHT_CLICK doesn't work, try uncommenting out the below line:
##RIGHT_CLICK = '<Button-3>'

## If that STILL doesn't work, you can have Tkinter listen for a "double click" instead
##RIGHT_CLICK = '<Double-Button-1>'

def make_circle(event):
    utilities.make_circle(
        canvas,
        (event.x, event.y),
        20,
        fill_color='hotpink'
    )

def remove_circle(event):
    # http://effbot.org/tkinterbook/canvas.htm#reference
    tag = utilities.get_tag_from_x_y_coordinate(canvas, event.x, event.y)
    utilities.delete_by_tag(canvas, tag)


canvas.create_text(
    (window_width / 2, window_height / 2),
    text='Click to create circle. Right-click to remove circle',
    font=("Purisa", 32)
)

canvas.bind(MOUSE_CLICK, make_circle)
canvas.bind(RIGHT_CLICK, remove_circle)

########################## YOUR CODE ABOVE THIS LINE ##############################

# makes sure the canvas keeps running:
canvas.mainloop()
