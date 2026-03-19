from cs110_p1 import *
_ignore = setup_shapes("Lecture 17", background="white", include_grid=False, width=600, height=600)
########################## YOUR CODE BELOW THIS LINE ##############################

from random import randint, choice

def make_square_from_click(event):
    # use the random module to pick a random number between 40 and 150
    a_width = randint(40, 150)
    # use the random module to pick a random color from a list of colors
    a_color = choice(["black", "yellow", "blue", "pink"])
    
    # create a square at the place the person clicked with
    square(top_left=(event.x, event.y), size=a_width, color=a_color)


def setup():
    ## Setting some listeners!
    # Notice first we define our function called do_something
    # then we tell the canvas to listen for a LEFT-CLICK and if
    # it hears one, run make_square_from_click
    listen_for("LEFT-CLICK", make_square_from_click)
    
    text((200, 200), text="Click anywhere add a square", font=("Purisa", 32))


def go():
    # Here's where you'll put everything you want to control your animations
    #   EXCEPT event listeners (look higher up)
    pass # this is a keyword that means DO NOTHING - It's just a placeholder

ticks_per_second = 30

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
