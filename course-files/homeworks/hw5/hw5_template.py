import time
from cs110_hw5 import *

_ignore = setup_shapes('HW 5', background="light blue", grid=True, width=1000, height=800)
ticks_per_second = None
ticks = 0
########################## YOUR CODE BELOW THIS LINE ############&&!*

####### YOUR  CREATURE FUNCTION DEFINITION GOES HERE ######&&!*######


# def creature(....



####### YOUR CREATURE DEFINITION GOES ABOVE HERE ##############


## This is a "helper" function that's only job is to setup our clouds!
def draw_clouds(num_clouds):
    cloud((450, 100), tag="cloud_1")
    cloud((100, 200), tag="cloud_2")
    cloud((300, 100), tag="cloud_3")
    cloud((600, 200), tag="cloud_4")
    cloud((700, 100), tag="cloud_5")


## This function controls all of the stuff necessary to setup your Animation.
##   We add any code that we want to be executed before the animation steps begin
##   here in this function.
def setup():
    print("Setting up everything!")

    draw_clouds(30)

    # Feel free to delete the test square when you're ready to add your creatures!
    square(top_left=(0, 450), size=50, color="olivedrab", tag="test-square")

    ###
    # Your calls to the creature function will go here inside of setup
    ###
    
    # This is how many animations to attempt per second. If you want to slow down your
    #   animations, just decrease this number! If you want to speed up...
    global ticks_per_second
    ticks_per_second = 1



def go():
    # Note, you can and should delete all of this demo stuff before adding your own stuff
    print("Animating step...", ticks)
    
    # Move the shape named test-square.
    move('test-square', x=50, y=0)

    # Print out it's left most x-coordinate (just as a demo)
    print("Left side", get_left('test-square'))


######&&!*%^#################### YOUR CODE ABOVE THIS LINE ##############################

## DO NOT MODIFY ANYTHING BELOW (otherwise we won't be able to grade your file)
setup()
while True:
    go()
    _ignore.update()
    time.sleep(1 / ticks_per_second)
    ticks = ticks + 1

# makes sure the canvas keeps running:
_ignore.mainloop()