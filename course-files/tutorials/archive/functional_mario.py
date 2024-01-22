from tkinter import Canvas, Tk
from tutorial2_shapes import (
    setup_shapes,
    rectangle,
    triangle,
    square,
    line,
    above,
    below,
    beside,
    overlay,
    rotate,
    underlay,
)

def iterated_beside(top_left, shape_function, n, colors=[]):
    if len(colors) != n:
        raise Exception(
            f"You specified {len(colors)} colors but asked me to draw {n} shapes!"
        )
    current_iteration = None
    for i in range(1, n):
        if len(colors) > 0:
            copy = shape_function(top_left=top_left, color=colors[i])
        else:
            copy = shape_function(top_left=top_left)
        if current_iteration:
            beside(copy, current_iteration)
        current_iteration = copy

    return current_iteration


gui = Tk()
the_canvas = Canvas(gui, width=900, height=900, background="white")
setup_shapes(the_canvas)
the_canvas.pack()


########################## YOUR CODE BELOW THIS LINE ##############################

def shift_down(point, amount=25):
    return (point[0], point[1] + amount)

def mario(
    top_left,
    pixel=25,
    clothes="red",
    overalls="blue",
    features="black",
    tone="bisque3",
    hair="saddle brown",
    buttons="gold",
):
    MARIO = [
        (
            "",
            "",
            "",
            clothes,
            clothes,
            clothes,
            clothes,
            clothes,
            clothes,
            clothes,
            "",
            "",
            "",
        ),
        (
            "",
            "",
            clothes,
            clothes,
            clothes,
            clothes,
            clothes,
            clothes,
            clothes,
            clothes,
            clothes,
            clothes,
            "",
        ),
        ("", "", hair, hair, hair, tone, tone, tone, features, tone, "", "", ""),
        ("", hair, tone, hair, tone, tone, tone, tone, features, tone, tone, tone, ""),
        (
            "",
            hair,
            tone,
            hair,
            tone,
            tone,
            tone,
            tone,
            tone,
            features,
            tone,
            tone,
            tone,
            "",
        ),
        (
            "",
            hair,
            hair,
            tone,
            tone,
            tone,
            tone,
            tone,
            features,
            features,
            features,
            features,
            "",
        ),
        (
            "",
            "",
            clothes,
            clothes,
            overalls,
            clothes,
            clothes,
            clothes,
            overalls,
            "",
            "",
            "",
            "",
        ),
        (
            "",
            clothes,
            clothes,
            clothes,
            overalls,
            clothes,
            clothes,
            overalls,
            clothes,
            clothes,
            clothes,
            "",
            "",
        ),
        (
            clothes,
            clothes,
            clothes,
            clothes,
            overalls,
            overalls,
            overalls,
            overalls,
            clothes,
            clothes,
            clothes,
            clothes,
            "",
        ),
        (
            tone,
            tone,
            clothes,
            overalls,
            buttons,
            overalls,
            overalls,
            buttons,
            overalls,
            clothes,
            tone,
            tone,
            "",
        ),
        (
            tone,
            tone,
            tone,
            overalls,
            overalls,
            overalls,
            overalls,
            overalls,
            overalls,
            tone,
            tone,
            tone,
            "",
        ),
        (
            tone,
            tone,
            overalls,
            overalls,
            overalls,
            overalls,
            overalls,
            overalls,
            overalls,
            overalls,
            tone,
            tone,
            "",
        ),
        (
            "",
            "",
            overalls,
            overalls,
            overalls,
            "",
            "",
            overalls,
            overalls,
            overalls,
            "",
            "",
            "",
        ),
        ("", hair, hair, hair, hair, "", "", hair, hair, hair, hair, "", ""),
        (hair, hair, hair, hair, hair, "", "", hair, hair, hair, hair, hair, ""),
    ]

    iterated_beside(
        top_left,
        square,
        13,
        colors=MARIO[0],
    )
    top_left = shift_down(top_left)

    iterated_beside(
        top_left,
        square,
        13,
        colors=MARIO[1],
    )
    top_left = shift_down(top_left)

    iterated_beside(
        top_left,
        square,
        13,
        colors=MARIO[2],
    )
    top_left = shift_down(top_left)

    iterated_beside(
        top_left,
        square,
        13,
        colors=MARIO[3],
    )
    top_left = shift_down(top_left)

    iterated_beside(
        top_left,
        square,
        13,
        colors=MARIO[4],
    )
    top_left = shift_down(top_left)

    iterated_beside(
        top_left,
        square,
        13,
        colors=MARIO[5],
    )
    top_left = shift_down(top_left)

    iterated_beside(
        top_left,
        square,
        13,
        colors=MARIO[6],
    )
    top_left = shift_down(top_left)

    iterated_beside(
        top_left,
        square,
        13,
        colors=MARIO[7],
    )
    top_left = shift_down(top_left)

    iterated_beside(
        top_left,
        square,
        13,
        colors=MARIO[8],
    )
    top_left = shift_down(top_left)

    iterated_beside(
        top_left,
        square,
        13,
        colors=MARIO[9],
    )
    top_left = shift_down(top_left)

    iterated_beside(
        top_left,
        square,
        13,
        colors=MARIO[10],
    )
    top_left = shift_down(top_left)

    iterated_beside(
        top_left,
        square,
        13,
        colors=MARIO[11],
    )
    top_left = shift_down(top_left)

    iterated_beside(
        top_left,
        square,
        13,
        size=
        colors=MARIO[12],
    )
    top_left = shift_down(top_left)

mario((0, 0))


########################## YOUR CODE ABOVE THIS LINE ##############################
# helper function that draws a grid.
def make_grid(c, w, h):
    interval = 100
    # Creates all vertical lines at intevals of 100
    for i in range(0, w, interval):
        c.create_line(i, 0, i, h, tag="grid_line")
    # Creates all horizontal lines at intevals of 100
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


make_grid(the_canvas, 900, 900)  # draw the grid
the_canvas.mainloop()
