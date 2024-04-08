---
layout: assignment-two-column
title: Practice with Functions
type: tutorial
abbreviation: Tutorial 2
draft: 0
points: 100
num: 1
canvas_title: Tutorial 2
canvas_id: 1407637
canvas_assignment_group: "Tutorial"
canvas_points_possible: 100
canvas_submission_types: "online_upload"
canvas_allowed_extensions: "py"
due_date: 2024-04-10
---

{: .blockquote-no-margin}
> **LEARNING OBJECTIVES:**
> In order to prepare you for this week's homework, we wanted to use this tutorial session to go over a couple of important logistical and conceptual ideas.
>
> 1. Making sure that the new graphics library is successfully running on your computer
> 1. Creating functions
> 1. Working with parameters & arguments
> 1. Translating specifications into smaller steps that a computer can perform

You need to download and place BOTH of these files in the same folder. You will only need to open / edit the one that's named `tutorial2_template.py`.

<a download class="nu-button" href="{{site.url}}/course-files/tutorials/tutorial2/tutorial2_template.py" target="_blank">
    Tutorial Template File <i class="fas fa-download"></i>
</a>

<br>

<a download class="nu-button" href="{{site.url}}/course-files/tutorials/tutorial2/cs110_t2.py" target="_blank">
    Helper File <i class="fas fa-download"></i>
</a>

Go ahead open the file in IDLE, take a look at it and then run it. You should see something like this:

<img alt="rectangle function output" class="medium frame" src="{{site.url}}/assets/images/tutorial02/rectangle.png" />

> **Note**: If you're on a Mac and are currently in Dark mode, you might see a dark background with white grid lines.
> If you would like to change this either:
>
> 1. <a href="https://support.apple.com/en-us/HT208976" target="_blank"> Use these instructions from Apple to switch to Light mode.</a>
> 2. On line 3, change the value of the `background` input to `"black"`.

* * *

## Getting Started

Scroll down in your file until you see the following:

```python
rectangle(
    100, 
    100,
    50, 
    100,
    color="blue")
```

> **Note**: If you'd like to show line numbers in IDLE, go to the `Options` menu and click on `Show Line Numbers`.

Here's the official documentation of the `rectangle` function:
> `rectangle` is a function used to draw rectangles in a popup window (sometimes called a "canvas"):
>
> 1. `int`: a top-left corner x-coordinate
> 2. `int`: a top-left corner y-coordinate
> 3. `int`: how wide should the rectangle be
> 4. `int`: how tall should the rectangle be
> and one **optional** argument:
> 1. **color** (`str`): the **name** of a color to fill in the shape with

Using the above documentation, think about what that function call does. Talk with a partner and see if you can figure it out.

<details>
<summary>Solution (don't click until you think about it!)</summary>
It asks Python to create a rectangle shape with the following 4 required inputs:
<ul>
<li>a top left corner x-coordinate of 100 (an <code>int</code>)</li>
<li>a top left corner y-coordinate of 100 (an <code>int</code>)</li>
<li>a width of 50 (an <code>int</code>)</li>
<li>a height of 100 (an <code>int</code>)</li>
<li>specify the optional parameter called <code>color</code> to the <code>string</code> <code>"blue"</code></li>
</ul>
</details>
<br>

Next practice using this function by making the following shapes:

* rectangle with its top-left coordinate at `(400, 400)` with width `100` and height `50` that's the default color (i.e. don't specify a color).
* rectangle at `(200, 400)` with width `25` and height `100 + 100` that's `"olive drab"`
* square at `(200, 500)` with width/height `20` that's `"cyan"`

<img alt="rectangle function calls" class="medium frame" src="{{site.url}}/assets/images/tutorial02/rectangles.png" />

* * *

## square

Last time, we talked about how we could write a function to replace the idea of "copy and pasting" code over and over again for repeated actions. However, we can also use functions to think about the concept of _flexibility_. For instance, right now, the `rectangle` can produce any rectangle. But squares are also rectangles (you even drew one above). 

A square is just a special rectangle. It's a rectangle with equal width and height.

