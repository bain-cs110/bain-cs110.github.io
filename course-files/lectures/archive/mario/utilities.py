from tkinter import Canvas

def make_square(canvas: Canvas, bottom_left: tuple, width: int, color: str='#84A9C0', outline_color='#DDD', tag=""):
    canvas.create_rectangle([
            bottom_left,
            (bottom_left[0] + width, bottom_left[1] + width)  # bottom_right
        ],
        fill=color,
        outline=outline_color
    )

def make_grid(c, w, h):
    interval = 100
    # Delete old grid if it exists:
    c.delete('grid_line')
    # Creates all vertical lines at intevals of 100
    for i in range(0, w, interval):
        c.create_line(i, 0, i, h, tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, interval):
        c.create_line(0, i, w, i, tag='grid_line')

    # Creates axis labels
    offset = 2
    for y in range(0, h, interval):
        for x in range(0, w, interval):
            c.create_oval(
                x - offset,
                y - offset,
                x + offset,
                y + offset,
                fill='black',
                tags='grid_line'
            )
            c.create_text(
                x + offset,
                y + offset,
                text="({0}, {1})".format(x, y),
                anchor="nw",
                font=("Purisa", 8),
                tags='grid_line'
            )
