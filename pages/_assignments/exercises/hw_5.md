---
layout: assignment-two-column
title: Intro to Animation
canvas_title: Homework 5
abbreviation: HW5
type: homework
due_date: 2024-02-09
points: 100
draft: 0
canvas_id: 
canvas_assignment_group: "Homework"
canvas_points_possible: 100
canvas_submission_types: "online_upload"
canvas_allowed_extensions: "py"
---

In this homework assignment, you'll be moving from making "static" pictures like in HW2 and HW3, to making live animations! Make sure to complete Tutorial 4 before attempting this homework. Once you've finished Tutorial 3, you'll see how the `move` function makes our work a little easier by getting rid of some of the steps of animation.

Note there are a number of functions in `hw5_utilities.py` that you *can* use but you only *have* to use `move` and `cloud`. You *should not* use any function that starts with an underscore. These are called "private functions" and are ONLY meant for use within that one particular file. In fact...rather than reading the .py file, instead, you can click on this dope purple button and see all the functions you have available to you and their documentation!

<a class="nu-button" href="{{site.url}}/course-files/homeworks/hw5/docs/hw5_utilities.html" target="_blank">
    Utilities Library Documentation
</a>
<br>

{: .blockquote-no-margin}
> **LEARNING OBJECTIVES:**
>
> 1. Practice working with loops
> 1. Practice working with if statements
> 1. Practice working with modules

<a class="nu-button" href="{{site.url}}/course-files/homeworks/hw5_template.py" target="_blank">
    Homework Starter File <i class="fas fa-download"></i>
</a>

You need to make sure they are BOTH in the same folder (but you will only submit the `hw5.py` file.)

<a class="nu-button" href="{{site.url}}/course-files/homeworks/hw5_utilities.py" target="_blank">
    Utilities Library File<i class="fas fa-download"></i>
</a>


* * *

## Part 1: Landscapes

In the `hw5_utilities.py` file you've downloaded. There's a `cloud` function that accepts the following inputs:

1. a `center` (tuple; `(x,y)`) to draw the center of the cloud.
2. a `tag` (`string`) to "name" the cloud (so it could be later animated)

In your `hw5.py`, find the `setup` function's body. In it, you'll find a call to a function called `setup_clouds` with an input of `30` which is right above `setup`. In it, you'll see the `cloud` function called several times (which is repetitive). Your job is to rewrite the `setup_clouds` function using a loop (any kind of loop you want) which makes however many clouds is specified by the input `num_clouds` at the top portion of the screen. <mark>Each cloud must have a <b>unique</b> tag that cannot start with a number</mark> I recommend `"cloud_1"`, `"cloud_2"`, etc..

<details>
  <summary><b>Hints!</b></summary>
  <ol>
  <li>Use a loop</li>
  <li>To generate a unique tag, consider starting a variable called <code>cloud_counter</code> and making sure to add one to it every time you make a new cloud. Use that <code>cloud_counter</code> variable as the basis of your tag!</li>
  <li>Use the <code>random</code> module, and in particular the <a href="https://docs.python.org/3/library/random.html#random.randint"><code>randint</code></a> function to give each cloud a random (x, y) position (given the dimensions of the screen). (Remember, you need to import the module in order to use it).</li>
  <li><b>remember</b> the y-axis is flipped now** which means you'll use y-values **CLOSE TO 0** because that will representative of the TOP of the screen.</b></li>
  </ol>
</details>

<details>
  <summary><b>Optional Enhancements</b></summary>
  <ol>
    <li>Make a new function called <code>storm_cloud</code> to make storm clouds!</li>
    <li>Make a new function called <code>realistic_cloud</code> to make more realistic clouds!</li>
    <li>Animate your clouds</li>
  </ol>
</details>

* * *

## Part 2: Make Creature from HW 3 Move

Scroll through `hw5.py` until you see the section labeled: `#### PUT YOUR CREATURE BELOW HERE ####`.

> **Note**: This assumes that your `creature` function worked correctly from HW 3. If it did not, we encourage you to go to office hours to get it working!

