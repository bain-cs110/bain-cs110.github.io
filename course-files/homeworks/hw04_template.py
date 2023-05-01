from tkinter import Canvas, Tk
import time
import hw04_utilities

gui = Tk()
gui.title('Animation')
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
the_canvas = Canvas(gui,
                    width=WINDOW_WIDTH,
                    height=WINDOW_HEIGHT,
                    background='light blue')
the_canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

hw04_utilities.make_cloud(the_canvas, (400, WINDOW_HEIGHT - 900))
hw04_utilities.make_cloud(the_canvas, (700, WINDOW_HEIGHT - 850))
hw04_utilities.make_cloud(the_canvas, (800, WINDOW_HEIGHT - 900))
hw04_utilities.make_cloud(the_canvas, (123, WINDOW_HEIGHT - 850))

####### YOUR MAKE CREATURE FUNCTION DEFINITION GOES HERE ############






####### YOUR CREATURE DEFINITION GOES ABOVE HERE ######


### YOUR CALLS TO MAKE_CREATURE (at least 2 unique ones) GO HERE

# draw a square and give it a unique tag "test-square"
the_canvas.create_rectangle((100, WINDOW_HEIGHT - 100), (200, WINDOW_HEIGHT - 200), fill="red", tags="test-square")

# draws a circle as a place holder for the second shape
the_canvas.create_oval((900, WINDOW_HEIGHT - 100), (1000, WINDOW_HEIGHT - 200), fill="green")

######## Your calls to make creature go above here #####


#### ANIMATION SECTION (your code to animate goes below)

# move shapes that have the tag 'test-square' 50 pixels to the right:
time.sleep(1) # wait one second
hw04_utilities.update_position(the_canvas, 'test-square', x=50, y=0)
print("Left side", hw04_utilities.get_left(the_canvas, 'test-square'))

# now do it again!
time.sleep(1)
hw04_utilities.update_position(the_canvas, 'test-square', x=50, y=0)
print("Left side", hw04_utilities.get_left(the_canvas, 'test-square'))

# and again!
time.sleep(1)
hw04_utilities.update_position(the_canvas, 'test-square', x=50, y=0)
print("Left side", hw04_utilities.get_left(the_canvas, 'test-square'))

########################## YOUR CODE ABOVE THIS LINE ##############################
# makes sure the canvas keeps running:
the_canvas.mainloop()