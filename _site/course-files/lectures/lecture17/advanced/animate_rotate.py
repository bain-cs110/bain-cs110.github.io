'''
Documentation:
  * tkinter events: https://www.python-course.eu/tkinter_events_binds.php
  * Canvas: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas.html
  * Other Canvas methods: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas-methods.html
'''
import tkinter
import utilities
import time

gui = tkinter.Tk()
gui.title('Tour of options...')
w = h = 300

canvas = tkinter.Canvas(gui, width=w, height=h, background='white')
canvas.pack()

# my make creature function
def make_creature(canvas, center, size=100, my_tag='creature', my_fill='hotpink'):
    left_eye_pos = (center[0] - size / 4, center[1] - size / 5)
    right_eye_pos = (center[0] + size / 4, center[1] - size / 5)
    eye_width = eye_height = size / 10


    ## Special Note: this rotate function doesn't work on circles and ovals so instead use
    ## the make_poly_circle and make_poly_oval functions to make your circles and ovals. these
    ## approximate the shape of a circle and oval by using a many sided polygon.

    utilities.make_poly_circle(canvas, center, size, fill_color=my_fill, tag=my_tag)
    utilities.make_poly_oval(canvas, left_eye_pos, eye_width, eye_height, fill_color='black', tag=my_tag)
    utilities.make_poly_oval(canvas, right_eye_pos, eye_width, eye_height, fill_color='black', tag=my_tag)
    utilities.make_line(canvas, [
        (center[0] - size / 2, center[1] + size / 3),
        (center[0], center[1] + size / 1.2),
        (center[0] + size / 2, center[1] + size / 3)
    ], curvy=True, tag=my_tag)

make_creature(canvas, (150, 150), my_tag='c1')

while True:
    gui.update()
    time.sleep(0.02)
    utilities.rotate(canvas, 'c1', degrees=1, origin=(150, 150))
    gui.update()
gui.mainloop()
