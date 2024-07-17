from p1_utilities import *
import time
_ignore = setup_shapes('Lecture 16', background="white", grid=True, width=600, height=600)
ticks_per_second = None
ticks = 0
########################## YOUR CODE BELOW THIS LINE ##############################

bounce_counter = 0
def setup():
    global bounce_counter
    bounce_counter = 40   
    square((400, 400), tag="bouncy_boi")
    
    # This is how many animations to attempt per second. If you want to slow down your
    #   animations, just decrease this number! If you want to speed up...
    global ticks_per_second
    ticks_per_second = 30


def go():
    # Here's where you'll put everything you want to control your animations
    #   EXCEPT event listeners (look higher up)
    
    global bounce_counter
    # If our counter is greater than 20!
    if bounce_counter > 20:
        bounce_counter = bounce_counter - 1
        move("bouncy_boi", y = -5)
    # or if it's only greater than 0!
    elif bounce_counter > 0:
        bounce_counter = bounce_counter - 1
        move("bouncy_boi", y = 5)
    # if we reached the end of our bounce...
    else:
        bounce_counter = 40


######&&!*#################### YOUR CODE ABOVE THIS LINE ##############################

## DO NOT MODIFY THIS STUFF
setup()
while True:
    go()
    _ignore.update()
    time.sleep(1 / ticks_per_second)
    ticks = ticks + 1