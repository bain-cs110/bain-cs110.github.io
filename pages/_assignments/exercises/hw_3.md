---
layout: assignment-two-column
title: Making Compound Shapes
abbreviation: HW3
type: homework
due_date: 2024-01-26
ordering: 3
points: 100
draft: 0
canvas_id: 
canvas_title: Homework 3
canvas_assignment_group: "Homework"
canvas_points_possible: 100
canvas_submission_types: "online_upload"
canvas_allowed_extensions: "py"
---

> **LEARNING OBJECTIVES:**
>
> 1. More practice working with built-in functions
> 1. Practice writing your own functions

<img class="creature" src="{{site.url}}/assets/images/hw03/creature.png" /> In this assignment, you are going to write some functions to draw compound shapes of your own design/choosing usingtkinter. At the end of this assignment, someone should be able to use your function to draw your creature: anywhere on the screen at any size or color. In other words, your function needs to honor the parameters that are passed into it. If you don't quite know what this means (it's a confusing concept for people just learning to program), make sure to ask questions!


<a class="nu-button" href="{{site.url}}/course-files/homeworks/hw03/hw3_template.py" target="_blank">
    Homework Starter File <i class="fas fa-download"></i>
</a>

Make sure to download the above template and move it to your `cs110` folder. Rename it `hw03.py` so you know exactly which file to submit when you're done. Then download the following shape library (like we did in the tutorial) and move it into the same folder!

<a class="nu-button" href="{{site.url}}/course-files/homeworks/hw03/hw3_shapes.py" target="_blank">
    Homework Shapes File <i class="fas fa-download"></i>
</a>

<br>

* * *

## Part 1: Compound Shape Warmup

Your first task is to write a function called `flower`, that draws a 4-petal flower like the below. Your function must be named `flower` and have the following inputs:

* A positional (required) parameter, `center`, specifying the x-y position of the center of your flower (should be a `tuple`).
* A keyword (optional) parameter, `radius_x`, specifying the radius in the x-direction of each petal (the default should be 50).
* A keyword (optional) parameter, `radius_y`, specifying the radius in the y-direction of each petal (the default should be 10).
* A keyword (optional) parameter, `color` (a `str`) which specifies the color of the petals. You can choose which color is the default value.

