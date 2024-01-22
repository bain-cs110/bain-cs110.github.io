---
layout: assignment-two-column
title: Practice with Compound Shapes
type: tutorial
abbreviation: Tutorial 3
draft: 0
points: 100
num: 3
due_date: 2024-01-24
canvas_title: Tutorial 3
canvas_id: 
canvas_assignment_group: "Tutorial"
canvas_points_possible: 100
canvas_submission_types: "online_upload"
canvas_allowed_extensions: "py"
---

In this tutorial, we're going to make more compound shapes like you did in HW 1. In part 1 (~15 minutes), we'll take a _functional_ approach to making compound shapes, using reporter functions to move shapes relative to one another. In part 2 (~30 minutes), we'll take a more _imperative_ approach, calculating specific coordinates by which to place our shapes.

* * *
## Part 1 - Compound Shapes

First download BOTH of these files and move them into your `cs110` folder. <mark>In order for this activity to work at all, these files must BOTH be in the same folder on your computer.<mark>

<a class="nu-button" href="{{site.url}}/course-files/tutorials/tutorial3/tutorial2_shapes.py" target="_blank">
    Tutorial Shapes Module <i class="fas fa-download"></i>
</a>

<br>

<a class="nu-button" href="{{site.url}}/course-files/tutorials/tutorial3/shapes_activity.py" target="_blank">
    Compound Shapes Activity <i class="fas fa-download"></i>
</a>

Next, open up the `shapes_activity.py` file. If you run it, you'll find our all-too-familiar grid, though a bit larger this time. In last week's HW you only had access to an `oval` function. Then on Friday in-class, we intrdouced the `rectangle` function. Today, WE UNLEASH THE TRUE POWER OF SHAPES. Here, you access to the following functions <mark>(some of them are a little different than they were before):

<details>
  <summary style="font-family: courier">oval</summary>
Oval is a reporter function that both draws the shape on a screen and returns that shape to be used later. It has the following inputs:
<ul>
<li>center (tuple, optional) - where to draw the shape</li>
<li>radius_x (int, optional) - how wide to make the shape</li>
<li>radius_y (int, optional) - how tall to make the shape</li>
<li>color (str, optional) - what color to make the shape</li>
</ul>
</details>

<details>
  <summary style="font-family: courier">circle</summary>
Circle is a reporter function that both draws the shape on a screen and returns that shape to be used later. It has the following inputs:
<ul>
<li>center (tuple, optional) - where to draw the shape</li>
<li>radius (int, optional) - how wide to make the shape</li>
<li>color (str, optional) - what color to make the shape</li>
</ul>
</details>

<details>
  <summary style="font-family: courier">rectangle</summary>
Rectangle is a reporter function that both draws the shape on a screen and returns that shape to be used later. It has the following inputs:
<ul>
<li>top_left (tuple, optional) - where to draw the shape</li>
<li>width (int, optional) - how wide to make the shape</li>
<li>height (int, optional) - how tall to make the shape</li>
<li>color (str, optional) - what color to make the shape</li>
</ul>
</details>

<details>
  <summary style="font-family: courier">square</summary>
Square is a reporter function that both draws the shape on a screen and returns that shape to be used later. It has the following inputs:
<ul>
<li>top_left (tuple, optional) - where to draw the shape</li>
<li>size (int, optional) - how wide to make the shape</li>
<li>color (str, optional) - what color to make the shape</li>
</ul>
</details>

<details>
  <summary style="font-family: courier">triangle</summary>
Triangle is a reporter function that both draws the shape on a screen and returns that shape to be used later. It has the following inputs:
<ul>
<li>bottom_center (tuple, optional) - where to draw the shape</li>
<li>width (int, optional) - how wide to make the shape</li>
<li>height (int, optional) - how tall to make the shape</li>
<li>top_shift (int, optional) - how much to offset the top of the triangle from the bottom_center</li>
<li>color (str, optional) - what color to make the shape</li>
</ul>
</details>

<details>
  <summary style="font-family: courier">polygon</summary>
Polygon is a reporter function that both draws the shape on a screen and returns that shape to be used later. It has the following inputs:
<ul>
<li>points (list, optional) - the points outlining the polygon; <b>this should be a list of tuples</b></li>
<li>color (str, optional) - what color to make the shape</li>
</ul>
</details>

