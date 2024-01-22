from tkinter import Canvas, Tk
from tutorial2_shapes import *

gui = Tk()
the_canvas = Canvas(gui, width=900, height=900, background="white")
setup_shapes(the_canvas)
the_canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################



########################## YOUR CODE ABOVE THIS LINE ##############################

make_grid(900, 900)  # draw the grid
the_canvas.mainloop()
