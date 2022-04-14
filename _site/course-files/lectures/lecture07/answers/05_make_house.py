from tkinter import Canvas, Tk

# initialize window
gui = Tk()
canvas = Canvas(gui, width=700, height=350, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################


def make_house(canvas:Canvas, bottom_left:tuple, height:int, fill_color:str="green"):

    list_of_points = []

    list_of_points.append(bottom_left)

    bottom_right_x = bottom_left[0] + height
    bottom_right_y = bottom_left[1]
    bottom_right = (bottom_right_x, bottom_right_y)
    list_of_points.append(bottom_right)

    top_right = (bottom_right_x, bottom_right_y - height)
    list_of_points.append(top_right)

    peak = (top_right[0] - (height / 2), top_right[1] - (height / 2))
    list_of_points.append(peak)

    top_left = (bottom_left[0], bottom_left[1] - height)
    list_of_points.append(top_left)

    canvas.create_polygon(
        list_of_points,
        fill=fill_color
    )

# Don't forget to actually call your function to draw the house!
make_house(canvas, (300, 300), 100, fill_color="red")
make_house(canvas, (150, 300), 100)
make_house(canvas, (450, 300), 100, fill_color="blue")



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
