from cs110_l8 import *
_ignore = setup_shapes('Lecture 8', background="white", width=600, height=600)
########################## YOUR CODE BELOW THIS LINE ##############################

def square(center_x, center_y, size, color="hot pink"):
    # center_x = whatever was passed as input to our function
    # center_y = whatever was passed as input to our function
    # size = whatever was passed as input to our function
    # color = whatever was passed as input to our function, otherwise hot pink

    # rectangle needs...
    #         center x  center y  width  height (opt) color
    rectangle(center_x, center_y, size, size, color=color)

# Example function calls for square
square(300, 100, 100)
square(300, 200, 50, color="olive drab")






########################## YOUR CODE ABOVE THIS LINE ##############################
_ignore.mainloop()