<details>
  <summary style="font-family: courier">line</summary>
Line is a reporter function that both draws the shape on a screen and returns that shape to be used later. It has the following inputs:
<ul>
<li>points (list, optional) - the points outlining the line; <b>this should be a list of tuples</b></li>
<li>color (str, optional) - what color to make the shape</li>
</ul>
</details>

<details>
  <summary style="font-family: courier">arc</summary>
Arc is a reporter function that both draws the shape on a screen and returns that shape to be used later. It has the following inputs:
<ul>
<li>points (list, optional) - the points outlining the line; <b>this should be a list of tuples - I recommend using 3 points.</b></li>
<li>width (int, optional) - what width to make the shape</li>
<li>color (str, optional) - what color to make the shape</li>
<li>line_steps (int, optional) - how many "points" to use to generate the arc</li>
</ul>
</details>

<details>
  <summary style="font-family: courier">star</summary>
Star is a reporter function that both draws the shape on a screen and returns that shape to be used later. It has the following inputs:
<ul>
<li>center (tuple, optional) - where to draw the shape</li>
<li>radius (int, optional) - how big to draw the shape</li>
<li>color (str, optional) - what color to make the shape</li>
</ul>
</details>

<details>
  <summary style="font-family: courier">interpolate_colors</summary>
Interpolate colors is a reporter function that returns a color that is <em>between</em> two given colors.
<ul>
<li>color1 (str) - the color to start with</li>
<li>color2 (str) - the color to end with</li>
<li>frac (float) - how far between the start color (0) and end color (1) to go (e.g. an input of 0.5 would result in a color perfectly in between the two colors)</li>
</ul>
</details>

* * *

### Task 1

Spend a few minutes calling each of these functions. If you were super comfortable with oval, circle, rectangle, and square, skip straight to triangle, polygon, and line. Make sure to experiment with different inputs to get a sense of what sorts of shapes each function can make. Tag team with your team mates and try unique inputs.

* * *

## Layout Functions

Now, in HW 1 (and in Part 2 of this tutorial), we used a bit of math to draw shapes on top of each other. However, we could also use some _layout functions_ to do the same thing! All the shape functions are **reporters** meaning they _return the shape they create back to us_. That means we could store that shape in a variable or use it as an input to another function! In addition to those shape functions we explored in the prior task, this file also has access to a bunch of layout functions:

<details>
  <summary style="font-family: courier">overlay</summary>
Overlay is a reporter function that takes its first input and overlays it on its second input by centering the images before returning the modified first shape.
<ul>
<li>shape1 (Shape) - the shape to be placed on top</li>
<li>shape2 (Shape) - the shape to be placed on the bottom</li>
<li>offset_x (int, optional) - an offset in the x-direction</li>
<li>offset_y (int, optional) - an offset in the y-direction</li>
</ul>
</details>

<details>
  <summary style="font-family: courier">underlay</summary>
Underlay is a reporter function that takes its first input and underlays it on its second input by centering the images before returning the modified first shape.
<ul>
<li>shape1 (Shape) - the shape to be placed on bottom</li>
<li>shape2 (Shape) - the shape to be placed on the top</li>
<li>offset_x (int, optional) - an offset in the x-direction</li>
<li>offset_y (int, optional) - an offset in the y-direction</li>
</ul>
</details>

<details>
  <summary style="font-family: courier">above</summary>
Above is a reporter function that takes its first input and places it above its second input before returning the modified first shape.
<ul>
<li>shape1 (Shape) - the shape to be placed above shape 2</li>
<li>shape2 (Shape) - the shape to be placed below shape 1</li>
<li>offset_x (int, optional) - an offset in the x-direction</li>
<li>offset_y (int, optional) - an offset in the y-direction</li>
</ul>
</details>

<details>
  <summary style="font-family: courier">below</summary>
Below is a reporter function that takes its first input and places it below its second input before returning the modified first shape.
<ul>
<li>shape1 (Shape) - the shape to be placed below shape 2</li>
<li>shape2 (Shape) - the shape to be placed above shape 1</li>
<li>offset_x (int, optional) - an offset in the x-direction</li>
<li>offset_y (int, optional) - an offset in the y-direction</li>
</ul>
</details>

