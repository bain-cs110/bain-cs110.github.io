---
layout: assignment-two-column
title: Practice with Functions
type: tutorial
abbreviation: Tutorial 2
draft: 0
points: 100
num: 1
canvas_title: Tutorial 2
canvas_id: 1357225
canvas_assignment_group: "Tutorial"
canvas_points_possible: 100
canvas_submission_types: "online_upload"
canvas_allowed_extensions: "rkt"
due_date: 2024-01-17
---

This tutorial is a warmup for HW 2. Please download the starter file and complete the instructions outlined below.

If you've never done this before, there are a lot of little typing / logic / conceptual mistakes that **everyone** makes. Please pay careful attention and help each other complete the assignment!

<a class="nu-button" href="{{site.url}}/course-files/tutorials/tutorial2/tutorial2_template.py" target="_blank">
    Tutorial Starter File<i class="fas fa-download"></i>
</a>

Once you've gotten the file, rename it to `tutorial02.py` and move it into your `cs110` folder.

{: .blockquote-no-margin}
> **LEARNING OBJECTIVES:**
> In order to prepare you for this week's homework, we wanted to use this tutorial session to go over a couple of important logistical and conceptual ideas.
>
> 1. Creating functions
> 1. Working with parameters & arguments
> 1. Translating specifications into smaller steps that a computer can perform

* * *

## Getting Started

Go ahead open the file in IDLE and you'll find the same file we left off with in the pre-recorded lecture. That means we've got one turtle named `shelly` and we've got a function named `draw_diamond` with the following parameters:

* `side_length` (`int`) - which defines how long each side will be in the diamond
* `color` (`str`) (_optional_) - which allows us to specifcy a diamond color (defaults to `"green"`)

* * *

## Task 1

First, write 4 function calls to `draw_diamond` to practice calling this newly defined function.

1. Draw a diamond of size 50 with the default color.
2. Draw a red diamond of size 100.
3. Draw a purple diamond of size 300.
4. Draw a diamond of any color you find from [this color chart](http://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html) at a size that is the result of some mathematical operation (`e.g. 37 / 8 * 2 - 2`)

* * *

## Task 2

`draw_diamond` works really quite well. However...it's got a fatal flaw. At the bottom of your program add the following line:

```python
franklin = MyTurtle(x=200, y=0, pencolor="cyan")
```

This creates a new turtle and names it `franklin` (note, the `MyTurtle` function is one that creates new turtles).

Now, write a function call to `draw_diamond` to have our new turtle `franklin` (they'll be the cyan one to the right of `shelly`) draw a diamond.

> **Note**: Yes, this is a trick question.

Take another look at the `draw_diamond` function's **body**. What turtle does it always ask to move? `shelly`! Your task is to modify the `draw_diamond` header to add a _positional_ parameter called `some_turtle`, which is then used in place of `shelly` in the function's body. In other words, `draw_diamond` will now be a function with the following parameters:

* `some_turtle` (`MyTurtle`) - which specifies which turtle to have draw the diamond
* `side_length` (`int`) - which defines how long each side will be in the diamond
* `color` (`str`) (_optional_) - which allows us to specify a diamond color (defaults to `"green"`)

Note, this will break your earlier function calls from Task 1! In order to test your fix, you'll need to _add_ a specific turtle to each of those earlier function calls as well. For the first two function calls, have `shelly` draw those diamonds. For the second two, have `franklin` draw those diamonds.

* * *

## Task 3

Now take your code from HW 1 that creates a rectangle and turn it into a function called `draw_rectangle` with the following parameters:

* `some_turtle` (`MyTurtle`) - which turtle to draws the shape
* `width` (`int`) - the width of the rectangle
* `height` (`int`) - the height of the rectangle
* `color` (`str`) (_optional_) - the color of the rectangle (defaults to `"blue"`)

Test your function by drawing at least one rectangle with `shelly` and one rectangle with `franklin`.

* * *

## Task 4

Now write a function called `draw_square` with the following parameters:

* `some_turtle` (`MyTurtle`) - which turtle to draws the square
* `size` (`int`) - the side length of the square
* `color` (`str`) (_optional_) - the color of the square (defaults to `"yellow"`)

**However**, you can't use your code from HW 1. Instead, your `draw_square` function's body **must only be one line long**. (Hint: think about what the `draw_rectangle` function does and what it's parameters are...).

* * *

## Task 5

Remember our turtle activities with the blocks-based programming language? One feature that we don't currently have with our turtles is _repeating_ actions over and over again.

In this file, we have a special function called `repeat` which has the following parameters:
* `some_turtle` (`MyTurtle`) - the turtle to ask to repeat something
* `an_action` (`function`) - the action to repeat (note: this **has** to be a function with a two inputs)
* `num_times` (`int`) - the number of times to repeat the action

This is unlike any function we've seen before. Notice the second parameter _is in fact also a function itself!_ This is totally okay. In fact, there's a whole type of programming called _functional programming_ (which is what COMP_SCI 111 teaches) that is based around this idea of using functions as inputs and outputs of other functions.

In this case, you can write any function to use an input to `repeat` as long as it has exactly two parameters:
* `some_turtle` (`MyTurtle`) - the turtle to do the thing
* `i` (`int`) - which "repetition" you're currently on

and pass it as an input (by its name) to the `repeat` function. For example, try this:

```python
def gentle_turn(a_turtle, i):
    left_turn(a_turtle, i)
    forward(a_turtle, 10)
    
repeat(shelly, gentle_turn, 100) 
```

Run it and see what happens! Then, write at least one function (like `gentle_turn`) that's compatible with `repeat` and use it with `repeat` to create at least one cool design! Show it off to your team mates. If you've got something you're really proud of, raise and your hand and we'll feature it on the projector!

<details>
  <summary>Challenge: Drawing any Regular Polygon</summary>
See if you can use the `repeat` function to write a function that can have a turtle draw any regular polygon. Remember that the sum of the interior angles of a regular polygon can be calculated using the number of sides: `(n - 2) * 180`.
</details>

* * *

## Get started on HW 2

For the rest of the time remaining, get a head start on HW 2! Note that **it doesn't use turtles** and instead starts us on a higher level of abstraction. Instead of worrying about the individual steps to draw shapes...now we just immediately draw shapes! To do this we'll use a programming library called `tkinter`. More details on the HW 2 page.

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

You can just submit your `.py` file to the Canvas assignment.
