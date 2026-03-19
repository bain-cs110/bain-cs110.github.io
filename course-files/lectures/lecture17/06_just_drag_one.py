from cs110_p1 import *
_ignore = setup_shapes("Lecture 18", background="white", include_grid=False, width=600, height=600)
########################## YOUR CODE BELOW THIS LINE ##############################

from random import randint

def move_circle(event):
    selected_tag = get_tag_from_event(event)
    
    # check to see if this thing is a circle
    if "circle" not in selected_tag:
        selected_tag = None # If it's not a circle let's not mess with it

    # as long as we have something selected, move it!
    if selected_tag != None:
        move_to(selected_tag, (event.x, event.y))
        change_color(selected_tag, "yellow")

def make_circle(event):
    global circle_counter

    circle((event.x, event.y), tag="circle_"+str(circle_counter))
    circle_counter = circle_counter + 1

circle_counter = 0
def setup():
    ## Setting some listeners!    
    listen_for("LEFT-DRAG", move_circle)
    listen_for("LEFT-CLICK", make_circle)


    text((300, 200), text="Drag a circle around!", font=("Purisa", 32), tag="instructions")

    # Draw some circles!
    global circle_counter
    circle_counter = 0
    while circle_counter < 50:
        circle((randint(0, 1000), randint(0, 1000)), radius=randint(10, 20), tag="circle_"+str(circle_counter))
        circle_counter += 1

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
