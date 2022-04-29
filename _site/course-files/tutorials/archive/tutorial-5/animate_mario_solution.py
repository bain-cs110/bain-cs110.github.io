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

# Ask python to start a counter
counter = 0

# Pick a pixel size
pixel_size = 15

# Infinitely loop
while True:

    # Delete the existing Mario on the screen
    canvas.delete("mario")
    canvas.delete("mario_2")

    # Each step, we draw a different mario in a cycle of 1, 2, 3
    if counter % 3 == 0:
        draw_pixel_art(canvas, (counter * pixel_size, 0), mario_0, marios_colors, tag="mario", pixel=pixel_size)
        draw_pixel_art(canvas, (counter * pixel_size - 100, 300), mario_0, marios_colors, tag="mario_2", pixel=pixel_size)

    elif counter % 3 == 1:
        draw_pixel_art(canvas, (counter * pixel_size, 0), mario_1, marios_colors, tag="mario", pixel=pixel_size)
        draw_pixel_art(canvas, (counter * pixel_size - 100, 300), mario_1, marios_colors, tag="mario_2", pixel=pixel_size)

    else:
        draw_pixel_art(canvas, (counter * pixel_size, 0), mario_2, marios_colors, tag="mario", pixel=pixel_size)
        draw_pixel_art(canvas, (counter * pixel_size - 100, 300), mario_2, marios_colors, tag="mario_2", pixel=pixel_size)


    # Ask Python to add one to the counter
    counter += 1

    # Ask TKinter to update our drawing
    gui.update()

    # Pause for a moment
    time.sleep(0.25)

########################## YOUR CODE ABOVE THIS LINE ##############################
canvas.mainloop()
