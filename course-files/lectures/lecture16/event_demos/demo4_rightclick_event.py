'''
Documentation:
  * tkinter events: https://www.python-course.eu/tkinter_events_binds.php
  * Canvas: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas.html
  * Other Canvas methods: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas-methods.html
'''
from tkinter import Canvas, Tk
import p1_utilities

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
    text='Click to create circle. Right-click to remove circle',
    font=("Purisa", 32)
)

def click_handler(event):
    shape_id = p1_utilities.make_circle(
        the_canvas,
        (event.x, event.y),
        20,
        fill_color='hotpink'
    )

def right_click_handler(event):
    tag = p1_utilities.get_tag_from_event(the_canvas, event)
    p1_utilities.delete(the_canvas, tag)

MOUSE_CLICK = '<Button-1>'
RIGHT_CLICK = '<Button-2>'

### NOTE: If you're RIGHT_CLICK doesn't work, try uncommenting out the below line:
##RIGHT_CLICK = '<Button-3>'

## If that STILL doesn't work, you can have Tkinter listen for a "double click" instead
##RIGHT_CLICK = '<Double-Button-1>'
the_canvas.bind(MOUSE_CLICK, click_handler)
the_canvas.bind(RIGHT_CLICK, right_click_handler)

########################## YOUR CODE ABOVE THIS LINE ##############################

# makes sure the canvas keeps running:
the_canvas.mainloop()
