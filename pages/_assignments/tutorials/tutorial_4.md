---
layout: assignment-two-column
title: Practice with Conditionals and Loops
type: tutorial
abbreviation: Tutorial 4
draft: 0
points: 100
num: 3
due_date: 2024-02-07
canvas_title: Tutorial 4
canvas_id: 1362727
canvas_assignment_group: "Tutorial"
canvas_points_possible: 100
canvas_submission_types: "online_upload"
canvas_allowed_extensions: "py"
---

The goal of this tutorial is to get you comfortable with if/else statements and while loops. Both of these types of statements are very powerful, so getting comfortable with them is essential (and will help you with HW 4).

* * *

## Stuck in an infinite loop?

When you write an infinite loop, like in in the below example, Python will keep running the loop until it literally can't anymore. You can  cancel out of the program by going back to your Interpreter window and hitting Ctl+C or go the Shell menu at the top of the screen and select `Interrupt Execution`.

```python
import time

while True:
    print('Hello! How are you doing today (this will go on forever)?')
    time.sleep(1)

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

Download these two starter files and make sure they're both in the same folder on your computer (preferably one named "Tutorial 5"):

<a class="nu-button" href="{{site.url}}/course-files/tutorials/tutorial4/animate_mario.py" target="_blank">
    Tutorial Starter File <i class="fas fa-download"></i>
</a>

<br>

<a class="nu-button" href="{{site.url}}/course-files/tutorials/tutorial4/tutorial4_utilities.py" target="_blank">
    Utilities Library File<i class="fas fa-download"></i>
</a>

Open up `animate_mario.py` and run it. You'll see we're basically where we left off on Monday. We've got a "static" (not moving) Mario drawn on the screen using `pixel_art`. Notice you can modify the colors we use to draw Mario by modifying the `marios_colors` list.

The main difference in this program is that instead of having just one Mario pixel art, we have 3 _different_ Marios that we can draw. If you open `tutorial4_utilities.py` you'll see not only all of the functions we wrote on Monday, but also 3 different Mario designs: `mario_0`, `mario_1`, and `mario_2`. At the top of our `animate_mario.py` file we **import** these designs as variables to our program, so you can use these designs inside `animate_mario.py`.

Additionally, `tutorial4_utilities` has lots of helpful functions in it which you can either view by opening up the file or by using the page here:

Note there are a number of functions in `tutorial4_utilities.py` that you _can_ use but you only _have_ to use `move` and `cloud`. You _should not_ use any function that starts with an underscore. These are called "private functions" and are ONLY meant for use within that one particular file. In fact...rather than reading the .py file, instead, you can click on this dope purple button and see all the function's you have available to you and their documentation!

<a class="nu-button" href="{{site.url}}/course-files/tutorials/tutorial4/docs/tutorial4_utilities.html" target="_blank">
    Utilities Library Documentation
</a>

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

## Step 2 - Pausing and Erasing Things

There are two new skills we need in order to animate Mario. The first one is we need to learn how to control `time` and the second is we need to know how to erase the Canvas. <mark>Note that we're done with the <code>setup</code> function now and will want to be working in the <code>go</code> function's body for the rest of our time in this tutorial</mark>.

In order to control Time...in Python...we're going to use the `Time` module which is already imported for you at the top of the file. The only function we need to know about right now is the `time.sleep` function. It has one required parameter: the number of seconds (`float`) you would like Python to sleep for (e.g. `time.sleep(1)` will ask the computer to sleep for 1 second before continuing on in your program).

In the `go` function, locate the `print` statement. Then add a call to call to `time.sleep` for 5 seconds. Then add another print statement right after that prints `"I AM WELL RESTED!"`. Run your program. Try some other values for `sleep` as well. You should see (in the Interpreter Window) repeated messages approximately however many seconds apart you specify.

> **Note**: The `go` function will actually take care of pausing for you (if you look all the way at the bottom of the file, it will pause for a bit after each call to the `go` function completes) so make sure to remove any calls to `time.sleep(...)` you've added before moving on.

In order to make a flip book, we essentially need to know how to erase something. In `tutorial4_utilities` there's a function called `delete` that allows us to delete stuff from our screen that we can just call in our template file. It takes one required input, namely a string that explains what to delete. Add a call to `delete` with an input of the tag `"all"` to the top of your `go` function. Does the grid disappear when you run the function?

What if we wanted to ONLY delete Mario and not our beautiful grid lines? If you take a look in `tutorial4_utilities`, you'll notice that there's an extra optional parameter that's been added to `pixel_art`, `row`, and `square` called `tag` (it expects a `str`). This `tag` is a system that `tkinter` allows us to use to "name" each of the things we draw. For instance, you'll see that the `make_grid` function tags all of its drawings with the `"grid_line"` name. This means we can modify our call to `pixel_art` to pass a value in for this new optional parameter. One logical name might be `"mario"` (that's the example the template uses).

Once we add that additional input to `pixel_art`, our canvas knows that our drawing is actually called "mario", so instead of deleting "all" things on the screen, we can change our call to `delete` to just delete Mario: `delete("mario")`.

Now that we can both erase/update our screen and control time...it's finally time to animate Mario.

* * *

## Step 3 - Introducing the Animation Loop

Now we could create an infinite loop by using a `while` block, however, instead of having you do that, we've got the template setup a little differently. Scroll down to the very bottom of the file. You'll see a `while` loop with a condition that's always `True` (aka, an infinite loop). This means that when you run the program, it will call the `go` function and briefly pause using the `time` module. When it's done...it'll call it again and briefly pause, and again...and again... Additionally the program keeps track of how many times `go` has been called in a global variable called `ticks`.

That means to animate our mario, we just need to write the body of the function `go` to explain to python how to continuously update (i.e. where do we draw the mario this time) and delete the mario image. Here's what we need to tell our `go` function to do:

1. Delete the mario currently on the screen
2. Draw a new mario (slightly shifted to the right)

That's it! So at the top of the `go` function's body, call some function that the screen to deletes our first mario named `"mario"`. Now, we need to teach it how to draw a new mario, slightly to the right of where the first one was. In other words, **the more ticks we have gone through** the more to the right (increase on the x-axis) we need to draw our mario. On tick 0, we want to shift mario over by 0 on the x-axis. One tick 1, we want to shift mario over by say 5. Then by 10. Then by 15. Then by 20. If only there was a mathematical operation that allowed us to represent the relationship between the value of `ticks` and the amount we want to shift by. Once you've got that figured out, modify the call to `pixel_art` so it's x-coordinate uses that relationship.

Now when you run your program Mario is racing across the screen; but more like an ice skater than the track and field star he actually is. To make this a little more "animation" like, we want to draw 3 different versions of Mario rather than just the same version of mario shifted a bit each time. Remember those other mario versions from Step 1? What we want to do is draw `mario_0`, then `mario_1`, then `mario_2`, then `mario_0`, then ... To do this, use an `if-elseif-else` conditional along with counter so that the mario version we draw changes each iteration (hint: `ticks % 3` will cycle between the values of 0, 1, and 2). This is a slightly more advanced version of what we talked about last week:

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

Start working on HW4! It's a little bit different than this mario example.

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

You can just submit your `.py` file to the Canvas assignment and they will be graded.
