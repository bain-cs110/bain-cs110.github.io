from tkinter import Canvas, Tk
from tutorial2_shapes import *

gui = Tk()
the_canvas = Canvas(gui, width=900, height=900, background="white")
setup_shapes(the_canvas)
the_canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################
clothes = "red"
accessories = "saddle brown"
tone = "bisque3"
features = "black"
buttons = "gold"

# row 0
# blank, pixel (0,0)
# blank, pixel (1,0)
# blank, pixel (2,0)
square(top_left=(75, 0), size=25, color=clothes)  # pixel (3, 0)
square(top_left=(100, 0), size=25, color=clothes)  # pixel (4, 0)
square(top_left=(125, 0), size=25, color=clothes)  # pixel (5, 0)
square(top_left=(150, 0), size=25, color=clothes)  # pixel (6, 0)
square(top_left=(175, 0), size=25, color=clothes)  # pixel (7, 0)
square(top_left=(200, 0), size=25, color=clothes)  # pixel (8, 0)

# row 1
# blank, pixel (0,1)
# blank, pixel (1,1)
square(top_left=(50, 25), size=25, color=clothes)  # pixel (2, 1)
square(top_left=(75, 25), size=25, color=clothes)  # pixel (3, 1)
square(top_left=(100, 25), size=25, color=clothes)  # pixel (4, 1)
square(top_left=(125, 25), size=25, color=clothes)  # pixel (5, 1)
square(top_left=(150, 25), size=25, color=clothes)  # pixel (6, 1)
square(top_left=(175, 25), size=25, color=clothes)  # pixel (7, 1)
square(top_left=(200, 25), size=25, color=clothes)  # pixel (8, 1)
square(top_left=(225, 25), size=25, color=clothes)  # pixel (9, 1)
square(top_left=(250, 25), size=25, color=clothes)  # pixel (10, 1)
square(top_left=(275, 25), size=25, color=clothes)  # pixel (11, 1)

# row 2
# blank, pixel (0,2)
# blank, pixel (1,2)
square(top_left=(50, 50), size=25, color=accessories)  # pixel (2, 2)
square(top_left=(75, 50), size=25, color=accessories)  # pixel (3, 2)
square(top_left=(100, 50), size=25, color=accessories)  # pixel (4, 2)
square(top_left=(125, 50), size=25, color=tone)  # pixel (5, 2)
square(top_left=(150, 50), size=25, color=tone)  # pixel (6, 2)
square(top_left=(175, 50), size=25, color=tone)  # pixel (7, 2)
square(top_left=(200, 50), size=25, color=features)  # pixel (8, 2)
square(top_left=(225, 50), size=25, color=tone)  # pixel (9, 2)

# row 3
# blank, pixel (0,3)
square(top_left=(25, 75), size=25, color=accessories)  # pixel (1, 3)
square(top_left=(50, 75), size=25, color=tone)  # pixel (2,3)
square(top_left=(75, 75), size=25, color=accessories)  # pixel (3, 3)
square(top_left=(100, 75), size=25, color=tone)  # pixel (4, 3)
square(top_left=(125, 75), size=25, color=tone)  # pixel (5, 3)
square(top_left=(150, 75), size=25, color=tone)  # pixel (6, 3)
square(top_left=(175, 75), size=25, color=tone)  # pixel (7, 3)
square(top_left=(200, 75), size=25, color=features)  # pixel (8, 3)
square(top_left=(225, 75), size=25, color=tone)  # pixel (9, 3)
square(top_left=(250, 75), size=25, color=tone)  # pixel (10, 3)
square(top_left=(275, 75), size=25, color=tone)  # pixel (11, 3)

# row 4
# blank, pixel (0,4)
square(top_left=(25, 100), size=25, color=accessories)  # pixel (1, 4)
square(top_left=(50, 100), size=25, color=tone)  # pixel (2, 4)
square(top_left=(75, 100), size=25, color=accessories)  # pixel (3, 4)
square(top_left=(100, 100), size=25, color=tone)  # pixel (4, 4)
square(top_left=(125, 100), size=25, color=tone)  # pixel (5, 4)
square(top_left=(150, 100), size=25, color=tone)  # pixel (6, 4)
square(top_left=(175, 100), size=25, color=tone)  # pixel (7, 4)
square(top_left=(200, 100), size=25, color=tone)  # pixel (8, 4)
square(top_left=(225, 100), size=25, color=features)  # pixel (9, 4)
square(top_left=(250, 100), size=25, color=tone)  # pixel (10, 4)
square(top_left=(275, 100), size=25, color=tone)  # pixel (11, 4)
square(top_left=(300, 100), size=25, color=tone)  # pixel (12, 4)

# row 5
# blank, pixel (0,5)
square(top_left=(25, 125), size=25, color=accessories)
square(top_left=(50, 125), size=25, color=accessories)
square(top_left=(75, 125), size=25, color=tone)
square(top_left=(100, 125), size=25, color=tone)
square(top_left=(125, 125), size=25, color=tone)
square(top_left=(150, 125), size=25, color=tone)
square(top_left=(175, 125), size=25, color=tone)
square(top_left=(200, 125), size=25, color=features)
square(top_left=(225, 125), size=25, color=features)
square(top_left=(250, 125), size=25, color=features)
square(top_left=(275, 125), size=25, color=features)

