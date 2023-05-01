from tkinter import Canvas, Tk
import time
from lecture15_utilities import make_grid

# initialize window
gui = Tk()
the_canvas = Canvas(gui, width=600, height=600, background='white')
the_canvas.pack()

# helper function that draws a grid.
make_grid(the_canvas, 600, 600)
########################## YOUR CODE BELOW THIS LINE ##############################

def make_square(a_canvas, top_left, width, fill_color='#84A9C0', outline_color='#DDD', tag=""):
    a_canvas.create_rectangle([
        top_left,
        (top_left[0] + width, top_left[1] + width)
        ],
        fill=fill_color,
        outline=outline_color,
        tags=tag
    )
    a_canvas.master.update()

width = 100

# Ask python to start a counter
counter = 0
# Infinite loop
while True:
    # Delete the existing shape on the screen
    the_canvas.delete("my_shape")

    # Each step, we draw a colored square
    make_square(the_canvas, (counter * 5, 100), width, fill_color="red", tag="my_shape")

    # Ask Python to add one to the counter
    counter += 1

    # Pause for a moment
    time.sleep(0.1)

########################## YOUR CODE ABOVE THIS LINE ##############################
the_canvas.mainloop()
