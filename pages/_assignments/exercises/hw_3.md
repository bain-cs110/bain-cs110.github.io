---
layout: assignment-two-column
title: Make a Creature
abbreviation: HW3
type: homework
due_date: 2023-04-21
ordering: 3
points: 100
canvas_id: 1224382
draft: 0
---

> **LEARNING OBJECTIVES:**
>
> 1. More practice working with built-in functions
> 1. Practice writing your own functions

<img class="creature" src="{{site.url}}/assets/images/hw03/creature.png" /> In this assignment, you are going to write a program to draw a creature of your own design/choosing using <a href="" target="_blank">tkinter</a>. At the end of this assignment, someone should be able to use your function to draw your creature: anywhere on the screen at any size or color. In other words, your function needs to honor the parameters that are passed into it. If you don't quite know what this means (it's a confusing concept for people just learning to program), make sure to ask questions!

<br>

<a class="nu-button" href="{{site.url}}/course-files/homeworks/hw03/hw03_template.py" target="_blank">
    Homework Starter File <i class="fas fa-download"></i>
</a>

<br>

Make sure to download the above template and move it to your `cs110` folder. Rename it `hw03.py` so you know exactly which file to submit when you're done.

* * *

## Part 1: Design your creature

On paper, sketch out some creature ideas (shoot for using between 4-8 shapes). These can be different variations of the same creature or all different ones. You can just implement the head of your creature (similar to the bear at the top) or the whole thing — the choice is up to you. Here are some links to ideas:

* <a href="https://www.youtube.com/watch?v=yh_A09CrT68" target="_blank">https://www.youtube.com/watch?v=yh_A09CrT68</a>
* <a href="https://www.pinterest.com/pin/118782508901992203/" target="_blank">https://www.pinterest.com/pin/118782508901992203/</a>
* <a href="https://stock.adobe.com/images/cute-simple-shape-monster-character-vector-flat-graphic-design-illustration-set/209183229" target="_blank">Simple monster designs</a>
* <a href="https://goo.gl/hKewyL" target="_blank">https://goo.gl/hKewyL</a>

After you've done some sketching on paper, _select the one_ that you would like to use for the assignment and draw the creature bigger on a different piece of paper — ideally graph paper — and label the points that will help you to program your creature. Remember, to think in terms of shapes that we already know how to make in TKinter: ovals, circles, bullseyes, squares/rectangles, and polygons! Just like we have with ovals, circles, squares, etc, you'll be repsonsible for writing a _function_ that creates your creature from a series of parameters (center coordinate, width, etc.).

If you want to draw using more advanced shapes than what we used last week (e.g. circles, ovals, bullseyes, and squares), sweet!

Take a look at the `tkinter_warmup.py` file (downloadable below) for some more advanced examples. If you're having trouble conceptualizing how to make a shape, come to office hours so we can help!

<a class="nu-button" href="{{site.url}}/course-files/lectures/lecture07/01_tkinter_warmup.py" target="_blank">
    More Advanced Tkinter Examples <i class="fas fa-download"></i>
</a>

{: .blockquote-no-margin}
> **AGAIN:** Making a simple creature (e.g using 4-8 shapes) is totally fine. You don’t need to get too detailed unless you want to! And you can always enhance your creature at a later point in time.

* * *

## Part 2: Implement your creature using function calls

Once you are satisfied with your animal concept, draw those shapes inside your `hw03.py` file. You can use any combination of shapes (points, lines, polygons, rectangles, ovals, etc.). Feel free to use the `make_circle` and `make_oval` functions that you already implemented in homework 2 (just copy and paste them above your make creature function). Also feel free to use any of the code in `tkinter_warmup.py` file. The spirit of this assignment is for you to get creative, given your developing knowledge of functions.

