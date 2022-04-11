'''
Documentation: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas.html
Color Picker: https://coolors.co/
'''
from tkinter import Canvas, Tk
from helpers import make_grid       # import the make_grid function (for debugging)

gui = Tk()
gui.title('Shapes')
canvas = Canvas(gui, width=500, height=500, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

# Your tasks: modify the function bodies of the following 4 function definitions:
#  1. make_oval (Exercise 1)
#  2. make_circle (Exercise 2)
#  3. make_bullseye (Exercise 3)
#  4. make_face (Exercise 4)

########################
# FUNCTION DEFINITIONS #
########################
def make_oval(canvas: Canvas, center: tuple, radius_x: float, radius_y: float, fill_color: str='hotpink'):
    # Exercise 1: currently, this function creates a hard-coded oval with a top-left
    # coordinate of (100, 100), and a bottom-right coordinate of (200, 150).
    #
    # Your job is to modify the code so that:
    # 1. the top-left (x, y) and bottom-right (x, y) coordinates are
    #    calculated  based on the radius_x, radius_y and center point
    #    specified by the arguments.
    # 2. the fill color is determined based on the color argument.
    canvas.create_oval(
        [
            (100, 100),
            (200, 150)
        ],
        fill='hotpink')



def make_circle(canvas: Canvas, center: tuple, radius: int, fill_color: str='hotpink'):
    # Exercise 2: currently, this function creates a hard-coded circle with a top-left
    # coordinate of (300, 100), and a bottom-right coordinate of (400, 200).
    #
    # Your job is  to modify the code so that:
    # 1.  the top-left (x, y) and bottom-right (x, y) coordinates are
    #     calculated based on the radius and center point specified
    #     by arguments.
    # 2.  the fill color is  determined by the color argument.
    #
    # HINT: complete this taks by calling (or "invoking") the
    #       make_oval function that you just made in Exercise 1.

    canvas.create_oval(
        [
            (300, 100),
            (400, 200)
        ],
        fill='hotpink')


## your make_bullseye fuction will go here

## your make_face function will go here

## SEE THE ASSIGNMENT DESCRIPTION FOR TEST SHAPES!

#####################################

# for measuring (optional):
make_grid(canvas, 500, 500)




########################## YOUR CODE ABOVE THIS LINE ##############################
# makes sure the canvas keeps running:
canvas.mainloop()
