import time
from cs110_t4 import *
_ignore = setup_shapes('Lecture 15', background="white", grid=True, width=600, height=600)
ticks_per_second = None
ticks = 0
########################## YOUR CODE BELOW THIS LINE ##############################

def setup():
    # helper function that draws a grid.

    square(top_left = (0, 450), size=50, color="yellow", tag="test_square")

    # This is how many animations to attempt per second. If you want to slow down your
    #   animations, just decrease this number! If you want to speed up...
    global ticks_per_second
    ticks_per_second = 20


def go():
    delete("test_square")
    square(top_left=(0 + ticks * 5, 450), color="green", tag="test_square")


########################## YOUR CODE ABOVE THIS LINE ##############################
## DO NOT MODIFY THIS STUFF
setup()
while True:
    go()
    _ignore.update()
    time.sleep(1 / ticks_per_second)
    ticks = ticks + 1
# makes sure the window keeps running:
_ignore.mainloop()