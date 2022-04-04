---
layout: assignment-two-column
title: Get Python Running
type: tutorial
abbreviation: Tutorial 1
draft: 0
points: 3
num: 2
description:
    - Installing Python 3 & IDLE
    - Writing your first programs
due_date: 2022-04-06
---

In tutorial today, you will meet your peer mentor and fellow classmates, install Python 3, and write a few simple programs. Attendance at your first tutorial session is **MANDATORY**.

{: .blockquote-no-margin}
> ### What if I've already installed Python on my laptop?
> Note: many people who have programmed with Python before already have Python 3.x installed. To check, search for an existing Python installation. If you already have a version of Python3 installed, move on to Part 2. It doesn't hurt to install another version of Python, but it's not necessary. If you have any questions, feel free to ask Connor or one of the peer mentors / TAs.

## Part 1: Install Python

We will use the Python 3 programming language and **IDLE**, which is Python's Integrated Development and Learning Environment.

Download the latest version (3.10.x) of python here: <a href="https://www.python.org/downloads/" target="_blank">https://www.python.org/downloads/</a>. You should be able to just click the big yellow "Download" button, but if it asks you which version you'd like to download: if you're on a Mac, use the "Universal2" installer; if you're on a Windows machine, pick the "Windows installer (64 bit)" version. Once it downloads, you'll need to launch the file you downloaded.

> ### Important Note for Windows Users
> Make sure that the checkbox at the very bottom that says Add Python 3.x (the screenshots show Python 3.7 but this applies to all Python installations) to PATH is checked: <img class="large frame" src="/assets/images/lectures/01-command-prompt-windows-installer.png" />

After going through the installation process, navigate to the folder on your machine where Python was installed. For me, on a Mac, my IDLE was saved to Applications > Python 3.10 (or you can also search for it). For Windows users, it will likely be in a folder inside of Program Files (which you can also search for). It should also create a shortcut on your Desktop.

Inside, the Python 3.10 folder, you'll find a program called **IDLE** - this is the IDLE executable. Double click on that file to run it. You should then see something like this:

<img style="width: 100%;" class="screenshot" src="/assets/images/hw01/idle1.png" />

I recommend keeping IDLE in your dock (on a Mac) or making a Desktop Shortcut to IDLE (on Windows).

At the **&gt;&gt;&gt;** prompt, you can type any valid python command. For example, type `print("hello world!")` and hit enter (Note: those quotation marks are important!). You should see something like this:

<img style="width: 100%;" class="screenshot" src="/assets/images/hw01/idle2.png" />

This is called the *Interpreter Window.* It allows you to run lines of Python code one at a time. The above example asks Python to run the `print` function with an input of `"hello world!"` (which is a type of data we call a `string`). Go ahead and Quit IDLE for now.

## Part 2: Get Your Files Organized
Create the folder organizational structure recommended in class during Friday's Lecture.

```
cs110
    |-- homework
    │   |-- hw01
    │   |-- hw02
    |   ...
    |-- lectures
    │   -- lecture01
    │   -- lecture02
    │   ...
    |-- tutorials
        ...
```

## Part 3: Create two Python files and Write Some Programs
When you're done, open IDLE and create a new python file (go to File menu > "New File"). This should open a blank document. Then save this blank document as **`grade_calculator.py`** (File menu > "Save as..."), and put it inside of your `cs110 > tutorials > tutorial01` folder (You'll need to make that `tutorial01` folder just like you did with the three top-level folders).

In this newly created `grade_calculator.py` file, you're going to write a program to calculate your grade in our class (see the [syllabus](../syllabus) for how your grade is calculated):

* First ask the user to input four values (hint: use the `input` function):
  * Prompt: `"Please input the number of total points you received on quizzes "`
    * store this in a variable called `quizzes`
    * This will look like this: `quizzes = input("Please input the number of total points you received on quizzes ")`
  * Prompt: `"Please input the number of total points you received on tutorials "`
    * store this in a variable called `tutorials`
  * Prompt: `"Please input the number of total points you received on homeworks "`
    * store this in a variable called `homeworks`
  * Prompt: `"Please input the number of total points you received on projects "`
    * store this in a variable called `projects`
* Next, convert each variable to an integer (e.g. `quizzes = int(quizzes)`)
* Use the variables to calculate user's final grade in the class (either out of 100) and store it in a variable called `total` (Hint: it'll look something like this `total = (quizzes + ...) / 200`)
* Make sure to print the final score!

Now create another new file (put it in that same folder) but call this one **`turtorial.py`** (it's a pun). In that new file:

* Copy and paste the below code into your new file:

```
from turtle import *
my_turtle = Turtle()

### Your code goes below here

my_turtle.forward(100)
my_turtle.left(90)
```
* Modify the program so that your turtle draws a square of any color

> ### Some Pro Tips
> * Always save your python file before running it so that the interpreter "sees" your changes.
> * In order for your interpreter to recognize your file as a Python file, you must give it the **`.py`** file extension (e.g. **`my_program.py`**).
> * Don't forget to name all of your programs "snake case" (all lower case, underscores to separate words).
> * If your code doesn't run, practice reading and trying to understand (often by Googling) what the interpreter is telling you. If you see red error text, the computer is trying to tell you where the problem is.

## Part 4: Submit your work as a ZIP file
Rather than having you upload each file individually to Canvas, we're going to use bundle together all of your files as a single ZIP file before uploading. The instructions to create a ZIP file are a little different for Mac users vs Windows users.

For Mac users, you're going to right-click (or Control-Click - that is, hold down the Control button and then click on the folder) on your tutorial01 folder and select `Compress "tutorial01"`. This will create a ZIP file in that same folder that you can then upload to Canvas. [Click here for a video walkthrough](https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=d73afe11-97ca-4bea-aebb-ae6901617294).

For Windows users, you're going to right-click (or Control-Click - that is, hold down the Control button and then click on the folder) on your tutorial01 folder, select the `Send to` option in that menu, and then click on `Compressed (zipped) folder`. This will create a ZIP file in that same folder that you can then upload to Canvas. [Click here for a video walkthrough](https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=57c749ea-3207-4f67-ba79-ae69016172d9).

Once you've created the ZIP file, upload that to the Canvas assignment for Tutorial 1. MAKE SURE YOU DON'T SUBMIT THE ONE NAMED `_template` as that doesn't contain any of your work! Congrats; you've finished Tutorial 1.
