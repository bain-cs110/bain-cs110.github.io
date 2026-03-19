from cs110_l8 import *
_ignore = setup_shapes('Lecture 8', background="white", width=500, height=500)
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


def squareface(center_x, center_y, width, eye_color="blue", face_color="gold"):
    # face
    square(center_x, center_y, width, color=face_color)

    # left eye
    rectangle(
        center_x - width / 5,  # center of this eye
        center_y - width / 5,
        width / 20,  # width of the eye
        width / 10,  # height of the eye
        color=eye_color,
    )

    # right eye
    rectangle(
        center_x + width / 5,  # center of this eye
        center_y - width / 5,
        width / 20,  # width of the eye
        width / 10,  # height of the eye
        color=eye_color,
    )


# Example function call to squareface
squareface(100, 400, 100, eye_color="olive drab", face_color="cyan")


########################## YOUR CODE ABOVE THIS LINE ##############################
_ignore.mainloop()
