from tkinter import Canvas, Tk
from helpers import make_circle

gui = Tk()
gui.title('Circles')
canvas = Canvas(gui, width=500, height=500, background='#000022')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

## One of many solutions
counter = 150
while counter > 0:
    make_circle(canvas, (250, 250), counter)
    counter -= 25


########################## YOUR CODE ABOVE THIS LINE ############################## 
canvas.mainloop()