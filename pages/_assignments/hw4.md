---
layout: assignment-two-column
title: Animations & Landscapes
abbreviation: HW4
type: homework
due_date: 2022-05-06
points: 8
draft: 0
---


<a class="nu-button" href="/course-files/homework/hw04_template.zip" target="_blank">
    Homework Starter Files <i class="fas fa-download"></i>
</a>

In this homework assignment, you'll be moving from making "static" pictures like in HW2 and HW3, to making live animations! Make sure to complete [Tutorial 5](tutorial05) before attempting this homework. Once you've finished Tutorial 5, you'll see how the `utilities.update_position` function makes our work a little easier by getting rid of some of the steps of animation.

Note there are a number of functions in `utilities.py` that you *can* use but you only *have* to use `update_position` to complete this assignment (though `get_left` and `get_right` might be useful depending on your approach to part 2). You _should not_ use any function that starts with an underscore. These are called "private functions" and are ONLY meant for use within that one particular file.

{: .blockquote-no-margin}
> **LEARNING OBJECTIVES:**
> 1. Practice working with loops
> 1. Practice working with if statements
> 1. Practice working with the random module

## Part 1: Landscapes

In `main.py`, replace the code on lines 18-21 (which is repetitive) with a loop (any kind of loop you want) that makes at least 10 to 30 clouds the top portion of the screen. Hints:

1. Use a loop
1. Use the random module, and in particular the [random.randint](https://docs.python.org/3/library/random.html#random.randint) function to give each cloud a random (x, y) position (given the dimensions of the screen). (Remember, you need to import the module in order to use it just like we imported the time module in the tutorial this week.)

### Optional enhancements
1. Modify make_cloud to make more realistic clouds
1. Make the clouds sometimes look like storm clouds
1. Animate your clouds

## Part 2: Animation

{: .blockquote-no-margin}
> **NOTE: There is an important difference between this assignment and the tutorial.**<br>
> In the tutorial, you had to manually delete mario each time you wanted to move the picture across the screen. In this homework we have a special function in the utilities library called `utilities.update_position` that gets rid of that step completely. Rather than having to erase and draw a completely new mario each time, this function allows us to specify a particular `tag` and move that shape by a certain amount in the x and/or y direction. However, you still have to use `gui.update()` to update the screen and the `time` library to control how fast the animation goes.

Below the part of your program where you make your clouds, you'll need to do the following:

<div>
  <ol>
        <li>Animate the car so that it moves across the screen.</li>
        <li>If the car gets to the end of the screen, it should seamlessly be moved to the beginning of the screen.</li>
        <li>Create a second car (your choice of new color) using the `shapes.make_car` function. Be sure to give your new car a unique tag.</li>
        <li>Make the second car move in the opposite direction, and also loop back around when it gets to the end of the screen (see the video below)</li>
    </ol>
</div>

<iframe src="https://northwestern.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=99980f14-bfe6-4986-a09c-ae89004d2ab2&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=true&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

Hint 1: You will only have 1 "animation loop" to animate both the cars.

Hint 2: To reset the cars position, you need to use a conditional to check the car's position each time it moves.

Hint 3: To find the left-most or right-most x-coordinate of a tagged object, you can use the `utilities.get_left` and `utilites.get_right` functions.

### Optional enhancements
The more you practice, the better you'll get!

1. Make the cars accelerate over time (start off slow and gradually move faster)
1. Add your creature to your animation:
    * Inside `shapes.py`:
      * Add your `make_creature` function definition (adapt from Homework 3).
      * Modify your `make_creature` function so that each constituent shape of your creature gets assigned a tag (study the `make_car` function and do the same thing).
    * animate your creature
1. Use loops and the random module to make many moving cars.

## What to Submit
When you’re done with the assignment, please submit a zip file called `hw04.zip` that contains the all of the files.

## Request an Extension
If you need to request an extension on the assignment (must be 24 hours in advance) use the <a href="https://forms.gle/PobKBdUkTpPJ3GbZ8">Extension Request form</a>.
