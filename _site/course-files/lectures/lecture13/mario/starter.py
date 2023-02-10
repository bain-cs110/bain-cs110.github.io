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
#   4. pixel (int; optional) how big each pixel should be
def draw_row(a_canvas, row, bottom_left, pixel=25):
    x = bottom_left[0]
    y = bottom_left[1]

    for cell in row:
        make_square(a_canvas, (x, y), pixel, color='grey')
        x += pixel

### Draw the smiley face
# first 6 rows of smiley
draw_row(the_canvas, smiley[0], (10, 150), pixel=20)
draw_row(the_canvas, smiley[1], (10, 130), pixel=20)
draw_row(the_canvas, smiley[2], (10, 110), pixel=20)
draw_row(the_canvas, smiley[3], (10, 90), pixel=20)
draw_row(the_canvas, smiley[4], (10, 70), pixel=20)
draw_row(the_canvas, smiley[5], (10, 50), pixel=20)


### Draw the goomba
# first 6 rows of the goomba
draw_row(the_canvas, goomba[0], (250, 300), pixel=10)
draw_row(the_canvas, goomba[1], (250, 290), pixel=10)
draw_row(the_canvas, goomba[2], (250, 280), pixel=10)
draw_row(the_canvas, goomba[3], (250, 270), pixel=10)
draw_row(the_canvas, goomba[4], (250, 260), pixel=10)
draw_row(the_canvas, goomba[5], (250, 250), pixel=10)


##draw_pixel_art(the_canvas, (0, 20), smiley, [None, "black"])
##draw_pixel_art(the_canvas, (120, 220), goomba, [None, "saddle brown", "black", "tan"], pixel=12)
##draw_pixel_art(the_canvas, (420, 250), goomba, [None, "black", "yellow" , "tan"], pixel=8)
##draw_pixel_art(the_canvas, (55, 415), goomba, [None, "yellow", "purple", "brown"], pixel=6)
##draw_pixel_art(the_canvas, (350, 115), smiley, ["white", "blue"], pixel=5)
##draw_pixel_art(the_canvas, (315, 380), smiley, ["black", "pink"], pixel=15)
##draw_pixel_art(the_canvas, (420, 10), smiley, [None, "red"], pixel=10)

########################## YOUR CODE ABOVE THIS LINE ##############################
the_canvas.scale("all", 0, 0, 1, -1)
the_canvas.mainloop()
