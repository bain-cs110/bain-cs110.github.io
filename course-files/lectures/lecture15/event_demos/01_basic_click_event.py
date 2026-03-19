from cs110_l15 import *
_ignore = setup_shapes("Lecture 15", background="white", grid=True, width=600, height=600)
ticks = 0
########################## YOUR CODE BELOW THIS LINE ##############################
ticks_per_second = 30 # animation rate - increasing speeds up animations

def do_something(event):
    print("You clicked..." + "LEFT_CLICK")
    print("And told me to run do_something when I heard that")
    print("And we got back the following event object!")
    print(str(type(event)) + " " + str(event))
    print("X: " + str(event.x) + " Y: " + str(event.y))

def setup():
    ## Setting some listeners!
    # Notice first we define our function called do_something
    # then we tell the canvas to listen for a left mouse click and if
    # it hears one, do_something
    listen_for("LEFT-CLICK", do_something)


def go():
    # Here's where you'll put everything you want to control your animations
    #   EXCEPT event listeners (look higher up)
    pass # we use this as a place holder - it's a keyword that means DO NOTHING.


########################## YOUR CODE ABOVE THIS LINE ##############################
## DO NOT MODIFY THIS STUFF
setup()
while True:
    go()
    _ignore.update()
    sleep(1 / ticks_per_second)
    ticks = ticks + 1
