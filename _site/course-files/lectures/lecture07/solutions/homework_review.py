from turtle import *

class MyTurtle(object):
    def __new__(cls, x=-100, y=-100, pencolor="black"):
        my_turtle = Turtle()
        Screen().tracer(0)
        my_turtle.pencolor(pencolor)
        my_turtle.penup()
        my_turtle.goto(x, y)
        my_turtle.pendown()
        Screen().tracer(1)
        return my_turtle

## DO NOT MODIFY ANY LINES ABOVE THIS LINE
## DO NOT MODIFY ANY LINES THAT BEGIN WITH ## (two hashtags).
## You can add as many new lines as you'd like
    
## TURTLE SECTION #####!!!#####

## Exercise 1 #####!!!#####
turtle_1 = MyTurtle(x = -300, y = 200)

turtle_1.forward(100)
turtle_1.right(90)
turtle_1.forward(100)
turtle_1.right(90)
turtle_1.forward(100)
turtle_1.right(90)
turtle_1.forward(100)
turtle_1.right(90)

## Exercise 2 #####!!!#####
turtle_2 = MyTurtle(x = -150, y = 200)

turtle_2.pencolor("green")

turtle_2.forward(100)
turtle_2.right(90)
turtle_2.forward(200)
turtle_2.right(90)
turtle_2.forward(100)
turtle_2.right(90)
turtle_2.forward(200)
turtle_2.right(90)

## Exercise 3 #####!!!#####
turtle_3 = MyTurtle(x = 0, y = 200)

turtle_3.pencolor("red")
turtle_3.forward(100)
turtle_3.right(120)
turtle_3.forward(100)
turtle_3.right(120)
turtle_3.forward(100)
turtle_3.right(120)

## Exercise 4 #####!!!#####
# Hint: Combine what you know from exercises 1 and 3!
turtle_4 = MyTurtle()

turtle_4.pencolor("green")

turtle_4.forward(100)
turtle_4.right(90)
turtle_4.forward(100)
turtle_4.right(90)
turtle_4.forward(100)
turtle_4.right(90)
turtle_4.forward(100)
turtle_4.right(90)
turtle_4.pencolor("red")
turtle_4.forward(100)
turtle_4.left(120)
turtle_4.forward(100)
turtle_4.left(120)
turtle_4.forward(100)
turtle_4.left(120)

## Optional Bonus #####!!!#####
turtle_5 = MyTurtle(x = 300, y = -300)
# Some ideas: a snowflake, a heptagon, a 2-D cube!
# Or, you could add windows or doors to your house
# If you choose not to do this its fine, but don't
# delete the line that starts with ## (two hashtags)


## CALCULATOR SECTION #####!!!#####

## Exercise 1 #####!!!#####

print((512 - 282) / (47 * 48 + 5))

## Exercise 2 #####!!!#####

a_name = input("Enter a name:")
print("Hello there,", a_name)

## Exercise 3 #####!!!#####

weight = input("Enter weight in kg: ")
weight = int(weight)
print(weight, "kilograms is", weight * 2.2, "pounds.")

## Exercise 4 #####!!!#####
# Hint: to find the length in number of letters of a string, we can use the len function
#       like so: len("hello"). If we wanted to find the number of characters in a string
#       that's stored in a variable, we'd instead use the variable's name: len(variable)

entry = input("Enter a word: ")
print("There are", len(entry), "letters in that word.")

