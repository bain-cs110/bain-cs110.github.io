from tkinter import Canvas, Tk
import mario_module
import utilities

gui = Tk()
gui.title('Keyboard Events')
canvas = Canvas(gui, width=500, height=500)
canvas.pack()

### NOTE: THE BELOW IS SUPER IMPORTANT FOR KEYBOARD EVENTS
canvas.focus_set()

########################## YOUR CODE BELOW THIS LINE ##############################

KEY_PRESS = '<Key>'
MOUSE_CLICK = '<Button-1>'

def select_mario(event):
    tag = utilities.get_tag_from_x_y_coordinate(canvas, event.x, event.y)
    print(tag)

def move_mario(event):
    print(event.keysym)
    utilities.update_position_by_tag(canvas, 'mario_0', x=10, y=0)

mario_module.make_mario(canvas, (0, 0), size=15, my_tag='mario_0')
mario_module.make_mario(canvas, (150, 200), size=10, version=2, my_tag='mario_1')

canvas.bind(KEY_PRESS, move_mario)
canvas.bind(MOUSE_CLICK, select_mario)

########################## YOUR CODE ABOVE THIS LINE ##############################

# makes sure the canvas keeps running:
canvas.mainloop()
