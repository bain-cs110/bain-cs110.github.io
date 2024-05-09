from p1_utilities import *
import time

_ignore = setup_shapes('Lecture 19', background="white", grid=False, width=800, height=800)
ticks = 0
ticks_per_second = None
########################## YOUR CODE BELOW THIS LINE ##############################


def setup():
    #text((500, 500), text='Click or drag to create circles', font=("Purisa", 32))

    # This is how many animations to attempt per second. If you want to slow down your
    #   animations, just decrease this number! If you want to speed up...
    global ticks_per_second
    ticks_per_second = 60


def go():
    pass


######&&!*#################### YOUR CODE ABOVE THIS LINE ##############################
## DO NOT MODIFY THIS STUFF
setup()
while True:
    go()
    _ignore.update()
    time.sleep(1 / ticks_per_second)
    ticks = ticks + 1