<details>
  <summary><b>Hints!</b></summary>
  <ul>
    <li>First make a single oval and place it at the right coordinate; save it in a variable</li>
    <li>Then make 3 more ovals – now we don't care about where they go; just about their size and color. Save them in variables so we can use them later</li>
    <li>Now rotate each of those 3 ovals using the rotate function (don't rotate the first one, then rotate the second one by 45 degrees, then 90 degrees, then 135 degrees)</li>
    <li>Finally, use the overlay function on each shape to overlay it onto the original oval!</li>
  </ul>
</details>


For example, I used these calls to make the flowers below (note, I used the `interpolate_colors` function to make multi-colored petals; yours can just be a single color).
```python
flower((450, 450), color="green")
flower((100, 100), color="red")
flower((300, 450), color="yellow")
flower((750, 300), color="cyan")
```

<details>
  <summary><b>Finished Product Screenshot</b></summary>
  <img alt="screenshot of flowers" class="medium frame center" src="{{site.url}}/assets/images/hw03/flowers.png" />
</details>

Make sure to test your function by writing some function calls. Remember, your function needs to use all of its inputs. (Hint: You'll need to use `overlay` and `rotate`)

* * *

## Part 2: Design your creature

On paper, sketch out some creature ideas (aim for using between 5-8 shapes). These can be different variations of the same creature or all different ones. You can just implement the head of your creature (similar to the bear at the top) or the whole thing — the choice is up to you. Here are some links to ideas:

* <a href="https://www.youtube.com/watch?v=yh_A09CrT68" target="_blank">https://www.youtube.com/watch?v=yh_A09CrT68</a>
* <a href="https://www.pinterest.com/pin/118782508901992203/" target="_blank">https://www.pinterest.com/pin/118782508901992203/</a>
* <a href="https://stock.adobe.com/images/cute-simple-shape-monster-character-vector-flat-graphic-design-illustration-set/209183229" target="_blank">Simple monster designs</a>
* <a href="https://goo.gl/hKewyL" target="_blank">https://goo.gl/hKewyL</a>

After you've done some sketching on paper, _select the one_ that you would like to use for the assignment and draw the creature bigger on a different piece of paper — ideally graph paper — and label the points that will help you to program your creature. Remember, to think in terms of shapes that we already know how to make in TKinter: ovals, circles, bullseyes, squares/rectangles, and polygons! Just like we have with ovals, circles, squares, etc, you'll be responsible for writing a _function_ that creates your creature from a series of parameters (center coordinate, width, etc.).

{: .blockquote-no-margin}
> **AGAIN:** Making a simple creature (e.g using 5-8 shapes) is totally fine. You don’t need to get too detailed unless you want to! And you can always enhance your creature at a later point in time.

* * *

## Part 3: Implement your creature using function calls

Once you are satisfied with your animal concept, draw those shapes inside your `hw03.py` file. You can use any combination of shapes (points, lines, polygons, rectangles, ovals, etc.) from Tutorial 3. This first "sketch" of your creature need only create _a single creature_ (i.e. if you run it over and over again it'll make the same creature over and over again). _Once you've gotten this simple version working_, then you can work on "parameterizing" it like we did Mario in Tutorial 3 (in the next part you'll turn this creature into a `creature` function).

<details>
  <summary><b>Tips!</b></summary>
  <ol>
  <li>You are free to use either method of compounding: math (HW2 or Mario) or layout functions (Tutorial 3 Part 1)</li>
  <li>Keep it simple (we recommend anywhere between 5 (minimum) to 8 shapes)! You can always add more functionality later.</li>
  <li>Make only one or two changes at a time and then test out those changes by running your file. This makes things easier to debug.</li>
<li>Use the grid that gets drawn to help you figure out the "math" behind your design! If you find the grid annoying you can comment it out by searching for the function call to make_grid and adding a # at the beginning of the line.</li>
  </ol>
</details>

* * *

## Part 4: Turn it into a `creature` function

Once your program successfully draws the creature that you sketched, we're going to turn it into a function (just like we did with mario). We'll start by adding positional and keyword parameters. First write a function header (<mark>the name needs to be</mark> `creature`) with the following inputs:

* A positional (required) parameter, `center`, specifying the x-y position of the center of your creature (should be a `tuple`).
* A keyword (optional) parameter, `primary_color` (a `str`) specifying the primary color of the creature. In the case of the bear, this is the face color. Remember, optional parameters require default values. You can choose which color to be the default value.
* A keyword (optional) parameter, `secondary_color` (a `str`) specifying the secondary color of the creature. In the case of the bear pictured above, this was the ear color. You can choose which color you'd like to be the default value.
* A keyword (optional) parameter, `size`, specifying the size of the creature (should be an `int` or `float`). You can choose the default value.
* If you want to add other parameters (for instance, the size of the ears for the bear) you are free to do so to further customize your creature, but make sure they are **optional** parameters!

Then move all of your creature code into the body of that function.

* * *

## Part 5: Parameterizing

Now comes the hard part, change your program so that it is _parameterized_–that is, instead of drawing a SINGLE version of your creature, it uses the inputs to the function to draw _any different creature_ specified by the inputs (e.g. different location, different size, different colors, etc.)

When you're done, please try at least three calls to the `creature` function, using different arguments to verify your function creates your creature at different locations, sizes, and colors. For instance, after completing the assignment, I used my `creature` function in the following way to produce the drawing below (feel free to use whatever arguments you want for your positional / keyword parameters):

```python
# with a function, you can make slightly different versions of your design,
# thereby reusing the same code over and over again
creature((92, 115))
creature((487, 110), size=101)
creature((650, 423), primary_color="#aebb83", secondary_color="#227876")
creature((333, 650), secondary_color="#3f5364", size=50)
creature((117, 875), size=91, primary_color="#648d8e", secondary_color="#afc272")
creature((875, 469), size=122, primary_color="#3f5364", secondary_color="#bfdc65")
```


<details>
<summary><b>Having a problem with your creature sizes?</b></summary>
Depending on how you implement the size input in your function body, your creature might appear WAY too <em>big</em> or WAY too <em>small</em>. While we won't be expecting an exact relationship between the size of your creature and the actual visual size it ends with, it should be roughly like our creature below. If you find your creature to be way too big with the test calls, an easy way to fix this is to, at the very beginning of your function, do the following:
<br><br>

size = size / 10
<br><br>

this just says "make the size 1/10 the size someone entered". Depending on your design, you might need to tweak that denominator to scale the image well. If your creature is too small on the other hand, you might do:
<br><br>

size = size * 10
<br><br>

The cool thing about this fix is that all it's doing is changing the value stored in the `size` variable. We only need to change it in that one place because everywhere we use `size`, python will use the smaller value cause that's what's stored in there!
</details>
<br>

<details>
  <summary><b>Finished Product Screenshot</b></summary>
  <img alt="screenshot of creatures" class="medium frame center" src="{{site.url}}/assets/images/hw03/creatures.png" />
</details>

* * *

## Part 6: Smoke Testing your Function

Using the above example tests is a great way to make sure that your function works as described. But often times in programming, we want to do more thorough testing than just a bunch of specific magic numbers. The concept of _smoke testing_ is meant to test functions by giving them a bunch of basic inputs, and making sure our functions don't crash and provide reasonable input. You last job is to write three new function calls to your `creature` function that instead of using "hard coded" inputs, uses calls to the `random` module that's built into Python (1. for random location; 2. for random size; 3. for random colors)

<details>
  <summary><b>Step by Step</b></summary>
<ol>
<li>Import the random module's functions named randint and choice into your file (hint: do this at the top of your file)</li>
<li>Write one function call to `creature` that uses two function calls to randint to place the creature at a random (x,y) coordinate on the canvas.</li>
<li>Write one function call to creature that uses a function call to randint to generate a random size of your creature.</li>
<li>Write one function call to creature that uses two function calls to choice to pick random a primary_color and secondary_color. (Hint: you can make a palette by just making a list of some of the colors you've loved or <a href="http://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html">pick some new ones</a>!)</li>
</ol>
</details>
<br>
Make sure your program runs with the **five** new function calls and that you get different results each time you run your program.

* * *

## What to Submit

If your function is working correctly, draws at least 5 shapes as part of your creature, and all of the input parameters will be honored (i.e. the creature will be drawn at the correct position at (roughly) the specified size, and with the specified colors). Make sure to submit ONLY your `hw03.py` file to Canvas by the deadline.

{% include submission_details.md %}
