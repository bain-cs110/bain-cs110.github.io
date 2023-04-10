from tkinter import Canvas, Tk

# initialize window
gui = Tk()
the_canvas = Canvas(gui, width=700, height=350, background='white',
                    scrollregion = "0 -350 700 0")
the_canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

# make an oval:
the_canvas.create_oval(
    50, 150,  # bottom left x-y
    300, 250, # top right x-y
    fill='red',
)

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
            
make_grid(the_canvas, 700, 350)

the_canvas.scale("all", 0, 0, 1, -1)
the_canvas.mainloop()
