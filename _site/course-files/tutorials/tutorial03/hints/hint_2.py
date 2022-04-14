from tkinter import Canvas, Tk
from helpers import make_square, make_grid

# initialize window
gui = Tk()
canvas = Canvas(gui, width=600, height=600, background='white')
canvas.pack()

make_grid(canvas, 600, 600)

# HINT 2:
# How could you alter this program so that Mario can easily be
# drawn *anywhere on the screen?
#
# Answer: you can always offset the x and y position of each "make_square"
# function call by ADDING the offset to each top_left coordinate argument.
# In other words, in the previous example, there was an implicit offset of
# (0, 0). But you wanted to change this offet to, say, (100, 50), then you
# would always add 100 to the value of your x coordinate and 50 to the
# value of your y coordinate as shown below.
#
# Now, how could you convert the program below to a function so that you
# could create multiple Marios drawn at different sizes, colors, and
# position?

# Mario anchored at position (x, y)
pixel = 20
top_left = (100, 50)
clothes = 'red'
overalls = 'blue'

x = top_left[0]
y = top_left[1]

# row 0 - Instead of using hard-coded x-coordinates, we can calculate each
# x-coordinate by multiplying whatever column we're in by the pixel size
# blank, pixel (0,0)
# blank, pixel (1,0)
# blank, pixel (2,0)
make_square(canvas, (x + 3*pixel, y), pixel, fill_color=clothes)  # pixel (3, 0)
make_square(canvas, (x + 4*pixel, y), pixel, fill_color=clothes)  # pixel (4, 0)
make_square(canvas, (x + 5*pixel, y), pixel, fill_color=clothes)  # pixel (5, 0)
make_square(canvas, (x + 6*pixel, y), pixel, fill_color=clothes)  # pixel (6, 0)
make_square(canvas, (x + 7*pixel, y), pixel, fill_color=clothes)  # pixel (7, 0)
make_square(canvas, (x + 8*pixel, y), pixel, fill_color=clothes)  # pixel (8, 0)

y = pixel + y # Move down one row in our drawing
# and update y so we don't have to add pixel * row_num each time

# row 1
# blank, pixel (0,1)
# blank, pixel (1,1)
make_square(canvas, (x + 2*pixel, y), pixel, fill_color=clothes)  # pixel (2, 1)
make_square(canvas, (x + 3*pixel, y), pixel, fill_color=clothes)  # pixel (3, 1)
make_square(canvas, (x + 4*pixel, y), pixel, fill_color=clothes)  # pixel (4, 1)
make_square(canvas, (x + 5*pixel, y), pixel, fill_color=clothes)  # pixel (5, 1)
make_square(canvas, (x + 6*pixel, y), pixel, fill_color=clothes)  # pixel (6, 1)
make_square(canvas, (x + 7*pixel, y), pixel, fill_color=clothes)  # pixel (7, 1)
make_square(canvas, (x + 8*pixel, y), pixel, fill_color=clothes)  # pixel (8, 1)
make_square(canvas, (x + 9*pixel, y), pixel, fill_color=clothes)  # pixel (9, 1)
make_square(canvas, (x + 10*pixel,y), pixel, fill_color=clothes)  # pixel (10, 1)
make_square(canvas, (x + 11*pixel,y), pixel, fill_color=clothes)  # pixel (11, 1)

## Now it's up to you to apply this to the next rows! ##

########################## YOUR CODE ABOVE THIS LINE ##############################
canvas.mainloop()
