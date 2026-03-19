from cs110_t4 import *
_ignore = setup_shapes('Lecture 14', background="white", grid=True, width=600, height=600)
########################## YOUR CODE BELOW THIS LINE ##############################
from time import sleep
ticks_per_second = 1
ticks = 0

def setup():
    # Inside the SETUP function we put anything we want drawn ONCE at the very
    #   beginning of our animation.
    square(top_left = (0, 450), size=50, color="yellow", tag="test_square")


def go():
    # Inside the GO function we put any actions we wanted REPEATEDLY done
    delete("test_square")

    if ticks % 2 == 0:
        color_to_use = "green"
    else:
        color_to_use = "red"
    
    square(top_left=(0 + ticks * 5, 450), color=color_to_use, tag="test_square")


########################## YOUR CODE ABOVE THIS LINE ##############################
## DO NOT MODIFY THIS STUFF
setup()
while True:
    go()
    _ignore.update()
    sleep(1 / ticks_per_second)
    ticks = ticks + 1
    
# makes sure the window keeps running:
_ignore.mainloop()
