from cs110_p1 import *
_ignore = setup_shapes("Lecture 16", background="salmon1", include_grid=False, width=400, height=1000)
########################## YOUR CODE BELOW THIS LINE ##############################

from random import randint, choice

user_shapes = [] # this is a GLOBAL variable

def click_handler(event):
    tag = "circle_"+ str(len(user_shapes))
    circle((event.x, event.y), randint(10, 50), color="cyan", tag=tag)
    # add our shape to a list called user_shapes by appending
    # a tuple with its tag and a randomly generated speed to travel at

    random_speed = randint(-10, 10)
    if random_speed == 0:
        random_speed = random_speed + choice([-1, 1])

    user_shapes.append((tag, random_speed))

def setup():
    ## Setting some listeners!
    listen_for("LEFT-CLICK", click_handler)
    listen_for("LEFT-DRAG", click_handler)

    ## Drawing some instructions to the screen
    text((300, 200), text="Click or drag to create circles", font=("Purisa", 32))

def go():
    
    for shape in user_shapes:

        shape_tag = shape[0] # load the shape's tag
        shape_speed = shape[1] # load the shape's speed

        # if one of our shapes reaches the bottom of the canvas
        if get_top(shape_tag) > 1000:
            # then calculate a new position at the "top" of the canvas
            reset_position = 1000 + get_height(shape_tag)
            # and move the shape with that tag to that "top" of the canvas
            move(shape_tag, y_shift=-1 * reset_position)

        # if one of our shapes reaches the top of the canvas
        if get_bottom(shape_tag) < 0:
            # then calculate a new position at the "bottom" of the canvas
            reset_position = 1000 + get_height(shape_tag)
            # and move the shape with that tag to that "top" of the canvas
            move(shape_tag, y_shift=reset_position)

        # regardless move the shape a little bit (determined by its speed)
        move(shape_tag, x_shift=0, y_shift=shape_speed)


ticks_per_second = 60

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

