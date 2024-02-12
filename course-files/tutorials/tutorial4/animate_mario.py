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

def setup():
    print("Setup time!")
    # helper function that draws a grid.
    make_grid(600, 600)

    # 3 Different Mario Drawings:
    #    mario_0
    #    mario_1
    #    mario_2
    # They are imported from tutorial4_utilities above so you can use them like regular variables
    pixel_art((150, 0), mario_0, mario_colors, tag="mario", pixel=10)

    # This is how many animations to attempt per second. If you want to slow down your
    #   animations, just decrease this number! If you want to speed up...
    global ticks_per_second
    ticks_per_second = 1


def go():
    print("Go time!")


########################## YOUR CODE ABOVE THIS LINE ##############################
## DO NOT MODIFY THIS STUFF
setup()
while True:
    go()
    gui.update()
    time.sleep(1 / ticks_per_second)
    ticks = ticks + 1