# row 6
# blank, pixel (0,6)
# blank, pixel (1,6)
square(top_left=(50, 150), size=25, color=clothes)
square(top_left=(75, 150), size=25, color=clothes)
square(top_left=(100, 150), size=25, color="blue")
square(top_left=(125, 150), size=25, color=clothes)
square(top_left=(150, 150), size=25, color=clothes)
square(top_left=(175, 150), size=25, color=clothes)
square(top_left=(200, 150), size=25, color="blue")

# row 7
# blank, pixel (0,7)
square(top_left=(25, 175), size=25, color=clothes)
square(top_left=(50, 175), size=25, color=clothes)
square(top_left=(75, 175), size=25, color=clothes)
square(top_left=(100, 175), size=25, color="blue")
square(top_left=(125, 175), size=25, color=clothes)
square(top_left=(150, 175), size=25, color=clothes)
square(top_left=(175, 175), size=25, color="blue")
square(top_left=(200, 175), size=25, color=clothes)
square(top_left=(225, 175), size=25, color=clothes)
square(top_left=(250, 175), size=25, color=clothes)

# row 8
square(top_left=(0, 200), size=25, color=clothes)
square(top_left=(25, 200), size=25, color=clothes)
square(top_left=(50, 200), size=25, color=clothes)
square(top_left=(75, 200), size=25, color=clothes)
square(top_left=(100, 200), size=25, color="blue")
square(top_left=(125, 200), size=25, color="blue")
square(top_left=(150, 200), size=25, color="blue")
square(top_left=(175, 200), size=25, color="blue")
square(top_left=(200, 200), size=25, color=clothes)
square(top_left=(225, 200), size=25, color=clothes)
square(top_left=(250, 200), size=25, color=clothes)
square(top_left=(275, 200), size=25, color=clothes)

# row 9
square(top_left=(0, 225), size=25, color=tone)
square(top_left=(25, 225), size=25, color=tone)
square(top_left=(50, 225), size=25, color=clothes)
square(top_left=(75, 225), size=25, color="blue")
square(top_left=(100, 225), size=25, color=buttons)
square(top_left=(125, 225), size=25, color="blue")
square(top_left=(150, 225), size=25, color="blue")
square(top_left=(175, 225), size=25, color=buttons)
square(top_left=(200, 225), size=25, color="blue")
square(top_left=(225, 225), size=25, color=clothes)
square(top_left=(250, 225), size=25, color=tone)
square(top_left=(275, 225), size=25, color=tone)

# row 10
square(top_left=(0, 250), size=25, color=tone)
square(top_left=(25, 250), size=25, color=tone)
square(top_left=(50, 250), size=25, color=tone)
square(top_left=(75, 250), size=25, color="blue")
square(top_left=(100, 250), size=25, color="blue")
square(top_left=(125, 250), size=25, color="blue")
square(top_left=(150, 250), size=25, color="blue")
square(top_left=(175, 250), size=25, color="blue")
square(top_left=(200, 250), size=25, color="blue")
square(top_left=(225, 250), size=25, color=tone)
square(top_left=(250, 250), size=25, color=tone)
square(top_left=(275, 250), size=25, color=tone)

# row 11
square(top_left=(0, 275), size=25, color=tone)
square(top_left=(25, 275), size=25, color=tone)
square(top_left=(50, 275), size=25, color="blue")
square(top_left=(75, 275), size=25, color="blue")
square(top_left=(100, 275), size=25, color="blue")
square(top_left=(125, 275), size=25, color="blue")
square(top_left=(150, 275), size=25, color="blue")
square(top_left=(175, 275), size=25, color="blue")
square(top_left=(200, 275), size=25, color="blue")
square(top_left=(225, 275), size=25, color="blue")
square(top_left=(250, 275), size=25, color=tone)
square(top_left=(275, 275), size=25, color=tone)

# row 12
# blank, pixel (0,12)
# blank, pixel (1,12)
square(top_left=(50, 300), size=25, color="blue")
square(top_left=(75, 300), size=25, color="blue")
square(top_left=(100, 300), size=25, color="blue")
# blank square
# blank square
square(top_left=(175, 300), size=25, color="blue")
square(top_left=(200, 300), size=25, color="blue")
square(top_left=(225, 300), size=25, color="blue")

# row 13
# blank, pixel (0,13)
square(top_left=(25, 325), size=25, color=accessories)
square(top_left=(50, 325), size=25, color=accessories)
square(top_left=(75, 325), size=25, color=accessories)
square(top_left=(100, 325), size=25, color=accessories)
# blank
# blank
square(top_left=(175, 325), size=25, color=accessories)
square(top_left=(200, 325), size=25, color=accessories)
square(top_left=(225, 325), size=25, color=accessories)
square(top_left=(250, 325), size=25, color=accessories)

# row 14
square(top_left=(0, 350), size=25, color=accessories)
square(top_left=(25, 350), size=25, color=accessories)
square(top_left=(50, 350), size=25, color=accessories)
square(top_left=(75, 350), size=25, color=accessories)
square(top_left=(100, 350), size=25, color=accessories)
# blank
# blank
square(top_left=(175, 350), size=25, color=accessories)
square(top_left=(200, 350), size=25, color=accessories)
square(top_left=(225, 350), size=25, color=accessories)
square(top_left=(250, 350), size=25, color=accessories)
square(top_left=(275, 350), size=25, color=accessories)


########################## YOUR CODE ABOVE THIS LINE ##############################
make_grid(900, 900)  # draw the grid
the_canvas.mainloop()
