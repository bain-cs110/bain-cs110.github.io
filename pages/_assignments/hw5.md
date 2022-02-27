---
layout: assignment-two-column
title: Building W0rdle
abbreviation: HW5
type: homework
files: course-files/assignments/hw05.zip
due_date: 2022-03-04
points: 8
draft: 0
---
<style>
    .bash-small .highlighter-rouge {
        width: 300px;
        margin: auto;
        margin-top: 10px;
    }
</style>

<a class="nu-button" href="/course-files/homework/hw05.zip" target="_blank">
    Homework Starter Files <i class="fas fa-download"></i>
</a>


> **LEARNING OBJECTIVES:**
> 1. Practice working with loops
> 1. Practice working with sequences
> 1. Practice with logic
> 1. Practice writing more complex programs

In this assignment, you will be making the full version of Wordle (we'll be calling it W0rdle), complete with its interface! While much of the program is already complete, your job will be to understand the existing program and functions, and use those to complete the full version of W0rdle. Make sure to review [Tutorial 08](./tutorial08).

Here's a video demo of what the finished version should look like:
<iframe src="https://northwestern.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=1083e1e7-9bda-4ca9-a30d-ae4901295b1c&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=true&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

> **PLEASE NOTE:**
> While you only have to write new code in the parts that are marked `TODO` in `wordle.py`, you'll
> likely need to understand the other functions in `wordle.py` and `helpers.py` in order
> to know how to use them to complete the assignment. You can search for the `TODO` tags using the File menu then "Search" in IDLE.

## Your Tasks
Please write a program that accomplishes the following tasks:

{:.bash-small}
1. Adapt your code from Tutorial 08 to finish the implementation of the `read_in_words` function. Make sure that your function matches the documentation for the function!

    * First it will read in all of the 5 letter words and add them to `game_data['word_list']`
    * Make sure to convert the words to UPPER CASE before adding them to the list
    * Secondly, it'll pick a random 5 letter word and save it into `game_data['solution']`

1. Adapt your code from Tutorial 08 to finish the implementation of the `generate_hint` function. Make sure that you function matches the documentation at the top of the function!
1. Finish the `render_previous_guess` function. It needs to go through each letter of the inputted `previous_guess`, and
    * draw the correct colored square (using `helpers.color_a_grid_square`)
    * draw the letter corresponding to that square
    * make sure to review the documentation for `helpers.color_a_grid_square` in `helpers.py`.
    * note: the coordinate it asks for is not the Canvas coordinate, but instead the coordinate on the W0rdle grid which looks like the grid below.
    * make sure to use the right colors which are defined as variables near the top of the file: `CORRECT_COLOR`, `PARTIAL_COLOR`, and `WRONG_COLOR`
1. Finish the `render_game_board` function by looping through the list of previous_guesses and calling the `render_previous_guess` function for each one.

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
> 1. Make sure that you carefully read what error pops up. It will tell you where and what to look for.
> 2. Use print statements to diagnose the state of the game. For instance, to check whether your generated hint is correct, before you `return hint`, add a new line that says `print(hint)` which will allow you to see the hint generated in the Interpreter window.
> 3. Make sure to read the documentation for each function!

## Checklist Before You Submit
Before you submit, make sure you’ve tested that your program does the following:

{:.checkbox-list}
* Reads in a list of 5-letter words from the `word_list.txt` file
* Only allows the user to enter 5 letter words
* If a user hits ENTER and hasn't entered 5 letters don't accept it as a guess
* If a user hits ENTER and has entered an INVALID word don't accept it as a guess
* You do not need to worry about the case where the user enters the same word multiple times
* After each guess, W0RDLE responds with the correct hint and moves to the next line
* Guesses currently being entered are black text on a white (`DEFAULT_COLOR`) background
* Previous guesses are rendered in black text
* The squares for letters in a previous guess are colored thusly:
    * Completely correct letters will have a green (`CORRECT_COLOR`) background
    * Partially correct letters will have a yellow (`PARTIAL_COLOR`) background
    * Letters that don't appear will have a grey (`WRONG_COLOR`) background
* The user can only make 6 valid guesses
* If the user guesses correctly, they should see a popup message
