from tkinter import Canvas, Tk
from lecture15_utilities import make_grid
import random

# initialize window
gui = Tk()
the_canvas = Canvas(gui, width=600, height=600, background='white')
the_canvas.pack()

def make_square(a_canvas, top_left, width, color="white"):
    a_canvas.create_rectangle(
        top_left,
        (top_left[0] + width, top_left[1] + width),
        fill=color)

make_grid(the_canvas, 600, 600) # draw the grid

MARIO = [
    (0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0),
    (0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0),
    (0, 0, 3, 3, 3, 4, 4, 4, 5, 4, 0, 0, 0, 0),
    (0, 3, 4, 3, 4, 4, 4, 4, 5, 4, 4, 4, 0, 0),
    (0, 3, 4, 3, 4, 4, 4, 4, 4, 5, 4, 4, 4, 0),
    (0, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 0, 0),
    (0, 0, 1, 1, 2, 1, 1, 1, 2, 0, 0, 0, 0, 0),
    (0, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 0, 0, 0),
    (1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0),
    (4, 4, 1, 2, 6, 2, 2, 6, 2, 1, 4, 4, 0, 0),
    (4, 4, 4, 2, 2, 2, 2, 2, 2, 4, 4, 4, 0, 0),
    (4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 0, 0),
    (0, 0, 2, 2, 2, 0, 0, 2, 2, 2, 0, 0, 0, 0),
    (0, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 0, 0, 0),
    (3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 0, 0)
]

mario_colors = [None, "red", "blue", "saddle brown", "bisque3", "black", "gold"]

########################## YOUR CODE BELOW THIS LINE ##############################
# Name: draw_row
# Purpose: draws a single row of pixel art
# Inputs:
#  1. a_canvas (Canvas), the canvas to draw on
#  2. row (tuple), the row of the artwork we want to draw
#  3. top_left (tuple), the top left coordinate to draw the picture at
#  4. colors (list) a list of colors to draw with
#  5. pixel (int; optional) the size of each pixel


# Name: draw_pixel_art
# Purpose: draws an entire piece of pixel art
# Inputs:
#  1. a_canvas (Canvas), the canvas to draw on
#  2. top_left (tuple), the top left coordinate to draw the picture at
#  3. artwork (list) the actual picture to draw
#  4. palette (list) a list of colors to draw with
#  5. pixel (int; optional) the size of each pixel



### OLD CODE WAS BELOW HERE...see mario_with_loops_old!

########################## YOUR CODE ABOVE THIS LINE ##############################
the_canvas.mainloop()
