from cs110_t4 import *
_ignore = setup_shapes('Lecture 15', background="white", grid=True, width=600, height=600)

MARIO = [
    (0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0),
    (0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0),
    (0, 0, 3, 3, 3, 4, 4, 4, 5, 4, 0, 0, 0, 0),
    (0, 3, 4, 3, 4, 4, 4, 4, 5, 4, 4, 4, 0, 0),
    (0, 3, 4, 3, 4, 4, 4, 4, 4, 5, 4, 4, 4, 0),
    (0, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 0, 0),
    (0, 0, 1, 1, 2, 1, 1, 1, 2, 0, 0, 0, 0, 0),
    (0, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 0, 0, 0),
    (1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0),
    (4, 4, 1, 2, 6, 2, 2, 6, 2, 1, 4, 4, 0, 0),
    (4, 4, 4, 2, 2, 2, 2, 2, 2, 4, 4, 4, 0, 0),
    (4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 0, 0),
    (0, 0, 2, 2, 2, 0, 0, 2, 2, 2, 0, 0, 0, 0),
    (0, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 0, 0, 0),
    (3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 0, 0)
]

mario_colors = [None, "red", "blue", "saddle brown", "bisque3", "black", "gold"]
########################## YOUR CODE BELOW THIS LINE ##############################

# Name: row_of_squares
# Purpose: draws a single row of pixel art
# Inputs:
#  1. row (tuple), the row of the artwork we want to draw
#  2. top_left (tuple), the top left coordinate to draw the picture at
#  3. colors (list) a list of colors to draw with
#  4. pixel (int; optional) the size of each pixel

        
# Name: pixel_art
# Purpose: draws an entire piece of pixel art
# Inputs:
#  1. top_left (tuple), the top left coordinate to draw the picture at
#  2. artwork (list) the actual picture to draw
#  3. palette (list) a list of colors to draw with
#  4. pixel (int; optional) the size of each pixel


########################## YOUR CODE ABOVE THIS LINE ##############################
_ignore.mainloop()