import random
from cs110_t4 import *
_ignore = setup_shapes('Lecture 15', background="white", grid=True, width=600, height=600)
########################## YOUR CODE BELOW THIS LINE ##############################

# Name: row
# Purpose: draws a single row of pixel art
# Inputs:
#  1. row (tuple), the row of the artwork we want to draw
#  2. top_left (tuple), the top left coordinate to draw the picture at
#  3. colors (list) a list of colors to draw with
#  4. pixel (int; optional) the size of each pixel
def row_of_squares(row, top_left, colors, pixel=25):
    x = top_left[0]
    y = top_left[1]

    for cell in row:
        if cell != 0:
            square(top_left=(x, y), size=pixel, color=colors[cell])
        x = pixel + x
        
# Name: pixel_art
# Purpose: draws an entire piece of pixel art
# Inputs:
#  1. top_left (tuple), the top left coordinate to draw the picture at
#  2. artwork (list) the actual picture to draw
#  3. palette (list) a list of colors to draw with
#  4. pixel (int; optional) the size of each pixel
def pixel_art(top_left, artwork, palette, pixel=25):

    x = top_left[0]
    y = top_left[1]

    for row in artwork:
        row_of_squares(row, (x, y), palette, pixel=pixel)
        y += pixel

# Draw 50 sample marios and goombas!
for counter in range(50):
    if counter % 2 == 0:
        pixel_art((random.randint(0, 600), random.randint(0, 600)),
                       DEFAULT_MARIO,
                       [None, "red", "blue", "saddle brown", "bisque3", "black", "gold"],
                       pixel=random.randint(1, 15))
    else:
        pixel_art((random.randint(0, 600), random.randint(0, 600)),
                  GOOMBA,
                  GOOMBA_COLORS,
                  pixel=random.randint(1, 15))

########################## YOUR CODE ABOVE THIS LINE ##############################
_ignore.mainloop()
