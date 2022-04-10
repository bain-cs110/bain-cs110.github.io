---
layout: assignment-two-column
title: Practice with Functions
type: tutorial
abbreviation: Tutorial 2
draft: 0
points: 3
num: 2
description:
    - Practice creating custom functions
    - Intro to Tkinter
due_date: 2022-04-13
---

<a class="nu-button" href="/course-files/tutorials/tutorial02_template.zip" target="_blank">
    Tutorial Starter Files <i class="fas fa-download"></i>
</a>

This tutorial is a warmup for HW 2. Please download the starter files and complete the instructions outlined below.

If you've never done this before, there are a lot of little typing / logic / conceptual mistakes that **everyone** makes. Please go to Office Hours or post on Campuswire questions that you have about defining these functions. Additionally, you should feel free to ask questions during class as well.

{: .blockquote-no-margin}
> **LEARNING OBJECTIVES:**
> In order to prepare you for this week's homework, we wanted to use this tutorial session to go over a couple of important logistical and conceptual ideas.
>
> 1. Making sure that TKinter is successfully running on your machine
> 1. Creating functions
> 1. Working with parameters & arguments
> 1. Translating specifications into smaller steps that a computer can perform

## Required: Square Challenge
Please open `square_challenge.py` in IDLE, which is located in the `tutorial02` folder. Take a look at it and then run it. You should see something like this:

<img class="small frame" src="/assets/images/tutorial01/before1.png" />

### A. Create a "make_square" function
In the `square_challenge.py` file, write a function called `make_square` that accepts the following arguments:

1. **canvas** *(Canvas)*: a tkinter Canvas object where you want the square to be drawn.
1. **top_left** *(tuple)*: a tuple -- an point, an (x, y) coordinate -- that defines the top-left position of the square. The first element in the tuple refers to the x-coordinate and the second element in the tuple refers to the y-coordinate.
1. **width** *(int)*: an int that specifies the width (and also height) of the square.
1. **fill_color** *(str, optional)*: a string that represents the color of the square, defaults to blue: `"blue"`.

In other words, if we invoked your `make_square` function as follows...

`make_square(canvas, (100, 100), 100, fill_color='blue')`

...your function would draw a 100x100 blue square with its top-left coordinate at position (100, 100), as pictured above.
> **Note on Tuples:**
> We'll be talking about what a `tuple` is during Monday's lecture. However, the idea is simple: just like an (x,y) coordinate a tuple is a way of storing multiple pieces of data (namely two integers representing an x and a y coordinate) inside of a single variable. The way we define a tuple is by starting with a left-parenthesis, adding as many "elements" as we'd like, each separated by a comma, and then ending with a right-parenthesis.
> <br> <br>
> For example `my_coordinate = (1,2)` is a single variable that contains two different integers in it. If we then want to access for instance, the x-coordinate of that `my_coordinate` variable, we have to use some extra notation:<br><br>
> `x_coordinate = my_coordinate[0]`<br>
>
> `y_coordinate = my_coordinate[1]`
> <br><br>
> Though there's more to it...that's enough to get you started if you want to work on the Tutorial before Monday.

### B. Use your "make_square" function to create the drawing pictured below
When you've finished with your `make_square` function, create the pattern pictured below by calling your function with the following arguments (below). Copy the following code and pasting it ***below*** your function definition, but ***above*** the helpers.make_grid(...) function:

```python
# center blue block
make_square(canvas, (100, 100), 100)

# dark green blocks
make_square(canvas, (0, 0), 100, fill_color='#5B9279')
make_square(canvas, (200, 0), 100, fill_color='#5B9279')
make_square(canvas, (0, 200), 100, fill_color='#5B9279')
make_square(canvas, (200, 200), 100, fill_color='#5B9279')

# light green blocks
make_square(canvas, (50, 200), 50, fill_color='#8FCB9B')
make_square(canvas, (200, 200), 50, fill_color='#8FCB9B')
make_square(canvas, (50, 50), 50, fill_color='#8FCB9B')
make_square(canvas, (200, 50), 50, fill_color='#8FCB9B')
```

<img class="small frame" src="/assets/images/tutorial01/after1.png" />

