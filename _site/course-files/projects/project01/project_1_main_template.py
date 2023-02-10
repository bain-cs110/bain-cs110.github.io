from tkinter import Canvas, Tk
import project_utilities
import time
gui = Tk()
gui.title('My Terrarium')

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
the_canvas = Canvas(gui, width=1000, height=1000, background='white')
the_canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

### MAKE CREATURE SECTION (put your function defs here ) ##########################
def make_creature(canvas, center, size=100, my_tag='creature', primary_color='lightgray', secondary_color="green"):
    radius = size / 2
    # just a demo of how you might think about making your creature:
    left_eye_pos = (center[0] - radius / 4, center[1] - radius / 5)
    right_eye_pos = (center[0] + radius / 4, center[1] - radius / 5)
    eye_width = radius / 10
    eye_height = radius / 10

    project_utilities.make_circle(canvas, center, radius,
                          fill_color=primary_color, tag=my_tag)
    project_utilities.make_oval(canvas, left_eye_pos, eye_width,
                        eye_height, fill_color="red", tag=my_tag)
    project_utilities.make_oval(canvas, right_eye_pos, eye_width,
                        eye_height, fill_color="green", tag=my_tag)
    project_utilities.make_line(canvas, [
        (center[0] - radius / 2, center[1] + radius / 3),
        (center[0], center[1] + radius / 1.2),
        (center[0] + radius / 2, center[1] + radius / 3)
    ], curvy=True, tag=my_tag)
####################################################################################


### MAKE LANDSCAPE OBJECT SECTION (put your function defs here ) ###################
# Note: if you're going to use shapes that ALSO were part of your creature, no need
# to copy those function definitions twice!


####################################################################################

## EVENT HANDLERS HERE ##############################################################

counter = 0
def click_handle(event):
    global counter
    new_tag = "square_" + str(counter)
    project_utilities.make_square(
        the_canvas, (event.x, event.y), 100, fill_color='pink', tag=new_tag)
    counter = counter + 1

def double_click_handle(event):
    print(event)
    print(project_utilities.get_tag_from_event(the_canvas, event))

the_canvas.bind('<Button-1>', click_handle)
the_canvas.bind('<Button-2>', double_click_handle)

####################################################################################


## Initial Terarium Setup Here ####################################################

# sample code to make a creature:
make_creature(the_canvas, (400, 400), primary_color='white', my_tag="test")




####################################################################################

## ANIMATION LOOP HERE ####################################################
# Note, you will only have ONE animation loop

while True:
    project_utilities.update_position(the_canvas, "test", x=2, y=-2)
    project_utilities.flip(the_canvas, "test")
    #print("top:", project_utilities.get_top(the_canvas, "test"))
    #print("bottom:", project_utilities.get_top(the_canvas, "test"))
    gui.update()
    time.sleep(0.1)


########################## YOUR CODE ABOVE THIS LINE ##############################

# makes sure the canvas keeps running:
the_canvas.mainloop()
