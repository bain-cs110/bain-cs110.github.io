from cs110_p1 import *
_ignore = setup_shapes("Lecture 17", background="white", include_grid=False, width=600, height=600)
########################## YOUR CODE BELOW THIS LINE ##############################

def click_handler(event):
    circle((event.x, event.y), 20, color="hot pink")


def right_click_handler(event):
    tag = get_tag_from_event(event)
    delete(tag)


def setup():
    ## Setting some listeners!
    # Notice first we define our function called do_something
    # then we tell the canvas to listen for MOUSE_CLICKs and if
    # it hears one, do_something
    listen_for("LEFT-CLICK", click_handler)
    listen_for("RIGHT-CLICK", right_click_handler)
    ## Right click not working on your computer? Change the magic string to "ALT-CLICK"

    text((300, 200), text="Click anywhere add a circle.\n Right click on a circle to delete!", font=("Purisa", 32))



def go():
    # Here's where you'll put everything you want to control your animations
    #   EXCEPT event listeners (look higher up)
    pass


ticks_per_second = 30

######&&!*#################### YOUR CODE ABOVE THIS LINE ##############################
## DO NOT MODIFY THIS STUFF
clear_window() ## Nothing should be drawn outside SETUP and GO!
ticks = 0
setup()
while True:
    go()
    update() # This function draws all your stuff to the screen!
    sleep(1 / ticks_per_second)
    ticks = ticks + 1
