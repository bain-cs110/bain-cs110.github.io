from p1_utilities import *
import time

_ignore = setup_shapes('Project 1', background="white", grid=False, width=800, height=800)
ticks_per_second = None
ticks = 0
########################## YOUR CODE BELOW THIS LINE ##############################

### CREATURE FUNCTION SECTION (put your function defs here ) ##########################
# Here's a delightful smiley face as an example (feel free to delete it)



####################################################################################


### LANDSCAPE OBJECT FUNCTION SECTION (put your function defs here ) ###################
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


    
    ## Setting some listeners!
    setup_listener('<Button-1>', click_handle)
    
    
    # This is how many animations to attempt per second. If you want to slow down your
    #   animations, just decrease this number! If you want to speed up...
    global ticks_per_second
    ticks_per_second = 10

####################################################################################

## ANIMATION GO FUNCTION HERE ####################################################
def go():
    # Here's where you'll put everything you want to control your animations
    #   EXCEPT event listeners (look higher up)
    print("Animating! ", ticks)


######&&!*#################### YOUR CODE ABOVE THIS LINE ##############################

## DO NOT MODIFY THIS STUFF
setup()
while True:
    go()
    _ignore.update()
    time.sleep(1 / ticks_per_second)
    ticks = ticks + 1
