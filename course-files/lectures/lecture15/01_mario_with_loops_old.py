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

########################## YOUR CODE BELOW THIS LINE ##############################
accessories = 'saddle brown'
tone = 'bisque3'
features = 'black'
clothes = "red"
pixel = 25
overalls = "blue"

def get_xy(origin, pixel_size, mario_coord):
    x = origin[0] # extract the x-coordinate
    y = origin[1] # extract the y-coordinate

    row = mario_coord[0] # extract the row number
    col = mario_coord[1] # extract the col number

    new_x = x + row * pixel_size # calculate the new x
    new_y = y - col * pixel_size # calculate the new y

    return (new_x, new_y)

def make_mario(the_canvas, top_left, pixel=25, clothes="red", overalls="blue"):
    origin = top_left
    
    # row 14
    # blank, pixel (0,14)
    # blank, pixel (1,14)
    # blank, pixel (2,14)
    make_square(the_canvas, get_xy(origin, pixel, (3,14)), pixel, color=clothes) # pixel (3, 14)
    make_square(the_canvas, get_xy(origin, pixel, (4,14)), pixel, color=clothes)  # pixel (4, 14)
    make_square(the_canvas, get_xy(origin, pixel, (5,14)), pixel, color=clothes)  # pixel (5, 14)
    make_square(the_canvas, get_xy(origin, pixel, (6,14)), pixel, color=clothes)  # pixel (6, 14)
    make_square(the_canvas, get_xy(origin, pixel, (7,14)), pixel, color=clothes)  # pixel (7, 14)
    make_square(the_canvas, get_xy(origin, pixel, (8,14)), pixel, color=clothes)  # pixel (8, 14)

    # row 13
    # blank, pixel (0,13)
    # blank, pixel (1,13)
    make_square(the_canvas, get_xy(origin, pixel, (2,13)), pixel, color=clothes)  # pixel (2, 13)
    make_square(the_canvas, get_xy(origin, pixel, (3,13)),pixel, color=clothes)  # pixel (3, 13)
    make_square(the_canvas, get_xy(origin, pixel, (4,13)),pixel, color=clothes) # pixel (4, 13)
    make_square(the_canvas, get_xy(origin, pixel, (5,13)),pixel, color=clothes) # pixel (6, 13)
    make_square(the_canvas, get_xy(origin, pixel, (6,13)),pixel, color=clothes) # pixel (6, 13)
    make_square(the_canvas, get_xy(origin, pixel, (7,13)),pixel, color=clothes) # pixel (7, 13)
    make_square(the_canvas, get_xy(origin, pixel, (8,13)),pixel, color=clothes) # pixel (8, 13)
    make_square(the_canvas, get_xy(origin, pixel, (9,13)),pixel, color=clothes) # pixel (9, 13)
    make_square(the_canvas, get_xy(origin, pixel, (10,13)),pixel, color=clothes) # pixel (10, 13)
    make_square(the_canvas, get_xy(origin, pixel, (11,13)),pixel, color=clothes) # pixel (11, 13)

    # row 12
    # blank, pixel (0,12)
    # blank, pixel (1,12)
    make_square(the_canvas, get_xy(origin, pixel, (2,12)),pixel, color=accessories) # pixel (2, 12)
    make_square(the_canvas, get_xy(origin, pixel, (3,12)),pixel, color=accessories) # pixel (3, 12)
    make_square(the_canvas, get_xy(origin, pixel, (4,12)),pixel, color=accessories) # pixel (4, 12)
    make_square(the_canvas, get_xy(origin, pixel, (5,12)),pixel, color=tone) # pixel (5, 12)
    make_square(the_canvas, get_xy(origin, pixel, (6,12)),pixel, color=tone) # pixel (6, 12)
    make_square(the_canvas, get_xy(origin, pixel, (7,12)),pixel, color=tone) # pixel (7, 12)
    make_square(the_canvas, get_xy(origin, pixel, (8,12)),pixel, color=features) # pixel (8, 12)
    make_square(the_canvas, get_xy(origin, pixel, (9,12)),pixel, color=tone) # pixel (9, 12)

    # row 11
    # blank, pixel (0,11)
    make_square(the_canvas, get_xy(origin, pixel, (1,11)),pixel, color=accessories) # pixel (1, 11)
    make_square(the_canvas, get_xy(origin, pixel, (2,11)),pixel, color=tone) # pixel (2,11)
    make_square(the_canvas, get_xy(origin, pixel, (3,11)),pixel, color=accessories) # pixel (3, 11)
    make_square(the_canvas, get_xy(origin, pixel, (4,11)),pixel, color=tone) # pixel (4, 11)
    make_square(the_canvas, get_xy(origin, pixel, (5,11)),pixel, color=tone) # pixel (5, 11)
    make_square(the_canvas, get_xy(origin, pixel, (6,11)),pixel, color=tone) # pixel (6, 11)
    make_square(the_canvas, get_xy(origin, pixel, (7,11)),pixel, color=tone) # pixel (7, 11)
    make_square(the_canvas, get_xy(origin, pixel, (8,11)),pixel, color=features) # pixel (8, 11)
    make_square(the_canvas, get_xy(origin, pixel, (9,11)),pixel, color=tone) # pixel (9, 11)
    make_square(the_canvas, get_xy(origin, pixel, (10,11)),pixel, color=tone) # pixel (10, 11)
    make_square(the_canvas, get_xy(origin, pixel, (11,11)),pixel, color=tone) # pixel (11, 11)

    # row 10
    # blank, pixel (0,10)
    make_square(the_canvas, get_xy(origin, pixel, (1,10)),pixel, color=accessories) # pixel (1, 10)
    make_square(the_canvas, get_xy(origin, pixel, (2,10)),pixel, color=tone) # pixel (2, 10)
    make_square(the_canvas, get_xy(origin, pixel, (3,10)),pixel, color=accessories) # pixel (3, 10)
    make_square(the_canvas, get_xy(origin, pixel, (4,10)),pixel, color=tone) # pixel (4, 10)
    make_square(the_canvas, get_xy(origin, pixel, (5,10)),pixel, color=tone) # pixel (5, 10)
    make_square(the_canvas, get_xy(origin, pixel, (6,10)),pixel, color=tone) # pixel (6, 10)
    make_square(the_canvas, get_xy(origin, pixel, (7,10)),pixel, color=tone) # pixel (7, 10)
    make_square(the_canvas, get_xy(origin, pixel, (8,10)),pixel, color=tone) # pixel (8, 10)
    make_square(the_canvas, get_xy(origin, pixel, (9,10)),pixel, color=features) # pixel (9, 10)
    make_square(the_canvas, get_xy(origin, pixel, (10,10)),pixel, color=tone) # pixel (10, 10)
    make_square(the_canvas, get_xy(origin, pixel, (11,10)),pixel, color=tone) # pixel (11, 10)
    make_square(the_canvas, get_xy(origin, pixel, (12,10)),pixel, color=tone) # pixel (12, 10)

    # row 9
    # blank, pixel (0,9)
    make_square(the_canvas, get_xy(origin, pixel, (1,9)),pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (2,9)),pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (3,9)),pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (4,9)),pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (5,9)),pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (6,9)),pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (7,9)),pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (8,9)),pixel, color=features)
    make_square(the_canvas, get_xy(origin, pixel, (9,9)),pixel, color=features)
    make_square(the_canvas, get_xy(origin, pixel, (10,9)),pixel, color=features)
    make_square(the_canvas, get_xy(origin, pixel, (11,9)),pixel, color=features)

    # row 8
    # blank, pixel (0,8)
    # blank, pixel (1,8)
    make_square(the_canvas, get_xy(origin, pixel, (2,8)),pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (3,8)),pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (4,8)),pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (5,8)),pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (6,8)),pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (7,8)),pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (8,8)),pixel, color=overalls)

    # row 7
    # blank, pixel (0,7)
    make_square(the_canvas, get_xy(origin, pixel, (1,7)),pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (2,7)),pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (3,7)),pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (4,7)),pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (5,7)),pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (6,7)),pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (7,7)),pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (8,7)),pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (9,7)),pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (10,7)),pixel, color=clothes)

    # row 6
    make_square(the_canvas, get_xy(origin, pixel, (0,6)),pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (1,6)),pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (2,6)),pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (3,6)),pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (4,6)),pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (5,6)),pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (6,6)),pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (7,6)),pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (8,6)),pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (9,6)),pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (10,6)),pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (11,6)),pixel, color=clothes)

    # row 5
    make_square(the_canvas, get_xy(origin, pixel, (0,5)),pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (1,5)),pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (2,5)),pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (3,5)),pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (4,5)),pixel, color='gold')
    make_square(the_canvas, get_xy(origin, pixel, (5,5)),pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (6,5)),pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (7,5)),pixel, color='gold')
    make_square(the_canvas, get_xy(origin, pixel, (8,5)),pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (9,5)),pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (10,5)),pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (11,5)),pixel, color=tone)

    # row 4
    make_square(the_canvas, get_xy(origin, pixel, (0,4)),pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (1,4)),pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (2,4)),pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (3,4)),pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (4,4)),pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (5,4)),pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (6,4)),pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (7,4)),pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (8,4)),pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (9,4)),pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (10,4)),pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (11,4)),pixel, color=tone)

    # row 3
    make_square(the_canvas, get_xy(origin, pixel, (0,3)),pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (1,3)),pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (2,3)),pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (3,3)),pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (4,3)),pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (5,3)),pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (6,3)),pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (7,3)),pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (8,3)),pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (9,3)),pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (10,3)),pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (11,3)),pixel, color=tone)

    # row 2
    # blank square
    # blank square
    make_square(the_canvas, get_xy(origin, pixel, (2,2)),pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (3,2)),pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (4,2)),pixel, color=overalls)
    # blank square
    # blank square
    make_square(the_canvas, get_xy(origin, pixel, (7,2)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (8,2)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (9,2)), pixel, color=overalls)

    # row 1
    make_square(the_canvas, get_xy(origin, pixel, (1,1)),pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (2,1)),pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (3,1)),pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (4,1)),pixel, color=accessories)
    # blank
    # blank
    make_square(the_canvas, get_xy(origin, pixel, (7,1)),pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (8,1)),pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (9,1)),pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (10,1)),pixel, color=accessories)

    # row 0
    make_square(the_canvas, get_xy(origin, pixel, (0,0)),pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (1,0)),pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (2,0)),pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (3,0)),pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (4,0)),pixel, color=accessories)
    # blank
    # blank
    make_square(the_canvas, get_xy(origin, pixel, (7,0)),pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (8,0)),pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (9,0)),pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (10,0)),pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (11,0)),pixel, color=accessories)

# After you're done making your "make_mario" function, invoke it as follows:

palette = ['blue', 'green', 'yellow', 'pink', 'hot pink', 'brown', 'gray', 'cyan', 'gold', 'red']

def random_color():
    r = lambda: random.randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())

def draw_some_marios():
    the_canvas.delete("all")

    make_grid(the_canvas, 600, 600) # draw the grid

    # The range method is a useful way of generating a sequence of numbers
    for i in range(50):
        make_mario(the_canvas, (random.randint(-50, 600), random.randint(-50, 600)), clothes=random_color(), overalls=random_color(), pixel=random.randint(5, 7))

    # Note, this is called the after method which we'll talk about on Friday
    gui.after(5000,draw_some_marios)


# Note, this is called the after method which we'll talk about on Friday
gui.after(1,draw_some_marios)

########################## YOUR CODE ABOVE THIS LINE ##############################
the_canvas.mainloop()
