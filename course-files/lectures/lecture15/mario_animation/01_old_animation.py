from cs110_l15a import *
_ignore = setup_shapes("Lecture 15", background="white", grid=True, width=1000, height=800)
ticks = 0

########################## YOUR CODE BELOW THIS LINE #######################################

# This is how many animations to attempt per second. If you want to slow down your
#   animations, just decrease this number! If you want to speed up...
ticks_per_second = 10


def setup():
    pixel_art((0, 100), GOOMBA, GOOMBA_COLORS, tag="DrGoomba")
    pixel_art((1000, 100), HEART, HEART_COLORS, tag="HeartBoi")

def go():
    delete("DrGoomba")
    delete("HeartBoi")
    pixel_art((0 + ticks * 5, 100), GOOMBA, GOOMBA_COLORS, tag="DrGoomba")
    pixel_art((1000 - ticks * 5, 400), HEART, HEART_COLORS, tag="HeartBoi")


########################## YOUR CODE ABOVE THIS LINE ##############################
## DO NOT MODIFY THE STUFF BELOW
setup()
while True:
    go()
    _ignore.update()
    sleep(1 / ticks_per_second)
    ticks = ticks + 1
