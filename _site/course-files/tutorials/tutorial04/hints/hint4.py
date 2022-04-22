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
        if cell != 0:
            make_square(canvas, (x, y), pixel, fill_color=colors[cell])
        x += pixel

# create function:
def draw_pixel_art(canvas:Canvas, top_left:tuple, artwork:list, palette:list, pixel:int=10):
    x = top_left[0]
    y = top_left[1]
    for row in artwork:
        # draw each row at the specified (x, y) position:
        draw_row(canvas, row, (x, y), colors=palette, pixel=pixel)

        # ...and don't forget to shift the y-value down by the proper
        #  amount so that the next row won't draw on top of the first one:
        y += pixel

# invoke function:
draw_pixel_art(canvas, (0, 20), smiley, [None, "black"])
draw_pixel_art(canvas, (120, 220), goomba, [None, "saddle brown", "black", "tan"], pixel=12)
draw_pixel_art(canvas, (420, 250), goomba, [None, "black", "yellow" , "tan"], pixel=8)
draw_pixel_art(canvas, (55, 415), goomba, [None, "yellow", "purple", "brown"], pixel=6)
draw_pixel_art(canvas, (350, 115), smiley, ["white", "blue"], pixel=5)
draw_pixel_art(canvas, (315, 380), smiley, ["black", "pink"], pixel=15)
draw_pixel_art(canvas, (420, 10), smiley, [None, "red"], pixel=10)

########################## YOUR CODE ABOVE THIS LINE ##############################
canvas.mainloop()