Your job is to write a function that draws squares, which we'll call `square`. It will have the following inputs:

> note, in the real world you get to decide on your own names for these inputs, but for simplicity, we're giving you the names you should use here:

1. <code>top_left_x</code>: an x-coordinate for the top-left corner of the square
1. <code>top_left_y</code>: an y-coordinate for the top-left corner of the square
1. <code>width</code>: the width (and also height) of the square.
1. <code>color</code> _(str, optional)_: a name of color of the square, which defaults to blue: `"hot pink"`.

In other words, if we invoked your `square` function as follows...

`square(200, 100, 100, color='blue')`

...your function would draw a 100x100 blue square with its top-left corner at position (200, 100), as pictured above.

To do this, you're going to create a function that accepts the above inputs and then uses them with the `rectangle` function to draw a square. Here's a few of the challenge's you'll need to address.

* First you'll need to write the function header. Here's a little hint of what that'll look like (note, if your browser window is narrow it will look like this is on two lines, but theoretically we put them all on the same line):

```python
def func_name(req_name_1, req_name_2, req_name_3, opt_name=default_value):
    ...
```

* Then you'll need to start on the function body:
  * The `rectangle` function draws rectangles not squares. What is the only difference between rectangles and squares?
  * The `rectangle` function takes as its first four parameters, an x,y coordinate pair and then a width and a height. Your `square` function only accepts a single coordinate pair as a parameter - the top-left, and then only a single side length / width. What value should you use in your `rectangle` function for `height`. Can you use a specific number? or can we use one of the input variables in this space?
  * Once you've got that working, all that's left is to make sure your `color` argument gets passed as the correct optional parameter to `rectangle`. Make sure to pay careful attention to variable names here. (Hint: this one is going to look weird...)
  * Then, just take that command and use it as the function body of your new function definition (remember, it will need to be indented 4 spaces)

```python
def func_name(req_name_1, req_name_2, req_name_3, opt_name=default_value):
    rectangle(function_inputs_go_here)
```

### Test Your New Function

When you've finished with your `square` function, create the pattern pictured below by calling your function with the following arguments (below). Copy the following code and pasting it _**below**_ your function definition. Make sure these function calls are NOT indented as they are not part of your function definition.

```python
# blue block
square(200, 100, 100, color='blue')

# dark green blocks
square(200, 0, 100, color="#5B9279")
square(200, 100, 100, color="#5B9279")
square(200, 200, 100, color="#5B9279")
square(200, 300, 100, color="#5B9279")

# light green blocks
square(300, 0, 50, color="#8FCB9B")
square(300, 100, 50, color="#8FCB9B")
square(300, 200, 50, color="#8FCB9B")
square(300, 300, 50, color="#8FCB9B")
```

<img alt="square function output" class="medium frame" src="{{site.url}}/assets/images/tutorial02/squares.png" />