Now, copy and paste your _function definition_ for `creature` from HW 3 into this space. If you used "helper functions" outside of the hw3 shapes functions we provided, you'll need to copy those definitions into this space as well. Make sure to put them ABOVE the `creature` definition, **not** inside it.

### Adding a `tag` to your creature

Like in the tutorial this week, we're going to encounter a problem: if we don't tell `tkinter` what shapes constitute a more compound shape (e.g. mario, your creature, etc.) **it has no idea that they are connected**.

`tkinter` instead relies on there being a `tag` (`str`) for each compound shape (i.e. shape group) in the window. You can think of it as a "name" for the shapes that make up your creature. If you wanted to make the individual shapes that make up your creature animate separately, each one would need a separate name. In this assignment, we want to animate *all* of the parts of our creature at once so we're going to simplify the process a little by giving *all* of the constituent shapes in our creature the same tag. To do this, you'll need to do the following:

#### Step 1

First, we need to add a new **optional** parameter to our `creature` function. Let's call it `tag` and have it default to an empty string (`""`).

#### Step 2

Now comes the hard part. We need to go to each shape that makes up your creature and make sure it gets assigned a tag. The process of adding this tag depends on what sorts of shape you drew for each of your feature creatures. **For each shape that makes up your creature...**

* Find the function call in the body of `creature` that creates the shape. For instance, you might see a call to the `oval` function.

```python
oval(center=(450,450), radius_x=50, radius_y=100, color="green")
```

* The new version of the `oval` function included in `hw5_utilities` supports an input called `tag` that allows you to give that shape a tag.

```python
oval(center=(450,450), radius_x=50, radius_y=100, color="green", tag=some_value_thats_a_string)
```

<details>
<summary><b>Example</b></summary>

Say we had the following function:

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">def</span> <span class="nf">creature</span><span class="p">(</span><span class="n">center</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="mi">25</span><span class="p">):</span>
    <span class="n">big_square_width</span> <span class="o">=</span> <span class="n">size</span>
    <span class="n">center_x</span> <span class="o">=</span> <span class="n">center</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
    <span class="n">center_y</span> <span class="o">=</span> <span class="n">center</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
    <span class="c1"># face
</span>    <span class="n">square</span><span class="p">(</span><span class="n">top_left</span><span class="o">=</span><span class="p">(</span><span class="n">center_x</span> <span class="o">-</span> <span class="n">size</span> <span class="o">/</span> <span class="mi">2</span><span class="p">,</span> <span class="n">center_y</span> <span class="o">-</span> <span class="n">size</span> <span class="o">/</span> <span class="mi">2</span><span class="p">),</span>
           <span class="n">size</span><span class="o">=</span><span class="n">width</span><span class="p">,</span>
           <span class="n">color</span><span class="o">=</span><span class="s">"green"</span><span class="p">)</span>
    <span class="c1"># right eye
</span>    <span class="n">square</span><span class="p">(</span><span class="n">top_left</span><span class="o">=</span><span class="p">(</span><span class="n">center_x</span> <span class="o">-</span> <span class="n">size</span> <span class="o">/</span> <span class="mi">3</span><span class="p">,</span> <span class="n">center_y</span> <span class="o">+</span> <span class="n">size</span> <span class="o">/</span> <span class="mi">6</span><span class="p">),</span>
           <span class="n">size</span><span class="o">=</span><span class="n">big_square_width</span> <span class="o">/</span> <span class="mi">6</span><span class="p">,</span>
           <span class="n">color</span><span class="o">=</span><span class="s">"purple"</span><span class="p">)</span>
    <span class="c1"># left eye
</span>    <span class="n">square</span><span class="p">(</span><span class="n">top_left</span><span class="o">=</span><span class="p">(</span><span class="n">center_x</span> <span class="o">+</span> <span class="n">size</span> <span class="o">/</span> <span class="mi">6</span><span class="p">,</span> <span class="n">center_y</span> <span class="o">+</span> <span class="n">size</span> <span class="o">/</span> <span class="mi">6</span><span class="p">),</span>
           <span class="n">size</span><span class="o">=</span><span class="n">big_square_width</span> <span class="o">/</span> <span class="mi">6</span><span class="p">,</span>
           <span class="n">color</span><span class="o">=</span><span class="s">"white"</span><span class="p">)</span>
    <span class="c1"># nose
