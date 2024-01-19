from tkinter import Canvas, Tk
import math

gui = Tk()
gui.title("MORE FUNCTIONS")
the_canvas = Canvas(gui, width=500, height=500, background="white")
the_canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################


def rectangle(center_x, center_y, width, height, color="hotpink"):
    x0, y0 = (center_x - width / 2, center_y - height / 2)
    x1, y1 = (center_x + width / 2, center_y + height / 2)
    return the_canvas.create_rectangle(x0, y0, x1, y1, fill=color)


def oval(center_x, center_y, radius_x, radius_y, color="hotpink"):
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

    return the_canvas.create_polygon(point_list, fill=color)


######################### YOUR CODE BELOW THIS LINE ###############################

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
# helper function that draws a grid.
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


make_grid(the_canvas, 500, 500)
the_canvas.mainloop()
