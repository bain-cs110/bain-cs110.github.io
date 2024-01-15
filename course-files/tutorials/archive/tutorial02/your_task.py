from tkinter import Canvas, Tk

# initialize window
gui = Tk()
the_canvas = Canvas(gui, width=600, height=600, background='white',
                    scrollregion="0 -600 600 0")
the_canvas.pack()

def make_square(a_canvas, bottom_left, width, color="white"):
    a_canvas.create_rectangle(
        bottom_left,
        (bottom_left[0] + width, bottom_left[1] + width),
        fill=color)

########################## YOUR CODE BELOW THIS LINE ##############################
clothes = "red"
accessories = "saddle brown"
tone = "bisque3"
features = "black"

# row 14
# blank, pixel (0,14)
# blank, pixel (1,14)
# blank, pixel (2,14)
make_square(the_canvas, (75,  350), 25, color=clothes)  # pixel (3, 14)
make_square(the_canvas, (100, 350), 25, color=clothes)  # pixel (4, 14)
make_square(the_canvas, (125, 350), 25, color=clothes)  # pixel (5, 14)
make_square(the_canvas, (150, 350), 25, color=clothes)  # pixel (6, 14)
make_square(the_canvas, (175, 350), 25, color=clothes)  # pixel (7, 14)
make_square(the_canvas, (200, 350), 25, color=clothes)  # pixel (8, 14)

# row 13
# blank, pixel (0,13)
# blank, pixel (1,13)
make_square(the_canvas, (50, 325), 25, color=clothes)  # pixel (2, 13)
make_square(the_canvas, (75, 325), 25, color=clothes)  # pixel (3, 13)
make_square(the_canvas, (100,325), 25, color=clothes) # pixel (4, 13)
make_square(the_canvas, (125,325), 25, color=clothes) # pixel (5, 13)
make_square(the_canvas, (150,325), 25, color=clothes) # pixel (6, 13)
make_square(the_canvas, (175,325), 25, color=clothes) # pixel (7, 13)
make_square(the_canvas, (200,325), 25, color=clothes) # pixel (8, 13)
make_square(the_canvas, (225,325), 25, color=clothes) # pixel (9, 13)
make_square(the_canvas, (250,325), 25, color=clothes) # pixel (10, 13)
make_square(the_canvas, (275,325), 25, color=clothes) # pixel (11, 13)

# row 12
# blank, pixel (0,12)
# blank, pixel (1,12)
make_square(the_canvas, (50, 300), 25, color=accessories) # pixel (2, 12)
make_square(the_canvas, (75, 300), 25, color=accessories) # pixel (3, 12)
make_square(the_canvas, (100,300), 25, color=accessories) # pixel (4, 12)
make_square(the_canvas, (125,300), 25, color=tone) # pixel (5, 12)
make_square(the_canvas, (150,300), 25, color=tone) # pixel (6, 12)
make_square(the_canvas, (175,300), 25, color=tone) # pixel (7, 12)
make_square(the_canvas, (200,300), 25, color=features) # pixel (8, 12)
make_square(the_canvas, (225,300), 25, color=tone) # pixel (9, 12)

# row 11
# blank, pixel (0,11)
make_square(the_canvas, (25,275), 25, color=accessories) # pixel (1, 11)
make_square(the_canvas, (50,275), 25, color=tone) # pixel (2,11)
make_square(the_canvas, (75,275), 25, color=accessories) # pixel (3, 11)
make_square(the_canvas, (100,275), 25, color=tone) # pixel (4, 11)
make_square(the_canvas, (125,275), 25, color=tone) # pixel (5, 11)
make_square(the_canvas, (150,275), 25, color=tone) # pixel (6, 11)
make_square(the_canvas, (175,275), 25, color=tone) # pixel (7, 11)
make_square(the_canvas, (200,275), 25, color=features) # pixel (8, 11)
make_square(the_canvas, (225,275), 25, color=tone) # pixel (9, 11)
make_square(the_canvas, (250,275), 25, color=tone) # pixel (10, 11)
make_square(the_canvas, (275,275), 25, color=tone) # pixel (11, 11)