</span>    <span class="n">square</span><span class="p">(</span><span class="n">top_left</span><span class="o">=</span><span class="p">(</span><span class="n">center_x</span> <span class="o">-</span> <span class="n">size</span> <span class="o">/</span> <span class="mi">60</span><span class="p">,</span> <span class="n">center_y</span> <span class="o">-</span> <span class="n">size</span> <span class="o">/</span> <span class="mi">60</span><span class="p">),</span>
           <span class="n">size</span><span class="o">=</span><span class="n">width</span> <span class="o">/</span> <span class="mi">30</span><span class="p">,</span>
           <span class="n">color</span><span class="o">=</span><span class="s">"white"</span><span class="p">)</span>
</code></pre></div></div>

First we add the new <code>tag</code> parameter to <code>creature</code>:

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">def</span> <span class="nf">creature</span><span class="p">(</span><span class="n">center</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="mi">25</span><span class="p">,</span> <span class="n">tag</span><span class="o">=</span><span class="s">""</span><span class="p">):</span>
    <span class="n">big_square_width</span> <span class="o">=</span> <span class="n">size</span>
    <span class="n">center_x</span> <span class="o">=</span> <span class="n">center</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
    <span class="n">center_y</span> <span class="o">=</span> <span class="n">center</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
    <span class="c1"># face
</span>    <span class="n">square</span><span class="p">(</span><span class="n">top_left</span><span class="o">=</span><span class="p">(</span><span class="n">center_x</span> <span class="o">-</span> <span class="n">size</span> <span class="o">/</span> <span class="mi">2</span><span class="p">,</span> <span class="n">center_y</span> <span class="o">-</span> <span class="n">size</span> <span class="o">/</span> <span class="mi">2</span><span class="p">),</span>
           <span class="n">size</span><span class="o">=</span><span class="n">width</span><span class="p">,</span>
           <span class="n">color</span><span class="o">=</span><span class="s">"green"</span><span class="p">)</span>
    <span class="c1"># right eye
</span>    <span class="n">square</span><span class="p">(</span><span class="n">top_left</span><span class="o">=</span><span class="p">(</span><span class="n">center_x</span> <span class="o">-</span> <span class="n">size</span> <span class="o">/</span> <span class="mi">3</span><span class="p">,</span> <span class="n">center_y</span> <span class="o">+</span> <span class="n">size</span> <span class="o">/</span> <span class="mi">6</span><span class="p">),</span>
           <span class="n">size</span><span class="o">=</span><span class="n">big_square_width</span> <span class="o">/</span> <span class="mi">6</span><span class="p">,</span>
           <span class="n">color</span><span class="o">=</span><span class="s">"purple"</span><span class="p">)</span>
    <span class="c1"># left eye
</span>    <span class="n">square</span><span class="p">(</span><span class="n">top_left</span><span class="o">=</span><span class="p">(</span><span class="n">center_x</span> <span class="o">+</span> <span class="n">size</span> <span class="o">/</span> <span class="mi">6</span><span class="p">,</span> <span class="n">center_y</span> <span class="o">+</span> <span class="n">size</span> <span class="o">/</span> <span class="mi">6</span><span class="p">),</span>
           <span class="n">size</span><span class="o">=</span><span class="n">big_square_width</span> <span class="o">/</span> <span class="mi">6</span><span class="p">,</span>
           <span class="n">color</span><span class="o">=</span><span class="s">"white"</span><span class="p">)</span>
    <span class="c1"># nose
