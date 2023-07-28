---
layout: assignment-two-column
title: Practice with Functions
type: tutorial
abbreviation: Tutorial 1
draft: 0
points: 100
num: 2
canvas_id: 1224390
description:
    - Practice creating custom functions
    - Intro to Tkinter
due_date: 2023-04-12
---

This tutorial is a warmup for HW 2. Please download the starter file and complete the instructions outlined below.

If you've never done this before, there are a lot of little typing / logic / conceptual mistakes that **everyone** makes. Please pay careful attention and help each other complete the assignment!

<a class="nu-button" href="{{site.url}}/course-files/tutorials/tutorial01/tutorial01_template.py" target="_blank">
    Tutorial Starter File<i class="fas fa-download"></i>
</a>

Once you've gotten the file, rename it to `tutorial_01.py` and move it into your `cs110` folder.

{: .blockquote-no-margin}
> **LEARNING OBJECTIVES:**
> In order to prepare you for this week's homework, we wanted to use this tutorial session to go over a couple of important logistical and conceptual ideas.
>
> 1. Making sure that TKinter is successfully running on your machine
> 1. Creating functions
> 1. Working with parameters & arguments
> 1. Translating specifications into smaller steps that a computer can perform

Go ahead open the file in IDLE, take a look at it and then run it. You should see something like this:

<img class="medium frame" src="{{site.url}}/assets/images/tutorial01/before.png" />


> **Note**: If you're on a Mac and are currently in Dark mode, you might see the below:
> 
> <img class="medium frame" src="{{site.url}}/assets/images/tutorial01/darkmode.png" />
> 
> For some reason, `Tkinter` switches the colors white and black when your Mac is in
> dark mode. To fix this, you have two options:
> 1. <a href="https://support.apple.com/en-us/HT208976" target="_blank"> Use these instructions from Apple to switch to Light mode.</a>
> 2. On line 3, change the value of the `background` input to `"black"`.

* * *

## Getting Started 

Scroll down in your file until you see the following:

```python
##?#!#?# SQUARE CHALLENGE
```

Below that you'll see a function call to a _method_ of a new datatype we call a `Canvas`. Remember how `shelly` was a turtle and we could ask them to go forward by calling the method `shelly.forward(100)`? This is just like that but for a different kind of object, a `Canvas` instead of a `Turtle`. And rather than call our `Canvas` `shelly`, we'll call it `the_canvas` instead.

> **Note**: If you'd like to show line numbers in IDLE, go to the `Options` menu and click on `Show Line Numbers`.

Here's the official documentation of the `create_rectangle` method:
> `create_rectangle` is a method of the data type `Canvas` meant to draw recetangles. It has 4 required arguments:
> 1. `int`: a bottom-left corner x-coordinate
> 2. `int`: a bottom-left corner y-coordinate
> 3. `int`: a top-right corner x-coordinate
> 4. `int`: a top-right corner x-coordinate
> and one **optional** argument:
> 1. **fill** (`str`): the name of a color to fill in the shape with

So now let's take a look at the function call that starts on line 12:

```python
the_canvas.create_rectangle(
    100, 
    100,
    200, 
    200,
    fill="blue")
```

Using the above documentation, think about what that function call does. Talk with your partner and see if you can figure it out.

* * *

## Square Challenge

Hopefully, you and your partner discussed something along the lines of the following:

> Line 12 asks `the_canvas` to create a rectangle shape with the following 4 required inputs:
> * a bottom left corner x-coordinate of 100 (an `int`)
> * a bottom left corner y-coordinate of 100 (an `int`)
> * a top right corner x-coordinate of 200 (an `int`)
> * a top right corner y-coordinate of 200 (an `int`)
> and also provide one optional input:
> * specify the optional parameter called `fill` to the `string` `"blue"`
> 
> Or if we're not interested in being overly verbose, draw a blue rectange with the bottom-left corner at `(100, 100)`, the top-right corner at ``(200, 200)`, and make it blue.

Sweet! That's cool. We can make any sort of rectangle we want! See if you can reproduce the below image by modifying the inputs given to the `create_rectangle` function (ignore the triangle for now, we'll get there later):

<img class="medium frame" src="{{site.url}}/assets/images/tutorial01/modified.png" />


### Writing our Own Version

Last time, we talked about how we could write a function to replace the idea of "copy and pasting" code over and over again for repeated actions. However, we can also use functions to think about the concept of _accessibility_. For instance, right now, the `create_rectangle` method requires the user to do a little Cartesian (i.e. `(x,y)`) coordinate math. What if we wanted to remove that aspect from our function completely – that is, write our own function that took that "manual" math out of the equation?

