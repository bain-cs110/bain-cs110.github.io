---
layout: assignment-two-column
title: Building Wordle
abbreviation: HW5
type: homework
files: course-files/assignments/hw05.zip
due_date: 2022-03-04
points: 8
draft: 1
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

In this assignment, you will be making a the full version of Wordle, complete with its interface!

## Your Tasks
Please write a program that accomplishes the following tasks:

{:.bash-small}
1. Ask the user whether they want to be x or o (and ensure your program honors their choice).
1. Ask the user if they want to go first (and ensure your program honors their choice)
Prompt the user for their move (they’ll enter a number from 1-9), which corresponds to where they want to go (as displayed below):
   * If the user does not enter a number from 1-9, tell them their entry was invalid and that they should try again (use try/except as well as if/else).
   * If the user enters a valid number that is not empty, tell them that slot is already taken.
1. If it’s the computer’s turn, have the computer randomly select a square, given the available choices (using the random module).
1. After each move, be sure to redraw the game board
1. If there is a win / loss / tie, print an appropriate message and terminate the game


## Checklist Before You Submit
Before you submit, make sure you’ve tested that your program does the following:

{:.checkbox-list}
* Reads in a list of 5-letter words from the `word_list.txt` file
* Only allows the user to enter 5 letter words (otherwise resets when they hit ENTER)
* If a user hits ENTER and hasn't entered 5 words don't accept it as a guess
* If a user hits ENTER and has entered an INVALID word don't accept it as a guess
* After each guess, W0RDLE responds with the correct hint and moves to the next line
* Guesses that are currently be entered are black text on a white (`DEFAULT_COLOR`) background
* Previous guesses are rendered in black text
* The squares for letters in a previous guess are colored thusly:
    * Completely correct letters will have a green (`CORRECT_COLOR`) background
    * Partially correct letters will have a yellow (`PARTIAL_COLOR`) background
    * Letters that don't appear will have a grey (`WRONG_COLOR`) background
* The user can only make 6 valid guesses
* If the user guesses correctly, they should see a popup message
