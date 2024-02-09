from tkinter import Canvas, Tk
from p1_utilities import *
import time
gui = Tk()
gui.title('Tour of options...')

# initialize canvas:
the_canvas = Canvas(gui, width=1000, height=1000, background='white')
the_canvas.pack()
setup_shapes(the_canvas)
ticks = 0
ticks_per_second = None
########################## YOUR CODE BELOW THIS LINE ##############################

def do_something(event):
    print("You clicked...", '<Button-1>')
    print("And told me to run do_something when I heard that")
    print(event)
    print(event.x, event.y)

def setup():

    ## Setting some listeners!
    # Notice first we define our function called do_something
    # then we tell the canvas to listen for MOUSE_CLICKs and if
    # it hears one, do_something
    setup_listener('<Button-1>', do_something)

    # This is how many animations to attempt per second. If you want to slow down your
    #   animations, just decrease this number! If you want to speed up...
    global ticks_per_second
    ticks_per_second = 30


def go():
    # Here's where you'll put everything you want to control your animations
    #   EXCEPT event listeners (look higher up)
    move("test", x_shift=2, y_shift=-2)


######&&!*#################### YOUR CODE ABOVE THIS LINE ##############################

## DO NOT MODIFY THIS STUFF
setup()
while True:
    go()
    gui.update()
    time.sleep(1 / ticks_per_second)
    ticks = ticks + 1