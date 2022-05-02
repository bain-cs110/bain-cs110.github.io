from tkinter import Canvas, Tk
import time
import shapes
import utilities

gui = Tk()
gui.title('Animation')
canvas = Canvas(gui, width=1000, height=500, background='light blue')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

# TODO: the code below to make clouds is repetitive. Replace it with a loop to make
# at least 10 clouds that fill the top part of the canvas. Hints:
#   a) use a loop
#   b) use the random module, and in particular the random.randint or function to
#      to give each cloud a random (x, y) position and a random width.

shapes.make_cloud(canvas, (400,50))
shapes.make_cloud(canvas, (200,75))
shapes.make_cloud(canvas, (800,127))
shapes.make_cloud(canvas, (123,88))

# TODO: The code below to move the car is also repetitve. You have three tasks:
#  1. Use a loop to animate the car across the screen using the update_position
#     function.
#  2. When the left edge of the car "leaves" the right edge of the canvas,
#     make a new car that looks the same at the left edge of the canvas.
#  3. Repeat this process for a new car but make it a new color!

# draw car (and give it a unique tag 'car1')
shapes.make_car(canvas, top_left=(0, 250), tag='car1')

# move shapes that have the tag 'car1' 50 pixels to the right:
time.sleep(1)
utilities.update_position(canvas, 'car1', x=50, y=0)
print("Left side", utilities.get_left(canvas, 'car1')) # Note, this is JUST for debugging
gui.update()

# move shapes that have the tag 'car1' 50 pixels to the right (exact same code):
time.sleep(1)
utilities.update_position(canvas, 'car1', x=50, y=0)
print("Left side", utilities.get_left(canvas, 'car1')) # Note, this is JUST for debugging
gui.update()

# move shapes that have the tag 'car1' 50 pixels to the right (exact same code):
time.sleep(1)
utilities.update_position(canvas, 'car1', x=50, y=0)
gui.update()

########################## YOUR CODE ABOVE THIS LINE ##############################
# makes sure the canvas keeps running:
canvas.mainloop()
