from tkinter import Canvas, Tk
import mario_module

gui = Tk()
gui.title('Mouse Events')
the_canvas = Canvas(gui, width=500, height=500)
the_canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################
MOUSE_CLICK = '<Button-1>'
MOUSE_DRAG = '<B1-Motion>'

# note that I'm assigning each goomba a unique tag. It's also important to note,
# that if we go look at the mario module (which is imported above), it's using the shape
# functions from the utilities module (also imported above). If we look at say,
# `make_square`, you'll see it too takes a "tag" as input. This is important because every
# single square in our drawing HAS TO HAVE THE SAME TAG, otherwise, Python won't know it's one
# continuous shape.
mario_module.make_goomba(the_canvas, (0, 0), size=15, my_tag='goomba_0')
mario_module.make_goomba(the_canvas, (300, 200), size=10, my_tag='goomba_1')

def add_new_goomba(event):
    print(event.x, event.y)

the_canvas.bind(MOUSE_CLICK, add_new_goomba)

########################## YOUR CODE ABOVE THIS LINE ##############################

# makes sure the canvas keeps running:
the_canvas.mainloop()
