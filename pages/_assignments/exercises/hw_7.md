---
layout: assignment-two-column
title: Building a Game
abbreviation: HW7
type: homework
due_date: 2024-03-01
draft: 0
canvas_id: 1371703
canvas_title: "Homework 7"
canvas_assignment_group: "Homework"
canvas_points_possible: 100
canvas_submission_types: "online_upload"
canvas_allowed_extensions: "py"
---
<style>
    .bash-small .highlighter-rouge {
        width: 300px;
        margin: auto;
        margin-top: 10px;
    }
</style>

> **LEARNING OBJECTIVES:**
>
> 1. Practice working with loops
> 1. Practice working with sequences
> 1. Practice with logic
> 1. Practice writing more complex programs
> 1. Practice working with and completing existing programs

In this assignment, you will be making the full version of Wordle, complete with its interface! While much of the program is already complete, your job will be to understand the existing program and functions, and use those to complete the full version of Wordle. If you haven't completed the tutorial for this week, now would be a good time to do so.

Here's a video demo of what the finished version should look like:

<iframe src="https://northwestern.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=546a2138-7d8e-4d03-afa2-b00a00348c36&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=true&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

> **PLEASE NOTE:**
> While you only have to write new code in the parts that are marked `TODO` in `wordle.py`, you'll
> need to understand the other functions in `wordle.py` and `hw7_utilities.py` in order
> to know how to use them to complete the assignment. You can search for the `TODO` tags using the File menu then "Search" in IDLE.

## Your Tasks

Please write a program that accomplishes the following tasks. **DO NOT TRY TO DO ALL OF THE TASKS AT ONCE.** Try to complete a task, test your work, fix any issues that come-up, and _THEN_ move on to the next task.

> **Note**: To run the game, make sure to uncomment out the lines of the program at the very bottom of the template under the section that is labeled `GAME SETUP AND PLAY`

{:.bash-small}

1. Adapt your code from the tutorial to finish the implementation of the `read_in_words` function. Make sure that your function matches the documentation for the function!

    * First it will read in all of the 5 letter words and add them to `game_data['word_list']`
    * Make sure to convert the words to **UPPER CASE** before adding them to the list
    * Secondly, it'll pick a random 5 letter word and save it into `game_data['solution']`

1. Adapt your code from the tutorial to finish the implementation of the `generate_hint` function. Make sure that your function matches the documentation at the top of the function!
1. Finish the `show_past_guess` function. It needs to go through each letter of the inputted `past_guess`, and
    * draw the correct colored square (using `hw7_utilities.color_a_grid_square`)
    * draw the letter corresponding to that square (using `hw7_utilities.draw_letter_in_grid`)
    * make sure to review the documentation for `hw7_utilities.color_a_grid_square` in `hw7_utilities.py`.
    * note: the coordinate it asks for is not the screen coordinates, but instead the coordinate on the Wordle grid which looks like the grid below.
    * make sure to use the right colors which are defined as variables near the top of the file: `CORRECT_COLOR`, `PARTIAL_COLOR`, and `WRONG_COLOR`
1. Finish the `show_game_board` function by looping through the list of previous_guesses and calling the `show_previous_guess` function for each one.

```bash
            ———————————––––––––––––––––––––––––––––
             (0,0) | (1,0) | (2,0) | (3,0) | (4,0)
            ———————————––––––––––––––––––––––––––––
             (0,1) | (1,1) | (2,1) | (3,1) | (4,1)
            ———————————––––––––––––––––––––––––––––
             (0,2) | (1,2) | (2,2) | (3,2) | (4,2)
            ———————————––––––––––––––––––––––––––––
             (0,3) | (1,3) | (2,3) | (3,3) | (4,3)
            ———————————––––––––––––––––––––––––––––
             (0,4) | (1,4) | (2,4) | (3,4) | (4,4)
            ———————————––––––––––––––––––––––––––––
             (0,5) | (1,5) | (2,5) | (3,5) | (4,5)
            ———————————––––––––––––––––––––––––––––
```

> **IF YOU GET STUCK:**
>
> 1. Make sure that you carefully read what error pops up. It will tell you where and what to look for.
> 2. Use print statements to diagnose the state of the game. For instance, to check whether your generated hint is correct, before you `return hint`, add a new line that says `print(hint)` which will allow you to see the hint generated in the Interpreter window.
> 3. Make sure to read the documentation for each function!

## Checklist Before You Submit

Before you submit, make sure you’ve tested that your program does the following:

{:.checkbox-list}

* Reads in a list of 5-letter words from the `wordlist.txt` file
* Does **not** print out anything to the Interpreter window except: 
  * (Optional) print out the solution to the puzzle in the interpreter window
  * Only allows the user to enter 5 letter words
  * If a user hits ENTER and hasn't entered 5 letters don't accept it as a guess (you'll see a message printed to the interpreter)
  * If a user hits ENTER and has entered an INVALID word don't accept it as a guess (you'll see a message printed to the interpreter)
* You do not need to worry about the case where the user enters the same word multiple times
* After each guess, Wordle responds with the correct hint and moves to the next line
* Guesses currently being entered are **black text** on a white (`DEFAULT_COLOR`) background
* Previous guesses are rendered in **white text**
* The squares for letters in a previous guess are colored thusly:
  * Completely correct letters will have a green (`CORRECT_COLOR`) background
  * Partially correct letters will have a yellow (`PARTIAL_COLOR`) background
  * Letters that don't appear will have a grey (`WRONG_COLOR`) background
* The user can only make 6 valid guesses (the game will be unplayable after that)
* If the user guesses correctly, they should see a popup message

## Starter Code

You'll need all of these downloaded but **you will only work in the `wordle.py` file**.

<a class="nu-button" href="{{site.url}}/course-files/homeworks/hw7/wordle.py" target="_blank" download>
    Homework Starter File <i class="fas fa-download"></i>
</a>
<br>
<br>

<a class="nu-button" href="{{site.url}}/course-files/homeworks/hw7/docs/wordle.html" target="_blank">
    Pretty Documentation for Starter File Functions<i class="fas fa-download"></i>
</a>
<br>
<br>

<a class="nu-button" href="{{site.url}}/course-files/homeworks/hw7/hw7_utilities.py" download>
    HW7 Utilities File<i class="fas fa-download"></i>
</a>
<br>
<br>

<a class="nu-button" href="{{site.url}}/course-files/homeworks/hw7/docs/hw7_utilities.html" target="_blank">
    Pretty Documentation for HW7 Library<i class="fas fa-download"></i>
</a>
<br>
<br>

<a class="nu-button" href="{{site.url}}/course-files/homeworks/hw7/wordlist.txt" download="wordlist.txt">
    Wordle Word List File<i class="fas fa-download"></i>
</a>
<br>

> **Note**: Depending on your browser, you may need to right click on the wordlist button and select "Download linked file..." or "Save linked file as...". Make sure to save it as `wordlist.txt`.


* * *

## What to Submit

Before you submit, make sure to go through the checklist to make sure everything is good-to-go. Once it is, submit **only** your `wordle.py` file to Canvas by the deadline.

{% include submission_details.md %}