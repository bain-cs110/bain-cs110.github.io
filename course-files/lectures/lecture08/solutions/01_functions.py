from cs110_l8 import *
_ignore = setup_shapes('Lecture 8', background="white", width=500, height=500)
########################## YOUR CODE BELOW THIS LINE ##############################

## rectangle: A function that creates rectangles!
## def rectangle(center_x, center_y, width, height, color="hotpink", **kwargs):
##     ...

# Example function calls for rectangle
rectangle(100, 200, 50, 100, color="red")
rectangle(100, 100, 100, 50)

def square(center_x, center_y, size, color="hotpink"):
    # center_x = whatever was passed as input to our function
    # center_y = whatever was passed as input to our function
    # size = whatever was passed as input to our function
    # color = whatever was passed as input to our function, otherwise hotpink

    # rectangle needs...
    #         center x  center y  width  height (opt) color
    rectangle(center_x, center_y, size, size, color=color)


# Example function calls for square
square(300, 100, 100)
square(300, 200, 50, color="olive drab")


def squareseye(center_x, center_y, size, color_a="blue", color_b="red"):
    square(center_x, center_y, size * 2.5, color=color_b)
    square(center_x, center_y, size * 2.0, color=color_a)
    square(center_x, center_y, size * 1.5, color=color_b)
    square(center_x, center_y, size * 1.0, color=color_a)
    print("hello")


# Example function calls for squareseye
squareseye(400, 100, 24, color_a="gold", color_b="blue")
squareseye(400, 200, 15, color_a="blue", color_b="gold")
squareseye(400, 250, 20, color_b="blue")
squareseye(400, 300, 20, color_a="gold")
squareseye(400, 400, 14)


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
