---
layout: assignment-two-column
title: Writing Our Own Programs
type: tutorial
abbreviation: Tutorial 0
draft: 0
points: 100
num: 0
description:
    - Writing some Math Programs
    - Writing some Turtle Programs
due_date: 2023-01-11
canvas_id: 1174713
---

In tutorial today, you will meet your assigned peer mentor and fellow classmates and write a few simple programs. Attendance at the first tutorial session is **MANDATORY**. There is nothing to submit for this tutorial. You will simply show your PM your completed work and they will mark you as present.

Our objectives for this assignment are:

1. Storing data in variables
2. Doing basic math in Python
3. Understanding data types
4. Calling basic functions

* * * 
## Part 0: Meet Your Group!

A first step to building any community is to introduce yourselves! 

Once in your group, figure out who has the earliest birthday (i.e. January 1st is the earliest possible birthday). This person will go first and introduce themselves with the following:
* Name
* Major
* Year in School
* Favorite Breakfast Cereal (or other delightful breakfast delicacy)

> Note, your group will have a Peer Mentor or TA assigned to it and they will come introduce themselves as well! They'll be easy to identify as they'll all have name tags! Because PMs are assigned to multiple groups, they may not be present for all the intros and might ask you to quickly go around and say names again.

Once you've all had a chance to introduce yourselves, you can get started on your tutorial!

* * * 

## Part 1: Get Your Files Organized
Create the folder organizational structure recommended in class during Monday's Lecture.

```
cs110
    |-- homework
    │   |-- hw00
    │   |-- hw01
    |   ...
    |-- lectures
    |   -- lecture00
    │   -- lecture01
    │   -- lecture02
    │   ...
    |-- tutorials
        ...
```

* * * 

## Part 2: Create two Python files and Write Some Programs
When you're done, open IDLE and create a new python file (go to File menu > "New File"). This should open a blank document. Then save this blank document as **`grade_calculator.py`** (File menu > "Save as..."), and put it inside of your `cs110 > tutorials > tutorial00` folder (You'll need to make that `tutorial00` folder just like you did with the three top-level folders).

In this newly created `grade_calculator.py` file, you're going to write a program to calculate your grade in our class:

### Storing Data in Variables

* First create a new variable called `miniquizzes` and store in it the number `100`
    * We'll help you on this first one in Python. Copy and paste the below into your file:
    ```python
    miniquizzes = 100
    ```
    In plain English this says: "Please **assign** the value `100` to the variable named `miniquizzes`".
* Next, create a new variable called `projects` and store in it the number `95`.
* Next, create a new variable called `homeworks` and store in it the number `95`.
* Next, create a new variable called `tutorials` and store in it the number `100`.
* Finally, create a new variable called `quizzes` and store in it the number `90`.

