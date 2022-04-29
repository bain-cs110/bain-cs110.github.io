from tkinter import Canvas, Tk
from helpers import make_circle

gui = Tk()
gui.title('Circles')
canvas = Canvas(gui, width=500, height=500, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

## One of many solutions
w = 80
inc = 4
counter = w
while counter > 0:
    make_circle(canvas, (250, 250+counter), counter/2, color=None)
    counter -= inc

counter = w
while counter > 0:
    make_circle(canvas, (250, 250-counter), counter/2, color=None)
    counter -= inc

counter = w
while counter > 0:
    make_circle(canvas, (250+counter, 250), counter/2, color=None)
    counter -= inc

counter = w
while counter > 0:
    make_circle(canvas, (250-counter, 250), counter/2, color=None)
    counter -= inc


########################## YOUR CODE ABOVE THIS LINE ############################## 
canvas.mainloop()