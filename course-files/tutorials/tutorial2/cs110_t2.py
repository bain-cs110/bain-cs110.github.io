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

def rectangle(top_left_x, top_left_y, width, height, color="hotpink", **kwargs):
    """
    A reporter function that draws a rectangle.
    Args:
        top_left_x (`int`): A x-coordinate representing the top left-hand corner of the shape.
        top_left_y (`int`): A y-coordinate representing the top left-hand corner of the shape.
        width (`int`): How wide to draw the shape.
        height (`int`): How tall to draw the shape.
        color (optional, `str`): What color to draw the shape.
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

