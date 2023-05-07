from tkinter import Canvas, Tk
import time
import p1_utilities

cars_to_make = [
    [(0, 0),    "blue", "car_1"],
    [(100, 100),"green", "car_2"],
    [(200, 200),"yellow", "car_3"],
    [(375, 375),"red", "car_4"]
]

gui = Tk()
gui.title('Animation')
the_canvas = Canvas(gui, width=500, height=500, background='white')
the_canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

# 1. Create all the cars in the cars_to_make list using a for loop
# 2. Animate car_1 so that it goes to the right 10 times by a x change of 25 each time.
# 3. Animate car_4 so that it goes to the left 10 times by an x change of 25 each time.
# 4. Now reverse the two motions!
# 5. Finally, reset all of the cars and then loop back to the beginning!


## NOTE: like the project, the y-axis is flipped!
project_utilities.make_car(the_canvas, (0, 0), car_color="blue", my_tag="car_1")
gui.update()
time.sleep(3)
project_utilities.update_position(the_canvas, "car_1", x=100)

########################## YOUR CODE ABOVE THIS LINE ##############################
# makes sure the canvas keeps running:
the_canvas.mainloop()
