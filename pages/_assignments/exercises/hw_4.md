---
layout: assignment-two-column
title: Animations & Landscapes
abbreviation: HW4
type: homework
due_date: 2023-05-05
points: 100
draft: 0
canvas_id: 1224383
---

In this homework assignment, you'll be moving from making "static" pictures like in HW2 and HW3, to making live animations! Make sure to complete [Tutorial 3](tutorial03) before attempting this homework. Once you've finished Tutorial 3, you'll see how the `hw04_utilities.update_position` function makes our work a little easier by getting rid of some of the steps of animation.

Note there are a number of functions in `hw04_utilities.py` that you *can* use but you only *have* to use `update_position` to complete this assignment (though `get_left` and `get_right` might be useful depending on your approach to part 2). You _should not_ use any function that starts with an underscore. These are called "private functions" and are ONLY meant for use within that one particular file.

{: .blockquote-no-margin}
> **LEARNING OBJECTIVES:**
> 1. Practice working with loops
> 1. Practice working with if statements
> 1. Practice working with modules

<a class="nu-button" href="/course-files/homeworks/hw04_template.py" target="_blank">
    Homework Starter File <i class="fas fa-download"></i>
</a>

<br>

<a class="nu-button" href="/course-files/homeworks/hw04_utilities.py" target="_blank">
    Utilities Library <i class="fas fa-download"></i>
</a>
<br>
<br>

Because we're now dealing with TWO files, you need to make sure they are BOTH in the same folder (but you will only submit the `hw04.py` file.)

> **Note:** Having trouble with IDLE and the Utilities file? See <a href="https://edstem.org/us/courses/37920/discussion/3050854" target="_blank">this edSTEM post to see if your issue is an easy fix.</a>

* * *

## Part 0: Actually Using `tkinter`

I've got some good news...and I've got some bad news. Let's start with the bad news. We've been lying to you for 4 weeks. `tkinter`'s y-axis is actually flipped from what we're used to from 8th grade math.

<img class="frame center med-lg" src="/assets/images/project01/grid.svg" />

We've been taking care of this for you with some magic in the templates you've started with...but we're removing that scaffold starting for this assignment. This means moving <mark>UP in the `tkinter` world means DECREASING the y-value</mark> and <mark>moving DOWN means INCREASING the y-value</mark>. We'll warn you about this in each of the parts below.

* * *

## Part 1: Landscapes

In the `hw04_utilities.py` file you've downloaded. There's a `make_cloud` function that accepts the following inputs:
1. a `canvas` to draw on 
2. a `center` tuple `(x,y)` to draw the center of the cloud.

In your `hw04.py`, replace the code in the landscape portion of the file near the top where it calls the `make_cloud` function several times (which is repetitive) with a loop (any kind of loop you want) that makes at least 10 to 30 clouds the top portion of the screen. Hints:

