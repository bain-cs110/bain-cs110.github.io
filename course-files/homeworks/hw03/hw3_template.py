from tkinter import Canvas, Tk
from hw3_shapes import *

gui = Tk()
gui.title("Homework 3")
the_canvas = Canvas(gui, width=900, height=900, background="white")
setup_shapes(the_canvas)
the_canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################









########################## YOUR CODE ABOVE THIS LINE ##############################
# helper function that draws a grid.
make_grid(900, 900)  # draw the grid
the_canvas.mainloop()
