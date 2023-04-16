from tkinter import Canvas, Tk
import random
gui = Tk()
gui.title('Shapes')
the_canvas = Canvas(gui, width=500, height=500, background='white',
                    scrollregion="0 -500 500 0")
the_canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################
def make_random_oval(canvas):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    
    x_radius = random.randint(10, 100)
    y_radius = random.randint(10, 100)
    
    canvas.create_oval(
        x - x_radius, y - y_radius,
        x + x_radius, y + y_radius
        fill="green"
    )

make_random_oval(the_canvas)
make_random_oval(the_canvas)
make_random_oval(the_canvas)
make_random_oval(the_canvas)
make_random_oval(the_canvas)
make_random_oval(the_canvas)

########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
the_canvas.scale("all", 0, 0, 1, -1)
the_canvas.mainloop()
the_canvas.mainloop()