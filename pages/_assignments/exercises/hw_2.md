---
layout: assignment-two-column
title: Writing Functions
abbreviation: HW2
type: homework
due_date: 2023-04-14
ordering: 2
points: 100
draft: 0
canvas_id: 1224381
---

{: .blockquote-no-margin}
> **LEARNING OBJECTIVES:**
> 1. Practice working with pre-built functions, including reading documentation
> 1. Practice writing your own functions

In this assignment, you are going to get some practice writing functions using tkinter that will ultimately enable you to create more complex shapes (like animals, trees, plants, etc.). To do this, we will be using a built-in python module: `tkinter`. Tkinter provides support for creating custom graphical user interfaces (GUIs). 

## Getting Started

First, download the homework 2 starter file below:

<a class="nu-button" href="{{site.url}}/course-files/homeworks/hw02_template.py" target="_blank">
    Homework Starter File <i class="fas fa-download"></i>
</a>

**Make sure to move it to your `cs110` folder and rename it `homework_02.py`.**

In `homework_02.py`, there will be some initialization code at the top of each file, which imports the Canvas and Tk modules (belonging to the `tkinter` module) and initializes the window, the canvas and some drawing code at the end of each file that will actually render your drawing.

Don’t worry about any of this code for now: just take it as a given. You will understand it more in the coming weeks and months. You will add your code in between the commented lines (as specified in the figure below).

```python
from tkinter import Canvas, Tk

# more cool stuff here we'll understand later in the class

########################## YOUR CODE BELOW THIS LINE ##############################



# All of your code will go in between these two lines:


########################## YOUR CODE ABOVE THIS LINE ##############################

# even more cool stuff here we'll understand later in class

canvas.mainloop()
```

### TKinter sample code
Reemeber that from our pre-recorded lecture we have a library of samples function calls to `tkinter` in our `warm_up.py` file. If you find yourself confused about how the functions work, you can use that as a reference as you learn how to draw shapes using the tkinter canvas library. When you run `warm_up.py` from IDLE (by pressing F5), you should see an image like this:

<img class="med-lg center" src="{{site.url}}/assets/images/hw02/warmup.png" />

> **Note**: If you're on a Mac and are currently in Dark mode, you might not see the grid lines.
> 
> For some reason, `Tkinter` switches the colors white and black when your Mac is in
> dark mode. To fix this, you have two options:
> 1. <a href="https://support.apple.com/en-us/HT208976" target="_blank"> Use these instructions from Apple to switch to Light mode.</a>
> 2. On line 8, change the value of the `background` input to `"black"`.

### Documentation
Learning to read technical documentation is one of the most important skills we need to practice in order to become a programmer. You are essentially learning to read in a new genre, so interpreting the documentation takes practice (and patience). Ultimately, learning the exact details of tkinter isn't crucial. However, learning how to work with modules (which all have structures similar to tkinter) is one of the most important things you will learn in the class. In this assignment, we're going to give you "digests" of technical documentaiton. In future weeks, it'll be up to you to read the real deal.

* * *

## Your Tasks
Open up `homework_02.py` and take a look at what's already existing in the file. Make sure to run it to see its output as it stands now. Your task for this homework is split up into 4 parts.

* * *

### 1. Modify the `make_oval` function
The job of the **make_oval** function is to draw an oval to the canvas, centered at a given center point, according to a given x-radius (the radius in the x-axis of the oval) and y-radius (the radius in the y-direction of an oval). You've been given the function header for this function as part of the template so you only need to focus on the function's body.

We are creating this function because in the existing `tkinter` function, `create_oval`, is not intuitive (just like in the Tutorial we created our own `make_square` function).

Here's the official documentation of the `create_oval` method:
> `create_oval` is a method of the data type `Canvas` meant to draw ovals by specify a "bounding box" around an oval. It has 4 required inputs:
> 1. `int`: a bottom-left corner x-coordinate
> 2. `int`: a bottom-left corner y-coordinate
> 3. `int`: a top-right corner x-coordinate
> 4. `int`: a top-right corner y-coordinate
>
> and one **optional** argument:
>
> 1. **fill** (`str`): the name of a color to fill in the shape with

