---
layout: assignment-two-column
title: Event Handlers
type: tutorial
abbreviation: Tutorial 6
draft: 0
num: 6
points: 3
due_date: 2022-05-11

---

<a class="nu-button" href="/course-files/tutorials/tutorial06_template.zip" target="_blank">
    Tutorial Starter Files <i class="fas fa-download"></i>
</a>

The goal of this tutorial is to get you more comfortable with event handlers. The demo files for [Lecture 17](../lectures/week07-lecture01) might be helpful in completing this exercise!

Please complete the following exercises:

## 1. Dealing with Mouse Events
Open `01_mouse_events.py` and complete the following tasks:
1. modify the `add_new_goomba` function so that it adds a new Goomba wherever the user clicks. Make the size of the Goomba random as its drawn. Also come up with a way of tracking how many Goomba have been created so that each Goomba can have a unique tag.
2. When you're done, add the following line to your program right below your MOUSE_CLICK event handler:<br><br>**`canvas.bind(MOUSE_DRAG, add_new_goomba)`** <br><br>Now run your program again, and notice that your `add_new_goomba` function is invoked when you either click or drag.

<iframe src="https://northwestern.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=888fa5b6-5f40-4179-85d6-ae8d012d0320&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=true&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

## 2. Dealing with Keyboard Events
Open `02_keyboard_events.py` and complete the following tasks:
1. When the user presses the w-key, move the creature **up** 10 pixels.
2. When the user presses the a-key, move the creature to the **left** 10 pixels.
3. When the user presses the d-key, move the creature to the **right** 10 pixels.
4. When the user presses the s-key, move the creature **down** 10 pixels.

{:.blockquote-no-margin}
> **NOTES:**
> In order for your Canvas to listen for keyboard events, you must invoke the **`canvas.focus_set()`** method after you invoke `canvas.pack()` (at the top of your program). Without **`canvas.focus_set()`**, your keyboard events will not fire because they will go to the IDLE application rather than specifically to your canvas.

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

## 4. (Optional) Get Started on P1
In [Project 1](p1), you'll be doing this same sort of thing but with YOUR custom creature rather than our pre-made Mario and Goombas. If you still have time in your tutorial-hour I highly recommend trying to repeat Parts 1 - 3 but this time replacing all of the "mario" and "goomba" parts of your program with your custom `creature.py` from HW 3.

To do this, you'll need to do the following:

1. Modify your `creature.py` and its functions so that your creature can have a custom tag (so we can animate it later). Use the `example_creature.py` as an example. Notice that it uses the functions from `utilities.py` to draw its constitutent shapes. This is because THOSE functions (unlike the ones we wrote in Tutorial 2) also take as inputs a tag. To successfully tag your creature, _every shape that its made out of_ has to have the same tag.
2. Once you've got `creature.py` modified to accept tags, you'll need to replace the import statements from the `mario_module` to import your creature module.
3. Now you'll have to go through and make sure your function calls are actually calling your make_creature function rather than `make_goomba` and `make_mario`.

This process can be difficult so if you start it in your tutorial you can ask lots of questions!

## What to turn in (same deal as always)
Please turn in your completed tutorial exercise(s) ON CANVAS by Wednesday night at midnight. To do this, first zip your entire `tutorial06` folder (with your edited files inside), and then upload your zip file to Canvas. Please ensure that your zip file includes **YOUR CODE**.  
