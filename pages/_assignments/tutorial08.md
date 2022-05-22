---
layout: assignment-two-column
title: Get Started with HW5
description:
    - Validating Data
    - Dealing with Dictionaries
type: tutorial
abbreviation: Tutorial 8
draft: 0
num: 8
points: 3
due_date: 2022-05-25
---

<style>
    .bash-small .highlighter-rouge {
        width: 520px;
        margin: auto;
        margin-top: 10px;
    }
</style>

<a class="nu-button" href="/course-files/tutorials/tutorial08_template.zip" target="_blank">
    Tutorial Starter Files <i class="fas fa-download"></i>
</a>


## Background
Today, we'll be combining a number of the concepts we've been practicing the last few week in order to create a version of the game known as <a href="https://www.nytimes.com/games/wordle/index.html">Wordle</a>: 1. loops; 2. reading from files; 3. validating inputs; 4. working with dictionaries.

### Input Handling in HW 5
You will be creating a Wordle-style game. If you haven't played Wordle before, your goal is to guess a secret 5-letter word in, at most, 6 guesses. Each time you guess, you're given some "hints" about about how correct your guess was:

<img class="medium frame" src="/assets/images/tutorials/wordle.webp" />

We'll be building a simpler, text-based version for the Tutorial but then using the same techniques in HW 5 to create the full version!

## Your Task
Please make the following enhancements to the `wordle_starter.py` file (each marked `TODO` in the `.py` file).
* First, read through the file called `wordlist.txt` and add all the 5-letter words to the `world_list` key of the `game_data` dictionary.
* Next, you'll have to take care of validating each user guess by:
    * Converting their guess to lower case
    * Seeing if their guess is exactly 5 characters long
    * Checking to see if the guess is in the word list you loaded in
* If any of these tests fails, you need to ask the user to guess again (hint: use `continue` to go to the next iteration of the loop)
* Once you've validated the guess, next up is to generate the `hint` for the user. You'll loop through each letter of the solution and...
    * If the letter perfectly matches the solution, you'll add a `$` to the hint
    * If the letter is in the solution, but isn't in the right location, you'll add a `-` to the hint
    * Otherwise the letter isn't in the solution at all, so you'll add a `*` to the hint

Once you've completed all of your to-dos, make sure to run your program and see if it works like it should!

## What to turn in (same deal as always)
Please turn in your completed tutorial exercise(s) ON CANVAS by Wednesday night at midnight. To do this, first zip your entire `tutorial08` folder (with your edited files inside), and then upload your zip file to Canvas. Please ensure that your zip file includes **YOUR CODE**. 
