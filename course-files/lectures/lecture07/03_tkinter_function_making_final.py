from tkinter import Canvas, Tk

# initialize window
gui = Tk()
the_canvas = Canvas(gui, width=700, height=350, background='white',
                    scrollregion = "0 -350 700 0")
the_canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

### NOTE IF YOU RUN THIS AND DON'T SEE THE GRID LIKE ON THE VIDEO,
### GO TO THE TUTORIAL PAGE FOR THIS WEEK FOR SOME SOLUTIONS

# Name: draw_circle
# Inputs:
# 0. a_canvas (the thing to draw on)
# 1. center_x
# 2. center_y
# 3. radius
# 4. fill_color
def draw_circle(a_canvas, center_x, center_y, radius, fill_color="yellow"):
    bottom_left_x = center_x - radius
    bottom_left_y = center_y - radius

    top_left_x = center_x + radius
    top_left_y = center_y + radius

    # make an oval:
    a_canvas.create_oval(
        bottom_left_x, bottom_left_y,  # bottom left x-y
        top_left_x, top_left_y, # top right x-y
        fill=fill_color
    )      

draw_circle(the_canvas, 300, 150, 150, fill_color="green")
draw_circle(the_canvas, 50, 150, 25, fill_color="purple")
draw_circle(the_canvas, 450, 150, 25, fill_color="red")



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
