from cs110_p1 import *
_ignore = setup_shapes("Lecture 18", background="salmon1", include_grid=False, width=400, height=1000)
########################## YOUR CODE BELOW THIS LINE ##############################
from random import randint, choice

def click_handler(event):
    circle((event.x, event.y), randint(10, 50), color="cyan", tag="bubble")

def setup():
    ## Setting some listeners!

    ## Drawing some instructions to the screen
    text((200, 200), text="Click or drag\n to create circles", font=("Purisa", 32))

def go():
    move("bubble", x_shift=0, y_shift=10)


ticks_per_second = 60

########################## YOUR CODE ABOVE THIS LINE ##############################
## DO NOT MODIFY THIS STUFF
clear_window() ## Nothing should be drawn outside SETUP and GO!
ticks = 0
setup()
while True:
    go()
    update() # This function draws all your stuff to the screen!
    sleep(1 / ticks_per_second)
    ticks = ticks + 1

