from tkinter import Canvas, Tk
import time
import utilities

gui = Tk()
gui.title('Animation')
the_canvas = Canvas(gui, width=1000, height=1000, background='light blue',
                    scrollregion="0 -1000 1000 0")
the_canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

utilities.make_cloud(the_canvas, (400, 900))
utilities.make_cloud(the_canvas, (700, 850))
utilities.make_cloud(the_canvas, (800, 900))
utilities.make_cloud(the_canvas, (123, 850))
####### YOUR CREATURE DEFINITION GOES HERE ############










####### YOUR CREATURE DEFINITION GOES ABOVE HERE ######


### MAKE YOUR CREATURES (at least 2 unique ones)

# draw a square and give it a unique tag "test-square"
the_canvas.create_rectangle((100, 100), (200, 200), fill="red", tags="test-square")

# draw a circle as a place holder for the second shape
the_canvas.create_oval((900, 100), (1000, 200), fill="green")


## NOTE: these next two lines are VERY IMPORTANT ######
the_canvas.scale("all", 0, 0, 1, -1)
gui.update()
# Make sure these are AFTER your calls to make_creature
# but BEFORE the animation stuff
#######################################################




#### ANIMATION SECTION (your code goes below)

# move shapes that have the tag 'test-square' 50 pixels to the right:
time.sleep(.1) # wait one second
utilities.update_position(the_canvas, 'test-square', x=50, y=0)
print("Left side", utilities.get_left(the_canvas, 'test-square'))
gui.update() # update the screen

# now do it again!
time.sleep(1)
utilities.update_position(the_canvas, 'test-square', x=50, y=0)
print("Left side", utilities.get_left(the_canvas, 'test-square'))
gui.update()

# and again!
time.sleep(.1)
utilities.update_position(the_canvas, 'test-square', x=50, y=0)
print("Left side", utilities.get_left(the_canvas, 'test-square'))
gui.update()


########################## YOUR CODE ABOVE THIS LINE ##############################
# makes sure the canvas keeps running:
the_canvas.mainloop()