<details>
  <summary style="font-family: courier">beside</summary>
Beside is a reporter function that takes its first input and places it beside its second input before returning the modified first shape.
<ul>
<li>shape1 (Shape) - the shape to be placed beside shape 2</li>
<li>shape2 (Shape) - the shape to be placed beside shape 1</li>
<li>offset_x (int, optional) - an offset in the x-direction</li>
<li>offset_y (int, optional) - an offset in the y-direction</li>
</ul>
</details>

<details>
  <summary style="font-family: courier">duplicate</summary>
Duplicate is a reporter function that takes the shape it is given as input and returns a perfect copy to be used elsewhere.
<ul>
<li>shape (Shape) - the shape to be duplicated</li>
</ul>
</details>

<details>
  <summary style="font-family: courier">rotate</summary>
Rotate is a reporter function that takes the shape it is given as input and rotates it about a given point by a certain number of degrees before returning the modified shape to be used elsewhere.
<ul>
<li>shape (Shape) - the shape to be rotated</li>
<li>degrees (int, optional) - how much to rotate</li>
<li>origin (tuple, optional) - about which point to rotate (defaults to center of shape)</li>
</ul>
</details>

Try out each of these functions with some of the shapes. Here's an example:

```python
circle1 = circle(center=(500, 500), radius=50, color="red")
a_square = square(size=25, color="blue")
a_sqaure = rotate(a_square, degrees=45)
overlay(a_square, circle1)
```
* * *

## Task 3

If you're **working on this tutorial remotely** (or feeling very uncreative), recreate your `bullseye` and `face` functions from the homework using these layout functions.

<details>
  <summary><b>Hint</b></summary>
You can start by just copy and pasting your function's header and body into this file. The initial shape you draw in each function's body (a circle in both cases) stays the same, but now that circle is a reporter, store the result of that function call (like we do in the above example) in a variable. Repeat this for each of the constituent shapes in your compound shapes but get rid of your earlier work where you specified the locations of those other shapes. Now use the overlay function, to position those newer shapes relative to the location of the first shape!
</details>

<br>

Otherwise, see what sorts of cool compound shapes you can make! Start small by making a row of squares. A stack of circles. Then graduate to making a square face (square for face, eyes for rectangle). Or maybe a pair of glasses (circle - rectangle - circle). How about a flag like the [flag of chicago](https://en.wikipedia.org/wiki/Flag_of_Chicago)?

When you feel like you've got the gist of each of the layout functions (note, you'll likely need these for HW 3 so better to get your questions answered now), move on to part 2.

* * * 

## Part 2 - Mario!

Here we're going to design a customizable function that creates an image of [Mario](https://en.wikipedia.org/wiki/Mario) (pictured below). The purpose of this exercise is to practice using parameters, variables, and reporters in order to make your ideas more flexible, customizable, and therefore more useful.

To do this, we're going to walk you through a series of steps to begin trying to "think computationally" -- i.e. finding places where code repeats and modularizing it using variables, functions, and parameters. We only have a few tools that are at our disposal right now, but we'll do our best with what we have so far.

In addition to gaining more practice with functions, there are three takeaways that we hope you will also get from this exercise:

1. That programming is a *process* of formulating solutions over time (versus having everything all planned out at the very the beginning).
2. That programmers are always trying to make their code efficient, readable, and succinct, which usually involves "refactoring" code so that it's not repeating the same lines of code over and over again. This is known as the "DRY Principle" -- " *D*on't *r*epeat *y*ourself."
3. That programmers learn new techniques for solving problems by looking at examples of how other people have solved similar problems. Over time, you too will begin to develop a set of common strategies for solving classes of problems, and that comes by seeing lots of examples (and practicing).

> **Note:** This will sometimes feel tedious. The key to being a good programmer is *working hard now to let us be lazy later*. We'll put in a good amount of work today, finalize it in a function, and then *never worry about it again* because now the computer will take care of it for us! Additionally, as we get more and more programming techniques throughout the quarter, some of these more repetitive tasks can be further automated by the computer...but we gotta start somewhere.

