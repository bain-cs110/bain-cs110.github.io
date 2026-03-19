from cs110_p1 import *
_ignore = setup_shapes("Lecture 17", background="white", include_grid=False, width=600, height=600)
########################## YOUR CODE BELOW THIS LINE ##############################

def make_a_circle(event):
    circle(center=(event.x, event.y), radius=20, color="hot pink")

def setup():
    listen_for("LEFT-DRAG", make_a_circle)

    text((200, 200), text="Drag to make circles!", font=("Purisa", 32))

def go():
    # Here's where you'll put everything you want to control your animations
    #   EXCEPT event listeners (look higher up)
    pass


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
