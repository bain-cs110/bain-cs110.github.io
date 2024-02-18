from tkinter import Canvas, Tk
from p1_utilities import *
import time
gui = Tk()
gui.title('Project 1')
# initialize canvas:
window_width = 800 
# gui.winfo_screenwidth() # you can use this if you want the canvas to be as wide as the screen
window_height = 800 
# gui.winfo_screenheight() # you can use this if you want the canvas to be as tall as the screen
the_canvas = Canvas(gui, width=window_width, height=window_height, background='white')
setup_shapes(the_canvas)
the_canvas.pack()
ticks_per_second = None
ticks = 0
########################## YOUR CODE BELOW THIS LINE ##############################

### MAKE CREATURE SECTION (put your function defs here ) ##########################
# Here's a delightful smiley face as an example (feel free to delete it)


def creature(center, size=100, tag='', primary_color='lightgray', secondary_color="green"):
 
    face = circle(center, radius=size, color="yellow", tag=tag) #face

    left_eye = oval(radius_x=size / 5, radius_y=size / 3.333, color="red", tag=tag) #left eye
    right_eye = oval(radius_x=size / 5, radius_y=size / 3.333, color="green", tag=tag) # right eye
    mouth = oval(radius_x= size / 2.5, radius_y=size / 10, color="blue", tag=tag) # mouth

    overlay(left_eye, face, offset_x=-size / 3.333, offset_y=-size / 20)
    overlay(right_eye, face, offset_x=size / 3.333, offset_y=-size / 20)
    overlay(mouth, face, offset_y=size/2)



####################################################################################


### MAKE LANDSCAPE OBJECT SECTION (put your function defs here ) ###################
# Note: if you're going to use shapes that ALSO were part of your creature, no need
# to copy those function definitions twice!





####################################################################################

## EVENT HANDLERS HERE ##############################################################

# feel free to delete these examples
square_counter = 0
def click_handle(event):
    global square_counter
    new_tag = "square_" + str(square_counter)
    square(top_left=(event.x, event.y), size=100, color='pink', tag=new_tag)
    square_counter = square_counter + 1
    print("Drawing square..." + new_tag)


####################################################################################

## Initial Terrarium Setup Here ####################################################
def setup():
    ## Put all your creature and landscape and other stuff that only needs to run
    #   once in this function!
    creature((400, 400), primary_color='white', tag="test")
    
    ## Setting some listeners!
    setup_listener('<Button-1>', click_handle)

    # This is how many animations to attempt per second. If you want to slow down your
    #   animations, just decrease this number! If you want to speed up...
    global ticks_per_second
    ticks_per_second = 30

####################################################################################

## ANIMATION GO FUNCTION HERE ####################################################
def go():
    # Here's where you'll put everything you want to control your animations
    #   EXCEPT event listeners (look higher up)
    move("test", x_shift=2, y_shift=-2)


######&&!*#################### YOUR CODE ABOVE THIS LINE ##############################

## DO NOT MODIFY THIS STUFF
setup()
while True:
    go()
    gui.update()
    time.sleep(1 / ticks_per_second)
    ticks = ticks + 1
