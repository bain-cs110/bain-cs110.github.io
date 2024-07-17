from tkinter import Canvas, Tk
from utilities import make_square, make_grid

# initialize window
gui = Tk()
the_canvas = Canvas(gui, width=600, height=600,
                    background='white', scrollregion="0 -600 600 0")
the_canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################
# smiley face
smiley = [
   (0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 1, 0, 0, 1, 0, 0),
   (0, 0, 1, 0, 0, 1, 0, 0),
   (0, 0, 1, 0, 0, 1, 0, 0),
   (1, 0, 0, 0, 0, 0, 0, 1),
   (1, 1, 0, 0, 0, 0, 1, 1),
   (0, 1, 1, 0, 0, 1, 1, 0),
   (0, 0, 1, 1, 1, 1, 0, 0)
]

# goomba
goomba = [
    (0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0),
    (0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0),
    (0, 0, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 0, 0),
    (0, 1, 1, 1, 0, 2, 1, 1, 1, 1, 2, 0, 1, 1, 1, 0),
    (0, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 0, 1, 1, 1, 0),
    (1, 1, 1, 1, 0, 2, 0, 1, 1, 0, 2, 0, 1, 1, 1, 1),
    (1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (0, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 0),
    (0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0),
    (0, 0, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 0, 0),
    (0, 2, 2, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 2, 0),
    (0, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0),
    (0, 0, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 0, 0)
]

# helper function that draws a grid.
make_grid(the_canvas, 600, 600)

# Name: draw_row
# Purpose: draws a given pixel art row using squares
# Inputs:
#   1. a canvas (Canvas) to draw on
#   2. a row (tuple) of ints each representing a color
#   3. a bottom_left (tuple; (x,y)) to start at
#   4. a colors (list) to list the different colors to draw with
#   5. pixel (int; optional) how big each pixel should be
def draw_row(a_canvas, row, bottom_left, colors, pixel=25):
    x = bottom_left[0]
    y = bottom_left[1]

    for cell in row:
        make_square(the_canvas, (x, y), pixel, color=colors[cell])
        x += pixel

# Name: draw_pixel_art
# Purpose: draws an entire pixel art given a list of tuples
# Inputs:
#   1. a canvas (Canvas) to drawn on
#   2. a coordinate (tuple) to draw the bottom left of the figure
#   3. a piece of artwork (list of tuples) to draw
#   4. a list of colors (strings) to draw with
#   5. pixel (int; optional) the size of each square
def draw_pixel_art(a_canvas, bottom_left, artwork, palette, pixel=10):
    x = bottom_left[0]
    y = bottom_left[1] + len(artwork) * pixel
    for row in artwork:
        draw_row(a_canvas, row, (x,y), palette, pixel=pixel)
        y = y - pixel

draw_pixel_art(the_canvas, (0, 20), smiley, [None, "black"])
draw_pixel_art(the_canvas, (120, 220), goomba, [None, "saddle brown", "black", "tan"], pixel=12)
draw_pixel_art(the_canvas, (420, 250), goomba, [None, "black", "yellow" , "tan"], pixel=8)
draw_pixel_art(the_canvas, (55, 415), goomba, [None, "yellow", "purple", "brown"], pixel=6)
draw_pixel_art(the_canvas, (350, 115), smiley, ["white", "blue"], pixel=5)
draw_pixel_art(the_canvas, (315, 380), smiley, ["black", "pink"], pixel=15)
draw_pixel_art(the_canvas, (420, 10), smiley, [None, "red"], pixel=10)

########################## YOUR CODE ABOVE THIS LINE ##############################
the_canvas.scale("all", 0, 0, 1, -1)
the_canvas.mainloop()
