from tkinter import Canvas

mario_0 = [
(0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0),
(0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0),
(0, 0, 0, 0, 3, 3, 3, 4, 4, 5, 4, 0, 0, 0, 0, 0),
(0, 0, 0, 3, 4, 3, 4, 4, 4, 5, 4, 4, 4, 0, 0, 0),
(0, 0, 0, 3, 4, 3, 3, 4, 4, 4, 5, 4, 4, 4, 0, 0),
(0, 0, 0, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 0, 0, 0),
(0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0),
(0, 0, 2, 2, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 0, 0),
(4, 4, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 4, 4, 4, 0),
(4, 4, 4, 0, 2, 2, 1, 6, 1, 1, 1, 2, 2, 4, 4, 0),
(4, 4, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 3, 0, 0),
(0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 0, 0),
(0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 0, 0),
(0, 3, 3, 1, 1, 1, 0, 0, 0, 1, 1, 1, 3, 3, 0, 0),
(0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
]

mario_1 = [
(0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0),
(0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0),
(0, 0, 0, 0, 3, 3, 3, 4, 4, 5, 4, 0, 0, 0, 0, 0),
(0, 0, 0, 3, 4, 3, 4, 4, 4, 5, 4, 4, 4, 0, 0, 0),
(0, 0, 0, 3, 4, 3, 3, 4, 4, 4, 5, 4, 4, 4, 0, 0),
(0, 0, 0, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 0, 0, 0),
(0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0),
(0, 0, 0, 0, 2, 2, 1, 2, 2, 2, 0, 0, 0, 0, 0, 0),
(0, 0, 0, 2, 2, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 0),
(0, 0, 0, 2, 2, 2, 1, 1, 6, 2, 2, 4, 0, 0, 0, 0),
(0, 0, 0, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0),
(0, 0, 0, 1, 2, 2, 4, 4, 4, 1, 1, 1, 0, 0, 0, 0),
(0, 0, 0, 0, 1, 2, 4, 4, 1, 1, 1, 0, 0, 0, 0, 0),
(0, 0, 0, 0, 0, 1, 1, 1, 3, 3, 3, 0, 0, 0, 0, 0),
(0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0),
(0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0)
]


mario_2 = [
(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0),
(0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0),
(0, 0, 0, 0, 3, 3, 3, 4, 4, 5, 4, 0, 0, 0, 0, 0),
(0, 0, 0, 3, 4, 3, 4, 4, 4, 5, 4, 4, 4, 0, 0, 0),
(0, 0, 0, 3, 4, 3, 3, 4, 4, 4, 5, 4, 4, 4, 0, 0),
(0, 0, 0, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 0, 0, 0),
(0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0),
(0, 0, 0, 0, 2, 2, 2, 2, 1, 2, 0, 4, 0, 0, 0, 0),
(0, 0, 0, 4, 2, 2, 2, 2, 2, 2, 4, 4, 4, 0, 0, 0),
(0, 0, 4, 4, 1, 2, 2, 2, 2, 2, 4, 4, 0, 0, 0, 0),
(0, 0, 3, 3, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0),
(0, 0, 3, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0),
(0, 3, 3, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0),
(0, 3, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0),
(0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0)
]

def draw_row(canvas:Canvas, row:tuple, top_left:tuple, colors:list, pixel:int=25, tag=""):
    x = top_left[0]
    y = top_left[1]
    for cell in row:
        if cell != 0:
            make_square(canvas, (x, y), pixel, fill_color=colors[cell], tag=tag)
        x += pixel

def draw_pixel_art(canvas:Canvas, top_left:tuple, artwork:list, palette:list, pixel:int=10, tag=""):
    x = top_left[0]
    y = top_left[1]
    for row in artwork:
        # draw each row at the specified (x, y) position:
        draw_row(canvas, row, (x, y), colors=palette, pixel=pixel, tag=tag)

        # ...and don't forget to shift the y-value down by the proper
        #  amount so that the next row won't draw on top of the first one:
        y += pixel

def make_square(canvas: Canvas, top_left: tuple, width: int, fill_color: str='#84A9C0', outline_color='#DDD', tag=""):
    canvas.create_rectangle([
            top_left,  # top_left
            (top_left[0] + width, top_left[1] + width)  # bottom_right
        ],
        fill=fill_color,
        outline=outline_color,
        tag=tag
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
                    fill='black'
                    )
                    c.create_text(
                    x + offset,
                    y + offset,
                    text="({0}, {1})".format(x, y),
                    anchor="nw",
                    font=("Purisa", 8)
                    )
