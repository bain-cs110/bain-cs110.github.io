from cs110_t3_shapes import *
_ignore = setup_shapes('Tutorial 3', background="white", width=800, height=800)
#### YOUR CODE BELOW THIS LINE ##########
from random import randint

## Flag of Chicago Challenge!
def chicago_flag(location, size):
    bg = rectangle(top_left=location,
                   width=size,
                   height=size/2,
                   color="white",
                   outline="black")
    stripe_1 = rectangle(width=size, height=size/10, color="#40B0DF")
    stripe_2 = duplicate(stripe_1)
    overlay(stripe_1, bg, offset_y = -size / 8)
    overlay(stripe_2, bg, offset_y = size / 8)

    star1 = star(radius = size / 50, color = "red", outer_radius=size/20, points = 6)
    overlay(star1, bg, offset_x=-3*size/10)
    star2 = duplicate(star1)
    overlay(star2, bg, offset_x=-size/10)
    star3 = duplicate(star1)
    overlay(star3, bg, offset_x=size/10)
    star4 = duplicate(star1)
    overlay(star4, bg, offset_x=3*size/10)

chicago_flag((0,0), 200)

#                   random x           random y
random_location = (randint(300, 500), randint(300, 500))
#       use our random loc  and pick a random size
chicago_flag(random_location, randint(0,500))


#### IGNORE BELOW
_ignore.mainloop()
