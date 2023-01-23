from tkinter import Canvas, Tk
import random
gui = Tk()
gui.title('Shapes')
the_canvas = Canvas(gui, width=500, height=500, background='white',
                    scrollregion="0 -500 500 0")
the_canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################
palette = ('royalblue', 'cornflowerblue', 'lightsteelblue', 'mistyrose', 'lightsalmon', 'tomato')

def make_random_oval(canvas):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    
    x_radius = random.randint(10, 100)
    y_radius = random.randint(10, 100)
    
    bottom_left = (x - x_radius, y - y_radius)
    top_right = (x + x_radius, y + y_radius)
    
    canvas.create_oval(
        bottom_left,
        top_right, 
        fill=random.choice(palette)
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
