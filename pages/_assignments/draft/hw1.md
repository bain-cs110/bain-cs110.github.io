---
layout: assignment-two-column
title: Installation & Introductory Exercises
abbreviation: HW1
type: homework
due_date: 2022-04-08
ordering: 1
draft: 1
points: 8
---

<style>
    .screenshot {
        width: 100%;
        border: solid 1px #ccc;
        padding: 6px;
        border-radius: 5px;
    }
</style>

<img class="screenshot" src="/assets/images/hw01/idle2.png" />

In the Interpreter window above, you can write a single line of python at the **&gt;&gt;&gt;** prompt. For instance:

`print("hello world!")`

However, in this class, you'll be writing larger programs that are saved as files that end with the "**.py**" extension. By writing your code in a file and then running that file, you will be able to execute many lines of code at once. To try this out, we will practice writing a Python file in this week's homework. Please follow the steps outlined below, and then complete the exercises.

### Step 1: Organize yourself!
File management and organization are an essential part of programming. As such, we suggest the following system:
1. Create a course folder: **cs110**
2. Create a **homework** folder inside of the cs110 folder.
3. Create a **hw01** folder inside of your homework folder.

Sample file structure (there will be course lecture files as well):

```
cs110
    |-- homework
    │   |-- hw01
    │   |-- hw02
    |   ...
    |
    |-- lectures
        |-- lecture_01
        |-- lecture_02
        |-- lecture_03
        ...
    |-- tutorials
        |-- tutorial_01
        |-- tutorial_02
        ...
```

It may seem trivial, but take some time now to organize yourself. It will save you time in the long run!

### Step 2: Complete the following exercises
Download the [main.py](../course-files/homework/hw01/main.py) starter file and save it in your hw01 folder. To edit **main.py** using IDLE:

1. Right click on the **main.py** file that you just saved in your **hw01 folder** and open it with IDLE.
2. You should now see some python code. Click anywhere inside that file so that your cursor is now in that window.
3. Hit F5 (if you're on a MAC with a touchbar, hit the **fn** key and then **F5**). As an alternative to F5, you can also go to the Run menu and select **Run Module**. Your code will then be executed by the Python interpreter.

When you're done, please complete the following 9 exercises by editing the **main.py** file using IDLE.

#### 1. Print a box like the one below:
```
*******************
*******************
*******************
*******************
```

#### 2. Print a box like the one below:
```
*******************
*                 *
*                 *
*******************
```

#### 3. Print a triangle like the one below:
```
*
**
***
****
```

#### 4. Write a program that computes and prints the result of:
<img src="/assets/images/hw01/equation.png" style="width: 100px;"/>

(The answer is roughly 0.1017).

#### 5. User input
Ask the user to enter a number. Convert it to an int, and print out the square of the number, but use the end optional argument to print it out in a full sentence that ends in a period (e.g. “The square of 5 is 25.”).
Sample output is shown below:

```python
Enter a number: 5 	     # prompt the user for a number (not necessarily 5)
The square of 5 is 25.   # output a sentance that communicates the result of the calculation
```

#### 6. Practice with the "sep" optional parameter
Ask the user to enter a number x. Use the sep optional argument to print out x, 2x, 3x, 4x, and 5x, each separated by three dashes, like below:

```python
Enter a number: 7         # prompt the user for a number (not necessarily 7)
7---14---21---28---35     # output the result
```

#### 7. Math Practice
Write a program that asks the user for a weight in kilograms and converts it to pounds. There are 2.2 pounds in a kilogram.

```python
Enter weight in kg: 5         # prompt the user for a weight in kg
5 kilograms is 11.0 pounds.   # output the result
```

#### 8. Calculate Average
Write a program that asks the user to enter three numbers (use three separate input statements). Create variables called _total_ and _average_ that hold the sum and average of the three numbers and print out the values of total and average.


#### 9. Tip Calculator
Write a tip calculator. Ask the user for the price of the meal and the percent tip they want to leave. Then print both the tip amount and the total bill with the tip included.


## What to Submit
Please submit a ZIP file that includes code that successfully implements the exercises above. If you've never made a ZIP file before, please make sure to review the lecture from Friday, April 1 or watch this walk-through for Mac computers or [this walkthrough for Windows computers]()

Before each exercise, use comments (or keep the existing ones) to indicate the number of the exercise that your code corresponds to.

## Request an Extension
If you need to request an extension on the assignment (must be 24 hours in advance) use the <a href="https://forms.gle/PobKBdUkTpPJ3GbZ8">Extension Request form</a>.
