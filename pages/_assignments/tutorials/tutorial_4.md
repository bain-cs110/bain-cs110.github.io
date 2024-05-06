---
layout: assignment-two-column
title: Practice with Conditionals and Loops
type: tutorial
abbreviation: Tutorial 4
draft: 0
points: 100
num: 3
due_date: 2024-05-01
canvas_title: Tutorial 4
canvas_id: 1412825
canvas_assignment_group: "Tutorial"
canvas_points_possible: 100
canvas_submission_types: "online_upload"
canvas_allowed_extensions: "py"
---

The goal of this tutorial is to get you comfortable with conditionals and loops. Both of these types of statements are very powerful, so getting comfortable with them is essential (and will help you with HW 4).

* * *

## Stuck in an infinite loop?

When you write an infinite loop, like in in the below example, Python will keep running the loop until it literally can't anymore. You can (normally) cancel out of the program by going back to your Interpreter window and hitting Ctl+C or go the Shell menu at the top of the screen and select `Interrupt Execution`.

> **Note**: <mark>If you're on a Mac</mark>, infinite loops that _only include print statements_ will actually cause more recent macOS versions to appear to "lockup." If this happens, you have to "force quit" IDLE by holding down the <code>COMMAND</code>, <code>OPTION</code>, and <code>ESCAPE</code> keys on your keyboard at the same time and then selecting IDLE in the resulting menu.

```python
while True:
    print('Hello! How are you doing today (this will go on forever)?')

print('Program terminated')
```

* * *

## Animating Mario

In the pre-recorded lecture we wrote a complete `pixel_art` function that allowed us to draw any pixel art that was stored as a list of tuples, with each inner element just representing a color. In this assignment, we're going to leverage this, along with loops, to make Mario run across the screen!

