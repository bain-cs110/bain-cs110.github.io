---
layout: assignment-two-column
title: Writing Functions
abbreviation: HW2
type: homework
due_date: 2024-01-19
ordering: 2
points: 100
draft: 0
points: 100
canvas_id: 1357224
canvas_title: Homework 2
canvas_assignment_group: "Homework"
canvas_points_possible: 100
canvas_submission_types: "online_upload"
canvas_allowed_extensions: "py"
---
{: .blockquote-no-margin}
> **LEARNING OBJECTIVES:**
>
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

Don’t worry about any of this code for now: just take it as a given. You will understand it more in the coming weeks. You will add your code in between the commented lines (as specified in the figure below).

```python
from tkinter import Canvas, Tk

# more cool stuff here we'll understand later in the class

########################## YOUR CODE BELOW THIS LINE ##############################



# All of your code will go in between these two lines:


########################## YOUR CODE ABOVE THIS LINE ##############################

# even more cool stuff here we'll understand later in class

canvas.mainloop()
```

<details>
  <summary>Note on Reading Documentation</summary>
 Learning to read technical documentation is one of the most important skills we need to practice in order to become a programmer. You are essentially learning to read in a new genre, so interpreting the documentation takes practice (and patience). Ultimately, learning the exact details of tkinter isn't crucial. However, learning how to work with modules (which all have structures similar to tkinter) is one of the most important things you will learn in the class. In this assignment, we're going to give you "digests" of technical documentation. In future weeks, it'll be up to you to read the real deal.
</details>

* * *

### Your Tasks

Open up `homework_02.py` and take a look at what's already existing in the file. Make sure to run it to see its output as it stands now. Your task for this homework is split up into 4 parts.

* * *

## Task 1. Practice

Right now if you run `homework_02.py` you'll see a coordinate grid. Notice that there's one strange thing about it – <mark>the y-axis is flipped! As we go DOWN on the y-axis, the y-values INCREASE. As we go UP the y-axis, the y-value DECREASES.</mark> Keep this in mind as you're working.

<details>
  <summary>On a Mac in Dark Mode?</summary>
  If you're on a Mac and are currently in Dark mode, you might not see the grid lines. For some reason, Tkinter switches the colors white and black when your Mac is in dark mode. To fix this, you have two options:<br>
  1. <a href="https://support.apple.com/en-us/HT208976" target="_blank"> Use these instructions from Apple to switch to Light mode.</a><br>
  2. On line 5, change the value of the <em>background</em> input to <em>"black"</em>.
</details>
<br>
While our turtles are great at drawing shapes, it's time to graduate to more abstract thinking. We don't want to be stuck having to think about desigining individual shapes. Instead, we just want to be able to use functions that make those shapes directly!

Built-in to `tkinter` is the function `oval`. It takes the following parameters:

* `x` (`int`) - the x-coordinate of the center of the oval
* `y` (`int`) - the y-coordinate of the center of the oval
* `radius_x` (`int`) - the radius on the x-axis of the oval
* `radius_y` (`int`) - the radius on the y-axis of the oval
* `color` (`string`, _optional_) - the color to draw the oval (defaults to `"hotpink"`)

In the section of the file marked `## TASK 1` write 4 function calls to `oval` that...

1. draw an oval with a center of `(100, 100)`, a _total_ width of 50 and a _total_ height of 80 (use the default color).
2. draw an oval with a center of `(200, 100)`, a _total_ width of 80 and a _total_ height of 50 that is navy.
3. draw an oval with a center of `(300, 100)`, a _total_ width of 50 and a _total_ height of 80 that is teal.
4. draw an oval with a center of `(400, 100)`, a _total_ width of 80 and a _total_ height of 50 (use the default color).

<details>
  <summary>Finished Product Screenshot</summary>
  <img style="width:50%" src="{{site.url}}/assets/images/hw02/task1.png" alt="screenshot of task 1">
</details>

* * *

## Task 2. Create a `circle` function

The job of the **circle** function is to draw a circle to the canvas with a given `radius` and centered at a given center point (`x` and `y`). It will have the following parameters:

1. `x` (`int`) - the x-coordinate of the center of the circle.
1. `y` (`int`) - the y-coordinate of the center of the circle.
1. `radius` (`int`) - specifies the radius of the circle.
1. `color` (`str`, _optional_) - represents the color of the oval, defaults to `"hot pink"`.

**Your job**: Write the appropriate function _header_ and _body_ for the `circle` function. Just like the `draw_square` function in Tutorial 2, the function's body will only be one line: a call to the `oval` function!

<details>
  <summary>Hint</summary>
  When calling the oval function, you're going to have set the parameter color to the value
  of whatever color your circle function is called with. Because they both have the same parameter
  name, you'll see something weird at the end of your call to oval: <em>color=color</em>.
