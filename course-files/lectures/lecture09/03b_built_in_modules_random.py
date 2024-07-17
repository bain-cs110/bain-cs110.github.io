from cs110_l9 import *
_ignore = setup_shapes('Lecture 9', background="white", width=600, height=600)
######################### YOUR CODE BELOW THIS LINE ###############################
from random import choice, randint

def random_oval(color_choices=["olive drab"]):
    x = randint(0, 500)
    y = randint(0, 500)

    radius_x = randint(10, 50)
    radius_y = randint(10, 50)

    the_color = choice(color_choices)

    my_shape = oval(x, y, radius_x, radius_y, the_color)

some_fave_colors = ["olive drab", "yellow", "blue", "purple4", "tomato"]

random_oval(some_fave_colors)
random_oval(some_fave_colors)
random_oval(some_fave_colors)
random_oval(some_fave_colors)
random_oval(some_fave_colors)
random_oval(some_fave_colors)

########################## YOUR CODE ABOVE THIS LINE ##############################
_ignore.mainloop()
