'''
This demo shows you how you can create a new image by clicking the screen.
Important: In order for this to work, you'll need to install pillow using PIP:

From your command line, type: pip3 install pillow

If you're not comfortable with the command line, you can run the file in this folder
named install_python_packages.py and when it asks, type pillow and hit enter.
'''

from tkinter import Canvas, Tk
import helpers
import utilities
import time
import random

gui = Tk()
gui.title('Tour of options...')

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
canvas = Canvas(gui, width=window_width, height=window_height, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

utilities.make_image(
    canvas,
    'images/landscape2.jpg',
    position=(0, 0),
    scale=0.7, # 70% of original
    anchor="nw",
    tag="bgimage"
)

########################## YOUR CODE ABOVE THIS LINE ##############################
# makes sure the canvas keeps running:
canvas.mainloop()
