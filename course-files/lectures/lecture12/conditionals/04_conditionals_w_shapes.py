from cs110_l12_shapes import *

_ignore = setup_shapes("Lecture 12", background="white", width=800, height=800)
#### YOUR CODE BELOW THIS LINE ##########
from random import randint

#                   random x           random y
random_location = (randint(100, 700), randint(100, 700))
random_size = randint(50, 100)

if random_location[0] < 350:
    color_to_use = "green"
else:
    color_to_use = "red"

circle(center=random_location, radius=random_size, color=color_to_use)


#### IGNORE BELOW
_ignore.mainloop()
