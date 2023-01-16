from tkinter import Canvas, Tk

# initialize window
gui = Tk()
the_canvas = Canvas(gui, width=700, height=350, background='white',
                scrollregion = "0 -350 700 0")
the_canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

### NOTE IF YOU RUN THIS AND DON'T SEE THE GRID LIKE ON THE VIDEO,
### GO TO THE TUTORIAL PAGE FOR THIS WEEK FOR SOME SOLUTIONS

# make an oval:
the_canvas.create_oval(
    50, 150,
    300, 250, # bottom left x-y, top right x-y
    fill='red',
    width=5
)

# make a polygon
the_canvas.create_polygon(
    370, 150,
    630, 150,
    500, 350,  # list of x-y pairs
    width=2,
    fill='#BCD39C',
    smooth=True)  # make smooth false for angular polygon

# make a line:
the_canvas.create_line(
    10, 0,
    210, 100,
    420, 0,
    630, 100,  # list of x-y pairs
    width=3)

# make an arc:
the_canvas.create_line(
      350, 50,
      430, 50,
      450, 200,  # list of x-y pairs
    width=5,
    fill='#0074D9',
    splinesteps=15,
    smooth=True)

# make line that looks like an arc:
the_canvas.create_arc(
    150, 50, 
    350, 350,
    width=5,
    style='arc',
    outline='#0074D9'
    )

# make a curvy line:
the_canvas.create_line(
    0,   100, 
    50,  150, 
    100, 100, 
    150, 150, 
    200, 100, 
    250, 150, 
    300, 100, 
    350, 150, 
    400, 100, 
    splinesteps=20,
    width=3, 
    smooth=True)

# make a rectangle
the_canvas.create_rectangle(
    500, 25,
    650, 75,  #  coords: top-left, bottom-right
    fill="#3D9970")

# make a label:
# Note, the font parameter accepts something
# called a *tuple* which a sequence of data we'll
# talk about in coming lectures.
the_canvas.create_text(
    210, 210, 
    text="Hello world!",
    font=('Times', '24', 'bold italic') ,
    anchor='nw'  # align to "northwest" corner
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
