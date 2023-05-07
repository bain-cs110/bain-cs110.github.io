'''
Documentation:
  * tkinter events: https://www.python-course.eu/tkinter_events_binds.php
  * Canvas: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas.html
  * Other Canvas methods: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas-methods.html
'''
from tkinter import Canvas, Tk
import p1_utilities
import random
import time

gui = Tk()
gui.title('Lava Lamp')

# initialize canvas:
window_width = 800
window_height = 800
the_canvas = Canvas(gui, width=window_width,
                    height=window_height, background='white')
the_canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

MOUSE_DRAG = '<B1-Motion>'
MOUSE_CLICK = '<Button-1>'

