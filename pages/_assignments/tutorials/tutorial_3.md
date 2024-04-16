---
layout: assignment-two-column
title: Practice with Compound Shapes
type: tutorial
abbreviation: Tutorial 3
draft: 0
points: 100
num: 3
due_date: 2024-04-17
canvas_title: Tutorial 3
canvas_id: 1409417
canvas_assignment_group: "Tutorial"
canvas_points_possible: 100
canvas_submission_types: "online_upload"
canvas_allowed_extensions: "py"
---

In this tutorial, we're going to A. practice using sequences and writing reporters; B. make more compound shapes like you did in HW 2.

First, download the starter template and move it into your `cs110` folder.

<a class="nu-button" href="{{site.url}}/course-files/tutorials/tutorial3/tutorial3_template.py" target="_blank">
    Tutorial 3 Starter File <i class="fas fa-download"></i>
</a>

Then grab this <code>shapes</code> helper and move it into the same folder as your tutorial file. <mark>In order for this activity to work at all, these files must BOTH be in the same folder on your computer.<mark>

<a class="nu-button" href="{{site.url}}/course-files/tutorials/tutorial3/cs110_t3_shapes.py" target="_blank">
    Tutorial Shapes Module <i class="fas fa-download"></i>
</a>

<br>

* * *
## Part 1 - Reporter Practice

Let's get some practice with sequences of data and with writing some reporters! First, locate the part of your template that says:

```
## Reporter and Sequence Practice goes here
```

**Activity 1.** First create a <code>list</code> called <code>my_favorite_things</code> and in it, store the following pieces of data in the order specified below:

* Your favorite number (<code>int</code>) (position `0`)
* Your favorite color (<code>string</code>) (position `1`)
* Your favorite TV show (<code>string</code>) (position ...)
* The department code of your favorite class at NU so far (e.g. COMP_SCI, HIST, MATH, etc.) (<code>string</code>)
* The class number of your favorite class at NU so far (e.g. `110`, `211`, etc.) (<code>int</code>)
* A list that contains all of the courses you're taking this quarter (e.g. <code>["COMP_SCI 110", "HIST 202", "ECON 304"]</code>) (list of <code>string</code>s)

For example, here's what mine would look like (go ahead and copy my fave things into your program and make sure to name yours <code>my_favorite_things</code> so that they're both in Python's brain):

```python
bains_favorite_things = [13, "green", "The West Wing", 
                        "COMP_SCI", 111, 
                        ["COMP_SCI 110", "COMP_SCI 396", 
                         "COMP_SCI 399"]]
```

**Activity 2.** Now write a function called `get_favorite_color` that takes as its only input a list of someone's favorite things and **returns** their _favorite color_. You can test your function by making sure that when you run the following program:

```python
my_fave_color = get_favorite_color(my_favorite_things)
print("My favorite color is: " + my_fave_color)

bains_fave_color = get_favorite_color(bains_favorite_things)
print("Dr. Bain's favorite color is: " + bains_fave_color)
```

You see both your favorite color printed AND my favorite color printed **and do not see <code>None</code> printed** (this would be a sign that your function is not actually a reporter).

**Activity 3.** Now write a functions called `multiply_favorite_numbers` that takes in **two inputs**, which are two favorite things lists like the above, and **returns** the product of the two favorite numbers. For instance, if you ran it like below:

```python
print("The product of my our fave numbers is...") 
print(multiply_favorite_numbers(my_favorite_things, bains_favorite_things))
```

You'd see whatever the result of multiplying 13 (my favorite number) by your favorite number is.

**Activity 4.** Finally, write a function called <code>rando_class</code> that takes in a list of someone's favorite things and **returns** a randomly selected class from their current enrollments. To test it, run it like the below several times and see if you get a different class each time!

```python
print("Rando class: " + rando_class(my_favorite_things))
print("Rando class: " + rando_class(my_favorite_things))
print("Rando class: " + rando_class(my_favorite_things))
```