Note, those weird colors (e.g. `"#8FCB9B"`) are called "hex codes" and are colors represented in a symbol system called "hexadecimal" (think of it like the Dewey Decimal system but for colors). Here is a <a href="https://coolors.co/app" target="_blank">link to a color generator</a> (to browse different hexadecimal color codes, press the spacebar). You can also use regular color names like `"green"`, `"blue"`, `"red"`, etc. (make sure they're strings though!).

* * *

## row_of_squares

Now use your `square` function to write a new function called `row_of_squares` that draws three squares right next to each other.

It needs to have the following inputs:

1. an x-coordinate for the top-left corner of the left-most square
1. an y-coordinate for the top-left corner of the left-most square
1. the width (and also height) of one of the squares.

The left-most square should be `"red"`, the second should be green, and the third should be blue. Now write some function calls to test your new function.

<img alt="row_of_squares function output" class="medium frame" src="{{site.url}}/assets/images/tutorial02/row_of_squares.png" />

* * *

## stack_of_squares

Now use your `square` function to write a new function called `row_of_squares` that draws three squares on top of each other.

It needs to have the following inputs:

1. an x-coordinate for the top-left corner of the top-most square
1. an y-coordinate for the top-left corner of the top-most square
1. the width (and also height) of one of the squares.

The top-most square should be `"red"`, the second should be green, and the third should be blue. Now write some function calls to test your new function.

<img alt="row_of_squares function output" class="medium frame" src="{{site.url}}/assets/images/tutorial02/stack_of_squares.png" />

* * *


## Pictureframe Challenge

Alright, let's take it up a notch.

Your job is to write a function which we'll call `picture_frame`. It will have the following inputs:

1. an x-coordinate for the top-left corner of the square
1. a y-coordinate for the top-left corner of the square
1. the width (and also height) of the outer square (the "frame")
1. the width (and also height) of the inner square (the "picture")
1. **frame_color** _(str, optional)_: a name of color of the square, which defaults to blue: `"blue"`
1. **pic_color** _(str, optional)_: a name of color of the square, which defaults to blue: `"yellow"`

> **Note:** That's a lot of inputs. If you'd like, you can add new lines (returns) after each comma, to make the function header a little more easy to read by spreading it out onto several lines instead of one long one.

Use the above definition to write the function header.

For the function body, you **should use your `square` function**. You're going to draw two squares,

1. The first will be the "frame" square and it will be a square that's the frame and have a top-left coordinate as specified by the function inputs.
2. The second will be the "picture" square. It will be a square that's the pic with the specified width. <mark>You have to calculate it's top-coordinate based off of the top-coordinate of the frame!</mark>.

<details>
<summary>Hint!</summary>
The top-left coordinate of the "pic square" will be the same as the "frame square" but shifted DOWN and to the right by something related to the pic width!
</details>

<details>
<summary>Hint 2!</summary>
If you draw it out...you might see some relationship between the two top-left coordinates... They're offset by half of the difference between the frame and pic widths!
</details>

> Note: the order in which you draw them matters because if you draw the smaller one first and then the bigger one...the bigger one will cover up (or occlude) the smaller one!

If you need more specific examples, checkout the below test cases you should try and their resulting output:

```python
pictureframe(100, 0, 100, 25)
pictureframe(200, 100, 100, 50, frame_color="black", pic_color="white")
pictureframe(100, 200, 100, 50)
pictureframe(0, 100, 100, 25, frame_color="purple", pic_color="white")   
```

<img alt="pictureframe function output" class="medium frame" src="{{site.url}}/assets/images/tutorial02/pictureframes.png" />

You might get stuck on this one. That's okay!

> ### Some Pro Tips
>
> * Always save your python file before running it so that the interpreter "sees" your changes.
> * In order for your interpreter to recognize your file as a Python file, you must give it the **`.py`** file extension (e.g. **`my_program.py`**).
> * Don't forget to name all of your variables "snake case" (all lower case, underscores to separate words).
> * If your code doesn't run, practice reading and trying to understand what the interpreter is telling you. If you see red error text, the computer is trying to tell you where the problem is.

* * *

## Getting Credit for Your Work

### If you're in class

If you're in class you don't need to submit a `.py` file on Canvas. Instead, find one other person in your group that is finished and peer review each other's work. Here are the things to check:

1. Does their code look readable and neat?
1. Can you understand what their code does by reading it?
1. How was their solution different from yours (if at all)?
1. Does their program run and generate the correct test images?

Once you've each taken a look, take a second to debrief. Anything either of you found difficult? Easy? Fun? Mind-blowing? Once you've debriefed, **both of you should fill out this** <a href="https://docs.google.com/forms/d/e/1FAIpQLSctX_8gvtFFdvg_8q7lbzccSgpXFZ2AJiZaI7GbkekM8F8pbQ/viewform?usp=sf_link" target="_blank">attendance Google Form</a>. **NOTE: You will need the NetID of the person's whose code you reviewed.** You're free to go after you're finished once we open the attendance form, though we hope that you might consider sticking around and helping others in your group.

### If you're not in attendance

You can just submit your `.py` file to the Canvas assignment and they will be graded. <mark>Make sure you have exactly followed the instructions.</mark>
