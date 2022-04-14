from tkinter import Canvas, Tk
from helpers import make_square, make_grid

# initialize window
gui = Tk()
canvas = Canvas(gui, width=600, height=600, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

# helper function that draws a grid.
make_grid(canvas, 600, 600)

clothes = 'red'
accessories = 'saddle brown'
tone = 'bisque3'
features = 'black'

# row 0
# blank, pixel (0,0)
# blank, pixel (1,0)
# blank, pixel (2,0)
make_square(canvas, (75,  0), 25, fill_color=clothes) # pixel (3, 0)
make_square(canvas, (100, 0), 25, fill_color=clothes) # pixel (4, 0)
make_square(canvas, (125, 0), 25, fill_color=clothes) # pixel (5, 0)
make_square(canvas, (150, 0), 25, fill_color=clothes) # pixel (6, 0)
make_square(canvas, (175, 0), 25, fill_color=clothes) # pixel (7, 0)
make_square(canvas, (200, 0), 25, fill_color=clothes) # pixel (8, 0)

# row 1
# blank, pixel (0,1)
# blank, pixel (1,1)
make_square(canvas, (50, 25), 25, fill_color=clothes) # pixel (2, 1)
make_square(canvas, (75, 25), 25, fill_color=clothes) # pixel (3, 1)
make_square(canvas, (100,25), 25, fill_color=clothes) # pixel (4, 1)
make_square(canvas, (125,25), 25, fill_color=clothes) # pixel (5, 1)
make_square(canvas, (150,25), 25, fill_color=clothes) # pixel (6, 1)
make_square(canvas, (175,25), 25, fill_color=clothes) # pixel (7, 1)
make_square(canvas, (200,25), 25, fill_color=clothes) # pixel (8, 1)
make_square(canvas, (225,25), 25, fill_color=clothes) # pixel (9, 1)
make_square(canvas, (250,25), 25, fill_color=clothes) # pixel (10, 1)
make_square(canvas, (275,25), 25, fill_color=clothes) # pixel (11, 1)

# row 2
# blank, pixel (0,2)
# blank, pixel (1,2)
make_square(canvas, (50, 50), 25, fill_color=accessories) # pixel (2, 2)
make_square(canvas, (75, 50), 25, fill_color=accessories) # pixel (3, 2)
make_square(canvas, (100,50), 25, fill_color=accessories) # pixel (4, 2)
make_square(canvas, (125,50), 25, fill_color=tone) # pixel (5, 2)
make_square(canvas, (150,50), 25, fill_color=tone) # pixel (6, 2)
make_square(canvas, (175,50), 25, fill_color=tone) # pixel (7, 2)
make_square(canvas, (200,50), 25, fill_color=features) # pixel (8, 2)
make_square(canvas, (225,50), 25, fill_color=tone) # pixel (9, 2)

# row 3
# blank, pixel (0,3)
make_square(canvas, (25,75), 25, fill_color=accessories) # pixel (1, 3)
make_square(canvas, (50,75), 25, fill_color=tone) # pixel (2, 3)
make_square(canvas, (75,75), 25, fill_color=accessories) # pixel (3, 3)
make_square(canvas, (100,75), 25, fill_color=tone) # pixel (4, 3)
make_square(canvas, (125,75), 25, fill_color=tone) # pixel (5, 3)
make_square(canvas, (150,75), 25, fill_color=tone) # pixel (6, 3)
make_square(canvas, (175,75), 25, fill_color=tone) # pixel (7, 3)
make_square(canvas, (200,75), 25, fill_color=features) # pixel (8, 3)
make_square(canvas, (225,75), 25, fill_color=tone) # pixel (9, 3)
make_square(canvas, (250,75), 25, fill_color=tone) # pixel (10, 3)
make_square(canvas, (275,75), 25, fill_color=tone) # pixel (11, 3)

# row 4
# blank, pixel (0,5)
make_square(canvas, (25,100), 25, fill_color=accessories) # pixel (1, 4)
make_square(canvas, (50,100), 25, fill_color=tone) # pixel (2, 4)
make_square(canvas, (75,100), 25, fill_color=accessories) # pixel (3, 4)
make_square(canvas, (100,100), 25, fill_color=tone) # pixel (4, 4)
make_square(canvas, (125,100), 25, fill_color=tone) # pixel (5, 4)
make_square(canvas, (150,100), 25, fill_color=tone) # pixel (6, 4)
make_square(canvas, (175,100), 25, fill_color=tone) # pixel (7, 4)
make_square(canvas, (200,100), 25, fill_color=tone) # pixel (8, 4)
make_square(canvas, (225,100), 25, fill_color=features) # pixel (9, 4)
make_square(canvas, (250,100), 25, fill_color=tone) # pixel (10, 4)
make_square(canvas, (275,100), 25, fill_color=tone) # pixel (11, 4)
make_square(canvas, (300,100), 25, fill_color=tone) # pixel (12, 4)

# row 5
make_square(canvas, (25,125), 25, fill_color=accessories)
make_square(canvas, (50,125), 25, fill_color=accessories)
make_square(canvas, (75,125), 25, fill_color=tone)
make_square(canvas, (100,125), 25, fill_color=tone)
make_square(canvas, (125,125), 25, fill_color=tone)
make_square(canvas, (150,125), 25, fill_color=tone)
make_square(canvas, (175,125), 25, fill_color=tone)
make_square(canvas, (200,125), 25, fill_color=features)
make_square(canvas, (225,125), 25, fill_color=features)
make_square(canvas, (250,125), 25, fill_color=features)
make_square(canvas, (275, 125), 25, fill_color=features)

# row 6
make_square(canvas, (50, 150), 25, fill_color=clothes)
make_square(canvas, (75, 150), 25, fill_color=clothes)
make_square(canvas, (100, 150), 25, fill_color='blue')
make_square(canvas, (125, 150), 25, fill_color=clothes)
make_square(canvas, (150, 150), 25, fill_color=clothes)
make_square(canvas, (175, 150), 25, fill_color=clothes)
make_square(canvas, (200, 150), 25, fill_color='blue')

# row 7
make_square(canvas, (25, 175), 25, fill_color=clothes)
make_square(canvas, (50, 175), 25, fill_color=clothes)
make_square(canvas, (75, 175), 25, fill_color=clothes)
make_square(canvas, (100, 175), 25, fill_color='blue')
make_square(canvas, (125, 175), 25, fill_color=clothes)
make_square(canvas, (150, 175), 25, fill_color=clothes)
make_square(canvas, (175, 175), 25, fill_color='blue')
make_square(canvas, (200, 175), 25, fill_color=clothes)
make_square(canvas, (225, 175), 25, fill_color=clothes)
make_square(canvas, (250, 175), 25, fill_color=clothes)

# row 8
make_square(canvas, (0, 200), 25, fill_color=clothes)
make_square(canvas, (25, 200), 25, fill_color=clothes)
make_square(canvas, (50, 200), 25, fill_color=clothes)
make_square(canvas, (75, 200), 25, fill_color=clothes)
make_square(canvas, (100, 200), 25, fill_color='blue')
make_square(canvas, (125, 200), 25, fill_color='blue')
make_square(canvas, (150, 200), 25, fill_color='blue')
make_square(canvas, (175, 200), 25, fill_color='blue')
make_square(canvas, (200, 200), 25, fill_color=clothes)
make_square(canvas, (225, 200), 25, fill_color=clothes)
make_square(canvas, (250, 200), 25, fill_color=clothes)
make_square(canvas, (275, 200), 25, fill_color=clothes)

# row 9
make_square(canvas, (0, 225), 25, fill_color=tone)
make_square(canvas, (25, 225), 25, fill_color=tone)
make_square(canvas, (50, 225), 25, fill_color=clothes)
make_square(canvas, (75, 225), 25, fill_color='blue')
make_square(canvas, (100, 225), 25, fill_color='gold')
make_square(canvas, (125, 225), 25, fill_color='blue')
make_square(canvas, (150, 225), 25, fill_color='blue')
make_square(canvas, (175, 225), 25, fill_color='gold')
make_square(canvas, (200, 225), 25, fill_color='blue')
make_square(canvas, (225, 225), 25, fill_color=clothes)
make_square(canvas, (250, 225), 25, fill_color=tone)
make_square(canvas, (275, 225), 25, fill_color=tone)

# row 10
make_square(canvas, (0, 250), 25, fill_color=tone)
make_square(canvas, (25, 250), 25, fill_color=tone)
make_square(canvas, (50, 250), 25, fill_color=tone)
make_square(canvas, (75, 250), 25, fill_color='blue')
make_square(canvas, (100, 250), 25, fill_color='blue')
make_square(canvas, (125, 250), 25, fill_color='blue')
make_square(canvas, (150, 250), 25, fill_color='blue')
make_square(canvas, (175, 250), 25, fill_color='blue')
make_square(canvas, (200, 250), 25, fill_color='blue')
make_square(canvas, (225, 250), 25, fill_color=tone)
make_square(canvas, (250, 250), 25, fill_color=tone)
make_square(canvas, (275, 250), 25, fill_color=tone)

# row 11
make_square(canvas, (0, 275), 25, fill_color=tone)
make_square(canvas, (25, 275), 25, fill_color=tone)
make_square(canvas, (50, 275), 25, fill_color='blue')
make_square(canvas, (75, 275), 25, fill_color='blue')
make_square(canvas, (100, 275), 25, fill_color='blue')
make_square(canvas, (125, 275), 25, fill_color='blue')
make_square(canvas, (150, 275), 25, fill_color='blue')
make_square(canvas, (175, 275), 25, fill_color='blue')
make_square(canvas, (200, 275), 25, fill_color='blue')
make_square(canvas, (225, 275), 25, fill_color='blue')
make_square(canvas, (250, 275), 25, fill_color=tone)
make_square(canvas, (275, 275), 25, fill_color=tone)

# row 12
make_square(canvas, (50, 300), 25, fill_color='blue')
make_square(canvas, (75, 300), 25, fill_color='blue')
make_square(canvas, (100, 300), 25, fill_color='blue')
# blank square
# blank square
make_square(canvas, (175, 300), 25, fill_color='blue')
make_square(canvas, (200, 300), 25, fill_color='blue')
make_square(canvas, (225, 300), 25, fill_color='blue')

# row 13
make_square(canvas, (25, 325), 25, fill_color=accessories)
make_square(canvas, (50, 325), 25, fill_color=accessories)
make_square(canvas, (75, 325), 25, fill_color=accessories)
make_square(canvas, (100, 325), 25, fill_color=accessories)
# blank
# blank
make_square(canvas, (175, 325), 25, fill_color=accessories)
make_square(canvas, (200, 325), 25, fill_color=accessories)
make_square(canvas, (225, 325), 25, fill_color=accessories)
make_square(canvas, (250, 325), 25, fill_color=accessories)

# row 14
make_square(canvas, (0, 350), 25, fill_color=accessories)
make_square(canvas, (25, 350), 25, fill_color=accessories)
make_square(canvas, (50, 350), 25, fill_color=accessories)
make_square(canvas, (75, 350), 25, fill_color=accessories)
make_square(canvas, (100, 350), 25, fill_color=accessories)
# blank
# blank
make_square(canvas, (175, 350), 25, fill_color=accessories)
make_square(canvas, (200, 350), 25, fill_color=accessories)
make_square(canvas, (225, 350), 25, fill_color=accessories)
make_square(canvas, (250, 350), 25, fill_color=accessories)
make_square(canvas, (275, 350), 25, fill_color=accessories)


'''
# After you're done making your "make_mario" function, invoke it as follows:
make_mario(canvas, (0, 20))
make_mario(canvas, (420, 250), clothes='#E0607E', pixel=10)
make_mario(canvas, (55, 415), clothes='green', pixel=15)
make_mario(canvas, (350, 115), pixel=5, clothes='#75B9BE')
make_mario(canvas, (420, 400), clothes='#E5F77D', overalls='#75B9BE', pixel=15)
make_mario(canvas, (420, 10), pixel=15)
'''

########################## YOUR CODE ABOVE THIS LINE ##############################
canvas.mainloop()
