from tkinter import Canvas, Tk
# initialize window
gui = Tk()
the_canvas = Canvas(gui, width=600, height=300, background='white',
                scrollregion = "0 -300 300 0")
the_canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

def make_square(a_canvas, bottom_left_x, bottom_left_y, width, color="blue"):
    a_canvas.create_rectangle(
        bottom_left_x, 
        bottom_left_y,
        bottom_left_x + width,
        bottom_left_y + width,
        fill=color)

# Function Outline
# Name: make_pyramid
# Inputs:
#   1. a_canvas - something to draw our shape on
#   2. bottom_left_x - x-coordinate for bottom left (int)
#   3. bottom_left_y - y-coordinate for bottom left (int)
#   4. width - width of each individual square (int)
#   5. fill_color (optional) - defaults to 'green' (string)

def make_pyramid(a_canvas, bottom_left_x, bottom_left_y, width, fill_color="green"):
    # make bottom row
    make_square(a_canvas, bottom_left_x, bottom_left_y, width, color="green")
    make_square(a_canvas, bottom_left_x + width,
                bottom_left_y, width, color="green")
    make_square(a_canvas, bottom_left_x + width*2,
                bottom_left_y, width, color="green")



########################## YOUR CODE ABOVE THIS LINE ##############################
# helper function that draws a grid.
def make_grid(c, w, h):
    interval = 100

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
            
make_grid(the_canvas, 700, 700)
the_canvas.scale("all", 0, 0, 1, -1)
the_canvas.mainloop()