</span>    <span class="n">square</span><span class="p">(</span><span class="n">top_left</span><span class="o">=</span><span class="p">(</span><span class="n">center_x</span> <span class="o">-</span> <span class="n">size</span> <span class="o">/</span> <span class="mi">60</span><span class="p">,</span> <span class="n">center_y</span> <span class="o">-</span> <span class="n">size</span> <span class="o">/</span> <span class="mi">60</span><span class="p">),</span>
           <span class="n">size</span><span class="o">=</span><span class="n">width</span> <span class="o">/</span> <span class="mi">30</span><span class="p">,</span>
           <span class="n">color</span><span class="o">=</span><span class="s">"white"</span><span class="p">)</span>
</code></pre></div></div>

Then we tackle the constituent shapes. Since my creature is relatively simple, I just need to go through each square, and label it with whatever tag someone has asked me to use!

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">def</span> <span class="nf">creature</span><span class="p">(</span><span class="n">center</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="mi">25</span><span class="p">,</span> <span class="n">tag</span><span class="o">=</span><span class="s">""</span><span class="p">):</span>
    <span class="n">big_square_width</span> <span class="o">=</span> <span class="n">size</span>
    <span class="n">center_x</span> <span class="o">=</span> <span class="n">center</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
    <span class="n">center_y</span> <span class="o">=</span> <span class="n">center</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
    <span class="c1"># face
</span>    <span class="n">square</span><span class="p">(</span><span class="n">top_left</span><span class="o">=</span><span class="p">(</span><span class="n">center_x</span> <span class="o">-</span> <span class="n">size</span> <span class="o">/</span> <span class="mi">2</span><span class="p">,</span> <span class="n">center_y</span> <span class="o">-</span> <span class="n">size</span> <span class="o">/</span> <span class="mi">2</span><span class="p">),</span>
           <span class="n">size</span><span class="o">=</span><span class="n">width</span><span class="p">,</span>
           <span class="n">color</span><span class="o">=</span><span class="s">"green"</span><span class="p">,</span>
           <span class="n">tag</span><span class="o">=</span><span class="n">tag</span><span class="p">)</span>
    <span class="c1"># right eye
</span>    <span class="n">square</span><span class="p">(</span><span class="n">top_left</span><span class="o">=</span><span class="p">(</span><span class="n">center_x</span> <span class="o">-</span> <span class="n">size</span> <span class="o">/</span> <span class="mi">3</span><span class="p">,</span> <span class="n">center_y</span> <span class="o">+</span> <span class="n">size</span> <span class="o">/</span> <span class="mi">6</span><span class="p">),</span>
           <span class="n">size</span><span class="o">=</span><span class="n">big_square_width</span> <span class="o">/</span> <span class="mi">6</span><span class="p">,</span>
           <span class="n">color</span><span class="o">=</span><span class="s">"purple"</span><span class="p">,</span>
           <span class="n">tag</span><span class="o">=</span><span class="n">tag</span><span class="p">)</span>
    <span class="c1"># left eye
</span>    <span class="n">square</span><span class="p">(</span><span class="n">top_left</span><span class="o">=</span><span class="p">(</span><span class="n">center_x</span> <span class="o">+</span> <span class="n">size</span> <span class="o">/</span> <span class="mi">6</span><span class="p">,</span> <span class="n">center_y</span> <span class="o">+</span> <span class="n">size</span> <span class="o">/</span> <span class="mi">6</span><span class="p">),</span>
           <span class="n">size</span><span class="o">=</span><span class="n">big_square_width</span> <span class="o">/</span> <span class="mi">6</span><span class="p">,</span>
           <span class="n">color</span><span class="o">=</span><span class="s">"white"</span><span class="p">,</span>
           <span class="n">tag</span><span class="o">=</span><span class="n">tag</span><span class="p">)</span>
    <span class="c1"># nose
