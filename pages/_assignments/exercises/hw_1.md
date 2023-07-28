---
layout: assignment-two-column
title: Introductory Exercises
abbreviation: HW1
type: homework
due_date: 2023-04-07
ordering: 1
draft: 0
points: 100
canvas_id: 1224380
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

1. Store data in variables
2. Identify a data type
2. Doing basic math in Python
3. Use the `input` function
4. Use the `print` function
4. Call some basic turtle functions

* * *

## Part 0: Download the Template File

First create a new folder in your CS 110 folder, inside the `homeworks` folder called `hw01` (or some variation).

Then download the starter file by clicking on the big button below.

<a download class="nu-button" href="{{site.url}}/course-files/homeworks/hw01_template.py" target="_blank">
    Homework Starter File <i class="fas fa-download"></i>
</a>

Move the downloaded file into your new `hw01` folder **and rename it `homework_01.py` so you don't accidentally get it confused with any other versions**.

* * *

## Part 1: More Turtle Programming

1. Right click on the **homework_01.py** file that you just saved in your **hw01 folder** and open it with IDLE.
2. You should now see some python code. Click anywhere inside that file so that your cursor is now in that window.
3. Hit F5 (if you're on a Mac, hit the **fn** key and then **F5**). As an alternative to F5, you can also go to the Run menu and select **Run Module**. Your code will then be executed by the Python interpreter. Right now, it doesn't do much, but using just `forward`, `left`, and `right` we can make some cool stuff!

Please complete the following exercises by editing the **homework_01.py** file using IDLE:

1. Teach `turtle_1` to draw a square
2. Teach `turtle_2` to draw a green rectangle
3. Teach `turtle_3` to draw a red equilateral triangle (3 equal length sides)
4. Teach `turtle_4` to draw a house (a square with an equilateral triangle on top)
> Hint: You can't just paste the two solutions together. Think about which direction your turtle is facing when it stops and starts drawing! It might help to play out the turtle's motion yourself!
5. (Optional) Teach `turtle_5` to draw something interesting!

> Hint: Don't forget about the turtle function cheatsheet from Lecture 4!
> Hint 2: **YOU MUST USE EXACTLY THESE TURTLE NAMES, just like we used `shelly` in the tutorial.


After completing all 4 exercises, your screen should look something like this (your shapes might be different sizes and colors):

<img src="{{site.url}}/assets/images/hw01/turtles.png" style="width: 33%;" class="screenshot"/>

## Part 2: Some Calculator Programs
Next we'll focus on some numerical programming toward the bottom of the `homework_01.py` file.

#### 1. Write a program that computes and prints the result of:

<img src="{{site.url}}/assets/images/hw01/equation.png" style="width: 30%" class="screenshot"/>

(The answer is roughly 0.1017).

#### 2. User input of `string`s
Write a program to ask the user to enter their name. Then print a message that says "hello" to them. For example, this is what you would see if you used my name (notice we use a `prompt`):

```python
Enter a name:Connor 	   # prompt the user for a name (not necessarily Connor)
Hello there, Connor        # output a sentence that says hello! (make sure there's a space)
```

#### 3. User input of numbers
Write a program that asks the user for a weight in kilograms and converts it to pounds. There are 2.2 pounds in a kilogram. You only need to worry about whole number weight entries. This is what it should look like:

```python
Enter weight in kg:5          # prompt the user for a weight in kg
5 kilograms is 11.0 pounds.   # output the result
```

#### 4. Calculate the length of an inputted string
Write a program that asks the user to input a word and then tell the user how many letters are in that word. For example:

```python
Enter a word:supercalifragilisticexpialidocious # prompt the user for a word
There are 34 letters in that word.   # output the result
```

* * *

## Turning it in

Most of the Exercises in this class will be graded via an autograder – a program, written in Python, that will run your program and test it to see if it meets all the expectations of the assignment.

This means that you must _carefully_ read each assignment description and follow it exactly. If your assignment does not satisfy the requirements in any way (even if you think it's small and inconsequential) you will receive points off (or in the worst case, not receive any points at all). For this assignment, you should make sure your turtle drawing looks like the one featured above and that the math calculations produce the expected output as specified.

For this assignment, you will upload your `homework_01.py` file to the assignment on Canvas. DO NOT UPLOAD ANY OTHER FILES. Once you've submitted your file to Canvas, you're done! You do not need to add your `netid` to the file like we did alast week.

<a href="https://community.canvaslms.com/t5/Student-Guide/How-do-I-upload-a-file-as-an-assignment-submission-in-Canvas/ta-p/274" target="_blank">Need help submitting a file to Canvas? See this video.</a>

> **Note**: You will not receive feedback from the autograder on your assignment until AFTER the final due date (which is the "available until date on Canvas").

* * *

## Requesting an extension
If you need to request an extension on this assignment use the <a target="_blank" href="https://docs.google.com/forms/d/e/1FAIpQLSeqyOhXfPiVuHh5AF5AIcoGEeTnMaq7o2P6yJzujFkQyXXSOA/viewform?usp=sf_link">Extension Request form</a>. Please see the Syllabus for requirements. Your extension is automatically accepted if you meet the conditions. You will see your due date on Canvas update approximately 24 hours prior to the original deadline.