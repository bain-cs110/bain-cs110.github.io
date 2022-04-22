---
layout: assignment-two-column
title: |
    For Loops Activity
description:
    - practice with for loops
    - practice with iterating through a tuple
    - practice writing functions
type: tutorial
abbreviation: Tutorial 4
points: 3
draft: 0
num: 4
due_date: 2022-04-27

---

<a class="nu-button" href="/course-files/tutorials/tutorial04_template.zip" target="_blank">
    Tutorial Starter Files <i class="fas fa-download"></i>
</a>

<img class="module-image" src="/assets/images/tutorial04/pixel_goomba.png" />In this tutorial, you are going to design a customizable function that creates an image of **any** pixel art that can be represented as rows and columns of integers. The data structure that we will use to store these rows and columns of integers will be a "list of tuples" (see below). The purpose of this exercise is to help you feel a little bit more comfortable with sequences of data, iteration, and functions. In addition to pixel art, many different kinds of entities can also be expressed using similar data formats (JPEG images, songs, DNA sequences, really anything).

## Introduction: New Data Representations
Below are two examples of three example "lists of tuples" that represent pixel art specifications. Note that "smiley" is made up of 8 rows and 8 columns, ["Goomba"](https://www.mariowiki.com/Goomba) is made up of is 16 rows and 16 columns. Each number in the row tuple represents a distinct color. So, for instance, "smiley" only has two distinct colors a `0` (which we'll say is no color) and `1` which we can define to be any color we'd like. The "goomba" has 4 distinct colors: `0` (which again we can say is no color), `1`, `2`, and `3`.


```python
# smiley face
smiley = [
   (0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 1, 0, 0, 1, 0, 0),
   (0, 0, 1, 0, 0, 1, 0, 0),
   (0, 0, 1, 0, 0, 1, 0, 0),
   (1, 0, 0, 0, 0, 0, 0, 1),
   (1, 1, 0, 0, 0, 0, 1, 1),
   (0, 1, 1, 0, 0, 1, 1, 0),
   (0, 0, 1, 1, 1, 1, 0, 0)
]

# goomba
goomba = [
    (0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0),
    (0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0),
    (0, 0, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 0, 0),
    (0, 1, 1, 1, 0, 2, 1, 1, 1, 1, 2, 0, 1, 1, 1, 0),
    (0, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 0, 1, 1, 1, 0),
    (1, 1, 1, 1, 0, 2, 0, 1, 1, 0, 2, 0, 1, 1, 1, 1),
    (1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (0, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 0),
    (0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0),
    (0, 0, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 0, 0),
    (0, 2, 2, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 2, 0),
    (0, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0),
    (0, 0, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 0, 0)
]

```

## Step 1: Update the `draw_row` function
Open `starter.py` and take a look at it. Then run it using IDLE (or a code editor of your choice). You should see the first 6 rows of pixels for each pixel art object. However, everything is being drawn as a grey square. In other words, the color distinctions aren't being honored (see image below).

<img class="small frame" src="/assets/images/tutorial04/starter.png" />

For your first task, you will modify the "draw_row" function -- in any way you can think of -- so that the function honors the color distinctions. Remember: a zero means that you shouldn't draw anything in that cell, but the `1`,  `2`, and `3` can be any color that you choose (see image below).

<img class="small frame" src="/assets/images/tutorial04/hint1.png" />

{:.blockquote-no-margin}
> **If you get stuck**: After you've given it a shot, take a look at `hints/hint1a.py` and `hints/hint1b.py` to consider a few approaches that you might have tried (but of course, there are others).

## Step 2: Replace the repetitive draw_row function calls
Next, you will simplify the repetitive "draw_row" function calls (pictured below) with a "for loop."

```python
# first 6 rows of smiley
draw_row(canvas, smiley[0], (10, 50), pixel=20)
draw_row(canvas, smiley[1], (10, 70), pixel=20)
draw_row(canvas, smiley[2], (10, 90), pixel=20)
...

# first 6 rows of the goomba
draw_row(canvas, goomba[0], (250, 250), pixel=10)
draw_row(canvas, goomba[1], (250, 260), pixel=10)
draw_row(canvas, goomba[2], (250, 270), pixel=10)
...
```
You will use 2 "for loops" -- one for `smiley` and one for the `goomba`. When you're done, the entirety of Smiley and the goomba should be drawn (see image below).

<img class="small frame" src="/assets/images/tutorial04/step2.png" />

{:.blockquote-no-margin}
> **If you get stuck**: After you've given it a shot, take a look at `hints/hint2.py` to get a sense of how you might use a for loop to complete this task. Smiley has been done for you. You try doing the goomba.

## Step 3: Edit `draw_row` so it takes an additional parameter
In Step 1, we manually specified the colors of each square when we drew them. But what if we wanted people to be able to specify their own colors for each pixel? Well, remember that each of our pixel-art objects is just a list of tuples: where each inner element is a number representing a color.

Instead of specifying the colors INSIDE of the `draw_row` function, we want to add a new required parameter to `draw_row`: namely, `colors` which will be a list.

We'll make this list so that the following is true: each element in the `colors` list should correspond to a number in the pixel-art objects. For example, for the smiley that only requires two distinct colors, our colors list might look like `[None, "teal"]`. For the Goomba, it might look like `[None, "saddle brown", "black", "tan"]`.

To do this, you'll have to make three big edits:
* First you'll need to add the new required parameter to the definition of the `draw_row` function.
* You'll need to add this new required parameter to all of your `draw_row` function calls.
* In the body of `draw_row`, you'll need to set the color of each square not via an if-statement, but instead by looking up the corresponding color inside the `colors` list.

It's also worth noting that not only have we now allowed anyone to specify ANY colors they want to draw with...but we've also made it so that our function can actually draw pixel art with ANY number of colors specified! Instead of just having it "hardcoded" so that we can only draw pixel art of 4 different colors...now we can draw pixel art of any number of colors!

{:.blockquote-no-margin}
> **If you get stuck**: After you've given it a shot, take a look at `hints/hint3.py` to get a sense of how you might use each "cell" number to grab the corresponding color from the `colors` list.

## Step 4: Create a draw_pixel_art function
Now, create a `draw_pixel_art` function, with a function definition that looks like this:

```python
def draw_pixel_art(canvas:Canvas, top_left:tuple, artwork:list, palette:list, pixel:int=10):
    # your function body will go here!
    pass
```

So if the function is invoked as follows...

```python
draw_pixel_art(canvas, (0, 20), smiley, [None, "black"])
draw_pixel_art(canvas, (120, 220), goomba, [None, "saddle brown", "black", "tan"], pixel=12)
draw_pixel_art(canvas, (420, 250), goomba, [None, "black", "yellow" , "tan"], pixel=8)
draw_pixel_art(canvas, (55, 415), goomba, [None, "yellow", "purple", "brown"], pixel=6)
draw_pixel_art(canvas, (350, 115), smiley, ["white", "blue"], pixel=5)
draw_pixel_art(canvas, (315, 380), smiley, ["black", "pink"], pixel=15)
draw_pixel_art(canvas, (420, 10), smiley, [None, "red"], pixel=10)
```

...it will generate the image pictured below.

<img class="medium frame" src="/assets/images/tutorial04/step4.png" />

Note that the (x,y) position refers to the top-left corner of where the pixel art will be drawn.

{:.blockquote-no-margin}
> **If you get stuck**: After you've given it a shot, take a look at `hints/hint3.py` to get a sense of how you might implement your `draw_pixel_art` function body.

## Step 5: Revisiting Mario
Now, take the below `mario` variable (you'll need to copy and paste it into your file near the `goomba` and `smiley`) and write a function call to `draw_pixel_art` that will recreate our Mario design from [Tutorial 2](tutorial02).

```python
# mario
mario = [
    (0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0),
    (0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0),
    (0, 0, 3, 3, 3, 4, 4, 4, 5, 4, 0, 0, 0, 0),
    (0, 3, 4, 3, 4, 4, 4, 4, 5, 4, 4, 4, 0, 0),
    (0, 3, 4, 3, 4, 4, 4, 4, 4, 5, 4, 4, 4, 0),
    (0, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 0),
    (0, 0, 1, 1, 2, 1, 1, 1, 2, 0, 0, 0, 0, 0),
    (0, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 0, 0, 0),
    (1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0),
    (4, 4, 1, 2, 6, 2, 2, 6, 2, 1, 4, 4, 0, 0),
    (4, 4, 4, 2, 2, 2, 2, 2, 2, 4, 4, 4, 0, 0),
    (4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 0, 0),
    (0, 0, 2, 2, 2, 0, 0, 2, 2, 2, 0, 0, 0, 0),
    (0, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 0, 0, 0),
    (3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 0, 0)
]
```

<img class="medium frame" src="/assets/images/tutorial04/final.png" />

Check that out. You just wrote a function that can draw ANY PIXEL ART IN THE ENTIRE WORLD. No matter the size or colors. Pretty sweet for an hour's worth of work. For loops allow us to quickly go through lots of data and apply the same set of basic operations to each item.

Now that you've gotten it to work with Mario, feel free to design your own pixel art (you'll need to make a grid of color numbers like our 3 examples here) and use `draw_pixel_art` to draw them!

## What to turn in (same deal as always)
Please turn in your completed tutorial exercise(s) ON CANVAS by Wednesday night at midnight. To do this, first zip your entire `tutorial04` folder (with your edited files inside), and then upload your zip file to Canvas. Please ensure that your zip file includes **YOUR CODE**.  
