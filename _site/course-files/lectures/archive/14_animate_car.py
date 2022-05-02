from tkinter import Canvas, Tk
import time
import shapes

cars_to_make = [
((0, 0),    "blue", "car_1"),
((100, 100),"green", "car_2"),
((200, 200),"yellow", "car_3"),
((100, 300),"red", "car_4")
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
# 3. Animate each car differently using a while loop.

def make_car(canvas:Canvas, top_left:tuple=(0,0), car_tag:str=None, car_color="blue"):

    x = top_left[0]
    y = top_left[1]

    # make car with top left at (50, 20)
    top_id    = shapes.make_rectangle(canvas, (x + 50, y), 100, 40, color=car_color, tag=car_tag)
    bottom_id = shapes.make_rectangle(canvas, (x, y + 30), 200, 45, color=car_color, tag=car_tag)
    wheel1_id = shapes.make_circle(canvas, (x + 50, y + 80), 20, color='black', tag=car_tag)
    wheel2_id = shapes.make_circle(canvas, (x + 150, y + 80), 20, color='black', tag=car_tag)

for car in cars_to_make:
    make_car(canvas, top_left=car[0], car_color=car[1], car_tag=car[2])

counter = 0
while counter < 20:
    # calculate the move of each car:
    if counter < 10:
        shapes.move(canvas, 'car_1', x=25, y=0)
        shapes.move(canvas, 'car_2', x=-25, y=0)
        shapes.move(canvas, 'car_3', x=25, y=0)
        shapes.move(canvas, 'car_4', x=-25, y=0)

    # reverse movements if greater than 10
    else:
        shapes.move(canvas, 'car_1', x=-25, y=0)
        shapes.move(canvas, 'car_2', x=25, y=0)
        shapes.move(canvas, 'car_3', x=-25, y=0)
        shapes.move(canvas, 'car_4', x=25, y=0)

    # draw the update
    gui.update()

    # increment our counter
    counter = counter + 1

    # Reset if we get to 20
    if counter == 20:
        counter = 0

    # make the computer pause
    time.sleep(1)


########################## YOUR CODE ABOVE THIS LINE ##############################
# makes sure the canvas keeps running:
canvas.mainloop()
