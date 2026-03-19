from cs110_p1 import *
_ignore = setup_shapes("Project 1", background="white", width=800, height=800)
###&&##################### YOUR CODE BELOW THIS LINE ##############################

## PARAGRAPH EXPLAINING WHICH
##   ANIMATION TASKS YOU CHOSE
##   GOES HERE!!!!!!!

###################################################################################
### CREATURE FUNCTION SECTION (put your function def here ) ######################


###################################################################################
### LANDSCAPE OBJECT FUNCTION SECTION (put your function def here ) ##############


###################################################################################

## EVENT HANDLERS HERE ############################################################



###################################################################################

## Initial Terrarium Setup Here ###################################################
def setup():
    print("Running setup....")
    ## Put all your creature and landscape and other stuff that only needs to run
    #   once in this function!
    car((350, 350), tag="car")


###################################################################################

## GO FUNCTION HERE !!#############################################################
def go():
    # Here's where you'll put everything you want to control your animations
    #   EXCEPT event handlers (look higher up)
    move("car", x_shift=1, y_shift=1)


ticks_per_second = 30  # change this to change the rate of animation

######&&!*#################### YOUR CODE ABOVE THIS LINE ##########################
## DO NOT MODIFY ANYTHING BELOW. You will receive a 0 on the assignment.
clear_window() ## Nothing should be drawn outside SETUP and GO!
ticks = 0
setup()
while True:
    go()
    update() # This function draws all your stuff to the screen!
    sleep(1 / ticks_per_second)
    ticks = ticks + 1
