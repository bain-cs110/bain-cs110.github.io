'''
This demo shows you how you can create a new image by clicking the screen.
Documentation: 
  * tkinter events: https://www.python-course.eu/tkinter_events_binds.php
  * Canvas: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas.html
  * Other Canvas methods: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas-methods.html
'''
from tkinter import Canvas, Tk
import helpers
import utilities
import time
import random

gui = Tk()
gui.title('Tour of options...')

# initialize canvas:

canvas = Canvas(gui, width=600, height=600, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

MOUSE_CLICK = '<Button-1>'

def do_something(event):
    print("You clicked...", MOUSE_CLICK)
    print("And told me to run do_something when I heard that")
    print(event)
    print(event.x, event.y)


# Notice first we define our function called do_something
# then we tell the canvas to listen for MOUSE_CLICKs and if
# it hears one, do_something
canvas.bind(MOUSE_CLICK, do_something)  # add event handler

########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()
