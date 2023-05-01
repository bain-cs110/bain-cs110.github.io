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

GOOMBA_COLORS = [None, "saddle brown", "black", "tan", "white"]
# goomba
GOOMBA = [
    (0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0),
    (0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0),
    (0, 0, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 0, 0),
    (0, 1, 1, 1, 4, 2, 1, 1, 1, 1, 2, 4, 1, 1, 1, 0),
    (0, 1, 1, 1, 4, 2, 2, 2, 2, 2, 2, 4, 1, 1, 1, 0),
    (1, 1, 1, 1, 4, 2, 4, 1, 1, 4, 2, 4, 1, 1, 1, 1),
    (1, 1, 1, 1, 4, 4, 4, 1, 1, 4, 4, 4, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (0, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 0),
    (0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0),
    (0, 0, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 0, 0),
    (0, 2, 2, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 2, 0),
    (0, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0),
    (0, 0, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 0, 0)
]

########################## YOUR CODE BELOW THIS LINE ##############################
# Name: draw_row
# Purpose: draws a single row of pixel art
# Inputs:
#  1. a_canvas (Canvas), the canvas to draw on
#  2. row (tuple), the row of the artwork we want to draw
#  3. top_left (tuple), the top left coordinate to draw the picture at
#  4. colors (list) a list of colors to draw with
#  5. pixel (int; optional) the size of each pixel
def draw_row(a_canvas, row, top_left, colors, pixel=25):
    x = top_left[0]
    y = top_left[1]

    for cell in row:
        if cell != 0:
            make_square(a_canvas, (x, y), pixel, color=colors[cell])
        x = pixel + x
        
# Name: draw_pixel_art
# Purpose: draws an entire piece of pixel art
# Inputs:
#  1. a_canvas (Canvas), the canvas to draw on
#  2. top_left (tuple), the top left coordinate to draw the picture at
#  3. artwork (list) the actual picture to draw
#  4. palette (list) a list of colors to draw with
#  5. pixel (int; optional) the size of each pixel

def draw_pixel_art(a_canvas, top_left, artwork, palette, pixel=25):

    x = top_left[0]
    y = top_left[1]

    for row in artwork:
        draw_row(a_canvas, row, (x,y), palette, pixel=pixel)
        y += pixel

# Draw 50 sample marios and goombas!
for counter in range(50):
    if counter % 2 == 0:
        draw_pixel_art(the_canvas,
                       (random.randint(0, 600), random.randint(0, 600)),
                       MARIO,
                       [None, "red", "blue", "saddle brown", "bisque3", "black", "gold"],
                       pixel=random.randint(1, 15))
    else:
        draw_pixel_art(the_canvas,
                       (random.randint(0, 600), random.randint(0, 600)),
                       GOOMBA,
                       GOOMBA_COLORS,
                       pixel=random.randint(1, 15))

########################## YOUR CODE ABOVE THIS LINE ##############################
the_canvas.mainloop()