Here's a sample function call of the `create_oval` function:

```python
the_canvas.create_oval(
    100, 100, # x, y of bottom-left
    200, 150, # x, y of top-right
    fill="hot pink")
```

This draws an oval with a "bounding box" (an imaginary rectangle that encompasses the oval) with a bottom-left coordinate of (100, 100), and a top-right coordinate of (200, 150) and makes it hot pink.

Your `make_oval` function will use `create_oval` but accept the following arguments:

1. **a_canvas (Canvas)**: where you want the oval to be drawn.
1. **center_x (int)**: the x-coordinate of the center of the oval.
1. **center_y (int)**: the y-coordinate of the center of the oval.
1. **radius_x (int)**: specifies the radius of the oval in the x-direction.
1. **radius_y (int)**: specifies the radius of the oval in the y-direction.
1. **color (str, optional)**: represents the color of the oval, defaults to `"hot pink"`.

**Your job**: Currently, the `create_oval` function has the correct function header, but always draws a hard-coded oval with a bottom-left coordinate of (100, 100), and a top-right coordinate of (200, 150) — which effectively draws it at a centerpoint of (150, 125), with an x-radius of 50 and a y-radius of 25. Don't believe me? Try changing the function call on line 24. When you change the inputs...does the oval change? Your job is to modify the code so that the bottom-left (x, y) and top-right (x, y) coordinates are calculated based on the radius_x, radius_y and center point specified by the arguments; and that the fill color is determined by the `color` argument. 

Here's some tests for your `make_oval` function (the image you should see can be seen below):

```python
# Test 1: ovals:
print('Testing ovals...')
make_oval(the_canvas, 100, 100, 25, 40)
make_oval(the_canvas, 200, 100, 40, 25, color='navy')
make_oval(the_canvas, 300, 100, 25, 40, color='teal')
make_oval(the_canvas, 400, 100, 40, 25)
```

* * *

### 2. Create the `make_circle` function
The job of the **make_circle** function is to draw a circle to the canvas, centered at the given center, and with the given radius. We are creating this function as a _convenience_ function. Though every circle is actually an ellipse, it's common enough that we're going to make a special function just for the circle shape. The function accepts the following arguments:

1. **a_canvas (Canvas)**: where you want the circle to be drawn.
1. **center_x (int)**: the x-coordinate of the center of the circle.
1. **center_y (int)**: the y-coordinate of the center of the circle.
1. **radius (int)**: specifies the radius of the circle.
1. **color (str, optional)**: represents the color of the circle, defaults to `"hot pink"`.

**Your job**: Your job is to use your `make_oval` function in the body of your new function `make_circle` to draw a circle with the given inputs. **YOU MAY NOT USE `create_oval` in this function.**

Here's some tests for your `make_circle` function (the image you should see can be seen below):
```python
# Test 2: circles:
print('Testing circles...')
make_circle(the_canvas, 100, 200, 25, color='teal')
make_circle(the_canvas, 200, 200, 50)
make_circle(the_canvas, 300, 200, 25, color='navy')
make_circle(the_canvas, 400, 200, 50, color='teal')
```

* * *

### 3. Create the `make_bullseye` function
The job of the **make_bullseye** function is to draw a bullseye of 4 concentric circles to the canvas, centered at center and alternating `"pink"` and `"purple"`. The smallest concentric circle will have a radius of `radius` (value of the argument), and each additional concentric circle will have a radius of `distance` units more than the previous circle. For instance, if `radius`=10 and `distance`=5, then the first circle has a radius of 10, the second a radius of 15, the third 20, and the fourth 25. The function accepts the following arguments:

