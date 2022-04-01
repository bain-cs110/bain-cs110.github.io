---
layout: assignment-two-column
title: Introductory Exercises
abbreviation: HW1
type: homework
due_date: 2022-04-08
ordering: 1
draft: 0
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

However, in this class, you'll be writing larger programs that are saved as files that end with the "**.py**" extension. By writing your code in a file and then running that file, you will be able to execute many lines of code at once.

{: .blockquote-no-margin}
> ### Please complete Tutorial 1 First!
> This assumes that you have already successfully completed and submitted [Tutorial 1](tutorial01). If you have not done so yet, please go do that first.

### Step 1: Download the Template Files
Download the [template files](../course-files/homework/hw01_template.zip) starter file and save it in your hw01 folder. *Make sure to extract it so that you can see the individual files (and on a Winwdows PC) you don't see that pink thing at the top of the Explorer.* We've demoed this in class a few times, but for PC users, remember there's a video walkthrough from [Lecture 02](/lectures/week01_lecture03).

Move the resulting folder into your homework folder.

### Step 2: More Turtle Programming
We'll first focus on programming our turtles in the `turtle_programs.py` file.
To edit **turtle_programs.py** using IDLE:

1. Right click on the **turtle_programs.py** file that you just saved in your **hw01 folder** and open it with IDLE.
2. You should now see some python code. Click anywhere inside that file so that your cursor is now in that window.
3. Hit F5 (if you're on a MAC with a touchbar, hit the **fn** key and then **F5**). As an alternative to F5, you can also go to the Run menu and select **Run Module**. Your code will then be executed by the Python interpreter.

When you're done, please complete the following exercises by editing the **turtle_programs.py** file using IDLE:

#### 1. Teach `turtle_1` to draw a square

#### 2. Teach `turtle_2` to draw a green rectangle

#### 3. Teach `turtle_3` to draw a red equilateral triangle (3 equal lengthed sides)

#### 4. Teach `turtle_4` to draw a house (a square with an equilateral triangle on top)

#### (Optional) 5. Teach `turtle_5` to draw something interesting!

After completing all 4 exercises, your screen should look something like this (your shapes might be different sizes and colors):

<img src="/assets/images/hw01/turtles.png" style="width: 100%;"/>


### Step 3: Some "Text" Programming
Next we'll focus on some numerical programming in the `calculator_programs.py` file.
To edit **calculator_programs.py** using IDLE, follow the same steps as before when you opened the turtles file. Once you've opened it, please complete the following exercises:

#### 1. Write a program that computes and prints the result of:
<img src="/assets/images/hw01/equation.png" style="width: 100px;"/>

(The answer is roughly 0.1017).

#### 2. User input of `string`s
Write a program to ask the user to enter their name. Then print a message that says "hello" to them. For example, this is what you would see if you used my name:

```python
Enter a name: Connor 	     # prompt the user for a name (not necessarily Connor)
Hello there, Connor        # output a sentence that says hello!
```

#### 3. User input of numbers
Write a program that asks the user for a weight in kilograms and converts it to pounds. There are 2.2 pounds in a kilogram. This is what it should look like:

```python
Enter weight in kg: 5         # prompt the user for a weight in kg
5 kilograms is 11.0 pounds.   # output the result
```

#### 4. Calculating the length of an input string
Write a program that asks the user to input a word and then tell the user how many letters are in that word. For example:

```python
Enter a word: supercalifragilisticexpialidocious # prompt the user for a word
There are 34 letters in that word.   # output the result
```

## What to Submit
Please submit a *single* ZIP file of your entire `hw01` folder. Make sure that folder has both your `calculator_programs.py` file as well as your `turtle_programs.py` file before you ZIP it (Note: there will be a third file called `MyTurtle.py` that you shouldn't mess with - just leave it be and submit it as part of your ZIP). For more on how to make ZIP files, make sure to review [Tutorial 1](/tutorials/tutorial01)
## Request an Extension
If you need to request an extension on the assignment (must be 24 hours in advance) use the <a href="https://forms.gle/PobKBdUkTpPJ3GbZ8">Extension Request form</a>.
