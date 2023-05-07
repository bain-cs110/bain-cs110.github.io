'''
Documentation:
  * tkinter events: https://www.python-course.eu/tkinter_events_binds.php
  * Canvas: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas.html
  * Other Canvas methods: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas-methods.html
'''
import tkinter
import p1_utilities
import time

gui = tkinter.Tk()
gui.title('Rotation Example')
w = h = 300

canvas = tkinter.Canvas(gui, width=w, height=h, background='white')
canvas.pack()

p1_utilities.make_car(canvas, (150, 150), my_tag='c1')

while True:
    gui.update()
    time.sleep(0.02)
    p1_utilities.rotate(canvas, 'c1', degrees=1, origin=(150, 150))
    gui.update()