1. Use a loop
1. Use the random module, and in particular the [random.randint](https://docs.python.org/3/library/random.html#random.randint) function to give each cloud a random (x, y) position (given the dimensions of the screen). (Remember, you need to import the module in order to use it just like we imported the time module in the tutorial this week.)
1. **remmber the y-axis is flipped now** which means you'll use y-values **CLOSE TO 0** because that will representative of the TOP of the screen.

### Optional enhancements
1. Modify `make_cloud` to make more realistic clouds
1. Make the clouds sometimes look like storm clouds
1. Animate your clouds

* * *

## Part 2: Make Creature from HW 3 Animatable

Scroll through `hw04.py` until you see the section labeled: `#### PUT YOUR CREATURE BELOW HERE ####`.

> **Note**: This assumes that your `make_creature` function worked correctly from HW 3. If it did not, we encourage you to go to office hours to get it working and fulfilling the requirements in the assignment.

Now, copy and paste your function definition for `make_creature` from HW 03 into this space. Some tips/reminders:
1. **DO NOT INCLUDE ANY FUNCTION CALLS TO `make_creature`**
2. If you used "helper functions" like `make_circle`, `make_square`, or `make_bullseye` you'll need to copy those definitions into this space as well. Make sure to put them ABOVE the `make_creature` defintion, **not** inside it.
3. Remember, inside of our `make_creature` body, we ONLY want to draw on the canvas GIVEN TO us to draw on–that is, the one specified in the function's header. If you've followed the instructions, that's called `a_canvas`. Inside your function's body, _make sure you only see uses of `a_canvas` and not `the_canvas`. Remember, `the_canvas` works in OUR file...but the moment we send our function to another person to draw on their canvas, they won't have access to it anymore.

Now...if you add a call to your copied `make_creature` function in the appropriate section of the file, you'll notice some weird stuff. Your beautiful creature is upside down! Why...oh yeah, it's cause the y-axis is flipped. Luckily this is easy to fix!

### Fixing the y-axis

In the body of `make_creature` you'll (**as a human**) just need "run" the following algorithm:

```
for shape in each_of_your_shapes:
    look to see if the y-coordinate is being shifted from the center or corner (i.e. relatively placed)
    if it is:
        if the offset is positive, flip it to negative
        otherwise if its negative, flip it to positive
    else:
        leave it alone
```

Again, that is NOT code you put in Python. That is a series of steps YOU will take to flip each of your y-values.

Once you've done this, you should now be able to run your program and see that your creature is back to normal! Nice work. On to the animation portion!

### Adding a `tag` to your Creature

In order to make the animation process as simple as possible, `tkinter` relies on there being a `tag` (`str`) for each shape / shape group on the canvas. You can think of it as a "name" for each shape in your creature. If you wanted to make the individual shapes that make up your creature animate separately, each one wolud need a separate name. In this assignment, we want to animate _all_ of the parts of our creature at once so we're going to simplify the process a little by giving _all_ of the constituent shapes in our creature the same tag. To do this, you'll need to do the following:

#### Step 1
First, we need to add a new **optional** parameter to our `make_creature` function. Let's call it `my_tag` and have it default to an empty string (`""`).

#### Step 2
Now comes the hard part. We need to go to each shape that makes up your creature and make sure it gets assigned a tag. The process of adding this tag depends on what sort of shape you drew for each of your feature creatures.

_For each shape..._

* If your shape is drawn by calling a method of the `a_canvas` object (e.g `a_canvas.create_oval(...)`) then you should follow these steps:

Since you're using the built-in shape methods to the `Canvas` object, we need to obey the rules of the people who wrote this function. These functions all have an **optional** parameter called `tags` (note the plural here) that can be set to any string. Let's imagine I had a call to the `create_polygon` function like the below:

```python
a_canvas.create_polygon([(0,0), (100, 100), (0, 100)], fill="green")
```

Then all I need to do is make sure I ALSO set the `tags` parameter in this function call to whatever tag has been inputted into `make_creature`. Since we named that parameter `my_tag`, then we'd update this line to:

```python
a_canvas.create_polygon([(0,0), (100, 100), (0, 100)], fill="green", tags=my_tag)
```

* Otherwise, if your shape is drawn by calling a helper function (e.g `make_oval` or `make_square`) then you should follow these steps:

Since you're taking advantage of a helper function, we'll need to follow a slightly different set of steps. First, find the helper function's header. Add a new **optional** parameter to it, let's call it `tag` (to differentiate it from the earlier `my_tag` parameter we added to `make_creature`) and have it default to the empty string (`""`). Okay, now OUR helper function accepts this input, but what about all of the functions we actually call inside its body? We'll need to take care of those next.

For each of the function calls inside this helper function's body, you'll either see something of the form `a_canvas.create_oval(...)` in which case you can follow the instructions above except...instead of giving it a value of `my_tag`, we'll give it the value of `tag` since in this function, that's the name of our input that representst the tag.

If you instead run into yet ANOTHER helper function...well then you need to repeat these steps on THAT helper function as well.

**Last but not least**, you need to actually add the parameter to your function call in the original `make_creature` body. Here's an example of doing this with my square face dude from <a href="https://edstem.org/us/courses/37920/discussion/2964272" target="_blank">edSTEM post</a>.

### Example

```python
def make_square(a_canvas, bottom_left, width, color="blue"):
    a_canvas.create_rectangle(
        bottom_left,
        (bottom_left[0] + width, bottom_left[1] + width),
        fill=color)

def make_creature(a_canvas, center, width):
    big_square_width = width
    center_x = center[0]
    center_y = center[1]
    # face
    make_square(a_canvas, 
                (center_x - width / 2, center_y - width / 2), 
                width, 
                color="green") 
    # left eye
    make_square(a_canvas, 
                (center_x - width / 3, center_y + width / 6), 
                big_square_width / 6, 
                color="purple")
    # right eye
    make_square(a_canvas, 
                (center_x + width / 6, center_y + width / 6), 
                big_square_width / 6, 
                color="white")
    # nose
    make_square(a_canvas, 
                (center_x - width / 60, center_y - width / 60), 
                width / 30, 
                color="white")
```

First we add the new `my_tag` parameter to `make_creature`:
```python
def make_creature(a_canvas, center, width, my_tag=""):
    big_square_width = width
    center_x = center[0]
    center_y = center[1]
    # face
    make_square(a_canvas, (center_x - width / 2, center_y - width / 2), width, color="green") # face
    # left eye
    make_square(a_canvas, (center_x - width / 3, center_y + width / 6), big_square_width / 6, color="purple")
    # right eye
    make_square(a_canvas, (center_x + width / 6, center_y + width / 6), big_square_width / 6, color="white")
    # nose
    make_square(a_canvas, (center_x - width / 60, center_y - width / 60), width / 30, color="white")
```

Then we tackle the constitutent shapes. The big sqaure face is first. It's drawn via a helper function so I need to go look at its function header and add the `tag` parameter.

```python
def make_square(a_canvas, bottom_left, width, color="blue", tag=""):
    a_canvas.create_rectangle(
        bottom_left,
        (bottom_left[0] + width, bottom_left[1] + width),
        fill=color)
```

Now this helper function uses in its body a call to `create_rectangle`, so I need to take the `tag` that `make_square` gets and feed it into `create_rectangle`'s `tags` parameter:

```python
def make_square(a_canvas, bottom_left, width, color="blue", tag=""):
    a_canvas.create_rectangle(
        bottom_left,
        (bottom_left[0] + width, bottom_left[1] + width),
        fill=color
        tags=tag
        )
```

BOOM. But don't forget that I now need to go back and add this new parameter to the call to `make_square` that actually draws the face:

```python
def make_creature(a_canvas, center, width, my_tag=""):
    big_square_width = width
    center_x = center[0]
    center_y = center[1]
    # face
    make_square(a_canvas, 
                (center_x - width / 2, center_y - width / 2),
                width, 
                color="green", tag=my_tag)
    # right eye
    make_square(a_canvas, 
                (center_x - width / 3, center_y + width / 6),
                big_square_width / 6, 
                color="purple")
    # left eye
    make_square(a_canvas, 
                (center_x + width / 6, center_y + width / 6),
                big_square_width / 6, 
                color="white")
    # nose
    make_square(a_canvas, 
                (center_x - width / 60, center_y - width / 60), 
                width / 30, 
                color="white")
```

I now just need to repeat the process for the rest of the shapes that make up my face! Let's look at the right eye next. It ALSO uses the helper function `make_square`...to which I already added the `tag` paremeter in the previous step! That means all I need to do is use it!

```python
def make_creature(a_canvas, center, width, my_tag=""):
    big_square_width = width
    center_x = center[0]
    center_y = center[1]
    # face
    make_square(a_canvas, 
                (center_x - width / 2, center_y - width / 2), 
                width, 
                color="green", tag=my_tag)
    # right eye
    make_square(a_canvas, 
                (center_x - width / 3, center_y + width / 6), 
                big_square_width / 6, 
                color="purple", tag=my_tag)
    # left eye
    make_square(a_canvas, 
                (center_x + width / 6, center_y + width / 6),
                big_square_width / 6, 
                color="white")  
    # nose
    make_square(a_canvas, 
                (center_x - width / 60, center_y - width / 60),
                width / 30, 
                color="white")
```

And repeat!
```python
def make_creature(a_canvas, center, width, my_tag=""):
    big_square_width = width
    center_x = center[0]
    center_y = center[1]
    # face
    make_square(a_canvas, 
                (center_x - width / 2, center_y - width / 2), 
                 width, 
                 color="green", tag=my_tag)
    # right eye
    make_square(a_canvas, 
                (center_x - width / 3, center_y + width / 6), 
                big_square_width / 6, 
                color="purple", tag=my_tag)
    # left eye
    make_square(a_canvas, 
                (center_x + width / 6, center_y + width / 6),
                big_square_width / 6, 
                color="white", tag=my_tag)
    # nose
    make_square(a_canvas, 
                (center_x - width / 60, center_y - width / 60), 
                width / 30, 
                color="white", tag=my_tag)  # nose
```

A completed example of this for my car creature is on <a href="https://edstem.org/us/courses/37920/discussion/3069299" target="_blank">edSTEM</a>.

All that for one lousy animation. This better be worth it...

* * *

## Part 3: Animate your Creatures

<mark>In the tutorial</mark> you had to manually delete Mario, then redraw him in a new place to move him across the screen. For the homework, since we don't need to "change" the version of the creature you're drawing each time, just update it's position, we can make this process a little simpler. Rather than doing the two step process of ERASE and DRAW, <mark>in this homework you can move your creature by using the function described below.</mark>

Here's the documentation from `update_position` (which you can see by opening the utilities file).

```python
'''
Name: update_position
Purpose: updates the x and y position of all shapes that have been tagged
with the tag argument
Inputs:
    1. a canvas (Canvas) to search
    2. a tag (str) to move
    3. x (int; optional) amount to move in the x direction
    4. y (int; optional) amount to move in the y direction
'''
```

That means to move, say, an object tagged `"mario"` 50 units in the x direction we'd just say:

```python
hw04_utilities.update_position(the_canvas, "mario", x=50)
```

Below the part of your program where you make your clouds, you'll need to do the following:

<div>
  <ol>
        <li>Create your creature somewhere on the bottom half of the screen. (make sure your call to <pre>make_creature</pre> goes inside the section labeled <pre>### YOUR CALLS TO MAKE_CREATURE</pre></li>
        <li>Animate that creature so that it moves across the screen.</li>
        <li>If the creature gets to the end of the screen, it should seamlessly be moved to the beginning of the screen.</li>
        <li>Create a second creature (e.g. use your same <pre>make_creature</pre> function but give it different colors, size, etc.; like my two cars in the video below). Be sure to give your new creature a <em>unique</em> tag.</li>
        <li>Make the second creature moves in the opposite direction, and also loops back around when it gets to the end of the screen (see the video below where I use a car as my creature)</li>
    </ol>
</div>

<iframe src="https://northwestern.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=99980f14-bfe6-4986-a09c-ae89004d2ab2&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=true&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

Hint 1: You will only have 1 "animation loop" to animate both the creatures. (See edSTEM for more on this)

Hint 2: To reset the creatures position, you need to use a conditional to check the creatures's position each time it moves.

Hint 3: To find the left-most or right-most x-coordinate of a tagged object, you can use the `hw04_utilities.get_left` and `hw04_utilities.get_right` functions. You can see what inputs those functions require by looking in the `hw04_utilities.py` file. There are examples of how to call those functions INCLUDED in the template file.

Hint 4: If you need to find the WIDTH of your object...get this...there's a function called `hw04_utilities.get_width`. Now why might that be useful...(see Hint 5).

Hint 5: In order to "reset" each creature once they go off the screen, you can still use `update_position`. The screen is 1000 pixels wide.

Hint 6: If you find only PART(s) of your creature moving but not others, it means you missed tagging one of the shapes in Part 2. Double check you've tagged all those shapes!

#### Optional enhancements
The more you practice, the better you'll get!

1. Make the creatures accelerate over time (start off slow and gradually move faster)
1. Use loops and the random module to make many moving creatures.

* * *
## What to Submit

If your function is working correctly, it'll look like the video above...but with your creature! Make sure to submit ONLY your `hw04.py` file to Canvas by the deadline.

* * *

## Requesting an extension

If you need to request an extension on this assignment use the <a target="_blank" href="https://docs.google.com/forms/d/e/1FAIpQLSeqyOhXfPiVuHh5AF5AIcoGEeTnMaq7o2P6yJzujFkQyXXSOA/viewform?usp=sf_link">Extension Request form</a>. Please see the Syllabus for requirements. Your extension is automatically accepted if you meet the conditions. You will see your due date on Canvas update 24 hours prior to the original deadline.
