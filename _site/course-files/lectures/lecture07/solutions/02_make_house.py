from tkinter import Canvas, Tk
# initialize window
gui = Tk()
the_canvas = Canvas(gui, width=300, height=300, background='white',
                scrollregion = "0 -300 300 0")
the_canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################s

def make_square(a_canvas, bottom_left_x, bottom_left_y, width, color="blue"):
    a_canvas.create_rectangle(
        bottom_left_x, 
        bottom_left_y,
        bottom_left_x + width,
        bottom_left_y + width,
        fill=color)

def make_house(a_canvas, bottom_left_x, bottom_left_y, height, fill_color="green"):
    make_square(a_canvas, bottom_left_x, bottom_left_y, height, color=fill_color)

    tri_1_x = bottom_left_x
    tri_1_y = bottom_left_y + height

    tri_top_x = bottom_left_x + (height / 2)
    tri_top_y = bottom_left_y + height + (height / 2)

    tri_2_x = bottom_left_x + height
    tri_2_y = bottom_left_y + height

    a_canvas.create_polygon(
        tri_1_x, tri_1_y,
        tri_top_x, tri_top_y,
        tri_2_x, tri_2_y,
        fill=fill_color)

make_house(the_canvas, 100, 100, 100, "cyan")
        


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