But...how do we animate something? Well, think of a [flip book](https://andymation.squarespace.com):

<img alt="a flipbook gif" class="frame" style="width: 25%;" src="{{site.url}}/assets/images/tutorials/flipbook.gif" />

A moving image, is just a series of still-images / drawings flashing by at a certain pace. So really, an animation is just a series of repeated steps:

1. Draw a picture
2. Erase the picture
3. Draw a slightly different picture
4. Erase the picture
5. Draw a another slightly different picture...
6. And so on...

If only there were a way to take a series of small steps in our program and repeat them over and over again.

"But wait...there is! Loops!!!"" you're screaming out loud as you read this assignment description.

* * *

## Step 1 - Getting Ready

Download these two starter files, rename the template file to <code>tutorial4.py</code>, and make sure they're both in the same folder on your computer (preferably one named <code>Tutorial 4</code>):

<a class="nu-button" href="{{site.url}}/course-files/tutorials/tutorial4/tutorial4_template.py" target="_blank">
    Tutorial Starter File <i class="fas fa-download"></i>
</a>

<br>

<a class="nu-button" href="{{site.url}}/course-files/tutorials/tutorial4/cs110_t4.py" target="_blank">
    Helper File<i class="fas fa-download"></i>
</a>

Now in the pre-recorded lecture we had just one single "pixel art" that represented mario. But in this file, we have 3 _different_ Marios that we can draw. If you open `cs110_t4.py` you'll see not only all of the functions we wrote on Monday, but also 3 different Mario designs: `mario_0`, `mario_1`, and `mario_2` (<mark>Note: make sure to close this file afterwards; all of our work will be in the `tutorial4.py` file). 

Open up `tutorial4.py` and run it. We've got a "static" (not moving) Mario drawn on the screen using `pixel_art`. At the top of our `tutorial4.py` file we **import** these designs and functions into to our program, so you can use that stuff inside our file.

Checkout the documentation below for all of those functions:

<a class="nu-button" href="{{site.url}}/course-files/tutorials/tutorial4/docs/cs110_t4.html" target="_blank">
    Utilities Library Documentation
</a>

Make sure to take an extra special look at the `pixel_art` function. Take careful note of each of its inputs!

Find the `setup` function definition in the template file. This is the part of the file that controls what to draw on the screen. Inside that function definition, modify the function call to `pixel_art` to draw these other two alternate designs (try one at a time; note that your mario might appear in another location).

<details>
<summary>What do the different Marios look like?</summary>
<table>
<caption>it's a me, mario!</caption>
<thead>
  <tr>
    <th>mario_0</th>
    <th>mario_1</th>
    <th>mario_2</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><img alt="mario 1" src="{{site.url}}/assets/images/tutorials/mario_0.png" width="250"></td>
    <td><img alt="mario 2" src="{{site.url}}/assets/images/tutorials/mario_1.png" width="250"></td>
    <td><img alt="mario 3" src="{{site.url}}/assets/images/tutorials/mario_2.png" width="250"></td>
  </tr>
</tbody>
</table>
</details>

* * *

## Step 2 - Erasing Things

In order to make a flip book, we essentially need to know how to erase something. In `cs110_t4` there's a function called `delete` that allows us to delete stuff from our screen that we can just call in our template file. It takes one required input, namely a string that explains what to delete. Add a call to `delete` with an input of the tag `"all"` to the top of your `go` function. Does the grid disappear when you run the function?

What if we wanted to ONLY delete Mario and not our beautiful grid lines? If you take a look in `cs110_t4`, you'll notice that there's an extra optional parameter that's been added to `pixel_art`, `row`, and `square` called `tag` (it expects a `str`). This `tag` is a system that allows us to assign "name" to the things we draw. For instance, the function that creates the grid on the window tags all of its drawings with the <code>"grid_line"</code> name.

_This means we could modify our call to `pixel_art` to pass a value in for this new optional parameter. One logical name might be `"mario"` (that's the example the template uses)._

Once we add that additional input to `pixel_art`, our canvas knows that our drawing is actually called "mario", so instead of deleting "all" things on the screen, we can change our call to `delete` to just delete Mario: `delete("mario")`.

* * *

## Step 3 - Introducing the Animation Loop

Now we could create an infinite loop by using a `while` block, however, instead of having you do that, we've got the template setup a little differently. Scroll down to the very bottom of the file. You'll see a `while` loop with a condition that's always `True` (aka, an infinite loop). This means that when you run the program, it will call the `go` function and briefly pause using the `time` module. When it's done...it'll call it again and briefly pause, and again...and again... Additionally the program keeps track of how many times `go` has been called in a global variable called `ticks`.

That means to animate our mario, we just need to write the body of the function `go` to explain to python how to continuously update (i.e. where do we draw the mario this time) and delete the mario image (in this tutorial, we don't have to put ANYTHING in the <code>setup</code> function). Here's what we need to tell our `go` function to do:

1. Delete the mario currently on the screen
2. Draw a new mario (slightly shifted to the right)

That's it! So at the top of the `go` function's body, call some function that the screen to deletes our first mario named `"mario"`. Now, we need to teach it how to draw a new mario, slightly to the right of where the first one was. In other words, **the more ticks we have gone through** the more to the right (increase on the x-axis) we need to draw our mario. On tick 0, we want to draw mario at "0" on the x-axis (<code>5 * 0</code>). On tick 1, we want to draw mario at 5 on the x-axis (<code>5 * 1</code>). Then by 10 (<code>5 * 2</code>). Then by 15... Then by 20... If only there was a mathematical operation that allowed us to represent the relationship between the value of `ticks` and the x-value we want to draw mario at... 

Once you've got that figured out, modify the call to `pixel_art` so its x-coordinate uses that relationship.

* * *

## Step 4 - Generating Frames

Now when you run your program Mario is racing across the screen; but more like an ice skater than the track and field star he actually is. To make this a little more "animation" like, we want to draw 3 different versions of Mario rather than just the same version of mario shifted a bit each time. Remember those other mario versions from Step 1? What we want to do is draw `mario_0`, then `mario_1`, then `mario_2`, then `mario_0`, then ... To do this, use an `if-elif-else` conditional along with counter so that the mario version we draw changes each iteration (hint: `ticks % 3` will cycle between the values of 0, 1, and 2). This is a slightly more advanced version of what we talked about last week:

```python
if condition_1:
    # something to do if condition_1 is met
elif condition_2:
    # something to do if condition_1 is NOT met but condition_2 IS met
else:
    # something to do otherwise
```

Once you've successfully implemented the conditional, you should see Mario smoothly animate across the screen. Great work!

Your last task is to make a SECOND mario also animate across the screen below the first who runs from right to left.

<details>
<summary>Hints!</summary>
<ul>
<li>Remember, you'll need to assign this mario a unique tag (maybe <code>"luigi"</code>) if you want it to be animated differently than our first mario.</li>
<li>Before we were moving left to right so we needed to <b>add</b> to the x-position. Now we're moving right to left. What can we do differently?</li>
<li> Rather than calling <code>pixel_art</code> 3 separate times for the 3 versions of mario. instead, try setting a variable called <code>style</code> to be equal to the three mario versions in the if-elif-else block, and then use that variable in place of the mario design in the call to <code>pixel_art</code>.</li>
<li>Mario facing the wrong direction? Try using the <code>mirror</code> function. It takes just one input, a <code>tag</code> with a shape to flip.</li>
</ul>
</details>

Here's approximately what the final product will look like (depending on how far you move each mario at each step):

<iframe src="https://northwestern.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=c6d25fb9-5a0f-47a9-b551-b10c01646d20&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=true&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay" aria-label="Panopto Embedded Video Player"></iframe>

* * *

## Extra time?

Start working on HW5! It's a little bit different than this mario example.

* * *

## Getting Credit for Your Work

### If you're in class

If you're in class you don't need to submit a `.py` file on Canvas. Instead, find one other person in your group that is finished and peer review each other's work. Here are the things to check:

1. Does their code look readable and neat?
1. Can you understand what their code does by reading it?
1. How was their solution different from yours (if at all)?
1. Does their program run and generate the correct test images?

Once you've each taken a look, take a second to debrief. Anything either of you found difficult? Easy? Fun? Mind-blowing? Once you've debriefed, **both of you should fill out this** <a href="https://docs.google.com/forms/d/e/1FAIpQLSfz1vAwwGuF1GZyhhdWylMMczF26e7xWBBx3kg3MxT-PTFC_A/viewform?usp=sf_link" target="_blank">attendance Google Form</a>. **NOTE: You will need the NetID of the person's whose code you reviewed.** You're free to go after you're finished once we open the attendance form, though we hope that you might consider sticking around and helping others in your group.

### If you're not in attendance

You can just submit your `.py` file to the Canvas assignment and they will be graded. <mark>Make sure you have exactly followed the instructions.</mark>
