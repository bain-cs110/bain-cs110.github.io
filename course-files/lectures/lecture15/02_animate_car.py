from tkinter import Canvas, Tk
import time
import shapes

cars_to_make = [
((0, 0),    "blue", "car_1"),
((100, 100),"green", "car_2"),
((200, 200),"yellow", "car_3"),
((375, 375),"red", "car_4")
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

x = 0
y = 0
car_color = "blue"
car_tag = "car_1"

# make car with top left at (50, 20)
shapes.make_rectangle(canvas, (x + 50, y), 100, 40, fill_color=car_color, tag=car_tag)
shapes.make_rectangle(canvas, (x, y + 30), 200, 45, fill_color=car_color, tag=car_tag)
shapes.make_circle(canvas, (x + 50, y + 80), 20, fill_color='black', tag=car_tag)
shapes.make_circle(canvas, (x + 150, y + 80), 20, fill_color='black', tag=car_tag)


### ITERATION 1

counter = 0
car_1_x = 0

# Erase the current car
canvas.delete("car_1")
# Shift the x coordinate
car_1_x += 25
# Draw the new car shifted over
shapes.make_rectangle(canvas, (car_1_x + 50, y), 100, 40, fill_color=car_color, tag=car_tag)
shapes.make_rectangle(canvas, (car_1_x, y + 30), 200, 45, fill_color=car_color, tag=car_tag)
shapes.make_circle(canvas, (car_1_x + 50, y + 80), 20, fill_color='black', tag=car_tag)
shapes.make_circle(canvas, (car_1_x + 150, y + 80), 20, fill_color='black', tag=car_tag)
# draw the update
gui.update()
time.sleep(5)

counter = counter + 1

### ITERATION 2

# Erase the current car
canvas.delete("car_1")
# Shift the x coordinate
car_1_x += 25
# Draw the new car shifted over
shapes.make_rectangle(canvas, (car_1_x + 50, y), 100, 40, fill_color=car_color, tag=car_tag)
shapes.make_rectangle(canvas, (car_1_x, y + 30), 200, 45, fill_color=car_color, tag=car_tag)
shapes.make_circle(canvas, (car_1_x + 50, y + 80), 20, fill_color='black', tag=car_tag)
shapes.make_circle(canvas, (car_1_x + 150, y + 80), 20, fill_color='black', tag=car_tag)
# draw the update
gui.update()

counter = counter + 1

# make the computer pause

########################## YOUR CODE ABOVE THIS LINE ##############################
# makes sure the canvas keeps running:
canvas.mainloop()
