from tkinter import Canvas, Tk
import time
import shapes

cars_to_make = [
((0, 0),    "blue", "car_1"),
((100, 100),"green", "car_2"),
((200, 200),"yellow", "car_3"),
((100, 300),"red", "car_4")
]
gui = Tk()
gui.title('Animation')
canvas = Canvas(gui, width=500, height=500, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

# Challenge:
# 1. Turn the car code into a function, with a customizable
#    position, car_color, and car_tag.
#    Note that the “tag” parameter is useful so that you can refer to
#    the car later when you want to animate it.
# 2. Create all the cars in the cars_to_make list using a for loop
# 3. Animate each car differently using a while loop.

# make car with top left at (50, 20)
top_id    = shapes.make_rectangle(canvas, (100, 20), 100, 40, tag='car_1')
bottom_id = shapes.make_rectangle(canvas, (50, 50), 200, 45, tag='car_1')
wheel1_id = shapes.make_circle(canvas, (100, 100), 20, color='black', tag='car_1')
wheel2_id = shapes.make_circle(canvas, (200, 100), 20, color='black', tag='car_1')

# move car:
shapes.move(canvas, 'car_1', x=60, y=0)
gui.update()
time.sleep(1)

# move car again:
shapes.move(canvas, 'car_1', x=60, y=0)
gui.update()
time.sleep(1)

# move car again:
shapes.move(canvas, 'car_1', x=60, y=0)
gui.update()
time.sleep(1)

########################## YOUR CODE ABOVE THIS LINE ##############################
# makes sure the canvas keeps running:
canvas.mainloop()
