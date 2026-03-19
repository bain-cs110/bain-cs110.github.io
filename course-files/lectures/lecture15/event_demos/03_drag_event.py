from cs110_l15 import *
_ignore = setup_shapes("Lecture 15", background="white", grid=False, width=600, height=600)
ticks = 0
########################## YOUR CODE BELOW THIS LINE ##############################
ticks_per_second = 30

def make_a_circle(event):
    circle(center=(event.x, event.y), radius=20, color="hot pink")

def setup():
    listen_for("LEFT-DRAG", make_a_circle)

    text((200, 200), text="Drag to make circles!", font=("Purisa", 32))

def go():
    # Here's where you'll put everything you want to control your animations
    #   EXCEPT event listeners (look higher up)
    pass


########################## YOUR CODE ABOVE THIS LINE ##############################

## DO NOT MODIFY THIS STUFF
setup()
while True:
    go()
    _ignore.update()
    sleep(1 / ticks_per_second)
    ticks = ticks + 1