</span>    <span class="n">square</span><span class="p">(</span><span class="n">top_left</span><span class="o">=</span><span class="p">(</span><span class="n">center_x</span> <span class="o">-</span> <span class="n">size</span> <span class="o">/</span> <span class="mi">60</span><span class="p">,</span> <span class="n">center_y</span> <span class="o">-</span> <span class="n">size</span> <span class="o">/</span> <span class="mi">60</span><span class="p">),</span>
           <span class="n">size</span><span class="o">=</span><span class="n">width</span> <span class="o">/</span> <span class="mi">30</span><span class="p">,</span>
           <span class="n">color</span><span class="o">=</span><span class="s">"white"</span><span class="p">,)</span>
           <span class="n">tag</span><span class="o">=</span><span class="n">tag</span>
</code></pre></div></div>
</details>
<br>

* * *

## Part 3: Instantiate your Creatures

In the `setup` function, below your clouds, call your newly improved `creature` function twice. The first creature needs to be in the bottom left hand portion of the screen <mark>and must have the tag <code>"creature_1"</code></mark>. The second creature needs to be in the bottom right hand portion of the screen <mark>and must have the tag <code>"creature_2"</code></mark>. Make sure to use different colors, sizes, etc., for the two creature calls like my two cars in the below screenshot.

* * *

## Part 4: Animate your Creatures

<mark>In the tutorial</mark> you had to manually delete Mario, then redraw him in a new place to move him across the screen. For the homework, since we don't need to "change" the version of the creature you're drawing each time, just update its position, we can make this process a little simpler. Rather than doing the two step process of ERASE and DRAW, <mark>in this homework you can move your creature by using the function described below.</mark>

Here's the documentation from `move`:

```python
'''
Name: move
Purpose: updates the x and y position of all shapes that have been tagged
with the tag argument
Inputs:
    1. a tag (str) to move
    2. x_shift (int; optional) amount to move in the x direction
    3. y_shift (int; optional) amount to move in the y direction
'''
```

That means to move, say, an object tagged `"mario"` 50 units in the x direction we'd just say:

```python
move("mario", x_shift=50)
```

Find the function definition called `go` near the bottom of the file. This is a function that is called using a `while` loop all the way at the bottom of the file. You can assume two things about this function: 1. it is continuously called when your program runs (i.e. once `go` finishes...it gets called again without any intervention on your part!); 2. there exists a global variable called `ticks` that counts how many times the `go` function has been called that you can use anywhere in your `go` function if you'd like.

Your job for this task is to...
<div>
  <ol>
        <li>Animate creature tagged <code>"creature_1"</code> so that it moves across the screen smoothly from left to right.</li>
        <li>If the creature gets to the end of the screen, it should seamlessly be moved to the beginning of the screen.</li>
        <li>Animate the creature tagged <code>"creature_2"</code> opposite direction, and also loops back around when it gets to the end of the screen (see the video below where I use a car as my creature)</li>
    </ol>
</div>

<iframe src="https://northwestern.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=99980f14-bfe6-4986-a09c-ae89004d2ab2&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=true&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>


<details>
  <summary><b>Hints!</b></summary>
  <ol>
  <li>To reset the creatures position, you need to use a conditional to check the creatures's position each time it moves.</li>
  <li>To find the left-most or right-most x-coordinate of a tagged object, you can use the <code>get_left</code> and <code>get_right</code> functions.</li>
  <li>If you need to find the <em>width</em> of your object...get this...there's a function called <code>get_width</code>. Now why might that be useful...(see Hint 4)</li>
  <li>In order to "reset" each creature once they go off the screen, you can still use <code>move</code>. The screen is 1000 pixels wide.</li>
  <li>If you find only PART(s) of your creature moving but not others, it means you missed tagging one of the shapes earlier in the HW! Double check you've tagged all those shapes!</li>
  </ol>
</details>

<details>
  <summary><b>Optional Enhancements</b></summary>
  The more you practice, the better you'll get!
  <ol>
    <li>Make the creatures accelerate over time (start off slow and gradually move faster)</li>
    <li>Use loops and the random module to make many moving creatures.</li>
    <li>Animate your clouds</li>
  </ol>
</details>

* * *

## What to Submit

If your program is working correctly, you should see something like the above linked video. Make sure to submit ONLY your `hw55.py` file to Canvas by the deadline.

{% include submission_details.md %}