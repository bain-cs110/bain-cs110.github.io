from tkinter import Canvas, Tk
import time
from helpers import make_grid

# initialize window
gui = Tk()
canvas = Canvas(gui, width=600, height=600, background='white')
canvas.pack()

# helper function that draws a grid.
make_grid(canvas, 600, 600)

########################## YOUR CODE BELOW THIS LINE ##############################

def make_square(canvas: Canvas, top_left: tuple, width: int, fill_color: str='#84A9C0', outline_color='#DDD', tag=None):
    canvas.create_rectangle([
            top_left,  # top_left
            (top_left[0] + width, top_left[1] + width)  # bottom_right
        ],
        fill=fill_color,
        outline=outline_color,
        tags=tag
    )

# Ask python to start a counter
counter = 0

width = 50
# Infinitely loop
while True:

    # Delete the existing shape on the screen
    canvas.delete("my_shape")
    canvas.delete("my_shape_2")

    # Each step, we draw a different colored square in a cycle of 1, 2, 3
    if counter % 3 == 0:
       make_square(canvas, (counter * 5, 100), width, fill_color="red", tag="my_shape")
       make_square(canvas, (counter * 5 + 100, 200), width, fill_color="red", tag="my_shape_2")

    elif counter % 3 == 1:
        make_square(canvas, (counter * 5, 100), width, fill_color="yellow", tag="my_shape")
        make_square(canvas, (counter * 5 + 100, 200), width, fill_color="yellow", tag="my_shape_2")
        
    else:
        make_square(canvas, (counter * 5, 100), width, fill_color="blue", tag="my_shape")
        make_square(canvas, (counter * 5 + 100, 200), width, fill_color="blue", tag="my_shape_2")

    # Ask Python to add one to the counter
    counter += 1

    # Ask TKinter to update our drawing
    gui.update()

    # Pause for a moment
    time.sleep(0.25)

########################## YOUR CODE ABOVE THIS LINE ##############################
canvas.mainloop()
