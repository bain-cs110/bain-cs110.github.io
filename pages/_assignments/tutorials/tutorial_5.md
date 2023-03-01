---
layout: assignment-two-column
title: Get Started with HW5
description:
    - Validating Data
    - Dealing with Dictionaries
type: tutorial
abbreviation: Tutorial 5
draft: 0
num: 5
points: 100
due_date: 2023-03-01
---

<style>
    .bash-small .highlighter-rouge {
        width: 520px;
        margin: auto;
        margin-top: 10px;
    }
</style>

## Background
Today, we'll be combining a number of the concepts we've been practicing the last few weeks in order to create a version of the game known as <a href="https://www.nytimes.com/games/wordle/index.html">Wordle</a>: 
1. using loops
2. reading from files
3. validating inputs
4. working with dictionaries

> **Note**: Because you will use this work in the HW this week, we won't provide solutions for this Tutorial so it's in your best interest to complete the assignment during the tutorial block.

* * *

## Input Handling in HW 5
You will be creating a Wordle-style game but in text rather than in graphics (spoiler alert: you'll do the graphics for the HW). If you haven't played Wordle before, your goal is to guess a secret 5-letter word in, at most, 6 guesses. Each time you guess, you're given some "hints" about about how correct your guess was:

<img class="medium frame" src="/assets/images/tutorials/wordle.webp" />

We'll be building a simpler, text-based version for the Tutorial but then using the same techniques in HW 5 to create the full version!

* * *

### Note on using the `range` Function
While working on the two W0rdle assignments, there will often be a time where it might be convenient to use a list of numbers to iterate through each letter of a guess and compare it to the secret word. Like anything in programming, there are lots of ways to do this. You could for instance, do:

```python
i = 0
while i < 6:
  print(secret_word[i], guess[i])
  i++
```

Alternatively, you can use the `range` function to emulate the same thing with a for loop:

```python
for i in range(0, 6):
  print(secret_word[i], guess[i])

# which is equivalent to
for i in [0, 1, 2, 3, 4, 5]:
  print(secret_word[i], guess[i])
```

When only given two inputs, `range` interprets them as a "from" and a "up to" constraint and assumes you want to count "by" one. That is, `range(0,6)` gives us back the list `[0, 1, 2, 3, 4, 5]`.

Both ways are totally fine, so use whatever way is most convenient for you.

* * *

## Your Task
Please make the following enhancements to the `tutorial05_template.py` file (each marked `TODO` in the `.py` file).
* First, read through the file called `list_of_words.txt` and add all the 5-letter words to the `word_list` key of the `game_data` dictionary.
* Next, you'll have to take care of validating each user guess by:
    * Converting their guess to lower case
    * Seeing if their guess is exactly 5 characters long
    * Checking to see if the guess is in the word list you loaded in
* If any of these tests fails, you need to ask the user to guess again (hint: use `continue` to go to the next iteration of the loop)
* Once you've validated the guess, next up is to generate the `hint` for the user. You'll loop through _each_ letter of the solution and...
    * If the letter perfectly matches the solution, you'll add a `$` to the hint
    * If the letter is in the solution, but isn't in the right location, you'll add a `+` to the hint
    * Otherwise the letter isn't in the solution at all, so you'll add a `X` to the hint

Once you've completed all of your to-dos, make sure to run your program and see if it works like it should!

> Note: If you follow these steps you'll create a W0rdle with a small "double-letter bug" in that the real Wordle gives you information about <a href="https://www.wordnerdle.com/wordle-double-letter/" target="_blank">how many times a letter appears in the solution</a>. You do NOT need to worry about this in either the tutorial or homework this week. If you _want_ to solve it you may–it just involves counting how many times a letter occurs and basing the "hint" off of that information.

* * *

## Starter Files
<a class="nu-button" href="/course-files/tutorials/tutorial05/tutorial05_template.py" target="_blank">
    Tutorial Starter File <i class="fas fa-download"></i>
</a>
<br>
<br>

<a class="nu-button" href="/course-files/tutorials/tutorial05/list_of_words.txt" target="_blank">
    Word List File<i class="fas fa-download"></i>
</a>

> **Note**: Depending on which browser you use, you may need to Right-Click on the World List button and select `Download Linked File` or `Save link as...` in order for your browser to download the file.

* * *

## Getting Credit for Your Work

If you're in class you don't need to submit a `.py` file on Canvas. Instead, find one other person in your group that is finished and peer review each other's work. Here are the things to check:

1. Does their code look readable and neat?
1. Can you understand what their code does by reading it?
1. How was their solution different from yours (if at all)?
1. Did they do anything cool?

Once you've each taken a look, take a second to debrief. Anything either of you found difficult? Easy? Fun? Mind-blowing? Once you've debriefed, **both of you should fill out this** <a href="https://docs.google.com/forms/d/e/1FAIpQLScFw18yE8C1L2te7MPFCvcbGCFkIdURc0aMonRGQ8-X0FJkwQ/viewform?usp=sf_link" target="_blank">attendance Google Form</a>. **NOTE: You will need the NetID of the person's whose code you reviewed.** You're free to go after you're finished, though we hope that you might consider sticking around and helping others in your group.

If you're submitting remotely, you MUST submit your completed tutorial to Canvas and it will be graded. Make sure that all of your functions are named correctly and that they use the EXACT parameter order, names, and types as specified.

Please turn in your completed `.py` file on Canvas by Wednesday night at midnight. ONLY SUBMIT the file you worked in and no other files.
