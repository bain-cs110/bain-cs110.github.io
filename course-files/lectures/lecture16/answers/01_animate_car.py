from tkinter import Canvas, Tk
import time
import shapes
import utilities

cars_to_make = [
    [(0, 0),    "blue", "car_1"],
    [(100, 100),"green", "car_2"],
    [(200, 200),"yellow", "car_3"],
    [(375, 375),"red", "car_4"]
]

gui = Tk()
gui.title('Animation')
canvas = Canvas(gui, width=500, height=500, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

# Challenge:
# 1. Turn the car code into a function, with a customizable
#    position, car_color, and car_tag.
#    Note that the “tag” parameter is useful so that you can refer to
#    the car later when you want to animate it.
# 2. Create all the cars in the cars_to_make list using a for loop
# 3. Animate car_1 so that it goes to the right 10 times by a x change of 25 each time.
# 4. Animate car_4 so that it goes to the left 10 times by an x change of 25 each time.
# 5. Now reverse the two motions!
# 6. Finally, reset all of the cars and then loop back to the beginning!

def make_car(canvas:Canvas, top_left:tuple=(0,0), car_tag:str=None, car_color="blue"):

    x = top_left[0]
    y = top_left[1]

    # make car with top left at (50, 20)
    shapes.make_rectangle(canvas, (x + 50, y), 100, 40, fill_color=car_color, tag=car_tag)
    shapes.make_rectangle(canvas, (x, y + 30), 200, 45, fill_color=car_color, tag=car_tag)
    shapes.make_circle(canvas, (x + 50, y + 80), 20, fill_color='black', tag=car_tag)
    shapes.make_circle(canvas, (x + 150, y + 80), 20, fill_color='black', tag=car_tag)

for car in cars_to_make:
    make_car(canvas, top_left=car[0], car_color=car[1], car_tag=car[2])

counter = 0
car_1_x = 0
car_4_x = 375

while counter < 20:

    #print("left side of car 1", utilities.get_left(canvas, "car_1"))
    #print("right side of car 4", utilities.get_right(canvas, "car_4"))

    if counter < 10:
        utilities.update_position_by_tag(canvas, "car_1", x=25)
        utilities.update_position_by_tag(canvas, "car_4", x=-25)

    # reverse movements if greater than 10
    else:
        utilities.update_position_by_tag(canvas, "car_1", x=-25)
        utilities.update_position_by_tag(canvas, "car_4", x=25)

    # draw the update
    gui.update()

    # make the computer pause
    time.sleep(0.25)

    counter = counter + 1

    # Reset if we get to 20
    if counter == 20:
        canvas.delete("all")
        for car in cars_to_make:
            make_car(canvas, top_left=car[0], car_color=car[1], car_tag=car[2])
        counter = 0

########################## YOUR CODE ABOVE THIS LINE ##############################
# makes sure the canvas keeps running:
canvas.mainloop()
