from tkinter import Canvas, Tk
import random
import time
import creature
import utilities
import math

gui = Tk()
gui.title('Circle')
canvas = Canvas(gui, width=500, height=500)
canvas.pack()
canvas.focus_set()

########################## YOUR CODE BELOW THIS LINE ##############################
KEY_PRESS = '<Key>'

def move_creature(event):
    print(event.keysym)

creature.make_creature(canvas, (200, 200), size=150, my_tag='creature_1', my_fill='white')


canvas.bind(KEY_PRESS, move_creature)

########################## YOUR CODE ABOVE THIS LINE ##############################

# makes sure the canvas keeps running:
canvas.mainloop()