</details>


Here's some tests for your `oval` function (the image you should see can be seen below). You can copy and paste them into your program but <mark>make sure they are not part of your function's body as otherwise they won't run!</mark>

```python
# Testing circle!
circle(100, 200, 25)
circle(200, 200, 50, color="purple4")
circle(300, 200, 25, color='gold')
circle(400, 200, 50, color="olive drab")
```

<details>
  <summary>Finished Product Screenshot</summary>
  <img style="width:50%"  src="{{site.url}}/assets/images/hw02/task2.png" alt="screenshot of task 2">
</details>

* * *

## Task 3. Create a `bullseye` function

The job of the **bullseye** function is to draw a bullseye of 4 concentric circles to the canvas, centered at center and alternating colors. The smallest concentric circle will have a radius of `radius` (value of the argument), and each additional concentric circle will be 50% bigger (i.e. `radius`, `radius * 1.5`, `radius * 2.0`, `radius * 2.5`). Your `bullseye` function needs to have five parameters:

* `x` (`int`) - the x-coordinate of the center of the bullseye
* `y` (`int`) - the y-coordinate of the center of the bullseye
* `start_radius` (`int`) - the radius of the innermost circle
* `color_a` (`string`, _optional_) - the first color to alternate with (defaults to `"blue"`)
* `color_b` (`string`, _optional_) - the other color to alternate with (defaults to `"red"`)

**Your job**: Your job is to use the `circle` function that you just created to draw a bullseye (with 4 concentric circles of alternating colors). **YOU MAY NOT USE `oval` in this function.** <mark>You'll receive 0 credit for this function if you use oval instead of circle.</mark>

**HINT**: you'll have to draw the biggest circle first, or else your big circle will overwrite (occlude) the smaller circles.

Here's some tests for your `bullseye` function:

```python
# Testing bullseye!
bullseye(100, 300, 5)
bullseye(200, 300, 10, color_a="aquamarine")
bullseye(300, 300, 15, color_b="salmon1")
bullseye(400, 300, 20, color_a="thistle1", color_b="thistle4")
```

<details>
  <summary>Finished Product Screenshot</summary>
  <img style="width:50%" src="{{site.url}}/assets/images/hw02/task3.png" alt="screenshot of task 3">
</details>

* * *

## Task 4. Create the `face` function

The job of the **face** function is to draw a face (i.e. a circle) with two eyes (i.e. ovals) to the canvas, according to the center point and width specified by the arguments. The function accepts the following arguments:

1. `x` (`int`) - the x-coordinate of the center of the face.
1. `y` (`int`) - the y-coordinate of the center of the face.
1. `width` (`int`) - the _width_ of the face. (Remember, your `circle` function takes as input a `radius` but this parameter specifies the whole width of the face.)
1. `eye_color` (`string`, _optional_) - a string that specifies the color of the eyes that defaults to `"white"`
1. `face_color` (`string`, _optional_) - a string that specifies the color of the face that defaults to `"purple"`

**Your job**: Your job is to use the `circle` and `oval` functions to draw a face. The face should be a circle, and it should have 2 oval eyes (see screenshot below).

> **Note:** You MUST use your `circle` and `oval` functions to complete this one. Why do all that work again? The eyes need to scale with the width of the face. Their **radius in the x-direction** should be 1/20 the `width` of the face. Their **radius in the y-direction** should be 1/18 the width of the face. They should be offset by 1/7 the width of the face from the center of the face in both the x and y-directions (remember, the y-axis is flipped!).

Here's some tests for your `face` function (the image you should see can be seen below):

```python
# Testing face!
face(100, 400, 40, eye_color="black", face_color="yellow")
face(200, 400, 60, face_color="yellow", eye_color="black")
face(300, 400, 80)
face(400, 400, 100)
```

<details>
  <summary>Finished Product Screenshot</summary>
  <img style="width:50%" src="{{site.url}}/assets/images/hw02/task4.png" alt="screenshot of task 4">
</details>

* * *

## Testing

Note that while the image you see above will be produced with those function calls, your functions **must be able to produce their output at any input**. That is, for example, your `bullseye` function has to actually use the inputs given to it. We will test your functions with other inputs to make sure that those inputs are actually used in the function body. One example test might be to move the bullseyes to a different y-coordinate and see if that is reflected in your final output!

<mark>Make sure to double check ALL function names, parameter names, and default values.</mark> Typos or not following the instructions will result in lost points.

> **Note**: You will not receive feedback from the autograder on your assignment until AFTER the final due date (which is the "available until date on Canvas").

{% include submission_details.md %}
