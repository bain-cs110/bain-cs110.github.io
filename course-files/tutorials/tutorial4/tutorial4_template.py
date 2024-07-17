import time
from cs110_t4 import *
_ignore = setup_shapes('Tutorial 4', background="white", grid=True, width=1000, height=800)
ticks_per_second = None
ticks = 0
########################## YOUR CODE BELOW THIS LINE ##############################

mario_colors = [None, "red", "blue", "saddle brown", "bisque3", "black", "gold"]

def setup():
    print("Setup time!")

    # 4 Different Mario Drawings:
    #    DEFAULT_MARIO
    #    mario_0
    #    mario_1
    #    mario_2
    # They are imported from cs110_t4 above so you can use them like regular variables
    pixel_art((150, 0), DEFAULT_MARIO, mario_colors, tag="mario", pixel=10)

    # This is how many animations to attempt per second. If you want to slow down your
    #   animations, just decrease this number! If you want to speed up...
    global ticks_per_second
    ticks_per_second = 1

def go():
    # This is where we put REPEATED or LOOPED actions
    print("Go time!", ticks)






########################## YOUR CODE ABOVE THIS LINE ##############################
## DO NOT MODIFY THE STUFF BELOW
setup()
while True:
    go()
    _ignore.update()
    time.sleep(1 / ticks_per_second)
    ticks = ticks + 1