1. **a_canvas (Canvas)** : a Canvas object where you want the bullseye to be drawn.
1. **center_x (int)**:  the x-coordinate of the center of the bullseye.
1. **center_y (int)**:  the y-coordinate of the center of the bullseye.
1. **radius (int)** : an int that specifies the radius of the inner-most circle.
1. **distance (int)** : an int that represents how far apart each circle should be drawn.

**Your job**: Your job is to use the `make_circle` function that you just created to draw a bullseye (with 4 concentric circles of alternating colors). **YOU MAY NOT USE `create_oval` in this function.**

**HINT**: you'll have to draw the biggest circle first, or else your big circle will overwrite (occlude) the smaller circles.

Here's some tests for your `make_bullseye` function (the image you should see can be seen below):
```python
# Test 3: bullseye:
print('Testing bullseyes...')
make_bullseye(the_canvas, 100, 300, 5, 5)
make_bullseye(the_canvas, 200, 300, 5, 10)
make_bullseye(the_canvas, 300, 300, 10, 5)
make_bullseye(the_canvas, 400, 300, 20, 10)
```

* * *

### 4. Create the `make_face` function
The job of the **make_face** function is to draw a face (i.e. a circle) with two eyes (i.e. ovals) to the canvas, according to the center point and width specified by the arguments. The function accepts the following arguments:

1. **a_canvas (Canvas)**: where you want the face to be drawn.
1. **center_x (int)**:  the x-coordinate of the center of the face.
1. **center_y (int)**:  the y-coordinate of the center of the face.
1. **width (int)**: the _width_ of the face. (Remember, your `make_circle` function takes as input a `radius` but this parameter specifies the whole width of the face.)
1. **eye_color (string, optional)**: a string that specifies the color of the eyes that defaults to `"white"`
1. **face_color (string, optional)**: a string that specifies the color of the face that defaults to `"purple"`

**Your job**: Your job is to use the make_circle and make_oval functions that you've just created to draw a face. The face should be a circle, and it should have 2 oval eyes (see screenshot below). **YOU MAY NOT USE `create_oval` in this function.**

> **Note:** The eyes need to scale with the width of the face. Their **radius in the x-direction** should be 1/25 the width of the face. Their **radius in the y-direction** should be 1/15 the height of the face. They should be offset by 1/8 the width of the face from the center of the face in both the x and y-directions.

> **Note:** You MUST use your `make_circle` and `make_oval` functions to complete this one. Why do all that work again?

Here's some tests for your `make_face` function (the image you should see can be seen below):
```python
# Test 4: face:
print('Testing faces...')
make_face(the_canvas, 100, 400, 40, eye_color="black", face_color="yellow")
make_face(the_canvas, 200, 400, 60, face_color="yellow", eye_color="black")
make_face(the_canvas, 300, 400, 80)
make_face(the_canvas, 400, 400, 100)
```

* * *

## Testing
When you’re done, your program should draw be able to draw the below image:

<img class="medium" src="{{site.url}}/assets/images/hw02/final-screenshot.png" />

Note that while the image you see above will be produced with those function calls, your functions **must be able to produce their output at any input**. That is, for example, your `make_face` function has to actually use the inputs given to it. We will test your functions with other inputs to make sure that those inputs are actually used in the function body.

* * *

## What to Submit
For this assignment, you will upload your `homework_02.py` file to the assignment on Canvas. DO NOT UPLOAD ANY OTHER FILES. 

Make sure you can reproduce the test images shown above. You may leave those tests in your submission file.

Once you've submitted your file to Canvas, you're done!

* * *

## Requesting an extension
If you need to request an extension on this assignment use the <a target="_blank" href="https://docs.google.com/forms/d/e/1FAIpQLSeqyOhXfPiVuHh5AF5AIcoGEeTnMaq7o2P6yJzujFkQyXXSOA/viewform?usp=sf_link">Extension Request form</a>. Please see the Syllabus for requirements. Your extension is automatically accepted if you meet the conditions. You will see your due date on Canvas update 24 hours prior to the original deadline.