## Understanding the "hardcoded" version of Mario

<a class="nu-button" href="{{site.url}}/course-files/tutorials/tutorial3/mario.py" target="_blank">
    Mario Starter File <i class="fas fa-download"></i>
</a>

Please download and open the `mario.py` file (<mark>Again, make sure it's in the same folder as your other files</mark>) and take a look at it. Note that it is making use of the `square` function we made in class on Friday **with two small changes** (it's included at the top of the file). Instead of using separate inputs for the CENTER x-coordinate and y-coordinate, it's combined those two into a single `tuple` (a sequence of two `int`s) and now it represents a TOP-LEFT coordinate. That means the way we call that function has slightly changed (take a close look at the function calls to `square`).

Scroll down in the file until you see the usual `"YOUR CODE BELOW HERE"` message and take a brief look at the code. It's a long file...but it's super repetitive. Let's see what it does:

<img alt="starting screenshot" class="medium frame" src="{{site.url}}/assets/images/tutorials/tutorial3/mario1.png" />

A few things to pay attention to in this file:

1. This program will always draw a Mario that is the same size and positioned in the exact same place.
1. Each "pixel" is 25 units wide / tall
1. If you were to draw a box around this particular Mario, the top left coordinate would be positioned at `(0, 0)`, and the bottom right coordinate would be positioned at `(300, 375)`.

* * *

## Task 1: Manipulating Mario's clothes and overalls color

