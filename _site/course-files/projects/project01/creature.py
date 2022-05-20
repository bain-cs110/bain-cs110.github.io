from tkinter import Canvas
import utilities

def make_creature(canvas, center, size=100, my_tag='creature', my_fill='lightgray'):
    radius = size / 2
    # just a demo of how you might think about making your creature:
    left_eye_pos = (center[0] - radius / 4, center[1] - radius / 5)
    right_eye_pos = (center[0] + radius / 4, center[1] - radius / 5)
    eye_width = eye_height = radius / 10

    # IMPORTANT that I'm tagging each of the shapes that makes up my "make_creature"
    # with the tag that the user passed in:

    ## ALSO IMPORTANT:
    # notice that I'm using the make_shape functions from the utilities module. Each of these functions has
    # an extra input called "tag" that allows us to specify the tag name for our creature. When updating YOUR
    # creature, make sure to either a) use the updated shape functions from utilities.py OR add the `tag` optional
    # parameter to your make_shape function headers AND in the call to any canvas.create_shape methods. see
    # utilities.py for some examples of those
    utilities.make_circle(canvas, center, radius, fill_color=my_fill, tag=my_tag)
    utilities.make_oval(canvas, left_eye_pos, eye_width, eye_height, fill_color='green', tag=my_tag)
    utilities.make_oval(canvas, right_eye_pos, eye_width, eye_height, fill_color='red', tag=my_tag)
    utilities.make_line(canvas, [
        (center[0] - radius / 2, center[1] + radius / 3),
        (center[0], center[1] + radius / 1.2),
        (center[0] + radius / 2, center[1] + radius / 3)
    ], curvy=True, tag=my_tag)
