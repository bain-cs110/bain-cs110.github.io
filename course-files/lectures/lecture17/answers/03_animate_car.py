from tkinter import Canvas, Tk
import time
import p1_utilities

cars_to_make = [
((0, 0),    "blue", "car_1"),
((100, 100),"green", "car_2"),
((200, 200),"yellow", "car_3"),
((375, 375),"red", "car_4")
]

gui = Tk()
gui.title('Animation')
the_canvas = Canvas(gui, width=500, height=500, background='white')
the_canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

# Challenge:
# 1. Create all the cars in the cars_to_make list using a for loop
# 2. Animate car_1 so that it goes to the right 10 times by a x change of 25 each time
#    and then goes down 10 times by a y change of 60 each time.
# 3. Animate car_4 so that it goes to the left 10 times by an x change of 25 each time, then
#    up 10 times with an y change of 60 each time.
# 4. Finally, delete all of the cars and then loop back to the beginning!

for car in cars_to_make:
    project_utilities.make_car(the_canvas, top_left=car[0], fill_color=car[1], my_tag=car[2])

counter = 0
while counter < 20:
    # calculate the move of car_1:
    if counter < 10:
        project_utilities.update_position(the_canvas, 'car_1', x=25, y=0)
        project_utilities.update_position(the_canvas, 'car_4', x=-25, y=0)

    # reverse movements if greater than 10
    else:
        project_utilities.update_position(the_canvas, 'car_1', x=0, y=60)
        project_utilities.update_position(the_canvas, 'car_4', x=0, y=-60)

    # draw the update
    gui.update()

    counter = counter + 1

    # Reset if we get to 20
    if counter == 20:
        for car in cars_to_make:
            project_utilities.delete(the_canvas, car[2])
            project_utilities.make_car(the_canvas, top_left=car[0], fill_color=car[1], my_tag=car[2])
        counter = 0

    # make the computer pause
    time.sleep(0.25)


########################## YOUR CODE ABOVE THIS LINE ##############################
# makes sure the canvas keeps running:
canvas.mainloop()
