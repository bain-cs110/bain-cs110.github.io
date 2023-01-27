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
+make_square(the_canvas, (50, 50), 300, color="green")  # face
+make_square(the_canvas, (100, 250), 50, color="purple")  # left eye
+make_square(the_canvas, (250, 250), 50, color="cyan")  # right eye
+make_square(the_canvas, (195, 196), 10, color="white")  # nose
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
