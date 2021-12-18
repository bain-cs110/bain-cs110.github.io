---
layout: assignment-two-column
title: Get Started with HW5 (Tic Tac Toe)
description:
    - When do you use if/else versus try/except?
    - What kind of errors do try/except statements usually handle?
type: tutorial
abbreviation: Tutorial 8
draft: 0
num: 8
points: 3
due_date: 2021-11-17
---

<style>
    .bash-small .highlighter-rouge {
        width: 520px;
        margin: auto;
        margin-top: 10px;
    }
</style>

<a class="nu-button" href="/fall2021/course-files/tutorials/tutorial08.zip" target="_blank">
    Tutorial Starter Files <i class="fas fa-download"></i>
</a> 


## Background
In preparation for Tic Tac Toe, we are going to help you get started by helping you to handle runtime errors. As you may recall, runtime errors typically happen when your program encounters data that was not adequately anticipated by the programmer. Examples of runtime errors include encountering (a) data with the wrong data type (e.g. a string instead of an int), or (b) data that doesn't make sense for the given context.

### Error Handling in HW5
In [Homework 5](../assignments/hw5), you will be creating a Tic-Tac-Toe game where a user will play a computer in a game of Tic-Tac-Toe. One critical part of engineering the game is making sure that your user enters the right input. Specifically:

{:.bash-small}
1. The user must enter an integer between 1-9.
2. The user cannot enter a number corresponding to a slot that has already been taken. For instance, in the scenario below, if the user (represented by the symbol `o`) types the number `5`, the program should refuse the request and explain to the user why their move is illegal (because the 5-slot is already take by `x`).
```bash
               |   |                7 | 8 | 9 
            ———————————            ———————————
             x | x |                4 | 5 | 6 
            ———————————            ——————————— 
               | o |                1 | 2 | 3 
```

## Your Task
Please make the following enhancements to the `tictactoe_starter.py` file (which correspond to the ability for the user to play their move):
1. If the user does not enter a number from 1-9, tell them their entry was invalid and that they should try again (use try/except as well as if/else).
2. If the user enters a valid number that is not empty, tell them that slot is already taken.
3. If the user types "Q", terminate the program.
4. Keep re-prompting the user until they enter a valid number (or Q). See sample video:

<iframe src="https://northwestern.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=d10536ec-2b52-4a2e-abb9-add1015550a0&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" width="620" height="405" style="padding: 0px; border: 1px solid #464646;" frameborder="0" allowfullscreen="" allow="autoplay"></iframe>

## What to turn in (same deal as always)
Please turn in your completed tutorial exercise(s) ON CANVAS by Wednesday night at midnight. To do this, first zip your entire `tutorial08` folder (with your edited files inside), and then upload your zip file to Canvas. Please ensure that your zip file includes **YOUR CODE**. 