# row 10
# blank, pixel (0,10)
make_square(the_canvas, (25,250), 25, color=accessories) # pixel (1, 10)
make_square(the_canvas, (50,250), 25, color=tone) # pixel (2, 10)
make_square(the_canvas, (75,250), 25, color=accessories) # pixel (3, 10)
make_square(the_canvas, (100,250), 25, color=tone) # pixel (4, 10)
make_square(the_canvas, (125,250), 25, color=tone) # pixel (5, 10)
make_square(the_canvas, (150,250), 25, color=tone) # pixel (6, 10)
make_square(the_canvas, (175,250), 25, color=tone) # pixel (7, 10)
make_square(the_canvas, (200,250), 25, color=tone) # pixel (8, 10)
make_square(the_canvas, (225,250), 25, color=features) # pixel (9, 10)
make_square(the_canvas, (250,250), 25, color=tone) # pixel (10, 10)
make_square(the_canvas, (275,250), 25, color=tone) # pixel (11, 10)
make_square(the_canvas, (300,250), 25, color=tone) # pixel (12, 10)

# row 9
# blank, pixel (0,9)
make_square(the_canvas, (25, 225), 25, color=accessories)
make_square(the_canvas, (50, 225), 25, color=accessories)
make_square(the_canvas, (75, 225), 25, color=tone)
make_square(the_canvas, (100, 225), 25, color=tone)
make_square(the_canvas, (125, 225), 25, color=tone)
make_square(the_canvas, (150, 225), 25, color=tone)
make_square(the_canvas, (175, 225), 25, color=tone)
make_square(the_canvas, (200, 225), 25, color=features)
make_square(the_canvas, (225, 225), 25, color=features)
make_square(the_canvas, (250, 225), 25, color=features)
make_square(the_canvas, (275, 225), 25, color=features)

# row 8
# blank, pixel (0,8)
# blank, pixel (1,8)
make_square(the_canvas, (50, 200), 25, color=clothes)
make_square(the_canvas, (75, 200), 25, color=clothes)
make_square(the_canvas, (100, 200), 25, color="blue")
make_square(the_canvas, (125, 200), 25, color=clothes)
make_square(the_canvas, (150, 200), 25, color=clothes)
make_square(the_canvas, (175, 200), 25, color=clothes)
make_square(the_canvas, (200, 200), 25, color="blue")

# row 7
# blank, pixel (0,7)
make_square(the_canvas, (25, 175), 25, color=clothes)
make_square(the_canvas, (50, 175), 25, color=clothes)
make_square(the_canvas, (75, 175), 25, color=clothes)
make_square(the_canvas, (100, 175), 25, color="blue")
make_square(the_canvas, (125, 175), 25, color=clothes)
make_square(the_canvas, (150, 175), 25, color=clothes)
make_square(the_canvas, (175, 175), 25, color="blue")
make_square(the_canvas, (200, 175), 25, color=clothes)
make_square(the_canvas, (225, 175), 25, color=clothes)
make_square(the_canvas, (250, 175), 25, color=clothes)

# row 6
make_square(the_canvas, (0, 150), 25, color=clothes)
make_square(the_canvas, (25, 150), 25, color=clothes)
make_square(the_canvas, (50, 150), 25, color=clothes)
make_square(the_canvas, (75, 150), 25, color=clothes)
make_square(the_canvas, (100, 150), 25, color="blue")
make_square(the_canvas, (125, 150), 25, color="blue")
make_square(the_canvas, (150, 150), 25, color="blue")
make_square(the_canvas, (175, 150), 25, color="blue")
make_square(the_canvas, (200, 150), 25, color=clothes)
make_square(the_canvas, (225, 150), 25, color=clothes)
make_square(the_canvas, (250, 150), 25, color=clothes)
make_square(the_canvas, (275, 150), 25, color=clothes)

# row 5
make_square(the_canvas, (0, 125), 25, color=tone)
make_square(the_canvas, (25, 125), 25, color=tone)
make_square(the_canvas, (50, 125), 25, color=clothes)
make_square(the_canvas, (75, 125), 25, color="blue")
make_square(the_canvas, (100, 125), 25, color='gold')
make_square(the_canvas, (125, 125), 25, color="blue")
make_square(the_canvas, (150, 125), 25, color="blue")
make_square(the_canvas, (175, 125), 25, color='gold')
make_square(the_canvas, (200, 125), 25, color="blue")
make_square(the_canvas, (225, 125), 25, color=clothes)
make_square(the_canvas, (250, 125), 25, color=tone)
make_square(the_canvas, (275, 125), 25, color=tone)