Note, those weird colors (e.g. `'#8FCB9B'`) are called "hex codes" and are colors reprsented in a symbol system called "hexidecimal" (think of it like the Dewey Decimal system but for colors.) Here is a <a href="https://coolors.co/app" target="_blank">link to a color generator</a> (to browse different hexidecimal color codes, press the spacebar). You can also use regular color names like `"green"`, `"blue"`, `"red"`, etc. (make sure they're strings though!).

### C. Use your "make_square" function to create your own drawing

Now, alter the code above to make your own drawing (anything that you can compose with squares). Feel free to alter the colors, positions, and sizes of your squares.


## More Practice (if you need it): Triangle Challenge
Please open `triangle_challenge.py` in IDLE (also located in the `tutorial02` folder). Take a look at it and then run it. You should see something like this:

<img class="medium frame" src="/assets/images/tutorial01/before2.png" />

### A. Create a "make_triangle_left" function
In the `triangle_challenge.py` file, create a function called `make_triangle_left` that draws a 45-45-90-degree right triangle, where the right angle is positioned at the bottom-left corner (as pictured above). It accepts the following arguments:

1. **canvas** *(Canvas)*: a tkinter Canvas object where you want the triangle to be drawn.
1. **bottom_left** *(tuple)*: a tuple -- an point, an (x, y) coordinate -- that defines the bottom-left position of the triangle. The first element in the tuple refers to the x-coordinate and the second element in the tuple refers to the y-coordinate.
1. **height** *(int)*: an int that specifies the height / length of the triangle.
1. **fill_color** *(str, optional)*: a string that represents the color of the triangle, defaults to a light blue: `#84A9C0`.


### B. Create a "make_triangle_right" function
Below the make_triangle_left function that you just made, create a function called `make_triangle_right` that draws a 45-45-90-degree right triangle, where the right angle is positioned at the bottom-right corner.

It accepts the following arguments:

1. **canvas** *(Canvas)*: a tkinter Canvas object where you want the triangle to be drawn.
1. **bottom_right** *(tuple)*: a tuple -- an point, an (x, y) coordinate -- that defines the bottom-left position of the triangle. The first element in the tuple refers to the x-coordinate and the second element in the tuple refers to the y-coordinate.
1. **height** *(int)*: an int that specifies the height / length of the triangle.
1. **fill_color** *(str, optional)*: a string that represents the color of the triangle, defaults to a light blue: `#84A9C0`.

### C. Use your "make_triangle_left" and "make_triangle_right" functions to create a drawing
When you've finished making your `make_triangle_left` and `make_triangle_right` functions, invoke these functions to create the pattern pictured below by copying the following code and pasting it ***below*** your function definition, but ***above*** the helpers.make_grid(...) function:

```python
# row 1
make_triangle_right(canvas, (100, 100), 100, fill_color='#5B9279')
make_triangle_left(canvas, (100, 100), 100, fill_color='#5B9279')
make_triangle_right(canvas, (300, 100), 100, fill_color='#5B9279')
make_triangle_left(canvas, (300, 100), 100, fill_color='#5B9279')
make_triangle_right(canvas, (500, 100), 100, fill_color='#5B9279')

# row 2
make_triangle_left(canvas, (0, 200), 100)
make_triangle_right(canvas, (200, 200), 100)
make_triangle_left(canvas, (200, 200), 100)
make_triangle_right(canvas, (400, 200), 100)
make_triangle_left(canvas, (400, 200), 100)

# row 3
make_triangle_right(canvas, (100, 300), 100, fill_color='#8FCB9B')
make_triangle_left(canvas, (100, 300), 100, fill_color='#8FCB9B')
make_triangle_right(canvas, (300, 300), 100, fill_color='#8FCB9B')
make_triangle_left(canvas, (300, 300), 100, fill_color='#8FCB9B')
make_triangle_right(canvas, (500, 300), 100, fill_color='#8FCB9B')
```

<img class="medium frame" src="/assets/images/tutorial01/after2.png" />

## What to Turn In
Please turn in your completed tutorial exercise(s) ON CANVAS by Wednesday night at midnight. To do this, please zip your `tutorial02` folder (i.e. create a new tutorial02.zip file), which includes your edited files, and upload it to Canvas. Please be careful that you **don't just upload the original starter files**, but that your zip file includes **YOUR CODE**.  
