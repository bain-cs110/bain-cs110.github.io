---
layout: assignment-two-column
title: Practice with Parameters & Arguments
type: tutorial
abbreviation: Tutorial 3
draft: 0
points: 3
num: 3
description:
  - Positional parameters/arguments
  - Keyword parameters/arguments
due_date: 2022-04-20
---

<a class="nu-button" href="/course-files/tutorials/tutorial03_template.zip" target="_blank">
    Tutorial Starter Files <i class="fas fa-download"></i>
</a>

In this tutorial, you are going to design a customizable function that creates an image of [Mario](https://en.wikipedia.org/wiki/Mario) (pictured below). The purpose of this exercise is to help you figure out how to use parameters and variables in order to make your ideas more flexible, customizable, and therefore more useful.

To do this, we're going to walk you through a series of steps to begin trying to "think computationally" -- i.e. finding places where code repeats and modularizing it using variables, functions, and parameters. We only have a few tools that are at our disposal right now, but just note that this code in this exercise can be further simplified in a few weeks when we learn more about loops.

In addition to gaining more practice with functions, there are three takeaways that we hope you will also get from this exercise:

1. That programming is a *process* of formulating solutions over time (versus having everything all planned out at the very the beginning).
2. That programmers are always trying to make their code efficient, readable, and succinct, which usually involves "refactoring" code so that it's not repeating the same lines of code over and over again. This is known as the "DRY Principle" -- " *D*on't *r*epeat *y*ourself."
3. That programmers learn new techniques for solving problems by looking at examples of how other people have solved similar problems. Over time, you too will begin to develop a set of common strategies for solving classes of problems, and that comes by seeing lots of examples (and practicing).

## Part 1: Understanding the "hardcoded" version of Mario
Please open the `your_task.py` file and take a look at it. Note that it is making use of the `make_square` function that you made in [Tutorial 2](tutorial02) (it's included in the `helpers` module).

```python
clothes = 'red'
accessories = 'saddle brown'
tone = 'bisque3'
features = 'black'

# row 0
# blank, pixel (0,0)
# blank, pixel (1,0)
# blank, pixel (2,0)
make_square(canvas, (75,  0), 25, fill_color=clothes) # pixel (3, 0)
make_square(canvas, (100, 0), 25, fill_color=clothes) # pixel (4, 0)
make_square(canvas, (125, 0), 25, fill_color=clothes) # pixel (5, 0)
make_square(canvas, (150, 0), 25, fill_color=clothes) # pixel (6, 0)
make_square(canvas, (175, 0), 25, fill_color=clothes) # pixel (7, 0)
make_square(canvas, (200, 0), 25, fill_color=clothes) # pixel (8, 0)

# row 1
# blank, pixel (0,1)
# blank, pixel (1,1)
make_square(canvas, (50, 25), 25, fill_color=clothes) # pixel (2, 1)
make_square(canvas, (75, 25), 25, fill_color=clothes) # pixel (3, 1)
make_square(canvas, (100,25), 25, fill_color=clothes) # pixel (4, 1)
make_square(canvas, (125,25), 25, fill_color=clothes) # pixel (5, 1)
make_square(canvas, (150,25), 25, fill_color=clothes) # pixel (6, 1)
make_square(canvas, (175,25), 25, fill_color=clothes) # pixel (7, 1)
make_square(canvas, (200,25), 25, fill_color=clothes) # pixel (8, 1)
make_square(canvas, (225,25), 25, fill_color=clothes) # pixel (9, 1)
make_square(canvas, (250,25), 25, fill_color=clothes) # pixel (10, 1)
make_square(canvas, (275,25), 25, fill_color=clothes) # pixel (11, 1)

# row 2
# blank, pixel (0,2)
# blank, pixel (1,2)
make_square(canvas, (50, 50), 25, fill_color=accessories) # pixel (2, 2)
make_square(canvas, (75, 50), 25, fill_color=accessories) # pixel (3, 2)
make_square(canvas, (100,50), 25, fill_color=accessories) # pixel (4, 2)
make_square(canvas, (125,50), 25, fill_color=tone) # pixel (5, 2)
make_square(canvas, (150,50), 25, fill_color=tone) # pixel (6, 2)
make_square(canvas, (175,50), 25, fill_color=tone) # pixel (7, 2)
make_square(canvas, (200,50), 25, fill_color=features) # pixel (8, 2)
make_square(canvas, (225,50), 25, fill_color=tone) # pixel (9, 2)
...
```

Then run it using IDLE (or a code editor of your choice). You should see a picture of Mario (below).

<img class="small frame" src="/assets/images/tutorials/mario1.png" />

A few things to pay attention to in this file:

1. This program will always draw a Mario that is the same size and positioned in the exact same place.
1. Each "pixel" is 25 units wide / tall
1. If you were to draw a box around this particular Mario, the top_left coordinate would be positioned at `(0, 0)`, and the bottom_right coordinate would be positioned at `(300, 375)`.

### Task 1: Manipulating Mario's clothes and overalls color
Try re-assigning a different color to the `clothes` variable, and running the program (note that Marios's shirt and hat change color). When you're done, please create another variable called `overalls`, and edit the code so that the color of Mario's overalls is determined by the value stored inside the `overalls` variable.

### Task 2: Customize Mario's size
Next, modify the code to make it easier to customize Mario's ***size*** (i.e. the size of each pixel). As the program currently stands, each pixel is hardcoded to 25 pixels. But what if you wanted to draw a mini-Mario, or a really big Mario? You would have to update every x and y value.

To make this process more efficient, create another variable called `pixel` and assign the value `20` (int) to it. Then, figure out a way to use the `pixel` variable to make Mario's size customizable. If you get stuck, see `hints/hint_1.py`. That said, don't just copy this code...think about why it works (and ask questions). It only helps you with the first few rows and it only shows you how to rewrite the x-coordinates. Think about how you can also apply this same process to the y-coordinates! (Hint: look at the "pixel coordinates" for each row. See a pattern?)

### Task 3: Customize Mario's position
Next, modify the code to make it easier to customize Mario's ***position***. Note that the top-left corner of the Mario pixel map is positioned at `(0, 0)`. In other words, the is an implicit offset of `(0, 0)`. But you wanted to change this offset to, say, `(100, 50)`, then you would have to manually add 100 to the value of every x-coordinate and 50 to the value of every y-coordinate.

To make this process more efficient, create another variable called `top_left` and assign the value `(100, 50)` (tuple) to it. Then, figure out a way to use the `top_left` variable to make Mario's position customizable. If you get stuck, see `hints/hint_2.py`. Just like before, don't just copy this code...think about why it works (and ask questions).

### Task 4: Create a function so that you can instantiate many Marios
When you're done, you have successfully made your Mario program customizable. However, if you wanted to make, say, 5 Marios, you would have to copy all of your code 5 times (and change the variables for each Mario). This is inefficient. In general, any time you're copying the same code over and over again, it makes sense to create a function. So, let's make that happen. For your final task, please create a `make_mario` function that accepts the following arguments:

1. **canvas** *(Canvas)*: a tkinter Canvas object where you want the square to be drawn.
1. **top_left** *(tuple)*: a tuple -- an point, an (x, y) coordinate -- that defines the top-left position of the rectangle bounding your picture of Mario. The first element in the tuple refers to the x-coordinate and the second element in the tuple refers to the y-coordinate.
1. **pixel** *(int, optional)*: an int that specifies the width (and also height) of the pixel; defaults to 25.
1. **clothes** *(str, optional)*: a string that represents the color Mario's clothes; defaults to `'red'`.
1. **overalls** *(str, optional)*: a string that represents the color of Mario's overalls; defaults to `'blue'`.

In other words, if I invoked your `make_mario` function as follows...

`make_mario(canvas, (180, 220), pixel=20, clothes='#75B9BE')`

...your function would draw a Mario with blue-ish clothes, with its top-left coordinate at position (180, 220), with a "pixel" size of 20, wearing blue overalls. After you're done making your function, please uncomment the `make_mario` function calls at the bottom of your `your_task.py` file to test your code. If it works, you should see something similar to the image shown below.

```python
# After you're done making your "make_mario" function, invoke it as follows:
make_mario(canvas, (0, 20))
make_mario(canvas, (420, 250), clothes='#E0607E', pixel=10)
make_mario(canvas, (55, 415), clothes='green', pixel=15)
make_mario(canvas, (350, 115), pixel=5, clothes='#75B9BE')
make_mario(canvas, (420, 400), clothes='#E5F77D', overalls='#75B9BE', pixel=15)
make_mario(canvas, (420, 10), pixel=15)
```

<img class="medium frame" src="/assets/images/tutorials/marios.png" />

## Optional Challenges
1. Create a helper function called `make_row` to further simplify your make_mario function. Then, rather than repeating almost identical code for each row created, you will simply invoke `make_row` 11 times (once for each row).
2. Create a second pixel art function that draws a different image. Google "pixel art simple" to get ideas.
3. The pixel argument is kind of awkward. Arguably a better function design would allow the calling function to specify the width of Mario (as opposed to the individual pixels that comprise him). Therefore, modify the function header so that it requires a `width` (int) parameter instead of a `pixel` parameter. This change means that you will need to derive the appropriate size of the pixel based on the width and the number of columns needed to generate Mario (which is 16). When you're done, update each of the function calls at the bottom of the file so that they pass in a width argument.

## What to Turn In
Please turn in your completed tutorial exercise(s) on Canvas by Wednesday night at midnight. To do this, first zip your entire `tutorial03` folder (with your edited files inside), and then upload your zip file to Canvas. Please ensure that your zip file includes **YOUR CODE**. You can double check by downloading the file once it has successfully submitted to Canvas, and confirming your work is in that ZIP file.