That's a great idea I heard you exclaim! After all, let's say we just want to draw a square. There's no need to specify both the bottom-left hand corner and top-right hand corner of a square. We just need one of those (let's just say the bottom-left hand corner) and a side length! So...let's get to function writing!

Your job is to write this function which we'll call `make_square`. It will have the following inputs:
> note, in the real world you get to decide on your own names for these inputs, but for simplicity, we're giving you the names you should use here:
1. **a_canvas** *`Canvas`*: the canvas where you want the square to be drawn 
1. **bottom_left_x** *(int)*: an x-coordinate for the bottom-left corner of the square
1. **bottom_left_y** *(int)*: a y-coordinate for the bottom-left corner of the square
1. **width** *(int)*: the width (and also height) of the square.
1. **color** *(str, optional)*: a name of color of the square, which defaults to blue: `"blue"`.

In other words, if we invoked your `make_square` function as follows...

`make_square(the_canvas, 100, 100, 100, color='blue')`

...your function would draw a 100x100 blue square with its bottom-right corner at position (100, 100), as pictured above.

To do this, you're going to create a function that accepts the above inputs and then uses them with the `create_rectangle` to draw a square. Here's a few of the challenge's you'll need to address.
* First you'll need to write the function header. Here's a little hint of what that'll look like (note, if your browser window is narrow it will look like this is on two lines, but theoretically we put them all on the same line):
```python
def func_name(req_name_1, req_name_2, req_name_3, req_name_4, opt_name=default_value):
```
* Then you'll need to start on the function body:
  * The `create_rectangle` function draws rectangles not squares. What is the only difference between rectangles and squares?
  * The `create_rectangle` function takes as its first four parameters, two x,y coordinate pairs - one for the top left of the rectangle and the other for the bottom right of the rectangle. Your `make_square` function only accepts a single coordinate pair as a parameter - the bottom-left. Your job will be to teach your program how to take the bottom-left coordinate and side length provided to your function to calculate the top-right coordinate you'll use with the `create_rectangle` function
  * Once you've got that working, all that's left is to make sure your `color` argument gets passed as the correct optional parameter to `create_rectangle`. Make sure to pay careful attention to variable names here.
  * Then, just take that command and use it as the function body of your new function definition (remember, it will need to be indented 4 spaces)
```python
def func_name(req_name_1, req_name_2, req_name_3, req_name_4, opt_name=default_value):
        a_canvas.create_rectangle(function_inputs_go_here)
```

> **HINT**: If you think you've got the function definition's body right...but don't see anything drawn to the screen double check your `Canvas` object. In the function body you need to use the inputted `a_canvas` versus what we use OUTSIDE the function defintion `the_canvas`. We do this so that in theory we could draw to ANY canvas someone asked us to!

### Test Your New Function!
When you've finished with your `make_square` function, create the pattern pictured below by calling your function with the following arguments (below). Copy the following code and pasting it ***below*** your function definition. Make sure these function calls are NOT indented as they are not part of your function definition.

```python
# center blue block
make_square(the_canvas, 100, 100, 100)

# dark green blocks
make_square(the_canvas, 0, 0, 100, color="#5B9279")
make_square(the_canvas, 200, 0, 100, color="#5B9279")
make_square(the_canvas, 0, 200, 100, color="#5B9279")
make_square(the_canvas, 200, 200, 100, color="#5B9279")

# light green blocks
make_square(the_canvas, 50, 200, 50, color="#8FCB9B")
make_square(the_canvas, 200, 200, 50, color="#8FCB9B")
make_square(the_canvas, 50, 50, 50, color="#8FCB9B")
make_square(the_canvas, 200, 50, 50, color="#8FCB9B")
```

<img class="medium frame" src="{{site.url}}/assets/images/tutorial01/after_square.png" />

