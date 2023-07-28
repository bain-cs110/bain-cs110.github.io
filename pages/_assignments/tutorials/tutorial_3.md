---
layout: assignment-two-column
title: Practice with Conditionals and Loops
type: tutorial
abbreviation: Tutorial 3
draft: 0
points: 100
num: 3
due_date: 2023-05-03
canvas_id: 1224392
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
In the pre-recorded lecture wrote a complete `draw_pixel_art` function that allowed us to draw any pixel art that was stored as a list of tuples, with each inner element just representing a color. In this assignment, we're going to leverage this, along with loops, to make Mario run across the screen!

But...how do we animate something? Well, think of a [flip book](https://andymation.squarespace.com):

<img class="frame" style="width: 25%;" src="{{site.base_url}}/assets/images/tutorials/flipbook.gif" />

A moving image, is just a series of still-images / drawings flashing by at a certain pace. So really, an animation is just a series of repeated steps:

1. Draw a picture
2. Erase the picture
3. Draw a slightly different picture
4. Erase the picture
5. Draw a another slightly different picture...
6. And so on...

If only there were a way to take a series of small steps in our program and repeat them over and over again.

"But wait...there is! Loops!!!"" you're screaming out loud as you read this assignment description. Your job is to use an "infinite" `while` loop to animate Mario running across the screen.

* * *

## Step 1 - Getting Ready

Download these two starter files and make sure they're both in the same folder on your computer:

<a class="nu-button" href="{{site.base_url}}/course-files/tutorials/tutorial03/animate_mario.py" target="_blank">
    Tutorial Starter File <i class="fas fa-download"></i>
</a>

<br>

<a class="nu-button" href="{{site.base_url}}/course-files/tutorials/tutorial03/tutorial03_utilities.py" target="_blank">
    Utilities Library <i class="fas fa-download"></i>
</a>

Open up `animate_mario.py` and run it. You'll see we're basically where we left off on Monday. We've got a few "static" (not moving) Mario drawn on the screen using `draw_pixel_art`. Notice you can modify the colors we use to draw Mario by modifying the `marios_colors` list.

The main difference in this program is that instead of having just one Mario pixel art, we have 3 _different_ Marios that we can draw. If you open `tutorial03_utilities.py` you'll see not only all of the functions we wrote on Monday, but also 3 different Mario designs: `mario_0`, `mario_1`, and `mario_2`. At the top of our `animate_mario.py` file we **import** these designs as variables to our program, so you can use these designs inside `animate_mario.py`.

Modify the function call to `draw_pixel_art` to draw these other two alternate designs (try one at a time; note that your mario might appear in another location).

<table>
<thead>
  <tr>
    <th>mario_0</th>
    <th>mario_1</th>
    <th>mario_2</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><img src="{{site.base_url}}/assets/images/tutorials/mario_0.png" width="250"></td>
    <td><img src="{{site.base_url}}/assets/images/tutorials/mario_1.png" width="250"></td>
    <td><img src="{{site.base_url}}/assets/images/tutorials/mario_2.png" width="250"></td>
  </tr>
</tbody>
</table>


* * *
## Step 2 - Learning how to deal with Time

There are two new skills we need in order to animate Mario. The first one is we need to learn how to control `time` and the second is we need to know how to erase the Canvas.

In order to control Time...in Python...we're going to use the `Time` module which is already imported for you at the top of the file. The only function we need to know about right now is the `time.sleep` function. It has one required parameter: the number of seconds (`float`) you would like Python to sleep for (e.g. `time.sleep(1)` will ask the computer to sleep for 1 second before continuing on in your program). Try adding a call to `time.sleep` for 5 seconds *before* your call to the `draw_pixel_art` function. If we first ask Python to pause for 5 seconds and then draw, we should see a 5 second delay between clicking "run" and seeing Mario pop up on our Canvas. Try some other values for sleep as well. (Don't add multiple sleeps though, just change the input to the function).

Now that we know how to pause time in Python, we also need to know how to erase our Canvas. Luckily, Canvas data objects have a built-in method called `delete` that allows us to delete stuff from the canvas. In our case, our `Canvas` is just named `canvas` so to delete something we just need to use the method `the_canvas.delete`. It takes one required input, namely a string that explains what to delete. Try rearranging your program so FIRST it draws the pixel art verison of mario, THEN it takes a 5 second pause, and then AFTER the pause add `the_canvas.delete('all')` (which asks Python to delete everything on the Canvas). Theoretically, we'll see Mario get drawn...then a 5 second pause...then Mario will go bye bye.