# row 4
make_square(the_canvas, (0, 100), 25, color=tone)
make_square(the_canvas, (25, 100), 25, color=tone)
make_square(the_canvas, (50, 100), 25, color=tone)
make_square(the_canvas, (75, 100), 25, color="blue")
make_square(the_canvas, (100, 100), 25, color="blue")
make_square(the_canvas, (125, 100), 25, color="blue")
make_square(the_canvas, (150, 100), 25, color="blue")
make_square(the_canvas, (175, 100), 25, color="blue")
make_square(the_canvas, (200, 100), 25, color="blue")
make_square(the_canvas, (225, 100), 25, color=tone)
make_square(the_canvas, (250, 100), 25, color=tone)
make_square(the_canvas, (275, 100), 25, color=tone)

# row 3
make_square(the_canvas, (0, 75), 25, color=tone)
make_square(the_canvas, (25, 75), 25, color=tone)
make_square(the_canvas, (50, 75), 25, color="blue")
make_square(the_canvas, (75, 75), 25, color="blue")
make_square(the_canvas, (100, 75), 25, color="blue")
make_square(the_canvas, (125, 75), 25, color="blue")
make_square(the_canvas, (150, 75), 25, color="blue")
make_square(the_canvas, (175, 75), 25, color="blue")
make_square(the_canvas, (200, 75), 25, color="blue")
make_square(the_canvas, (225, 75), 25, color="blue")
make_square(the_canvas, (250, 75), 25, color=tone)
make_square(the_canvas, (275, 75), 25, color=tone)

# row 2
# blank, pixel (0,2)
# blank, pixel (1,2)
make_square(the_canvas, (50, 50), 25, color="blue")
make_square(the_canvas, (75, 50), 25, color="blue")
make_square(the_canvas, (100, 50), 25, color="blue")
# blank square
# blank square
make_square(the_canvas, (175, 50), 25, color="blue")
make_square(the_canvas, (200, 50), 25, color="blue")
make_square(the_canvas, (225, 50), 25, color="blue")

# row 1
# blank, pixel (0,1)
make_square(the_canvas, (25, 25), 25, color=accessories)
make_square(the_canvas, (50, 25), 25, color=accessories)
make_square(the_canvas, (75, 25), 25, color=accessories)
make_square(the_canvas, (100, 25), 25, color=accessories)
# blank
# blank
make_square(the_canvas, (175, 25), 25, color=accessories)
make_square(the_canvas, (200, 25), 25, color=accessories)
make_square(the_canvas, (225, 25), 25, color=accessories)
make_square(the_canvas, (250, 25), 25, color=accessories)

# row 0
make_square(the_canvas, (0, 0), 25, color=accessories)
make_square(the_canvas, (25, 0), 25, color=accessories)
make_square(the_canvas, (50, 0), 25, color=accessories)
make_square(the_canvas, (75, 0), 25, color=accessories)
make_square(the_canvas, (100, 0), 25, color=accessories)
# blank
# blank
make_square(the_canvas, (175, 0), 25, color=accessories)
make_square(the_canvas, (200, 0), 25, color=accessories)
make_square(the_canvas, (225, 0), 25, color=accessories)
make_square(the_canvas, (250, 0), 25, color=accessories)
make_square(the_canvas, (275, 0), 25, color=accessories)

'''
# After you're done making your "make_mario" function, invoke it as follows:
make_mario(the_canvas, (0, 20))
make_mario(the_canvas, (420, 250), clothes='#E0607E', pixel=10)
make_mario(the_canvas, (55, 415), clothes='green', pixel=15)
make_mario(the_canvas, (350, 115), pixel=5, clothes='#75B9BE')
make_mario(the_canvas, (420, 400), clothes='#E5F77D', overalls='#75B9BE', pixel=15)
make_mario(the_canvas, (420, 10), pixel=15)
'''

########################## YOUR CODE ABOVE THIS LINE ##############################


# helper function that draws a grid.


def make_grid(c, w, h):
    interval = 100
    # Creates all vertical lines at intevals of 100
    for i in range(0, w, interval):
        c.create_line(i, 0, i, h, tag='grid_line')
    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, interval):
        c.create_line(0, i, w, i, tag='grid_line')
    # Creates axis labels
    offset = 2
    for y in range(0, h, interval):
        for x in range(0, w, interval):
            c.create_oval(
                x - offset,
                y - offset,
                x + offset,
                y + offset,
                fill='black'
            )
            c.create_text(
                x + offset,
                y + offset,
                text="({0}, {1})".format(x, y),
                anchor="nw",
                font=("Purisa", 8)
            )


make_grid(the_canvas, 600, 600)  # draw the grid

the_canvas.scale("all", 0, 0, 1, -1)
the_canvas.mainloop()
