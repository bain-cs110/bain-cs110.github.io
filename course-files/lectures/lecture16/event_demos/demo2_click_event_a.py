'''
This demo shows you how you can create a new image by clicking the screen.
Documentation:
  * tkinter events: https://www.python-course.eu/tkinter_events_binds.php
  * Canvas: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas.html
  * Other Canvas methods: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas-methods.html
'''
from tkinter import Canvas, Tk
import p1_utilities

gui = Tk()
gui.title('Tour of options...')

# initialize canvas:
the_canvas = Canvas(gui, width=1000, height=1000, background='white')
the_canvas.pack()

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
the_canvas.bind(MOUSE_CLICK, do_something)  # add event handler

########################## YOUR CODE ABOVE THIS LINE ##############################

# makes sure the canvas keeps running:
the_canvas.mainloop()