Try re-assigning a different color to the `clothes` variable, and running the program (note that Mario's shirt and hat change color). When you're done, please create another variable called `overalls`, and edit the code so that the color of Mario's overalls is determined by the value stored inside the `overalls` variable.

### Using the Find tool

A lot of the times in programming (or really in text-editing too), you might want to find a certain line or word in a really long program. To do this, we can use the **FIND** tool. To do this in IDLE, open the `Edit` menu and select `Find...`. It'll bring up a menu like the below:

<img alt="screenshot of find tool" class="medium frame" src="{{site.url}}/assets/images/tutorials/tutorial3/find.png" />

> **Note**: On some versions of IDLE `Whole Word` is checked by default. You'll want to UNCHECK that option as it looks for blank space at the end of your search string which we don't need right now.

Say you wanted to see which lines of our program pertain to Mario's overalls. Well they start off blue, so you'd open up the Find tool and then search for `"blue"`. Once you click **Find** it will highlight the first occurrence of that search term in the file. If you want to find the next one, then you'd just click **Find Next**.

You can also bring the find tool up quickly via the keyboard shortcut Ctrl-F on a PC or Command-F on a Mac.

* * *

### Task 2: Customize Mario's size

Next, modify the code to make it easier to customize Mario's ***size*** (i.e. the size of each pixel). As the program currently stands, each pixel is hardcoded to 25 pixels for their width. But what if you wanted to draw a mini-Mario, or a really big Mario? You would have to update **every single** call to the `square` function.

To make this process more efficient, create another variable called `pixel` and assign the value `25` (int) to it. Then, figure out a way to use the `pixel` variable to change all of those square sizes.

### Using the Find and Replace Tool

The *Find* tool is really dope. It does a great job of locating things you might want to change. What if you wanted to make a ton of the same change. Say...replace the value `25` with the variable `pixel`. For this sort of thing, you can use the **Find and Replace** tool. Open up the `Edit` menu and then select `Replace...`.

<img alt="Screenshot of find and replace" class="medium frame" src="{{site.url}}/assets/images/tutorials/tutorial3/replace.png" />

> **NOTE**: BE VERY CAREFUL WITH THIS TOOL. Though it's possible to reverse your changes with Undo, remember computers are not particularly smart and will only do *exactly* what you tell them to and no more.

Now, we want to replace all the instances of `25` for the `width` parameter for each `make_square` call. But if we just do `25` in Find and `pixel` in Replace...this tool will replace EVERYWHERE we see a 25 with the text `width`. There's lots of other `25s` (e.g. `325`) in it that we don't want to mess with.

You can actually avoid those cases by selecting the `Whole Word` option in the tool...but that still doesn't fix the problem of other `25s` elsewhere in the document.

However...we've got two extra symbols on either end of our `25` for the `width` input that makes it special: a space (``) on the left hand side and a comma (`,`) on the right hand side. If we instead search for the string `25,` and replace with `pixel,`, then IDLE will only replace the ones we care about! Try a couple of instances using the `Replace + Find` button and once you're sure it's working correctly, try using `Replace All`.

> **NOTE**: At this point, you should have some weird looking Marios (try running your code after doing the above). Why is this? What's going on? Take a look at WHERE the squares are being drawn. Talk with someone next to you and try to figure out why your code does what it does. Brainstorm with the people in your team. What did we miss? Consider the inputs we give to each call to the `square` function...

* * *

### Task 3: Customize Mario's position

Hopefully you've been able to figure out the problem. Mario's position was dependent on how big the squares we were drawing was!

Next, modify the code to make it easier to customize Mario's ***position***. Note that the bottom-left corner of the Mario pixel map is positioned at `(0, 0)` – we'll call this the `origin` (the place where we start drawing Mario). In other words, there is an implicit offset of `(0, 0)` for this Mario. If you wanted to change this offset to, say, `(100, 50)` (move Mario's origin to this location), then you would have to manually add 100 to the value of every x-coordinate and 50 to the value of every y-coordinate.

What we could do, is replace this thinking with a *formula*. For instance, the top row of Mario is all at a y-value of 0; but really it's "row 0". So instead of thinking about row 14 as a series of numbers like we have right now:

```python
# row 0
# blank, pixel (0,0)
# blank, pixel (1,0)
# blank, pixel (2,0)
square(top_left=(75, 0), size=pixel, color=clothes)  # pixel (3, 0)
square(top_left=(100, 0), size=pixel, color=clothes)  # pixel (4, 0)
...
```

we could think about it in terms of a formula based on what row and column the pixel represents, the `origin` we're drawing around, and the `pixel` size of the Mario. So say if we set some variables, `origin`, `x`, and `y`...

```python
origin = (0,0)
x = origin[0]
y = origin[1]

# row 0
# blank, pixel (0,0)
# blank, pixel (1,0)
# blank, pixel (2,0)
square(top_left=(x + 3 * pixel, y * pixel), size=pixel, color=clothes)  # pixel (3, 0)
square(top_left=(x + 4 * pixel, y * pixel), size=pixel, color=clothes)  # pixel (4, 0)
square(top_left=(x + 5 * pixel, y * pixel), size=pixel, color=clothes)  # pixel (4, 0)
...
```

If we do it this way, suddenly we no longer care about exactly which numbers to put in those slots, instead Python will do all of that work for us! Of course...this means we'd have to go through each `(x,y)` coordinate and enter the formula for that particular pixel. That seems like a lot of extra work. Really all we need is a machine that calculates the coordinates for us...and we just change the inputs to it. Wouldn't it be great if there was a way to write a machine that **returns some value** in Python...

```python
def get_xy(origin, pixel_size, mario_coord):
    x = origin[0] # extract the x-coordinate
    y = origin[1] # extract the y-coordinate

    row = mario_coord[0] # extract the row number
    col = mario_coord[1] # extract the col number

    new_x = x + row * pixel_size # calculate the new x
    new_y = y + col * pixel_size # calculate the new y
```

Wow! That's convenient! This thing takes in a tuple `origin`, a int `pixel_size`, and a tuple `mario_coord` and calculates the `new_x` and `new_y` we need. **But**, there's a problem. This function is supposed to be a reporter...but the `return` statement is missing. Copy and paste this code right below the lines that set our color variables. Now fix the function so that it **returns** a tuple containing the `new_x` and `new_y`. (Hint: to make a tuple of data, we just say `(first_piece, second_piece)`).

Once we have this function working, then all we need to do is replace those `(x,y)` coordinates in each `square` call like this:

```python
# row 0
# blank, pixel (0,0)
# blank, pixel (1,0)
# blank, pixel (2,0)
square(top_left=get_xy(origin, pixel, (3,0)), size=pixel, color=clothes)  # pixel (3, 0)
square(top_left=get_xy(origin, pixel, (4,0)), size=pixel, color=clothes)  # pixel (4, 0)
square(top_left=get_xy(origin, pixel, (5,0)), size=pixel, color=clothes)  # pixel (4, 0)
...
```

You can think of this function as a *helper* or *translation* function that is built to do one thing and one thing only. Use the example above to complete row 0, and also update rows 1, 2 to the same syntax.

Once you get 0, and 1 done (and you feel like you've got a handle for WHY that works) checkout the hint below for the remaining rows. Yes, you can copy and paste the remaining rows...but only do so if you understand why this works. Otherwise, it's time to ask some questions!

<a class="nu-button" href="{{site.url}}/course-files/tutorials/tutorial02/hint_1.py" target="_blank">
    Hint<i class="fas fa-download"></i>
</a>

* * *

### Task 4: Create a function so that you can instantiate many Marios

When you're done, you have successfully made your Mario program customizable. However, if you wanted to make, say, 5 Marios, you would have to copy all of your code 5 times (and change the variables for each Mario). This is inefficient. In general, any time you're copying the same code over and over again, it makes sense to create a function. So, let's make that happen. For your final task, please create a `mario` function that accepts the following arguments:

1. **origin** *(tuple)*: a tuple -- an point, an (x, y) coordinate -- that defines the top-left position of the rectangle bounding your picture of Mario. The first element in the tuple refers to the x-coordinate and the second element in the tuple refers to the y-coordinate.
1. **pixel** *(int, optional)*: an int that specifies the width (and also height) of the pixel; defaults to 25.
1. **clothes** *(str, optional)*: a string that represents the color Mario's clothes; defaults to `'red'`.
1. **overalls** *(str, optional)*: a string that represents the color of Mario's overalls; defaults to `'blue'`.
1. **accessories** *(str, optional)*: a string that represents the color of Mario's accessories; defaults to `'brown'`.
1. **tone** *(str, optional)*: a string that represents the color of Mario's tone; defaults to `'bisque3'`.
1. **features** _(str, optional)_: a string that represents the color of Mario's features; defaults to `'black'`.
1. **buttons** _(str, optional)_: a string that represents the color of Mario's buttons; defaults to `'gold'`.

In other words, if I invoked your `mario` function as follows...

`mario((180, 220), pixel=20, clothes='olive drab')`

...your function would draw a Mario with olive-drab clothes, with its top_left coordinate at position (180, 220), with a "pixel" size of 20, wearing blue overalls.

After you're done making your function, add some `mario` function calls at the bottom of your `your_task.py` file to test your code. You can use these as examples if you'd like.

```python
# After you're done making your "mario" function, invoke it as follows:
mario((0, 20))
mario((420, 250), clothes='#E0607E', pixel=10)
mario((55, 415), clothes='green', pixel=15)
mario((350, 115), pixel=5, clothes='#75B9BE')
mario((420, 400), clothes='#E5F77D', overalls='#75B9BE', pixel=15)
mario((420, 10), pixel=15)
```

> **Note**: Wondering what those weird colors are? Those are 'hexcolors' which are colors represented in a number system called hexadecimal. You can use any of them! [See here to explore](https://htmlcolorcodes.com)!

<img class="medium frame" src="{{site.url}}/assets/images/tutorials/tutorial3/marios.png" />

Make some other custom marios that use different inputs to make sure your function works as expected. I'd suggest also trying out the random functions as inputs to these things as practice for the homework!

* * *

## Optional Challenges

1. Create a helper function called `make_row` to further simplify your `mario` function. Then, rather than repeating almost identical code for each row created, you will simply invoke `make_row` 15 times (once for each row).
2. Create a second pixel art function that draws a different image. Google "pixel art simple" to get ideas.
3. The pixel argument is kind of awkward. Arguably a better function design would allow the calling function to specify the width of Mario (as opposed to the individual pixels that comprise him). Therefore, modify the function header so that it requires a `width` (int) parameter instead of a `pixel` parameter. This change means that you will need to derive the appropriate size of the pixel based on the width and the number of columns needed to generate Mario (which is 13). When you're done, update each of the function calls at the bottom of the file so that they pass in a width argument.

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

You can just submit <mark>BOTH</mark> your `.py` file to the Canvas assignment and they will be graded.