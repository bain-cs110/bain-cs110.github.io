---
layout: assignment-two-column
title: Event Handlers
type: tutorial
abbreviation: Tutorial 4
draft: 0
num: 4
points: 100
due_date: 2023-05-10
canvas_id: 1224393
---

The goal of this tutorial is to get you more comfortable with event handlers. The demo files for [Lecture 17](../lectures/week07-lecture02) might be helpful in completing this exercise! Remember, we expect you to watch the pre-recorded lecture BEFORE completing the tutorial.

* * *

## Getting Started

You'll need the `p1_utilities` library in your Tutorial 04 folder to complete today's activity (if you haven't been moving stuff to your `cs110` folder that we setup in the very first tutorial...nows a good time to start).

<a class="nu-button" href="/course-files/projects/project01/p1_utilities.py" target="_blank">
    Utilities Library <i class="fas fa-download"></i>
</a>

Here's the documentation for it in case you need it:

<a class="nu-button" href="/course-files/projects/project01/docs/p1_utilities.html" target="_blank">
    Utilities Library Documentation <i class="fas fa-download"></i>
</a>

And you'll need the Mario Module (also in the same folder:

<a class="nu-button" href="/course-files/tutorials/tutorial04/mario_module.py" target="_blank">
    Mario Module <i class="fas fa-download"></i>
</a>

* * *

Please complete the following exercises:

## 1. Dealing with Mouse Events
Open `01_mouse_events.py` (linked below) and complete the following tasks:
1. modify the `add_new_goomba` function so that it adds a new Goomba wherever the user clicks. Make the size of the Goomba random as its drawn. Optional: come up with a way of tracking how many Goomba have been created so that each Goomba can have a unique tag.
2. When you're done, add the following line to your program right below your MOUSE_CLICK event handler:<br><br>**`the_canvas.bind(MOUSE_DRAG, add_new_goomba)`** <br><br>Now run your program again, and notice that your `add_new_goomba` function is invoked when you either click or drag.

<a class="nu-button" href="/course-files/tutorials/tutorial04/01_mouse_events.py" target="_blank">
    Mouse Events <i class="fas fa-download"></i>
</a>


<iframe src="https://northwestern.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=888fa5b6-5f40-4179-85d6-ae8d012d0320&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=true&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>


* * *

## 2. Dealing with Keyboard Events
Open `02_keyboard_events.py` (linked below) and complete the following tasks:
1. When the user presses the w-key, move one of the marios **up** 10 pixels.
2. When the user presses the a-key, move one of the marios **left** 10 pixels.
3. When the user presses the d-key, move one of the marios **right** 10 pixels.
4. When the user presses the s-key, move one of the marios **down** 10 pixels.

{:.blockquote-no-margin}
> **NOTES:**
> In order for your Canvas to listen for keyboard events, you must invoke the **`the_canvas.focus_set()`** method after you invoke `the_canvas.pack()` (at the top of your program). Without **`the_canvas.focus_set()`**, your keyboard events will not fire because they will go to the IDLE application rather than specifically to your canvas. _We did NOT do this for you._

<a class="nu-button" href="/course-files/tutorials/tutorial04/02_keyboard_events.py" target="_blank">
    Keyboard Events <i class="fas fa-download"></i>
</a>

* * *

## 3. Combining both Mouse and Keyboard Events
In the third exercise, you are going to use a global variable to track which creature your keyboard will control. To do this, you will combine the use of the click event handler and the keyboard event handlers.

Inside `02_keyboard_events.py` do the following:

1. Create a global variable called **`active_tag`** and initialize it to `'mario_0'`.
3. Update your `move_mario` functionality so that instead of always moving ``'mario_0'``, you reference the **`active_tag`** variable instead.
4. Modify the **`select_mario`** function so that it sets the **`active_tag`** variable based on mario on which the user clicks. Hint: use the **`global`** keyword (see below).
5. Test your code by making sure that when you click on a different creature, the keyboard moves the correct one.

<iframe src="https://northwestern.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=7cc80c3b-4bb7-412e-9a5d-ae8d012d079f&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=true&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

Hint: if you want a variable to be accessible across a bunch of different parts of your program, you should make it a "global variable." However, because local variables take precendence over globals, inside functions, you need to specify which version of the variable you want to use. For example, in the below example we have a global variable named `color` that is updated within a function called `change_color` (notice the use of the `global` keyword that tells Python "by `color` we mean the global variable `color` not a new local variable named `color`")


```python
color = 'red'
def change_color():
  global color
  color = "green"

print(color)
change_color()
print(color)
```

Check it out in [Python Tutor](https://pythontutor.com/visualize.html#code=color%20%3D%20'red'%0Adef%20change_color%28%29%3A%0A%20%20global%20color%0A%20%20color%20%3D%20%22green%22%0A%0Aprint%28color%29%0Achange_color%28%29%0Aprint%28color%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)!

* * *

## 4. (Optional) Challenges
* Make it so that as you move mario from left to right by hitting the keys that he shifts between his different "versions" that we used last week. Go checkout the `make_mario` function inside the mario module to see what parameter controls the version. (Hint: you'll probably need to use a `global` variable to keep track of which version is being drawn over time).
* Alternatively, try and make Mario "jump" when hitting the space bar. That is animate him briefly upward then downward again whenever someone hits the space bar.
* Create a two player version where one set of 4 keys controls one mario and another set of 4 keys controls a different mario (or make it a luigi!)
* In [Project 1](p1), you'll be doing this same sort of thing but with YOUR custom creature rather than our pre-made Mario and Goombas. If you still have time in your tutorial-hour I highly recommend trying to repeat Parts 1 - 3 but this time replacing all of the "mario" and "goomba" parts of your program with your custom tagged creature from HW 4. This process can be difficult so if you start it in your tutorial you can ask lots of questions!

* * *

## Getting Credit for Your Work

If you're in class you don't need to submit a `.py` file on Canvas. Instead, find one other person in your group that is finished and peer review each other's work. Here are the things to check:

1. Does their code look readable and neat?
1. Can you understand what their code does by reading it?
1. How was their solution different from yours (if at all)?
1. Did they do anything cool?

Once you've each taken a look, take a second to debrief. Anything either of you found difficult? Easy? Fun? Mind-blowing? Once you've debriefed, **both of you should fill out this** <a href="https://forms.gle/TfwheoqHmuRTY4UcA" target="_blank">attendance Google Form</a>. **NOTE: You will need the NetID of the person's whose code you reviewed.** You're free to go after you're finished, though we hope that you might consider sticking around and helping others in your group.

If you're submitting remotely, you MUST submit your completed tutorial to Canvas and it will be graded. Make sure that all of your functions are named correctly and that they use the EXACT parameter order, names, and types as specified.

Please turn in your completed `.py` file on Canvas by Wednesday night at midnight. ONLY SUBMIT the file you worked in...not the `p1_utilities.py` file.