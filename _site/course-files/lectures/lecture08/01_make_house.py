from tkinter import Canvas, Tk

# initialize window
gui = Tk()
canvas = Canvas(gui, width=700, height=350, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

# make a polygon

# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/create_polygon.html
canvas.create_polygon(
    [ (370, 150),  (630, 150), (500, 350) ],  # list of x-y pairs
    fill='#BCD39C'
)










########################## YOUR CODE ABOVE THIS LINE ##############################
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
canvas.mainloop()
