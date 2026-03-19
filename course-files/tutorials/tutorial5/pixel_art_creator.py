from cs110_p1 import *
_ignore = setup_shapes("Pixel Art Designer", background="white", include_grid=False, width=800, height=800)
########################## YOUR CODE BELOW THIS LINE ##############################
from math import floor

def reset_square(event):
    BASE = 50
    relative_x = floor(event.x / BASE)
    relative_y = floor(event.y / BASE)
    output_art[relative_y][relative_x] = 0
    update_screen()

def handle_click(event):
    BASE = 50
    relative_x = floor(event.x / BASE)
    relative_y = floor(event.y / BASE)
    current = output_art[relative_y][relative_x]
    output_art[relative_y][relative_x] = (current + 1) % 10
    update_screen()

# Start off the pixel_art as all blanks
output_art = []
# range(16) gives you back a list of all numbers from 0 to 15.
for i in range(16):
    output_art.append([])
    for j in range(16):
        output_art[i].append(0)


def update_screen():
    clear_window()
    y = 0
    for row in output_art:
        x = 0
        for cell in row:
            if cell != 0:
                sq = square((x, y), 50, color="grey")
                label = text(text=str(cell), color="black")
                overlay(label, sq)
            x += 50
        y += 50

def show_results(event):
    if event.keysym == "Return":
        print(output_art)
    

def setup():
    ## Setting some listeners!
    # Notice first we define our function called do_something
    # then we tell the canvas to listen for a LEFT-CLICK and if
    # it hears one, run make_square_from_click
    listen_for("LEFT-CLICK", handle_click)
    listen_for("RIGHT-CLICK", reset_square)

    listen_for("KEY", show_results)
    grid(800, 800, interval=50, show_labels=False)

def go():
    # Here's where you'll put everything you want to control your animations
    #   EXCEPT event listeners (look higher up)
    pass # this is a keyword that means DO NOTHING - It's just a placeholder

ticks_per_second = 30

########################## YOUR CODE ABOVE THIS LINE ##############################
## DO NOT MODIFY THIS STUFF
clear_window() ## Nothing should be drawn outside SETUP and GO!
ticks = 0
setup()
while True:
    go()
    update() # This function draws all your stuff to the screen!
    sleep(1 / ticks_per_second)
    ticks = ticks + 1
