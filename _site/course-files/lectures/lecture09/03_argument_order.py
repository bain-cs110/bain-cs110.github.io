from tkinter import Canvas, Tk

# initialize window
gui = Tk()
a_canvas = Canvas(gui, width=700, height=450, background='white')
a_canvas.pack()

def make_diamond(canvas, center:tuple, size:int, my_color='teal', border_width=5, border_color='black'):
    x = center[0]
    y = center[1]
    radius = size / 2
    canvas.create_polygon(
        [
            (x, y - radius), # top-most coordinate
            (x + radius, y), # right-most coordinate
            (x, y + radius), # bottom-most coordinate
            (x - radius, y)  # left-most coordinate
        ],
        fill=my_color,
        width=border_width,
        outline=border_color,
        activefill='hotpink',
        activeoutline='#999999'
    )

########################## YOUR CODE BELOW THIS LINE ##############################

# Positional arguments are REQUIRED, have to be in order, and come first
make_diamond(a_canvas, (100, 100), 50) # works
# make_diamond(a_canvas, (150, 150)) # won't work
make_diamond(a_canvas, (200, 200), 50, my_color="cyan") # works
# make_diamond(my_color="cyan", a_canvas, (250, 250), 50) # won't work

# Keyword arguments come AFTER positional and can be in any order
make_diamond(a_canvas, (300, 300), 50, my_color="cyan", border_width=10) # works
make_diamond(a_canvas, (75, 75), 25, border_color="blue", my_color="cyan") # works

########################## YOUR CODE ABOVE THIS LINE ##############################
a_canvas.mainloop()

# imagine a function like that looks like this…
