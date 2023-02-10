'''
This demo shows you how you can change an image using a time-based event.
Documentation:
  * tkinter events: https://www.python-course.eu/tkinter_events_binds.php
  * Canvas: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas.html
  * Other Canvas methods: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas-methods.html
'''
from tkinter import Canvas, Tk
import project_utilities
import time

gui = Tk()
gui.title('Tour of options...')

# initialize canvas:
window_width = 1000
window_height = 1000

the_canvas = Canvas(gui, width=window_width,
                    height=window_height, background='white')
the_canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

def make_square_face(a_canvas, center, width, my_tag=""):
    big_square_width = width
    center_x = center[0]
    center_y = center[1]
    project_utilities.make_square(a_canvas, (center_x - width / 2,
       center_y - width / 2), width, fill_color="green", tag=my_tag)
    project_utilities.make_square(a_canvas, (center_x - width / 3, center_y - width / 6),
       big_square_width / 6, fill_color="purple", tag=my_tag)  # left eye
    project_utilities.make_square(a_canvas, (center_x + width / 6, center_y - width / 6),
       big_square_width / 6, fill_color="white", tag=my_tag)  # right eye
    project_utilities.make_square(a_canvas, (center_x - width / 60, center_y +
        width / 60), width / 30, fill_color="white", tag=my_tag)  # nose
   

# First draw our square face
make_square_face(the_canvas, (250, 250), 50, my_tag="test_creature")
gui.update()

# Wait five seconds and then turn the creature yellow:
time.sleep(5)
project_utilities.update_fill(the_canvas, 'test_creature', color='yellow')

# then update the screen
gui.update()

########################## YOUR CODE ABOVE THIS LINE ##############################
# makes sure the canvas keeps running:
the_canvas.mainloop()
