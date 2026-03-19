from cs110_p1 import *
_ignore = setup_shapes("Lecture 20", background="salmon1", include_grid=False, width=400, height=1000)
########################## YOUR CODE BELOW THIS LINE ##############################

from random import randint, choice

# Change bubbles to dictionaries!
#   Add colors!
#   Add directions!

user_shapes = {}
def click_handler(event):
    new_tag = "circle_" + str(len(user_shapes))
    the_circle = {
        "speed": randint(1, 10),
        "direction": choice([-1, 1]),
        "color": random_color(),
        "size": randint(10, 50)
    }
    circle((event.x, event.y),
           radius = the_circle["size"],
           color = the_circle["color"],
           tag = new_tag)
    
    # add our shape to a dictionary called user_shapes
    #   using the TAG as its KEY and the dict we made as its VALUE
    user_shapes[new_tag] = the_circle
    print(user_shapes)
    
def setup():
    ## Setting some listeners!
    listen_for("LEFT-CLICK", click_handler)
    listen_for("LEFT-DRAG", click_handler)

    text((200, 200), text="Click or drag\n to create circles", font=("Purisa", 32))

def go():
    # Here"s where you"ll put everything you want to control your animations
    #   EXCEPT event listeners (look higher up)

    # so for each KEY in user_shapes
    #   where every KEY is a string (the shape's tag)
    for key in user_shapes:
    
        direction = user_shapes[key]["direction"] # load the shape's direction

        # if one of our shapes touches the edge of the canvas
        if get_bottom(key) > 1000 or get_top(key) < 0:
            user_shapes[key]["direction"] = -1 * direction

        # regardless move the shape a little bit (determined by its speed)
        move(key, x_shift=0, y_shift=user_shapes[key]["direction"] * user_shapes[key]["speed"])     

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
