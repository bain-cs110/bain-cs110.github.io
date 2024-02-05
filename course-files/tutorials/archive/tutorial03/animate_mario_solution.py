from tkinter import Canvas, Tk
from tutorial4_utilities import *
import time

# initialize window
gui = Tk()
the_canvas = Canvas(gui, width=600, height=600, background='white')
setup_shapes(the_canvas)
the_canvas.pack()
ticks_per_second = None
ticks = 0
########################## YOUR CODE BELOW THIS LINE ##############################

mario_colors = [None, "red", "blue", "saddle brown", "bisque3", "black", "gold"]
mario_colors_alt = [None, "cyan", "olive drab", "saddle brown", "bisque3", "black", "purple4"]

def setup():
    # helper function that draws a grid.
    make_grid(600, 600)

    # 3 Different Mario Drawings:
    #    mario_0
    #    mario_1
    #    mario_2
    # They are imported from tutorial4_utilities above so you can use them like regular variables
    pixel_art((0, 0), mario_0, mario_colors, tag="mario_1", pixel=10)

    pixel_art((575, 300), mario_0, mario_colors_alt, tag="mario_2", pixel=20)
    mirror("mario_2")

    # This is how many animations to attempt per second. If you want to slow down your
    #   animations, just decrease this number! If you want to speed up...
    global ticks_per_second
    ticks_per_second = 20


def go():

    delete("mario_1")
    delete("mario_2")

    if ticks % 3 == 0:
        style = mario_0
    elif ticks % 3 == 1:
        style = mario_1
    else:
        style = mario_2

    pixel_art((0 + 5 * ticks, 0), style, mario_colors, tag="mario_1", pixel=10)

    pixel_art((575 - 10 * ticks, 300), style, mario_colors_alt, tag="mario_2", pixel=20)
    mirror("mario_2")


########################## YOUR CODE ABOVE THIS LINE ##############################
## DO NOT MODIFY THIS STUFF
setup()
while True:
    go()
    gui.update()
    time.sleep(1 / ticks_per_second)
    ticks = ticks + 1

# makes sure the canvas keeps running:
the_canvas.mainloop()