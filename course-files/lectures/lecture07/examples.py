from cs110_hw2 import *
_ignore = setup_shapes('Shape Examples', background="white", width=600, height=600)
#### IGNORE THE ABOVE

# oval: a reporter function that draws an oval.
# Args:
#   center_x (`int`): A x-coordinate representing the center of the shape.
#   center_y (`int`): A y-coordinate representing the center of the shape.
#   radius_x (`int`): How wide to draw the oval in the x-direction.
#   radius_y (`int`): How tall to draw the oval in the y-direction.
#   color (optional) (`str`): What color to draw the shape.
# Returns:
#   `Shape`: The oval that was created.


# eyeball: a function that draws an eyeball
# Args:
#    center_x
#    center_y
#    radius_x
#    radius_y
#    eye_color (opt, default to "purple")

def eyeball(center_x, center_y, radius_x, radius_y, eye_color="purple"):
    oval(center_x, center_y, radius_x, radius_y, color=eye_color)
    oval(center_x, center_y, radius_x / 2, radius_y / 2, color="white")

#eyeball(300, 400, 50, 25)
#eyeball(300, 300, 100, 50, eye_color="green")
#eyeball(400, 200, 25, 10, eye_color="yellow")

# rectangle: a reporter function that draws a rectangle.
# Args:
#   top_left_x (`int`): A x-coordinate representing the top left-hand corner of the shape.
#   top_left_y (`int`): A y-coordinate representing the top left-hand corner of the shape.
#   width (`int`): How wide to draw the shape.
#   height (`int`): How tall to draw the shape.
#   color (optional) (`str`): What color to draw the shape.
#   Returns:
#         `Shape`: The rectangle that was created.

rectangle(300, 300, 200, 100, color="cyan")

# square: a function to draw squares
# Args:
#   top_left_x
#   top_left_y
#   width
#   color (optional) - default to "hot pink"

def square(top_left_x, top_left_y, width, color="hot pink"):
    rectangle(top_left_x, top_left_y, width, width, color=color)

square(300, 250, 50, color="purple")

# two_squares: a function to draw two squares side-by-side (red, then gold)
# Args:
#   top_left_x
#   top_left_y
#   width (a single square)
def two_squares(top_left_x, top_left_y, width):
    # Draw 1 square
    square(top_left_x, top_left_y, width, color="red")
    # Draw another square right next to it
    square(top_left_x + width, top_left_y, width, color="gold")

two_squares(400, 450, 50)
two_squares(100, 100, 100)




#### IGNORE BELOW
_ignore.mainloop()
