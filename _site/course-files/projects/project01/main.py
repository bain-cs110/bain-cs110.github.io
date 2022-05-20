from tkinter import Canvas, Tk
import utilities
import time
import random

import creature
import landscape

gui = Tk()
gui.title('My Terrarium')

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
canvas = Canvas(gui, width=window_width,
                height=window_height, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

# sample code to make a creature:
creature.make_creature(canvas, (400, 400), my_fill='white', my_tag="test")

print(utilities.get_center(canvas, "test"))

def click_handle(event):
    creature.make_creature(canvas, (100, 100), my_fill='white', my_tag="test")

canvas.bind('<Button-1>', click_handle)

########################## YOUR CODE ABOVE THIS LINE ##############################

# makes sure the canvas keeps running:
canvas.mainloop()
