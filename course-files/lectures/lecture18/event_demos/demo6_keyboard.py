'''
This demo shows you how to move an object using the keyboard.
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
the_canvas = Canvas(gui, width=window_width, height=window_height, background='white')
the_canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################
the_canvas.create_text(
    (window_width / 2, window_height / 2),
    text='Click anywhere add a circle. Press arrow keys to move circle',
    font=("Purisa", 32)
)
the_canvas.create_text(
    (window_width / 2, window_height / 2 + 50),
    text='Note: before keyboard functions work, you need to call canvas.focus_set()',
    font=("Purisa", 32)
)

def handle_click(event):
    p1_utilities.make_circle(
        the_canvas,
        (event.x, event.y),
        20,
        fill_color='hotpink',
        tag='circle'
    )

def handle_keyboard(event):
    # Key symbols names for Tkinter: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/key-names.html
    print(event)

    distance = 10

    # if they press up on the keyboard
    if event.keysym == "Up":
        p1_utilities.update_position(the_canvas, tag='circle', x=0, y=-distance)
    # otherwise if they press down on the keyboard
    elif event.keysym == "Down":
        p1_utilities.update_position(the_canvas, tag='circle', x=0, y=distance)
    # otherwise if they press left on the keyboard
    elif event.keysym == "Left":
        p1_utilities.update_position(the_canvas, tag='circle', x=-distance, y=0)
    # otherwise if they press right on the keyboard
    elif event.keysym == "Right":
        p1_utilities.update_position(the_canvas, tag='circle', x=distance, y=0)
    else:
        print('Key sym:', event.keysym, 'not handled by this if/elif/else statement.')

MOUSE_CLICK = '<Button-1>'
KEY_PRESS = '<Key>'

# NOTE: canvas.focus_set() is critical to making the keyboard functions work:
the_canvas.focus_set()

the_canvas.bind(MOUSE_CLICK, handle_click)
the_canvas.bind(KEY_PRESS, handle_keyboard)

########################## YOUR CODE ABOVE THIS LINE ##############################
# makes sure the canvas keeps running:
the_canvas.mainloop()
