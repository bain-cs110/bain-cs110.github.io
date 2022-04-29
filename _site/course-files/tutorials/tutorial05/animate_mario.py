from tkinter import Canvas, Tk
from helpers import draw_pixel_art, make_grid, mario_0, mario_1, mario_2
import time

# initialize window
gui = Tk()
canvas = Canvas(gui, width=600, height=600, background='white')
canvas.pack()

# helper function that draws a grid.
make_grid(canvas, 600, 600)

########################## YOUR CODE BELOW THIS LINE ##############################
marios_colors = [None, "red", "blue", "saddle brown", "bisque3", "black", "gold"]

# 3 Different Mario Drawings:
#    mario_0
#    mario_1
#    mario_2
# They are imported from helpers.py above so you can use them like regular variables

draw_pixel_art(canvas, (150, 0), mario_0, marios_colors, tag="mario", pixel=15)

########################## YOUR CODE ABOVE THIS LINE ##############################
canvas.mainloop()