What if we wanted to ONLY delete Mario and not our beautiful grid lines? If you take a look in `tutorial03_utilities.py`, you'll notice that there's an extra optional parameter that's been added to `draw_pixel_art`, `draw_row`, and `draw_square` called `tag` (it expects a `str`). This `tag` is a system that TKinter allows us to use to "name" each of the things we draw. You'll see that the `make_grid` function tags all of its drawings with the `"grid_line"` name. This means we can modify our call to `draw_pixel_art` to pass a value in for this new optional parameter. One logical name might be `"mario"`.

Once we add that additional input to `draw_pixel_art`, Canvas knows that our drawing is actually called "mario", so instead of deleting "all" things on the canvas, we can change our call to `the_canvas.delete` to just delete Mario: `the_canvas.delete("mario")`.

Now that we can both erase/update our Canvas and control time...it's finally time to animate Mario.

* * *

## Step 3 - Introducing the Animation Loop

Now, your job is to move this code into an "infinite" `while` loop. So in each iteration of our loop, you'll need to do the following:
1. Erase the mario currently on the screen
2. Draw a new mario (slightly shifted to the right)
3. Update the screen (call the `gui.update()` method) and then pause (let's say for `0.25` seconds)

Put your existing drawing code inside of a new infinite `while` loop and rearrange it so it looks like the above steps. Try running your animation.

WOW. A whole lot of nothing. Well, that's because we never asked Python to actually draw a different mario each time! It's always drawing the same exact mario in the same exact position. Using the "counting" technique in class, teach Python how to count the number of iterations of your loop. Then use this `counter` to update the x-position of your Mario each iteration (hint: the default pixel size is 15, so maybe your mario should move 15 pixels each iteration).

{: .blockquote-no-margin}
> **Stuck?**
> Note, the below hint must be put in the same folder as your other two files for it to work!
> <br>
> <br>
> <a class="nu-button" href="{{site.base_url}}/course-files/tutorials/tutorial03/hint.py" target="_blank">Hint 1 <i class="fas fa-download"></i></a>

How cool is THAT!? Mario is racing across the screen; but more like an ice skater than the track and field star he actually is. To make this a little more "animation" like, we want to draw 3 different versions of Mario rather than just the same version of mario shifted a bit each time. Remember those other mario versions from Step 1? What we want to do is draw `mario_0`, then `mario_1`, then `mario_2`, then `mario_0`, then ... To do this, use an `if-elseif-else` conditional along with counter so that the mario version we draw changes each iteration (hint: `counter % 3` will cycle between the values of 0, 1, and 2). This is a slightly more advanced version of what we talked about last week:

```python
if condition_1:
    # something to do if condition_1 is met
elif condition_2:
    # something to do if condition_1 is NOT met but condition_2 IS met
else:
    # something to do otherwise
```

Once you've successfully implemented the conditional, you should see Mario smoothly animate across the screen. Great work!

Your last task is to make a SECOND mario also animate across the screen below the first. See if you can shift it slightly (like the below video) so that the mario on the top always wins the race! (Hint: DO NOT USE A SECOND WHILE LOOP. All of your code will be inside of your single while loop)

<iframe src="https://northwestern.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=0fd80643-2426-470c-9b43-ae86000a910e&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=true&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

* * *

## Getting Credit for Your Work

If you're in class you don't need to submit a `.py` file on Canvas. Instead, find one other person in your group that is finished and peer review each other's work. Here are the things to check:

1. Does their code look readable and neat?
1. Can you understand what their code does by reading it?
1. How was their solution different from yours (if at all)?
1. Does their program run and generate the correct test images?

Once you've each taken a look, take a second to debrief. Anything either of you found difficult? Easy? Fun? Mind-blowing? Once you've debriefed, **both of you should fill out this** <a href="https://forms.gle/TfwheoqHmuRTY4UcA" target="_blank">attendance Google Form</a>. **NOTE: You will need the NetID of the person's whose code you reviewed.** You're free to go after you're finished, though we hope that you might consider sticking around and helping others in your group.

If you're submitting remotely, you MUST submit your completed tutorial to Canvas and it will be graded. Make sure that all of your functions are named correctly and that they use the EXACT parameter order, names, and types as specified.

Please turn in your completed `.py` file on Canvas by Wednesday night at midnight. ONLY SUBMIT the file you worked in...not the `tutorial03_utilities.py` file.