Make sure to run your program by going to the `Run` menu at the top of the screen and selecting `Run Module...`. If you don't see any red error text, that means your program successfully ran! Since we haven't asked Python to actually output anything yet (we've only asked it to remember some numbers) we won't see any output.

### Accessing Data in Variables

Accessing data stored in a variable is as easy as using the name of the variable in another line of our program. Python will then see this name and lookup what value you've asked it to remember is stored inside that container.

Now let's actually calculate the course average for these 5 inputs. Recall from our syllabus that your grade is broken down in the following categories.

{:.medium}
| **Tutorials**     | 15% |
| **Mini-Quizzes**  | 5%  |
| **Homeworks**     | 25% |
| **2 Projects**    | 25% |
| **3 Quizzes**     | 30% |

When you see a weighted average like this, it means that different assignments are _weighted_ by their respective percentages (i.e. a category with a higher weight means it constitutes a larger part of your final grade). To calculate the final weighted average, we take the decimal form of the weight for each category and multiply that weight by the average for that category, after doing that for each category, we add up all of those calculations and that gives us our final grade. 

For example, to calculate the part of your grade determined by the tutorials, we would take the tutorial weight in decimal form (`15% -> 0.15`) and multiply it by the overall tutorial score. Then you'd repeat this process for each different assignment cateogry. Imagine you got a `100` for all 5 categories, that would mean your final grade would be calculated by saying:

**Grade Calculation Equation**
`(0.15 * 100) + (0.05 * 100) + (0.25 * 100) + (0.25 * 100) + (0.3 * 100)`

However, we need to use the grades that are stored in the variables we created earlier. For example, the overall tutorial score is scored in the variable `tutorials`. To access the actual value of that variable, we simply use its name (`tutorials`) in place of an actual number. For instance, to calculate the part of your grade determined by the tutorials, in Python we'd say:

```python
(0.15 * tutorials)
```

That says multiply `0.15` with whatever value is stored in the variable `tutorials`. When you go to run your file, Python will then lookup whatever number is stored in that container and use it for the calcuation.

* Use this example to modify the **Grade Calculation Equation** above so that is uses the variables you created earlier rather than values of `100`.
* Store the result of this calculation in a variable called `grade`
* Run your program! (if you run into an error (i.e. red text or a popup saying it can't run) raise your hand to ask for help!)

### Using the `print` Function

Well that was a let down...nothing got outputted!

Remember: _computers don't do anything we don't ask of them._ Because we didn't ask Python to output the value of `grade`, when we run our program...it doesn't output the result of the calculation.

Add a new line to your program that calls the `print` function with an input of the variable `grade`. Now try running your program again. If everything is correct with your calculator, you should see `94.5` printed out in the Interprter (`>>>`) Window since we've asked our program to output the value stored in that variable.

### Using the `input` Function

What we've done now is essentially asked the computer to remember the average of our scores across these 5 different types of assignments and then calcuate the resulting course average. Now, these variables are currently "set in stone" or _hardcoded_ to be particular numbers. In other words, every time we run this program, it will _always_ use those exact same numbers for the grade calculation. While that's fine when calculating our grade, what if we wanted to be able to send our program to a friend in the class so they could calculate their grade without modifying the code?

Using the `input` function, we can tell Python to ask the person running the program to input a number by typing it in the keyboard. The `input` function takes a `string` as an argument which represents the _prompt_ Python shows the user and returns a `string` of whatever the person typed in.

* Modify the `quizzes` variable so that instead of being _assigned_ the value of 90, it is instead assigned the value of running the below `input` function call:
  * `input("Please enter your quiz average:")`
* Now try running your program.

Did it work? No? Uh oh. Let's think about why by using the error we got as a clue:

```python
Traceback (most recent call last):
  File "/Users/username/Desktop/tutorial0/grade_calculator.py", line 7, in <module>
    grade = (0.15 * tutorials) + (0.05 * miniquizzes) + (0.25 * homeworks) + (0.25 * projects) + (0.3 * quizzes)
TypeError: can't multiply sequence by non-int of type 'float'
```

This error says it occurs on the line where we calculate the final `grade` and that it says it's a `TypeError`. In other words, Python says you asked me to multiply the value stored in this variable...but it's not a number! Why might that be? Well remember that the `input` function **returns** a `str` or `string`. But the `*` operator only knows how to deal with numbers! That means we need to convert or **cast** the value we get back from `input` from a `str` to an `int` (or integer).

To convert the `quizzes` variable to an integer we need to use the `int` function which accepts any input and will try its best to return an `int` (integer) from that input.

There's two (easy) ways you can implement this in your program.

1. You could add a new line after the line that says `quizzes = ...` that says `quizzes = int(quizzes)` – in other words, you'd ask Python to replace the existing `quizzes` variable with the result of converting whatever is currently in the `quizzes` variable to an `int`.
2. You could change the calculation of `grade` to use `int(quizzes)` rather than just `quizzes` – this essentially tells Python to not modify the original variable but to instead just convert the value for the purposes of the calculation.

Pick an approach and implement in your program. Finally Run your program again and make sure you get the expected output given your input! In fact...run it twice with two different numeric inputs (note, it will only work with whole numbers) and make sure you get two different final grades!

* * * 

## Part 3: Turtle Time!

This time, rather than starting from scratch, we're going to give you a template to work in. Click the big purple button below to download the file `turtorial.py`. Move that downloaded file into your `tutorial0` folder.

<a download class="nu-button" href="/course-files/tutorials/tutorial00/turtorial.py" target="_blank">
    Tutorial Starter File <i class="fas fa-download"></i>
</a>

* Once you've moved it, open it up in IDLE
* Modify the program so that your turtle draws a square.
* Modify the program so that after drawing a square the turtle...
  * first changes its pen color to `"cyan"`
  * then draws a rectangle (i.e. a shape with non-equal sides)
* Finally, depending on how much time is left, make a SUPER COOL design. What sorts of shapes are easy to draw? What sorts of shapes are difficult to draw?

> ### Some Pro Tips
> * Always save your python file before running it so that the interpreter "sees" your changes.
> * In order for your interpreter to recognize your file as a Python file, you must give it the **`.py`** file extension (e.g. **`my_program.py`**).
> * Don't forget to name all of your programs "snake case" (all lower case, underscores to separate words).
> * If your code doesn't run, practice reading and trying to understand (often by Googling) what the interpreter is telling you. If you see red error text, the computer is trying to tell you where the problem is.

* * * 

## Getting Credit for your Work

Because attendance is required, there is no formal submission for this tutorial on Canvas. Instead, you will show your completed program to a PM/TA and they will mark your assignment as complete.

In future weeks, you may choose to submit the tutorial assignment remotely by 11:59pm. If you choose to submit remotely your tutorial will be autograded for completeness in accuracy.