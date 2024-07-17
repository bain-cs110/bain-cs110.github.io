_a_canvas = None
from tkinter import Canvas, Tk

def setup_shapes(title, background="white", width=600, height=600):
    """
    A static function that sets up the pop-up window. **DO NOT USE THIS FUNCTION**.
    """
    global _a_canvas
    gui = Tk()
    gui.title(title)
    _a_canvas = Canvas(gui, background=background, width=width, height=width)
    _a_canvas.pack()
    make_grid(_a_canvas, width, height)
    return _a_canvas

def make_grid(c, w, h):
    interval = 100

    # Creates all vertical lines at intervals of 100
    for i in range(0, w, interval):
        c.create_line(i, 0, i, h, tag="grid_line")

    # Creates all horizontal lines at intervals of 100
    for i in range(0, h, interval):
        c.create_line(0, i, w, i, tag="grid_line")

    # Creates axis labels
    offset = 2
    for y in range(0, h, interval):
        for x in range(0, w, interval):
            c.create_oval(x - offset, y - offset, x + offset, y + offset, fill="black")
            c.create_text(
                x + offset,
                y + offset,
                text="({0}, {1})".format(x, y),
                anchor="nw",
                font=("Purisa", 8),
            )

import math     
def oval(center_x, center_y, radius_x, radius_y, color="hotpink"):
    """
    A reporter function that draws an oval.
    Args:
        center_x (`int`): A x-coordinate representing the center of the shape.
        center_y (`tuple`): A y-coordinate representing the center of the shape.
        radius_x (`int`): How wide to draw the oval in the x-direction.
        radius_y (`int`): How tall to draw the oval in the y-direction.
        color (`str`): What color to draw the shape.
    Returns:
         `Shape`: The oval that was created.
    """
    x = center_x
    y = center_y
    x0, y0, x1, y1 = (x - radius_x, y - radius_y, x + radius_x, y + radius_y)
    steps = 100
    # major and minor axes
    a = (x1 - x0) / 2.0
    b = (y1 - y0) / 2.0
    # center
    xc = x0 + a
    yc = y0 + b
    point_list = []
    # create the oval as a list of points
    for i in range(steps):
        # Calculate the angle for this step
        theta = (math.pi * 2) * (float(i) / steps)
        x = a * math.cos(theta)
        y = b * math.sin(theta)
        point_list.append(round(x + xc))
        point_list.append(round(y + yc))

    return _a_canvas.create_polygon(point_list, fill=color)


def rectangle(top_left_x, top_left_y, width, height, color="hotpink", **kwargs):
    """
    A reporter function that draws a rectangle.
    Args:
        top_left_x (`int`): A x-coordinate representing the top left-hand corner of the shape.
        top_left_y (`tuple`): A y-coordinate representing the top left-hand corner of the shape.
        width (`int`): How wide to draw the shape.
        height (`int`): How tall to draw the shape.
        color (`str`): What color to draw the shape.
    Returns:
         `Shape`: The rectangle that was created.
    """
    point_0 = (top_left_x, top_left_y)
    point_1 = (top_left_x + width, top_left_y)
    point_2 = (top_left_x + width, top_left_y + height)
    point_3 = (top_left_x, top_left_y + height)
    return _a_canvas.create_polygon(
        point_0, point_1, point_2, point_3, fill=color, **kwargs
    )
