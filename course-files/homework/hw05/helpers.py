from tkinter import Canvas, messagebox

CORRECT_COLOR = "#6BA965"
PARTIAL_COLOR = "#C8B458"
WRONG_COLOR = "#787C7E"
DEFAULT_COLOR = "white"
KEY_PRESS = "<Key>"


def make_grid(canvas, w, h):
    interval = 100

    # Delete old grid if it exists:
    canvas.delete('grid_line')
    # Creates all vertical lines at intevals of 100
    for i in range(0, w, interval):
        canvas.create_line(i, 0, i, h, tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, interval):
        canvas.create_line(0, i, w, i, tag='grid_line')


def draw_letter_in_grid(canvas: Canvas, letter: str, grid_coord: tuple, finalized: bool = False):
    text_color = "black"
    if finalized:
        text_color = "white"

    canvas.create_text(
        (grid_coord[0] * 100) + 50,
        (grid_coord[1] * 100) + 50,
        text=letter.upper(),
        anchor="center",
        font=("Purisa", 100),
        fill=text_color
    )


def game_over(canvas, happy: bool = False):
    if happy:
        messagebox.showinfo("Congratulations",  "You've won!")
    canvas.bind(KEY_PRESS, None)


def color_a_grid_square(canvas: Canvas, color: str, grid_coord: tuple):
    top_left = (grid_coord[0] * 100, grid_coord[1] * 100)
    bottom_right = (top_left[0] + 100, top_left[1] + 100)
    canvas.create_rectangle(
        top_left,
        bottom_right,
        fill=color
    )
