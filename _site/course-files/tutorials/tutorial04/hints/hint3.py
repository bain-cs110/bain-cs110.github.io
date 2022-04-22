from tkinter import Canvas, Tk
from helpers import make_square, make_grid

# initialize window
gui = Tk()
canvas = Canvas(gui, width=600, height=600, background='white')
canvas.pack()

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
make_grid(canvas, 600, 600)

def draw_row(canvas:Canvas, row:tuple, top_left:tuple, colors:list, pixel:int=25):
    x = top_left[0]
    y = top_left[1]
    for cell in row:
        # Remember that 0 means "no square here" so this skips any pixel that is a 0
        if cell != 0:
            # We use the cell we're looking at as the address of the color we want
            make_square(canvas, (x, y), pixel, fill_color=colors[cell])
        x += pixel

############################
# EXAMPLE FOR YOU: SMILEY #
############################
y = 50
for row in smiley:
    # draw each row at the specified (x, y) position:
    draw_row(canvas, row, (50, y), [None, "teal"], pixel=20)
    # ...and don't forget to shift the y-value down by the proper
    #  amount so that the next row won't draw on top of the first one:
    y += 20

############################
# STILL TO DO: Goomba #
############################



########################## YOUR CODE ABOVE THIS LINE ##############################
canvas.mainloop()
