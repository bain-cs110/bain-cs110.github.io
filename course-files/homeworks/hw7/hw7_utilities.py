from tkinter import Canvas, messagebox

CORRECT_COLOR = "#6BA965"
PARTIAL_COLOR = "#C8B458"
WRONG_COLOR = "#787C7E"
DEFAULT_COLOR = "white"
KEY_PRESS = "<Key>"

__docformat__ = "google"

canvas = None

def make_grid(w, h):
    '''
    Makes a grid on a screen.

    Args:
        w (`int`): The width of the screen
        h (`int`): The height of the screen

    Returns:
      * `None`, draws to the screen
    '''
    interval = 100

    # Delete old grid if it exists:
    canvas.delete('grid_line')
    # Creates all vertical lines at intevals of 100
    for i in range(0, w, interval):
        canvas.create_line(i, 0, i, h, tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, interval):
        canvas.create_line(0, i, w, i, tag='grid_line')


def draw_letter_in_grid(letter, grid_coord, past_guess=False):
    '''
    Draws letters on a window in a particular grid coordinate.

    Args:
        letter (`str`): The letter we wish to draw on the canvas
        grid_coord (`tuple`): An x,y coordinate that says where to draw the letter
        past_guess (`bool`): If true, then this is a previous guess (otherwise current guess)

    Returns:
      * `None`, draws to the scren
    '''
    text_color = "black"
    if past_guess:
        text_color = "white"

    canvas.create_text(
        (grid_coord[0] * 100) + 50,
        (grid_coord[1] * 100) + 50,
        text=letter.upper(),
        anchor="center",
        font=("Purisa", 100),
        fill=text_color
    )


def game_over(happy = False):
    '''
    Ends the game.

    Args:
        happy (`bool`): If this is true, that means the user has won!

    Returns:
      * `None`, maybe shows a pop-up window and possibly stops listening for keyboard events.
    '''
    if happy:
        messagebox.showinfo("Congratulations",  "You've won!")
    canvas.unbind(KEY_PRESS)


def color_a_grid_square(color, grid_coord):
    '''
    Colors a particular grid square on a canvas.

    Args:
        color (`str`): The color to draw the square in
        grid_coord (`tuple`): The x,y coordinate of the square we wish to draw

    Returns:
      * `None`, draws to the screen.
    '''
    top_left = (grid_coord[0] * 100, grid_coord[1] * 100)
    bottom_right = (top_left[0] + 100, top_left[1] + 100)
    canvas.create_rectangle(
        top_left,
        bottom_right,
        fill=color
    )


def delete(shape):
    """
    A function that deletes a shape from our screen.

    Args:
        shape (`Shape` or Tag): The shape to delete.
    """
    canvas.delete(shape)

def setup_listener(event, handler_function):
    '''
    Sets up a listener for a given event on our window.
    
    Args:
        event (`str`): The magic string that represents this event in tkinter
        handler_function (`func`): The name (not a string though) of the function you want called when the event his heard.
    '''
    canvas.bind(event, handler_function)

def fix_file_path(file_path):
    """
    Only use this function if you're using an IDE that is NOT IDLE.

    Args:
        file_path (`str`): A path to a file you want to use.

    Returns:
        * An augmented file path (`str`) to fix issues with non-IDLE IDEs.
    """
    import os
    import sys
    dir_path = os.path.dirname(sys.argv[0])
    return os.path.join(dir_path, file_path)

def setup_window(some_canvas):
    """DO NOT USE THIS FUNCTION"""
    global canvas
    canvas = some_canvas
    canvas.pack()
    canvas.focus_set()
