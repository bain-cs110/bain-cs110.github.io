from cs110_p1 import *
from pixel_friends import *
_ignore = setup_shapes("Lecture 20", background="white", include_grid=False, width=800, height=800)
########################## YOUR CODE BELOW THIS LINE ##############################

from random import randint, choice

goomba_direction = 1
def setup():
    mario((400, 200), tag="mario")
    goomba((200, 200), tag="goomba")
    
def go():
    move("mario", x_shift=2)

    global goomba_direction
    move("goomba", x_shift=goomba_direction * 2)

    if get_right("mario") < 0:
        move("mario", x_shift=1*(get_window_width()+get_width("mario")))
    elif get_left("mario") > 800:
        move("mario", x_shift=-1*(get_window_width()+get_width("mario")))

    if get_left("goomba") < 0:
        goomba_direction = 1
    elif get_right("goomba") > 800:
        goomba_direction = -1 

ticks_per_second = 60
######&&!*#################### YOUR CODE ABOVE THIS LINE ##############################
clear_window() ## Nothing should be drawn outside SETUP and GO!
ticks = 0
setup()
while True:
    go()
    update() # This function draws all your stuff to the screen!
    sleep(1 / ticks_per_second)
    ticks = ticks + 1
