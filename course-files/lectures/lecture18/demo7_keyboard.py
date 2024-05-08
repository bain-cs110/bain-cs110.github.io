from p1_utilities import *
import time

_ignore = setup_shapes('Lecture 18', background="white", grid=False, width=600, height=600)
ticks_per_second = None
ticks = 0
########################## YOUR CODE BELOW THIS LINE ##############################

def handle_click(event):
    circle(
        (event.x, event.y),
        20,
        color='hotpink',
        tag='circle'
    )

def handle_keyboard(event):
    #print(event)

    distance = 10

    # if they press up on the keyboard
    if event.keysym == "Up":
        move('circle', y=-distance)
    # otherwise if they press down on the keyboard
    elif event.keysym == "Down":
        move('circle', y=distance)
    # otherwise if they press left on the keyboard
    elif event.keysym == "Left":
        move('circle', x=-distance)
    # otherwise if they press right on the keyboard
    elif event.keysym == "Right":
        move('circle', x=distance)
    else:
        print('Key sym:', event.keysym, 'not handled by this if/elif/else statement.')

def setup():

    MOUSE_CLICK = '<Button-1>'
    KEY_PRESS = '<Key>'
    
    setup_listener(MOUSE_CLICK, handle_click)
    setup_listener(KEY_PRESS, handle_keyboard)

    text(
    (1000 / 2, 1000 / 2),
    text='Click anywhere add a circle. Press arrow keys to move circle',
    font=("Purisa", 32)
    )

    # This is how many animations to attempt per second. If you want to slow down your
    #   animations, just decrease this number! If you want to speed up...
    global ticks_per_second
    ticks_per_second = 60


def go():
    # Here's where you'll put everything you want to control your animations
    #   EXCEPT event listeners (look higher up)
    pass

######&&!*#################### YOUR CODE ABOVE THIS LINE ##############################

## DO NOT MODIFY THIS STUFF
setup()
while True:
    go()
    _ignore.update()
    time.sleep(1 / ticks_per_second)
    ticks = ticks + 1
