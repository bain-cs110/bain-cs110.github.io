---
layout: assignment-two-column
title: Practice with Parameters & Arguments
type: tutorial
abbreviation: Tutorial 2
draft: 0
points: 100
num: 3
canvas_id: 1224391
description:
  - Positional parameters/arguments
  - Keyword parameters/arguments
due_date: 2023-04-19
---

In this tutorial, you are going to design a customizable function that creates an image of [Mario](https://en.wikipedia.org/wiki/Mario) (pictured below). The purpose of this exercise is to help you figure out how to use parameters and variables in order to make your ideas more flexible, customizable, and therefore more useful.

To do this, we're going to walk you through a series of steps to begin trying to "think computationally" -- i.e. finding places where code repeats and modularizing it using variables, functions, and parameters. We only have a few tools that are at our disposal right now, but just note that this code in this exercise can be further simplified in a few weeks when we learn more about loops.

In addition to gaining more practice with functions, there are three takeaways that we hope you will also get from this exercise:

1. That programming is a *process* of formulating solutions over time (versus having everything all planned out at the very the beginning).
2. That programmers are always trying to make their code efficient, readable, and succinct, which usually involves "refactoring" code so that it's not repeating the same lines of code over and over again. This is known as the "DRY Principle" -- " *D*on't *r*epeat *y*ourself."
3. That programmers learn new techniques for solving problems by looking at examples of how other people have solved similar problems. Over time, you too will begin to develop a set of common strategies for solving classes of problems, and that comes by seeing lots of examples (and practicing).

> **Note:** This will sometimes feel tedious. The key to being a good programmer is _working hard now to let us be lazy later_. We'll put in a good amount of work today, finalize it in a function, and then _never worry about it again_ because now the computer will take care of it for us! Additionally, as we get more and more programming techniques throughout the quarter, some of these more repetitive tasks can be further automated by the computer...but we gotta start somewhere.

## Understanding the "hardcoded" version of Mario

<a class="nu-button" href="{{site.base_url}}/course-files/tutorials/tutorial02/your_task.py" target="_blank">
    Tutorial Starter File <i class="fas fa-download"></i>
</a>

Please download and open the `your_task.py` file and take a look at it. Note that it is making use of the `make_square` function that you made in [Tutorial 1](tutorial01) **with one small change** (it's included at the top of the file). Instead of using separate inputs for the bottom left x-coordinate and y-coordinate, it's combined those two into a single `tuple` (a sequence of two `int`s). That means the way we call that function has slightly changed (take a close look at the function calls to `make_square`).

Scroll down in the file until you see the usual `"YOUR CODE BELOW HERE"` message and take a brief look at the code. It's a long file...but it's super repetitive. Let's see what it does:

<img class="medium frame" src="{{site.base_url}}/assets/images/tutorials/mario1.png" />

A few things to pay attention to in this file:

1. This program will always draw a Mario that is the same size and positioned in the exact same place.
1. Each "pixel" is 25 units wide / tall
1. If you were to draw a box around this particular Mario, the bottom left coordinate would be positioned at `(0, 0)`, and the top right coordinate would be positioned at `(300, 375)`.

* * *

## Task 1: Manipulating Mario's clothes and overalls color

Try re-assigning a different color to the `clothes` variable, and running the program (note that Mario's shirt and hat change color). When you're done, please create another variable called `overalls`, and edit the code so that the color of Mario's overalls is determined by the value stored inside the `overalls` variable.

### Using the Find tool

A lot of the times in programming (or really in text-editing too), you might want to find a certain line or word in a really long program. To do this, we can use the **FIND** tool. To do this in IDLE, open the `Edit` menu and select `Find...`. It'll bring up a menu like the below:

<img class="medium frame" src="{{site.base_url}}/assets/images/tutorials/find.png" />

Say you wanted to see which lines of our program pertain to Mario's overalls. Well they start off blue, so you'd open up the Find tool and then search for `"blue"`. Once you click **Find** it will highlight the first occurrence of that search term in the file. If you want to find the next one, then you'd just click **Find Next**.

You can also bring the find tool up quickly via the keyboard shortcut Ctrl-F on a PC or Command-F on a Mac.

* * *

### Task 2: Customize Mario's size

Next, modify the code to make it easier to customize Mario's ***size*** (i.e. the size of each pixel). As the program currently stands, each pixel is hardcoded to 25 pixels for their width. But what if you wanted to draw a mini-Mario, or a really big Mario? You would have to update every x and y value.

To make this process more efficient, create another variable called `pixel` and assign the value `25` (int) to it. Then, figure out a way to use the `pixel` variable to change all of those square sizes.

### Using the Find and Replace Tool

The _Find_ tool is really dope. It does a great job of locating things you might want to change. What if you wanted to make a ton of the same change. Say...replace the value `25` with the variable `pixel`. For this sort of thing, you can use the **Find and Replace** tool. Open up the `Edit` menu and then select `Replace...`.

<img class="medium frame" src="{{site.base_url}}/assets/images/tutorials/replace.png" />

> **NOTE**: BE VERY CAREFUL WITH THIS TOOL. Though it's possible to reverse your changes with Undo, remember computers are not particularly smart and will only do _exactly_ what you tell them to and no more.

Now, we want to replace all the instances of `25` for the `width` parameter for each `make_square` call. But if we just do `25` in Find and `pixel` in Replace...this tool will replace EVERYWHERE we see a 25 with the text `width`. There's lots of other `25s` (e.g. `325`) in it that we don't want to mess with.

You can actually avoid those cases by selecting the `Whole Word` option in the tool...but that still doesn't fix the problem of other `25s` elsewhere in the document.

However...we've got two extra symbols on either end of our `25` for the `width` input that makes it special: a space (` `) on the left hand side and a comma (`,`) on the right hand side. If we instead search for the string ` 25,` and replace with `pixel,`, then IDLE will only replace the ones we care about! Try a couple of instances using the `Replace + Find` button and once you're sure it's working correctly, try using `Replace All`.

> **NOTE**: At this point, you may have some weird looking Marios (try running your code after doing the above). Why is this? What's going on? Take a look at WHERE the squares are being drawn. Talk with someone next to you and try to figure out why your code does what it does. (you'll fix it in the next step)

* * *

### Task 3: Customize Mario's position

Hopefully you've been able to figure out the problem. Mario's position was dependent on how big the squares we were drawing was!

Next, modify the code to make it easier to customize Mario's ***position***. Note that the bottom-left corner of the Mario pixel map is positioned at `(0, 0)` – we'll call this the `origin` (the place where we start drawing Mario). In other words, there is an implicit offset of `(0, 0)` for this Mario. If you wanted to change this offset to, say, `(100, 50)` (move Mario's origin to this location), then you would have to manually add 100 to the value of every x-coordinate and 50 to the value of every y-coordinate.

What we could do, is replace this thinking with a _formula_. For instance, the top row of Mario is all at a y-value of 350; but really it's row 14. So instead of thinking about row 14 as a series of numbers like we have right now:

```python
# row 14
# blank, pixel (0,14)
# blank, pixel (1,14)
# blank, pixel (2,14)
make_square(the_canvas, (75,  350), pixel, color=clothes)  # pixel (3, 14)
make_square(the_canvas, (100, 350), pixel, color=clothes)  # pixel (4, 14)
make_square(the_canvas, (125, 350), pixel, color=clothes)  # pixel (5, 14)
...
```

We could think about it in terms of a formula based on what row and column the pixel represents, the `origin` we're drawing around, and the `pixel` size of the Mario. So say if we set some variables, `origin`, `x`, and `y`...

```python
origin = (0,0)
x = origin[0]
y = origin[1]

# row 14
# blank, pixel (0,14) -> x + 0 * pixel, y + 14 * pixel
# blank, pixel (1,14) -> x + 1 * pixel, y + 14 * pixel
# blank, pixel (2,14) -> x + 2 * pixel, y + 14 * pixel
make_square(the_canvas, (x + 3 * pixel, y + 14 * pixel), pixel, color=clothes)  # pixel (3, 14)
make_square(the_canvas, (x + 4 * pixel, y + 14 * pixel), pixel, color=clothes)  # pixel (4, 14)
make_square(the_canvas, (x + 5 * pixel, y + 14 * pixel), pixel, color=clothes)  # pixel (5, 14)
...
```

If we do it this way, suddenly we no longer care about exactly which numbers to put in those slots, instead Python will do all of that work for us! Of course...this means we'd have to go through each `(x,y)` coordinate and enter the formula for that particular pixel. That seems like a lot of extra work. Really all we need is a machine that calculates the coordinates for us...and we just change the inputs to it. Wouldn't it be great if there was a way to write a machine in Python...

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

Once we have this function working, then all we need to do is replace those `(x,y)` coordinates in each `make_square` call like this:

```python
# row 14
# blank, pixel (0,14)
# blank, pixel (1,14)
# blank, pixel (2,14)
make_square(the_canvas, get_xy(origin, pixel, (3,14)), pixel, color=clothes) # pixel (3, 14)
make_square(the_canvas, get_xy(origin, pixel, (4,14)), pixel, color=clothes)  # pixel (4, 14)
make_square(the_canvas, get_xy(origin, pixel, (5,14)), pixel, color=clothes)  # pixel (5, 14)
...
```

You can think of this function as a _helper_ or _translation_ function that is built to do one thing and one thing only. Use the example above to complete row 14, and also update rows 13, 12, and 11 to the same syntax.

Once you get 14, 13, 12, and 11 (and you feel like you've got a handle for WHY that works) checkout the hint below for the remaining rows. Yes, you can copy and paste the remaining rows...but only do so if you understand why this works. Otherwise, it's time to ask some questions!

<a class="nu-button" href="{{site.base_url}}/course-files/tutorials/tutorial02/hint_1.py" target="_blank">
    Hint<i class="fas fa-download"></i>
</a>

* * *

### Task 4: Create a function so that you can instantiate many Marios

When you're done, you have successfully made your Mario program customizable. However, if you wanted to make, say, 5 Marios, you would have to copy all of your code 5 times (and change the variables for each Mario). This is inefficient. In general, any time you're copying the same code over and over again, it makes sense to create a function. So, let's make that happen. For your final task, please create a `make_mario` function that accepts the following arguments:

1. **the_canvas** *(Canvas)*: a tkinter Canvas object where you want the square to be drawn.
1. **bottom_left** *(tuple)*: a tuple -- an point, an (x, y) coordinate -- that defines the top-left position of the rectangle bounding your picture of Mario. The first element in the tuple refers to the x-coordinate and the second element in the tuple refers to the y-coordinate.
1. **pixel** *(int, optional)*: an int that specifies the width (and also height) of the pixel; defaults to 25.
1. **clothes** *(str, optional)*: a string that represents the color Mario's clothes; defaults to `'red'`.
1. **overalls** *(str, optional)*: a string that represents the color of Mario's overalls; defaults to `'blue'`.

> **NOTE**: the use of `the_canvas` as the first input name. This is so you don't have to rename ALL of the inputs to each of the `make_square` calls. We'll talk a little bit about this on Friday, but when we do this, `the_canvas` inside of the function will be whatever canvas is inputted to the function rather than what it is outside the function (the same is true of the different variables we used for colors as well). **DON'T DO THIS IN YOUR HW THIS WEEK**.

In other words, if I invoked your `make_mario` function as follows...

`make_mario(the_canvas, (180, 220), pixel=20, clothes='#75B9BE')`

...your function would draw a Mario with blue-ish clothes, with its bottom-left coordinate at position (180, 220), with a "pixel" size of 20, wearing blue overalls.

After you're done making your function, add some `make_mario` function calls at the bottom of your `your_task.py` file to test your code. You can use these as examples if you'd like.

```python
# After you're done making your "make_mario" function, invoke it as follows:
make_mario(the_canvas, (0, 20))
make_mario(the_canvas, (420, 250), clothes='#E0607E', pixel=10)
make_mario(the_canvas, (55, 415), clothes='green', pixel=15)
make_mario(the_canvas, (350, 115), pixel=5, clothes='#75B9BE')
make_mario(the_canvas, (420, 400), clothes='#E5F77D', overalls='#75B9BE', pixel=15)
make_mario(the_canvas, (420, 10), pixel=15)
```

<img class="medium frame" src="{{site.base_url}}/assets/images/tutorials/marios.png" />

Make some other custom marios that use different inputs to make sure your function works as expected.

* * *

## Optional Challenges

1. Create a helper function called `make_row` to further simplify your `make_mario` function. Then, rather than repeating almost identical code for each row created, you will simply invoke `make_row` 15 times (once for each row).
2. Create a second pixel art function that draws a different image. Google "pixel art simple" to get ideas.
3. The pixel argument is kind of awkward. Arguably a better function design would allow the calling function to specify the width of Mario (as opposed to the individual pixels that comprise him). Therefore, modify the function header so that it requires a `width` (int) parameter instead of a `pixel` parameter. This change means that you will need to derive the appropriate size of the pixel based on the width and the number of columns needed to generate Mario (which is 13). When you're done, update each of the function calls at the bottom of the file so that they pass in a width argument.

* * *

## Getting Credit for Your Work

If you're in class you don't need to submit a `.py` file on Canvas. Instead, find one other person in your group that is finished and peer review each other's work. Here are the things to check:

1. Does their code look readable and neat?
1. Can you understand what their code does by reading it?
1. How was their solution different from yours (if at all)?
1. Does their program run and generate the correct test images?

Once you've each taken a look, take a second to debrief. Anything either of you found difficult? Easy? Fun? Mind-blowing? Once you've debriefed, **both of you should fill out this** <a href="https://forms.gle/TfwheoqHmuRTY4UcA" target="_blank">attendance Google Form</a>. **NOTE: You will need the NetID of the person's whose code you reviewed.** You're free to go after you're finished, though we hope that you might consider sticking around and helping others in your group.

If you're completing it remotely, please submit your `.py` file on Canvas.
