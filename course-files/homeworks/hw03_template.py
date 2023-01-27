'''
Documentation: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas.html
Color Picker: https://coolors.co/
'''
from tkinter import Canvas, Tk
gui = Tk()
gui.title('Shapes')
the_canvas = Canvas(gui, width=500, height=500, background='white',
                    scrollregion="0 -500 500 0")

the_canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

## We've copied make_square from our earlier tutorial to this file so we can use it.
## Note, we've modified it to use a tuple instead of two separate x, y inputs.

def make_square(a_canvas, bottom_left, width, color="blue"):
    a_canvas.create_rectangle(
        bottom_left,
        (bottom_left[0] + width, bottom_left[1] + width),
        fill=color)



# a sample creation

# square face



def make_square_face(a_canvas, center, a_color="green", size=300):
    
    center_x = center[0] # grab the center x coord
    center_y = center[1] # grab the center y coord

    # the face is centered  at the center of my creature
    # with the width of the face being the same
    make_square(a_canvas, (center_x - size / 2, center_y - size/2), size, color="green") # face

    # the left eye is shifted by 50 in the x-direction (1/6 the size of the square)
    # to the left and by 50 i the y-direction (1/6 the size of the square)
    make_square(a_canvas, (center_x - size / 6, center_y + size / 6), size / 6, color="purple") # left eye

    # right eye is the same, but different x coordinate
    make_square(a_canvas, (center_x + size / 6, center_y + size / 6), size / 6, color="cyan") # right eye

    # the nose, is shifted by a much smaller amount. and is 1/30 the size
    make_square(a_canvas, (center_x - size / 60, center_y - size / 60), size / 30, color="white") # nose

make_square_face(the_canvas, (200, 200))
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

make_grid(the_canvas, 500, 500)

the_canvas.scale("all", 0, 0, 1, -1)
the_canvas.mainloop()
