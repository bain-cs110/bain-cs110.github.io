from tkinter import Canvas, Tk

# initialize window
gui = Tk()
canvas = Canvas(gui, width=700, height=350, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

# make a label:
canvas.create_text(
    (210, 210),
    text="Hello world!",
    font=("Purisa", 32),
    anchor='nw'  # align to "northwest" corner
)

# make an oval:
canvas.create_oval(
    [ (50, 150),  (150, 250) ], # top left x-y, bottom right x-y
    fill='#FF4136',
    width=5
)

# make a polygon
canvas.create_polygon(
    [ (370, 150),  (630, 150), (500, 350) ],  # list of x-y pairs
    width=2,
    fill='#BCD39C',
    smooth=True)  #make smooth false for angular polygon

# make a line:
canvas.create_line(
    [ (10, 0),  (210, 100),  (420, 0),  (630, 100) ],  # list of x-y pairs
    width=3)

# make a dashed line:
canvas.create_line(
    [ (10, 100),  (210, 0),  (420, 100),  (630, 10) ],
    fill="#3D9970",
    dash=(4, 4),
    width=3)

# make a curvy line:
canvas.create_line(
    [
        (0,   100),
        (50,  150),
        (100, 100),
        (150, 150),
        (200, 100),
        (250, 150),
        (300, 100),
        (350, 150),
        (400, 100)
    ],
    splinesteps=20,
    width=3,
    smooth=True)

# make a rectangle
canvas.create_rectangle(
    [ (500, 25), (650, 75) ],  #  coords: top-left, bottom-right
    fill="#3D9970")



### Create a grid
interval = 100

# Delete old grid if it exists:
canvas.delete('grid_line')
# Creates all vertical lines at intevals of 100
for i in range(0, 700, interval):
    canvas.create_line(i, 0, i, 350, tag='grid_line')

# Creates all horizontal lines at intevals of 100
for i in range(0, 350, interval):
    canvas.create_line(0, i, 700, i, tag='grid_line')

# Creates axis labels
offset = 2
for y in range(0, 350, interval):
    for x in range(0, 750, interval):
        canvas.create_oval(
            x - offset,
            y - offset,
            x + offset,
            y + offset,
            fill='black'
        )
        canvas.create_text(
            x + offset,
            y + offset,
            text="({0}, {1})".format(x, y),
            anchor="nw",
            font=("Purisa", 8)
        )

########################## YOUR CODE ABOVE THIS LINE ##############################
canvas.mainloop()
