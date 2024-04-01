---
layout: assignment-two-column
title: Introductory Exercises
abbreviation: HW1
type: homework
due_date: 2024-04-05
ordering: 1
draft: 0
points: 100
canvas_id: 
canvas_title: Homework 1
canvas_assignment_group: "Homework"
canvas_points_possible: 100
canvas_submission_types: "online_upload"
canvas_allowed_extensions: "py"
---

<style>
    .screenshot {
        width: 100%;
        border: solid 1px #ccc;
        padding: 6px;
        border-radius: 5px;
    }
</style>

This week's assignment is focused on writing simple programs just like the tutorial. It does not ask you to write any functions of your own (which is the focus of our Friday lecture this week).

By the end of this assignment you should be able to:

1. Call some basic turtle functions
2. Store data in variables
3. Identify a data type
4. Doing basic math in Python
5. Use the `input` function
6. Use the `print` function

* * *

## Part 0: Download the Template File

First create a new folder in your CS 110 folder, inside the `homeworks` folder called `hw01` (or some variation).

Then download the starter file by clicking on the big button below.

<a download class="nu-button" href="{{site.url}}/course-files/homeworks/hw01_template.py" target="_blank">
    Homework Starter File <i class="fas fa-download"></i>
</a>

Move the downloaded file into your new `hw01` folder **and rename it something like `hw01.py` so you don't accidentally get it confused with any other versions**.

* * *

## Part 1: More Turtle Programming

1. Open up **hw01.py** file that you just saved in your **hw01 folder** and open it with IDLE (if you're on a Mac, you can double-click on it; if you're on a Windows computer, it's often easier to first open IDLE, then click on the `File` menu then `Open`...)
2. You should now see some python code. Click anywhere inside that file so that your cursor is now in that window.
3. Hit F5 (if you're on a Mac, hit the **fn** key and then **F5**). As an alternative to F5, you can also go to the Run menu and select **Run Module**. Your code will then be executed by the Python interpreter. Right now, it doesn't do much, but using just `forward`, `left_turn`, and `right_turn` we can make some cool stuff!

Please complete the following exercises by editing the **hw01.py** file using IDLE:

1. Teach `turtle_1` to draw a square with sides of length 100.
2. Teach `turtle_2` to draw a green rectangle with sides of length 100 and 120.
3. Teach `turtle_3` to draw a red equilateral triangle (3 equal length sides) with side length 100.
4. Teach `turtle_4` to draw a house (a square of sides of 100 with an equilateral triangle with sides of 100 on top). Color(s) are up to you.

> Hint: You can't just paste the two solutions together. Think about which direction your turtle is facing when it stops and starts drawing! It might help to play out the turtle's motion yourself!

5. Teach `turtle_5` to draw something interesting! It needs to use at least two pen colors and needs to include at least 3 rotations and 3 forward commands.

> Remember: **YOU MUST USE EXACTLY THESE TURTLE NAMES**, just like we used `shelly` in the tutorial.

After completing all 5 exercises, your screen should look something like this:

<img alt="Turtle Section Complete!" src="{{site.url}}/assets/images/hw01/turtles.png" style="width: 33%;" class="screenshot"/>

## Part 2: Some Data Programs

Next we'll focus on some data programming toward the bottom of the `hw01.py` file.

#### 1. Write a program that computes and prints the result of

<img alt="sample equation" src="{{site.url}}/assets/images/hw01/equation.png" style="width: 30%" class="screenshot"/>

(The answer is roughly 0.1017). <mark>Store the result of this equation in a variable called <code>question_1</code> and then print it out.</mark>

#### 2. User input of `string`s

Write a program to ask the user to enter their name. Make a message that says "hi" to them and <mark>store the entire message in a variable called <code>question_2</code> and then print it out.</mark>

For example, this is what you would see if you used my name (notice we use a `prompt`):

```python
Enter a name:Connor  # prompt the user for a name (not necessarily Connor)
Hi Connor!           # output a sentence that says hi (make sure there's a space)
```

> Note: when your program runs, it should look exactly like the above with whatever name you input

#### 3. User input of numbers

Write a program that asks the user for a distance in kilometers and converts it to miles. There are 0.62 miles in a kilometer. You only need to worry about whole number weight entries. <mark>Store _just_ the converted value in a variable called <code>question_3</code> and then print it out in a nice message like the below.</mark>

```python
Enter weight in kg:5          # prompt the user for a weight in kg
5 kilograms is 11.0 pounds.   # output the result
```

> Note: when your program runs, it should look exactly like the above with whatever weight you input. In some circumstances, you might get
> a number with a huge number of decimal places – that's fine.

#### 4. Calculate the length of an inputted string

Write a program that asks the user to input a word and then tell the user how many letters are in that word. <mark>Store _just_ the number of letters of the inputted word in a variable called <code>question_4</code> and then print it out in a nice message like the below.</mark>

For example:

```python
Enter a word:supercalifragilisticexpialidocious # prompt the user for a word
There are 34 letters in that word.   # output the result
```

> Note: when your program runs, it should look exactly like the above with whatever name you input

* * *

## Turning it in

Most of the Exercises in this class will be graded via an autograder – a program, written in Python, that will run your program and test it to see if it meets all the expectations of the assignment.

This means that you must _carefully_ read each assignment description and follow it exactly. If your assignment does not satisfy the requirements in any way (even if you think it's small and inconsequential) you will receive points off (or in the worst case, not receive any points at all). For this assignment, you should make sure your turtle drawing looks like the one featured above and that the math calculations produce the expected output as specified.

For this assignment, you will upload your `hw01.py` file to the assignment on Canvas. DO NOT UPLOAD ANY OTHER FILES. Once you've submitted your file to Canvas, you're done! You do not need to add your `netid` to the file like we did last week.

> **Note**: The autograder won't start checking assignments until late on Monday. 

{% include submission_details.md %}
