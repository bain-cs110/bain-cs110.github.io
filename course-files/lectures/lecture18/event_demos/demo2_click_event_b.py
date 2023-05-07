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
    text='Click anywhere add a square',
    font=("Purisa", 32))

square_counter = 0
def make_square_from_click(event):

    # use the random module to pick a random number between 40 and 150
    a_width = random.uniform(40, 150)

    # use the random module to pick a random color from a list of colors
    a_color = random.choice(['white', 'yellow', 'blue', 'pink'])

    # Tell Python we're using the GLOBAL version of this variable
    global square_counter
    # generate a new tag for this shape based on how many there are on the screen
    my_tag = "sqaure_" + str(square_counter)
    square_counter += 1

    # create a creature at the place the person clicked with
    p1_utilities.make_square(
        the_canvas,
        (event.x, event.y),
        a_width,
        fill_color=a_color,
        tag=my_tag
    )
    
MOUSE_CLICK = '<Button-1>'
the_canvas.bind(MOUSE_CLICK, make_square_from_click)  # add event handler

########################## YOUR CODE ABOVE THIS LINE ##############################

# makes sure the canvas keeps running:
the_canvas.mainloop()
