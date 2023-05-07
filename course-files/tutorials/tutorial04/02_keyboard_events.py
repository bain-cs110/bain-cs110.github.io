from tkinter import Canvas, Tk
import mario_module
import p1_utilities

gui = Tk()
gui.title('Keyboard Events')
the_canvas = Canvas(gui, width=500, height=500)
the_canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

KEY_PRESS = '<Key>'
MOUSE_CLICK = '<Button-1>'

def select_mario(event):
    tag = p1_utilities.get_tag_from_event(the_canvas, event)
    print(tag)

def move_mario(event):
    print(event.keysym)
    p1_utilities.update_position(the_canvas, 'mario_0', x=10, y=0)

mario_module.make_mario(the_canvas, (0, 0), size=15, my_tag='mario_0')
mario_module.make_mario(the_canvas, (150, 200), size=10, version=2, my_tag='mario_1')

the_canvas.bind(KEY_PRESS, move_mario)
the_canvas.bind(MOUSE_CLICK, select_mario)

########################## YOUR CODE ABOVE THIS LINE ##############################

# makes sure the canvas keeps running:
the_canvas.mainloop()
