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

def draw_row(canvas:Canvas, row:tuple, top_left:tuple, pixel:int=25):
    x = top_left[0]
    y = top_left[1]
    for cell in row:
        make_square(canvas, (x, y), pixel, fill_color='grey')
        x += pixel

### Draw the smiley face
# first 6 rows of smiley
draw_row(canvas, smiley[0], (10, 50), pixel=20)
draw_row(canvas, smiley[1], (10, 70), pixel=20)
draw_row(canvas, smiley[2], (10, 90), pixel=20)
draw_row(canvas, smiley[3], (10, 110), pixel=20)
draw_row(canvas, smiley[4], (10, 130), pixel=20)
draw_row(canvas, smiley[5], (10, 150), pixel=20)


### Draw the goomba
# first 6 rows of the goomba
draw_row(canvas, goomba[0], (250, 250), pixel=10)
draw_row(canvas, goomba[1], (250, 260), pixel=10)
draw_row(canvas, goomba[2], (250, 270), pixel=10)
draw_row(canvas, goomba[3], (250, 280), pixel=10)
draw_row(canvas, goomba[4], (250, 290), pixel=10)
draw_row(canvas, goomba[5], (250, 300), pixel=10)


########################## YOUR CODE ABOVE THIS LINE ##############################
canvas.mainloop()