Note, those weird colors (e.g. `"#8FCB9B"`) are called "hex codes" and are colors reprsented in a symbol system called "hexidecimal" (think of it like the Dewey Decimal system but for colors). Here is a <a href="https://coolors.co/app" target="_blank">link to a color generator</a> (to browse different hexidecimal color codes, press the spacebar). You can also use regular color names like `"green"`, `"blue"`, `"red"`, etc. (make sure they're strings though!).

* * *

## Square Face Challenge

Now that we've got a handle on our own `make_square` function, we **never** have to worry about how to draw a square again. We just call up our function and rely on it to remember the details.

Now your job is to write a function which we'll call `make_squareface`. It will have the following inputs:
> note, in the real world you get to decide on your own names for these inputs, but for simplicity, we're giving you the names you should use here:

1. **a_canvas** _(`Canvas`_): the canvas where you want the square to be drawn
1. **bottom_left_x** _(int)_: an x-coordinate for the bottom-left corner of the face
1. **bottom_left_y** _(int)_: a y-coordinate for the bottom-left corner of the face
1. **width** _(int)_: the width (and also height) of the face.
1. **eye_color** _(str, optional)_: a name of color of the square, which defaults to blue: `"blue"`.
1. **face_color** _(str, optional)_: a name of color of the square, which defaults to yellow: `"yellow"`.

> **Note:** That's a lot of inputs. If you'd like, you can add new lines (returns) after each comma, to make the function header a little more easy to read by spreading it out onto several lines instead of one long one.

This function will use three calls to your `make_square` function to create a face (see below)! First, you'll make the big square for the face, then you'll make two more squares for the eyes. In the below, we draw a square face at a coordinate of `(400, 100)`, a width of `100`, a eye color of `"purple"` and a face color of `"gray"`.

<img class="medium frame" src="{{site.url}}/assets/images/tutorial01/squareface.png" />

The tricky part here is that we the location of the eyes...depends on the location of the face! And not only that...the size of the eyes depends on the size of the face!

That means, when you draw the two eyes, you need to teach Python how to calculate each one's bottom_left coordinates AND each one's size. Try drawing it out on a piece of paper and see if you can get it working. Hint: use a simple ratio of the face's `width` for the eye's size and use another ratio of the `width` to _add_ to the `bottom_left_x` and `bottom_left_y` coordinates. If you get stuck...you can use the below but please try your best before revealing!:

<details>
  <summary>Eye Size</summary>
 For the eye's size, just use the width of the face divided by 4: <pre>width / 4</pre>
</details>

<br>

<details>
  <summary>Eye Y-Coordinates</summary>
 Since both eye's are at the same vertical level, they'll have the same y-coordinate. You can use the following formula to shift the eyes "up" above the center of the square: <pre>bottom_left_y + width * 2 / 3</pre>
</details>

<br>

<details>
  <summary>Left Eye X-Coordinate</summary>
For the left eye, it needs to be to the left of the center of the square...say 1/8 of the way across the square! <pre>bottom_left_x + width * 1 / 8</pre>
</details>

<br>

<details>
  <summary>Right Eye X-Coordinate</summary>
For the right eye, it needs to be to the RIGHT of the center of the square...say 1/8 of the way past the half point the square! <pre>bottom_left_x + width * 5 / 8`</pre>
</details>

<br>

This time...we're not going to give you the function call to `make_squareface`. Use the inputs above to make a function call to your new function! Remember, first you need the function's name, then a `(`, then the inputs separated by commas (first go the required ones; then the optional ones with their keywords), and finally a `)`. Try to model it off the example ones we gave you for `make_square`.

> Note: the order in which you draw them matters because if you draw the smaller one first and then the bigger one...the bigger one will cover up (or occlude) the smaller one!

Once you've got the test face working, see if you can generate some other faces in other parts of the canvas!

* * *

## Optional: Pictureframe Challenge

> Note: If you're completing this remotely, you really should do this one and the triangle one to make sure you understand the process. 

Alright, now that we're experts in writing our own functions...let's do it again! This time we're going to use our `make_square` function inside ANOTHER custom function that draws a picture frame (a square with a smaller square laid on top). Scroll down in your file until you see `##?#!#?# PICTUREFRAME CHALLENGE`.

Your job is to write a function which we'll call `make_picture_frame`. It will have the following inputs:
> note, in the real world you get to decide on your own names for these inputs, but for simplicity, we're giving you the names you should use here:
1. **a_canvas** *`Canvas`*: the canvas where you want the square to be drawn 
1. **bottom_left_x** *(int)*: an x-coordinate for the bottom-left corner of the square
1. **bottom_left_y** *(int)*: a y-coordinate for the bottom-left corner of the square
1. **width** *(int)*: the width (and also height) of the square.
1. **frame_width** *(int)*: the width of the picture frame
1. **frame_color** *(str, optional)*: a name of color of the square, which defaults to blue: `"blue"`.
1. **pic_color** *(str, optional)*: a name of color of the square, which defaults to blue: `"yellow"`.

> **Note:** That's a lot of inputs. If you'd like, you can add new lines (returns) after each comma, to make the function header a little more easy to read by spreading it out onto several lines instead of one long one.

This looks pretty similar to our `make_square` function with the exception of a few extra inputs (and some renamed ones). Use the above definition to write the function header.

For the function body, you **should use your `make_square` function**. You're going to draw two squares,
1. The first will be the "frame" square and it will be a square of size `width` and have a bottom-left coordinate as specified by the function inputs.
2. The second will be the "picture" square. It will be a square of size `width - frame_width` and will have a bottom-left coordinate that is the same as the bottom-left coordinate of the "frame square" **but shifted up and to the right by `frame_width`**!

> Note: the order in which you draw them matters because if you draw the smaller one first and then the bigger one...the bigger one will cover up (or occlude) the smaller one!

If you need more specific examples, checkout the below test cases you should try and their resulting output.

```python
make_pictureframe(the_canvas, 100, 0, 100, 10)
make_pictureframe(the_canvas, 200, 100, 100, 20, frame_color="black", pic_color="white")
make_pictureframe(the_canvas, 100, 200, 100, 25)
make_pictureframe(the_canvas, 0, 100, 100, 15, frame_color="purple", pic_color="white")
```

<img class="medium frame" src="{{site.url}}/assets/images/tutorial01/after_overlay.png" />

* * *

## Optional: Triangle Challenge

Scroll down in your file until you see the following:

```python
##?#!#?# TRIANGLE CHALLENGE
```

If you recall from earlier, the right side of our canvas has a dope triangle on it. Let's tackle that one now.

<img class="medium frame" src="{{site.url}}/assets/images/tutorial01/before.png" />

This challenge asks you to do the same thing as the first challenge, but instead of designing a function `make_square` using TKinter's `create_rectangle`, you"ll design `make_triangle_left` and `make_triangle_right` to use TKinter"s `create_polygon` function. Here, instead of calculating just one extra coordinate point...you'll have to calculate two more coordinates and use all three coordinates as input to the `create_polygon` function.

### Create a left triangle function

In the Triangle Challenge section of the file, create a function called `make_triangle_left` that draws a 45-45-90-degree right triangle, where the right angle is positioned at the bottom-left corner. It accepts the following arguments:

1. **a_canvas** *(Canvas)*: where you want the triangle to be drawn.
1. **bottom_left_x** *(int)*: defines the x-coordinate of the bottom-left position of the triangle.
1. **bottom_left_y** *(int)*: defines the y-coordinate of the bottom-left position of the triangle.
1. **height** *(int)*: specifies the height / length of the triangle.
1. **color** *(str, optional)*: represents the color of the triangle, defaults to a light blue: `"#84A9C0"`.

### Create a right triangle function
Below the make_triangle_left function that you just made, create a function called `make_triangle_right` that draws a 45-45-90-degree right triangle, where the right angle is positioned at the bottom-right corner.

It accepts the following arguments:

1. **a_canvas** *(Canvas)*: where you want the triangle to be drawn.
1. **bottom_right_x** *(int)*: defines the x-coordinate of the bottom-left position of the triangle.
1. **bottom_right_y** *(int)*: defines the y-coordinate of the bottom-left position of the triangle.
1. **height** *(int)*: specifies the height / length of the triangle.
1. **color** *(str, optional)*: represents the color of the triangle, defaults to a light blue: `"#84A9C0"`.

### Test Your Functions
When you've finished making your `make_triangle_left` and `make_triangle_right` functions, invoke these functions to create the pattern pictured below by copying the following code and pasting it ***below*** your function definition, above the thing that says `# YOUR CODE ABOVE HERE` and make sure it is NOT indented:

```python
# row 1
make_triangle_right(the_canvas, 400, 0, 100, color="#5B9279")
make_triangle_left(the_canvas, 400, 0, 100, color="#5B9279")
make_triangle_right(the_canvas, 600, 0, 100, color="#5B9279")

# row 2
make_triangle_left(the_canvas, 300, 100, 100)
make_triangle_right(the_canvas, 500, 100, 100)
make_triangle_left(the_canvas, 500, 100, 100)

# row 3
make_triangle_right(the_canvas, 400, 200, 100, color="#8FCB9B")
make_triangle_left(the_canvas, 400, 200, 100, color="#8FCB9B")
```

<img class="medium frame" src="{{site.url}}/assets/images/tutorial01/after_both.png" />

* * *

## Getting Credit for Your Work

If you're in class you don't need to submit a `.py` file on Canvas. Instead, find one other person in your group that is finished and peer review each other's work. Here are the things to check:

1. Does their code look readable and neat?
1. Can you understand what their code does by reading it?
1. How was their solution different from yours (if at all)?
1. Does their program run and generate the correct test images?

Once you've each taken a look, take a second to debrief. Anything either of you found difficult? Easy? Fun? Mind-blowing? Once you've debriefed, **both of you should fill out this** <a href="https://forms.gle/TfwheoqHmuRTY4UcA" target="_blank">attendance Google Form</a>. **NOTE: You will need the NetID of the person's whose code you reviewed.** You're free to go after you're finished, though we hope that you might consider sticking around and helping others in your group.

If you're completing it remotely, please submit your `.py` file on Canvas.