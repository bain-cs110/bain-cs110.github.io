from cs110_p1 import *
_ignore = setup_shapes("Lecture 18", background="white", include_grid=False, width=600, height=600)
########################## YOUR CODE BELOW THIS LINE ##############################

def handle_click(event):
    circle(
        (event.x, event.y),
        20,
        color="hot pink",
        tag="circle"
    )

def handle_keyboard(event):

    distance = 10

    # if they press up on the keyboard
    if event.keysym == "Up":
        move("circle", y_shift=-distance)
    # otherwise if they press down on the keyboard
    elif event.keysym == "Down":
        move("circle", y_shift=distance)
    # otherwise if they press left on the keyboard
    elif event.keysym == "Left":
        move("circle", x_shift=-distance)
    # otherwise if they press right on the keyboard
    elif event.keysym == "Right":
        move("circle", x_shift=distance)
    else:
        print("Key sym:", event.keysym, "not handled by this if/elif/else statement.")


def setup():
    print("Running setup!")
    listen_for("LEFT-CLICK", handle_click)
    listen_for("KEY", handle_keyboard)

    text((300, 300),
        text="Click anywhere add a circle.\n Press arrow keys to move circle",
        font=("Purisa", 32)
    )


def go():
    # Here's where you'll put everything you want to control your animations
    #   EXCEPT event listeners (look higher up)
    pass


ticks_per_second = 60
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
