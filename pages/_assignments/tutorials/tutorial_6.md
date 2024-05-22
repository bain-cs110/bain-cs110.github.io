---
layout: assignment-two-column
title: Reading from a File
type: tutorial
abbreviation: Tutorial 6
draft: 0
num: 6
points: 100
due_date: 2024-05-22
canvas_title: Tutorial 6
canvas_id: 1418267
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

### Note on importing

In both of these assignments, we're going to practice the other way to <code>import</code> libraries (modules) in Python. For the past few weeks, if we wanted to use say the <code>randint</code> function we did...

```python
from random import randint
print(randint(0, 100)) # prints a random number between 0 and 100
```

Alternatively, we can import the **entire** library and then specify which function we want to use more specifically:

```python
import random
print(random.randint(0, 100))
```

These two programs are equivalent in terms of their functionality, though if you continue in CS courses, you'll learn how the former method is actually a more sustainable software engineering technique than the latter.


In the Tutorial, you'll only need to worry about using the `random` library, but in the homework you'll also need to take advantage of some functions defined in the `cs110_hw7` library you'll download.

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

## Note on reading Files

When we read files line by line, the very END of each line contains what we call in CS a "carriage return." That's literally just a fancy name for a "new line", something we tell Python about by using the special character combo: <code>\n</code>. Each line of a file when we read it is just a string, so we can ask for its length using the <code>len</code> function. However, try running this in the IDLE interpreter window:

```python
print(len("\n"))
```

You might expect it to show 0, there are no "letters" in this string, just a "new line," so it should have a length of 0. **Nope.** Instead, Python considers this to be a string of length 1 – there's exactly one character here, the "new line character." So just like a space (`" "`), Python treats `"\n"` as if it's a unique letter. This will matter in our Wordle program since, if we read in a line with a 5 letter word...well technically that line is 6 characters long – 5 letters + 1 new line character.

To fix this, we've added to the template file you'll download a call to the `strip` method of a string which takes in one input, a string, and _removes_ that string from the string it's called upon. So in essence, we'll turn something like <code>"dillo\n"</code> (which is a string of length 6) to <code>"dillo"</code> (a string of length 5).

* * *

## Your Task

Please make the following enhancements to the `tutorial6.py` file (each marked `TODO` in the `.py` file). In addition to the `TODO`s you'll find a number of commented out `print` statements that might help you figure out how to perform each task.

> **PLEASE NOTE:**
> While you only have to write new code in the parts that are marked `TODO` in `wordle.py`, you'll
> need to understand the other code in `tutorial6.py` in order
> to know how to edit it to complete the assignment. You can search for the `TODO` tags using the File menu then "Search" in IDLE. <mark>THIS MEANS YOU WILL NEED TO LOOK AT THE EXISTING CODE AROUND THE TODOs to see what is done already and what you'll need to fill-in. DON'T JUST START WRITING CODE. First, understand <a href="https://edstem.org/us/courses/57557/">what's there</a> THEN start editing.

* First, read through the file called `eng_wordlist.txt` and add all the 5-letter words *converted to UPPER CASE* to the `word_list` key of the `game_data` dictionary. You'll complete all this work in the <code>read_in_words</code> function.
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

> Note: If you follow these steps you'll create a Wordle with a small "double-letter bug" in that the real Wordle gives you information about <a href="https://nerdschalk.com/wordle-same-letter-twice-rules-explained-how-does-it-work/" target="_blank">how many times a letter appears in the solution</a>. You do NOT need to worry about this in either the tutorial or homework this week. If you <em>want</em> to solve it you may–it just involves counting how many times a letter occurs and basing the "hint" off of that information.

* * *

## Starter Files

<a class="nu-button" href="{{site.url}}/course-files/tutorials/tutorial6/tutorial6.py" target="_blank" download>
    Tutorial Starter File <i class="fas fa-download"></i>
</a>
<br>
<br>

<a class="nu-button" href="{{site.url}}/course-files/tutorials/tutorial6/eng_wordlist.txt" target="_blank" download>
    Word List File<i class="fas fa-download"></i>
</a>

> **Note**: Depending on your browser, you may need to right click on the wordlist button and select "Download linked file..." or "Save linked file as...". Make sure to save it as `eng_wordlist.txt`.

<a class="nu-button" href="{{site.url}}/course-files/homeworks/hw7/common_words.txt" target="_blank" download>
    More Common Words<i class="fas fa-download"></i>
</a>

> **Note**: The previous file contains ALL "words" (a lot). This one only contains COMMON words and can give you more "reasonable" Wordle puzzles. To use this one, change the call to the <code>read_in_words</code> function to point towards the new file name (I recommend <code>common_words.txt</code>).

* * *

## Getting Credit for Your Work

### If you're in class

If you're in class you don't need to submit a `.py` file on Canvas. Instead, find one other person in your group that is finished and peer review each other's work. Here are the things to check:

1. Does their code look readable and neat?
1. Can you understand what their code does by reading it?
1. How was their solution different from yours (if at all)?
1. Does their program run and generate the correct images?

Once you've each taken a look, take a second to debrief. Anything either of you found difficult? Easy? Fun? Mind-blowing? Once you've debriefed, **both of you should fill out this** <a href="https://docs.google.com/forms/d/e/1FAIpQLSfz1vAwwGuF1GZyhhdWylMMczF26e7xWBBx3kg3MxT-PTFC_A/viewform?usp=sf_link" target="_blank">attendance Google Form</a>. **NOTE: You will need the NetID of the person's whose code you reviewed.** You're free to go after you're finished once we open the attendance form, though we hope that you might consider sticking around and helping others in your group.

### If you're not in attendance

You can just submit your `.py` file to the Canvas assignment and they will be graded. <mark>Make sure you have exactly followed the instructions.</mark>
