---
layout: assignment-two-column
title: Reading from a File
type: tutorial
abbreviation: Tutorial 6
draft: 0
num: 6
points: 100
due_date: 2024-02-28
canvas_title: Tutorial 6
canvas_id: 1371704
canvas_assignment_group: "Tutorial"
canvas_points_possible: 100
canvas_submission_types: "online_upload"
canvas_allowed_extensions: "py"
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

* * *

## Input Handling in HW 7

You will be creating a Wordle-style game but in text rather than in graphics (spoiler alert: you'll do the graphics for the HW). If you haven't played Wordle before, your goal is to guess a secret 5-letter word in, at most, 6 guesses. Each time you guess, you're given some "hints" about about how correct your guess was:

<img class="medium frame" src="{{site.url}}/assets/images/tutorials/wordle.webp" />

We'll be building a simpler, text-based version for the Tutorial but then using the same techniques in HW 7 to create the full version!

* * *

### Note on using the `range` Function

While working on the two Wordle assignments, there will often be a time where it might be convenient to use a list of numbers to iterate through each letter of a guess (you can use our square bracket index notations to get specific letters of a string) and compare it to the secret word. Like anything in programming, there are lots of ways to do this. You could for instance, do:

```python
i = 0
while i < 6:
  print(secret_word[i], guess[i])
  i += 1 # short hand for i = i + 1
```

Alternatively, you can use the `range` function to emulate the same thing with a `for` loop:

```python
for i in range(0, 6):
  print(secret_word[i], guess[i])

# which is equivalent to
for i in [0, 1, 2, 3, 4, 5]:
  print(secret_word[i], guess[i])
```

When only given two inputs, `range` interprets them as a "from" and a "up to" constraint and assumes you want to count "by" one. That is, `range(0, 6)` gives us back the list `[0, 1, 2, 3, 4, 5]`.

Both ways are totally fine, so use whatever way is most convenient for you.

* * *

## Your Task

Please make the following enhancements to the `tutorial06.py` file (each marked `TODO` in the `.py` file).

* First, read through the file called `wordlist.txt` and add all the 5-letter words *converted to UPPER CASE* to the `word_list` key of the `game_data` dictionary. You'll complete all this work in the <code>read_in_words</code> function.
* Next, you'll have to take care of validating each user guess by:
  * Converting their guess to *UPPER CASE*
  * Seeing if their guess is exactly 5 characters long
  * Checking to see if the guess is in the word list you loaded in
* If any of these tests fails, you need to ask the user to guess again (hint: use `continue` to go to the next iteration of the loop)
* Once you've validated the guess, next up is to generate the `hint` for the user inside the <code>generate_hint</code> function. You'll loop through *each* letter of the solution and...
  * If the letter perfectly matches the solution, you'll add a `"🟩"` to the hint
  * If the letter is in the solution, but isn't in the right location, you'll add a `"🟨"` to the hint
  * Otherwise the letter isn't in the solution at all, so you'll add a `"⬜"` to the hint

Once you've completed all of your to-dos, make sure to run your program and see if it works like it should!

> Note: If you follow these steps you'll create a Wordle with a small "double-letter bug" in that the real Wordle gives you information about <a href="https://www.wordnerdle.com/wordle-double-letter/" target="_blank">how many times a letter appears in the solution</a>. You do NOT need to worry about this in either the tutorial or homework this week. If you <em>want</em> to solve it you may–it just involves counting how many times a letter occurs and basing the "hint" off of that information.

* * *

## Starter Files

<a class="nu-button" href="{{site.url}}/course-files/tutorials/tutorial6/tutorial6.py" target="_blank" download>
    Tutorial Starter File <i class="fas fa-download"></i>
</a>
<br>
<br>

<a class="nu-button" href="{{site.url}}/course-files/tutorials/tutorial6/wordlist.txt" target="_blank" download>
    Word List File<i class="fas fa-download"></i>
</a>

> **Note**: Depending on your browser, you may need to right click on the wordlist button and select "Download linked file..." or "Save linked file as...". Make sure to save it as `wordlist.txt`.

* * *
 
## Getting Credit for Your Work

### If you're in class

If you're in class you don't need to submit a `.py` file on Canvas. Instead, find one other person in your group that is finished and peer review each other's work. Here are the things to check:

1. Does their code look readable and neat?
1. Can you understand what their code does by reading it?
1. How was their solution different from yours (if at all)?
1. Does their program run and generate the correct test images?

Once you've each taken a look, take a second to debrief. Anything either of you found difficult? Easy? Fun? Mind-blowing? Once you've debriefed, **both of you should fill out this** <a href="https://docs.google.com/forms/d/e/1FAIpQLSctX_8gvtFFdvg_8q7lbzccSgpXFZ2AJiZaI7GbkekM8F8pbQ/viewform?usp=sf_link" target="_blank">attendance Google Form</a>. **NOTE: You will need the NetID of the person's whose code you reviewed.** You're free to go after you're finished once we open the attendance form, though we hope that you might consider sticking around and helping others in your group.

### If you're not in attendance

You can just submit your `.py` file to the Canvas assignment and they will be graded.