<details>
<summary>Can't remember how to use the <code>random</code> module?</summary>
<ul>
<li>First you'll need to import the appropriate function near the top of your program: <code>from module_name import function_name</code></li>
<li>The module we want to use is called <code>random</code></li>
<li>The function that randomly selects an element from a list is called <code>choice</code></li>
<li><code>choice</code> is a reporter that takes a sequence as input and _returns_ a randomly chosen element from the list.</li>
</ul>
</details>

<details>
<summary>Did you get the same course everytime?</summary>
<ul>
<li>Any chance you did something like: <code>return choice(list_name[-1])</code>?</li>
<li>If so, you're on the right track...but Python is a peculiar language. It's trying to be helpful but is instead doing something we can't actually see.</li>
<li>Instead of this approach try separating out the random choice and return steps.</li>
<li>So first...<code>chance = choice(list_name)</code></li>
<li>And then <code>return chance</code></li>
</ul>
</details>

* * *

## Part 2 - Compound Shapes

Alright, time to have some fun with art. In last week's HW you only had access to an `oval` function. Then on Friday in-class, we introduced the `rectangle` function. Today, WE UNLEASH THE TRUE POWER OF SHAPES. Here, you access to all of the functions described in the below:

<a class="nu-button" href="{{site.url}}/course-files/tutorials/tutorial3/docs/cs110_t3_shapes.html" target="_blank">
    Shapes Module Documentation <i class="fas fa-download"></i>
</a>
<br>

Which includes a variety of dope shapes:

* rectangle
* square
* oval
* circle
* triangle
* line
* arc
* star
* polygon
* spiral

<mark>Pay very close attention to the type of inputs each one requires.</mark> They're different than our functions from last week!

* * *

## Task 1
 
Spend a few minutes calling each of these functions. If you were super comfortable with oval, circle, rectangle, and square, skip straight to triangle, polygon, and line. Make sure to experiment with different inputs to get a sense of what sorts of shapes each function can make. Tag team with your team mates and try unique inputs.

<details>
<summary>Want some cooler colors to work with?</summary>
<img style="width: 90%;" src="{{site.url}}/assets/images/tutorial3/colors.png" alt="Color names">
</details>

* * *

## Task 2

Now, in HW 2 (and in Part 2 of this tutorial), we used a bit of math to draw shapes on top of each other. However, we could also use some _layout functions_ to do the same thing! All the shape functions are **reporters** meaning they _return the shape they create back to us_. That means we could store that shape in a variable or use it as an input to another function! In addition to those shape functions we explored in the prior task, this file also has access to a bunch of layout functions which are also described in the documentation linked above:

* <code>overlay</code>
* <code>underlay</code>
* <code>above</code>
* <code>below</code>
* <code>beside</code>
* <code>duplicate</code>
* <code>rotate</code>

Try out each of these functions with some of the shapes. Here's an example:

```python
# First make a circle like we did last week
circle1 = circle(center=(200, 200), radius=50, color="red")
# Now make a square...but notice we don't need to specify a center!
a_square = square(size=25, color="blue")
# Now rotate the square to make it more like a diamond
a_square = rotate(a_square, degrees=45)
# Finally use overlay to position the diamond ON TOP of the circle 
overlay(a_square, circle1)
# notice, in this example we didn't have to ever think about the location of any shape
# other than the first one we drew!
```

* * *

## Task 3

Now we're going to make a compound shape using these new techniques – namely the [flag of the Chicago](https://en.wikipedia.org/wiki/Flag_of_Chicago).

> **Note**: Want to make a different flag? Go for it!

You'll need, at minimum, to use <code>rectangle</code>, <code>star</code>, and <code>overlay</code> to recreate the shape. Here's what mine looked like below:

<img style="width: 50%;" alt="sample chicago flag" src="{{site.url}}/assets/images/tutorial3/flag.png"/>

<mark>If you have extra time, get started on HW 3.</mark>

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
