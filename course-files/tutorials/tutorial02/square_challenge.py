from tkinter import Canvas, Tk
import helpers

# initialize window
gui = Tk()
canvas = Canvas(gui, width=300, height=300, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################


### YOUR FUNCTION CODE WILL GO RIGHT HERE

# Here's a reminder of how Tkinter draws rectangles. What your goal is to create a function
# that will use this code...but allow you to specifically create squares by inputting a
# series of specific inputs described on the assignment page.
canvas.create_rectangle([
        (100, 100),  # top_left
        (200, 200)  # bottom_right
    ],
    fill='#84A9C0'
)

# helper function that draws a grid.
helpers.make_grid(canvas, 300, 300)

########################## YOUR CODE ABOVE THIS LINE ##############################
canvas.mainloop()
