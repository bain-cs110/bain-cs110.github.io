from tkinter import Canvas, Tk
from helpers import make_square, make_grid

# initialize window
gui = Tk()
canvas = Canvas(gui, width=600, height=600, background='white')
canvas.pack()


# helper function that draws a grid.
make_grid(canvas, 600, 600)

# HINT 1:
# Note that each of the x-positions can be re-written in terms of
# the pixel value. The advantage of rewriting your code in this
# way is that it allows you to be able to scale your frankenstein.
# In other words, if you update the size of the pixel (using the
# pixel variable below), Mario scales.

# However, no matter what, Mario is still anchored at
# position (0, 0). How could you alter this program so that frank
# could be drawn *anywhere on the screen?
pixel = 25

clothes = 'red'
accessories = 'saddle brown'
tone = 'bisque3'
features = 'black'
overalls = "blue"

# row 0 - Instead of using hard-coded x-coordinates, we can calculate each
# x-coordinate by multiplying whatever column we're in by the pixel size
# blank, pixel (0,0)
# blank, pixel (1,0)
# blank, pixel (2,0)
make_square(canvas, (3*pixel, 0), pixel, fill_color=clothes)  # pixel (3, 0)
make_square(canvas, (4*pixel, 0), pixel, fill_color=clothes)  # pixel (4, 0)
make_square(canvas, (5*pixel, 0), pixel, fill_color=clothes)  # pixel (5, 0)
make_square(canvas, (6*pixel, 0), pixel, fill_color=clothes)  # pixel (6, 0)
make_square(canvas, (7*pixel, 0), pixel, fill_color=clothes)  # pixel (7, 0)
make_square(canvas, (8*pixel, 0), pixel, fill_color=clothes)  # pixel (8, 0)

# row 1
# blank, pixel (0,1)
# blank, pixel (1,1)
make_square(canvas, (2*pixel, 25), pixel, fill_color=clothes)  # pixel (2, 1)
make_square(canvas, (3*pixel, 25), pixel, fill_color=clothes)  # pixel (3, 1)
make_square(canvas, (4*pixel, 25), pixel, fill_color=clothes)  # pixel (4, 1)
make_square(canvas, (5*pixel, 25), pixel, fill_color=clothes)  # pixel (5, 1)
make_square(canvas, (6*pixel, 25), pixel, fill_color=clothes)  # pixel (6, 1)
make_square(canvas, (7*pixel, 25), pixel, fill_color=clothes)  # pixel (7, 1)
make_square(canvas, (8*pixel, 25), pixel, fill_color=clothes)  # pixel (8, 1)
make_square(canvas, (9*pixel, 25), pixel, fill_color=clothes)  # pixel (9, 1)
make_square(canvas, (10*pixel,25), pixel, fill_color=clothes)  # pixel (10, 1)
make_square(canvas, (11*pixel,25), pixel, fill_color=clothes)  # pixel (11, 1)

## Now it's up to you to apply this to the next rows! ##


########################## YOUR CODE ABOVE THIS LINE ##############################
canvas.mainloop()
