from tkinter import Canvas, Tk

# initialize window
gui = Tk()
canvas = Canvas(gui, width=700, height=450, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################
def make_square(canvas: Canvas, top_left: tuple, width: int, fill_color: str='#84A9C0'):
    canvas.create_rectangle([
            top_left,  # top_left
            (top_left[0] + width, top_left[1] + width)  # bottom_right
        ],
        fill=fill_color
    )

def make_triangle_left(canvas: Canvas, bottom_left: tuple, height: int, fill_color: str='#84A9C0'):
    canvas.create_polygon([
            bottom_left,
            (bottom_left[0], bottom_left[1] - height),
            (bottom_left[0] + height, bottom_left[1])
        ],
        fill=fill_color
    )

def make_triangle_right(canvas: Canvas, bottom_right: tuple, height: int, fill_color: str='#84A9C0'):
    canvas.create_polygon([
            bottom_right,
            (bottom_right[0], bottom_right[1] - height),
            (bottom_right[0] - height, bottom_right[1])
        ],
        fill=fill_color
    )

def make_house(canvas: Canvas, bottom_left: tuple, height: int, fill: str='#84A9C0'):
    make_square(canvas, (bottom_left[0], bottom_left[1] - height), height, fill_color=fill)
    make_triangle_left(canvas, (bottom_left[0] + (height / 2), bottom_left[1] - height), height / 1.5, fill_color=fill)
    make_triangle_right(canvas, (bottom_left[0] + (height / 2), bottom_left[1] - height), height / 1.5, fill_color=fill)


make_house(canvas, (400, 400), 100, fill="green")

make_house(canvas, (200, 400), 50, fill="yellow")

########################## YOUR CODE ABOVE THIS LINE ##############################
canvas.mainloop()