This first "sketch" of your creature need only create _a single creature_ (i.e. if you run it over and over again it'll make the same creature over and over again). _Once you've gotten this simple version working_, then you can work on "parameterizing" it like we did Mario in Tutorial 3 (in the next part you'll turn this creature into a `make_creature` function).

**Tips**:

1. Keep it simple (we recommend anywhere between 4 (minimum) to 8 shapes)! You can always add more functionality later.
2. Make only one or two changes at a time and then test out those changes by running your file. This makes things easier to debug.
3. Use the grid that gets drawn to help you figure out the "math" behind your design! If you find the grid annoying you can comment it out by searching for the function call to `make_grid` and adding a `#` at the beginning of the line.

* * *

## Part 3: Turn it into a `make_creature` function

Once your program successfully draws the creature that you sketched, we're going to turn it into a function (just like we did with mario). We'll start by adding positional and keyword parameters. First write a function header (the name needs to be `make_creature`) with the following inputs:

* A positional (required) parameter, `a_canvas`, which will be a reference to your canvas object.
* A positional (required) parameter, `center`, specifying the x-y position of the center of your creature (should be a `tuple`).
* A keyword (optional) parameter, `primary_color` (a `str`) specifying the primary color of the creature. In the case of the bear, this is the face color. Remember, optional parameters require default values. You can choose which color to be the default value.
* A keyword (optional) parameter, `secondary_color` (a `str`) specifying the secondary color of the creature. In the case of the bear pictured above, this was the ear color. You can choose which color you'd like to be the default value.
* A keyword (optional) parameter, `size`, specifying the size of the creature (should be an `int` or `float`). You can choose the default value.
* If you want to add other parameters (for instance, the size of the ears for the bear) you are free to do so to further customize your creature, but make sure they are **optional** parameters!

Then move all of your creature code into the body of that function. <mark><b>Make sure to change</b> the_canvas to a_canvas in your function definition since now we want to draw on the Canvas specified by the function input and <b>not just</b> the canvas that our file has. You'll get a 0 from the autograder if your program does this!</mark> You'll use `a_canvas` when inside your functions' header and body and `the_canvas` outside.

* * *

## Part 4: Parameterizing

Now comes the hard part, change your program so that it is _parameterized_–that is, instead of drawing a SINGLE version of your creature, it uses the inputs to the function to draw _any different creature_ specified by the inputs (e.g. different location, different size, different colors, etc.)

When you're done, please try at least three calls to the `make_creature` function, using different arguments to verify your function creates your creature at different locations, sizes, and colors. For instance, after completing the assignment, I used my `make_creature` function in the following way to produce the drawing below (feel free to use whatever arguments you want for your positional / keyword parameters):

```python
# with a function, you can make slightly different versions of your design,
# thereby reusing the same code over and over again
make_creature(the_canvas, (92, 115))
make_creature(the_canvas, (487, 110), size=101)
make_creature(the_canvas, (454, 423), primary_color='#aebb83', secondary_color='#227876')
make_creature(the_canvas, (333, 227), secondary_color='#3f5364')
make_creature(the_canvas, (117, 314), size=91, primary_color='#648d8e', secondary_color='#afc272')
make_creature(the_canvas, (199, 469), size=122, primary_color='#3f5364', secondary_color='#bfdc65')
```

> **Note**: Depending on how you implement the `size` input in your function body, your creature might appear WAY too _big_ or WAY too _small_. While we won't be expecting an exact relationship between the `size` of your creature and the actual visual size it ends with, it should be roughly like our creature below. If you find your creature to be way too big with the test calls, an easy way to fix this is to, at the very beginning of your funciton, do the following:
> 
> `size = size / 10`
>
> this just says "make the size 1/10 the size someone entered". Depending on your design, you might need to tweak that denominator to scale the image satisfactorally. If your creature is too small on the other hand, you might do:
>
> `size = size * 10`
>
> The cool thing about this fix is that all it's doing is changing the value stored in the `size` variable. We only need to change it in that one place because everywhere we use `size`, python will use the smaller value cause that's what's stored in there!

<img class="medium frame center" src="{{site.url}}/assets/images/hw03/creatures.png" />


* * *

## Part 5: Smoke Testing your Function

Using the above example tests is a great way to make sure that your function works as described. But often times in programming, we want to do more thorough testing than just a bunch of specific magic numbers. The concept of _smoke testing_ is meant to test functions by giving them a bunch of basic inputs, and making sure our functions don't crash and provide reasonable input. You last job is to write three new function calls to your `make_creature` function that instead of using "hard coded" inputs, uses calls to the `random` module that's built into Python.

You'll need to:

1. Import the `random` module into your file (hint: do this at the top of your file)
2. Write one function call to `make_creature` that uses two function calls to `randint` to place the creature at a random (x,y) coordinate on the canvas.
3. Write one function call to `make_creature` that uses a function call to `randint` to generate a random size of your creature.
4. Write one function call to `make_creature` that uses two function calls to `choice` to pick random a `primary_color` and `secondary_color`. (Hint: you can use the palette below or select your own random palette of colors)

```python
palette = ['royalblue', 'cornflowerblue', 'lightsteelblue', 'mistyrose', 'lightsalmon', 'tomato']
```

Make sure your program runs with the three new function calls and that you get different results each time you run your program.

* * *

## What to Submit

If your function is working correctly, draws at least 4 shapes as part of your creature, and all of the input parameters will be honored (i.e. the creature will be drawn at the correct position at (roughly) the specified size, and with the specified colors). Make sure to submit ONLY your `hw03.py` file to Canvas by the deadline.

* * *

## Requesting an extension

If you need to request an extension on this assignment use the <a target="_blank" href="https://docs.google.com/forms/d/e/1FAIpQLSeqyOhXfPiVuHh5AF5AIcoGEeTnMaq7o2P6yJzujFkQyXXSOA/viewform?usp=sf_link">Extension Request form</a>. Please see the Syllabus for requirements. Your extension is automatically accepted if you meet the conditions. You will see your due date on Canvas update 24 hours prior to the original deadline.
