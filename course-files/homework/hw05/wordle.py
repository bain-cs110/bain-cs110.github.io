#!/usr/bin/env python3

from tkinter import Canvas, Tk, messagebox

########################## CANVAS SETUP CODE ##############################

import helpers
import random
# initialize window
gui = Tk()
gui.title('W0rdle')

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 600

canvas = Canvas(gui, width=CANVAS_WIDTH,
                height=CANVAS_HEIGHT, background='white')
canvas.pack()
canvas.focus_set()

########################## FUNCTIONS ##############################

CORRECT_COLOR = "#6BA965"
PARTIAL_COLOR = "#C8B458"
WRONG_COLOR = "#787C7E"
DEFAULT_COLOR = "white"

game_data = {
  "solution": "",
  "current_guess": "",
  "previous_guesses": [],
  "word_list": []}


def read_in_words(file_path: str):
    '''
    Function that reads in a list of words and adds them to the game_data. Then,
    picks a random word to set as the 'solution' key in the game_data dictionary.

    Parameters:
        file_path (str): The file to be read in

    Returns:
        None
    '''

    # TODO: Loop through in the `wordlist.txt` file and append all of the 5 letter
    # words (converted to UPPER CASE) to the 'word_list' key of the game_data dictionary.
    my_file = open(file_path, 'r')
    for line in my_file:
        word = line.strip('\n')
        if len(word) == 5:
            game_data['word_list'].append(word.upper())

    # TODO: Pick a random word as a solution
    game_data['solution'] = random.choice(game_data['word_list'])


def finalize_guess(canvas: Canvas, guess: str, hint: str):
    '''
    Finalizes a valid user guess.

    This function does a few things:
        1. It saves the current guess as a previous guess
        2. It clears out the current guess
        3. It checks to see if the guess matches the solution
        4. It checks to see if the user has reached the max number of guesses

    Parameters:
        canvas (Canvas): The canvas being used for the game.
        guess (str): The guess to be rendered on the screen.
        hint (str): The evaluated hint so that we can color the blocks correctly.

    Returns:
        None
    '''

    # Append the inputted guess to the previous_guesses list in game_data
    game_data['previous_guesses'].append(guess)

    # Set the current_guess key in game_data to the empty string ("")
    if hint == "$$$$$":
        helpers.game_over(canvas, happy=True)
    elif len(game_data['previous_guesses']) == 6:
        helpers.game_over(canvas)


def render_previous_guess(canvas: Canvas, previous_guess: str, guess_number: int, hint: str):
    '''
    Renders a previous guess on the canvas.

    Parameters:
        canvas (Canvas): The canvas to play the game on.
        previous_guess (str): The previous guess to be rendered
        guess_number (int): The number of the guess to be drawn (y-coordinate)
        hint (str): The hint string that was generated from that guess

    Outputs:
        None. (Draws to the canvas)
    '''
    for i in range(0, 5):
        if hint[i] == "$":
            helpers.color_a_grid_square(
                canvas, CORRECT_COLOR, (i, guess_number))

        elif hint[i] == "-":
            helpers.color_a_grid_square(
                canvas, PARTIAL_COLOR, (i, guess_number))
        else:
            helpers.color_a_grid_square(canvas, WRONG_COLOR, (i, guess_number))

        helpers.draw_letter_in_grid(canvas, previous_guess[i],
                                    (i, guess_number), finalized=True)


def render_game_board(canvas):
    canvas.delete("all")

    helpers.make_grid(canvas, CANVAS_WIDTH, CANVAS_HEIGHT)

    current_guess = game_data['current_guess']
    previous_guesses = game_data['previous_guesses']
    guess_count = len(game_data['previous_guesses'])

    # TODO: using a loop, render all of the previous guesses using the function
    #       called render_previous_guess
    for i in range(0, guess_count):
        render_previous_guess(
            canvas, previous_guesses[i], i, game_data['solution'])

    # TODO: using a loop, render the current guess
    for i in range(0, 5):
        if i >= len(current_guess):
            break
        helpers.color_a_grid_square(canvas,
                                    DEFAULT_COLOR,    (i, guess_count))
        helpers.draw_letter_in_grid(canvas,
                                    current_guess[i], (i, guess_count))


def generate_hint(guess: str, solution: str):
    '''
    Generates a hint from a guess and a solution.

    This should be the same as the one from the Tutorial. A hint string will
    be 5 letters long, where each letter represents

    Parameters:
        guess (str): The guess to be evaluated
        solution (str): The solution to be compared to

    Returns:
        hint (str): The hint for the user
    '''

    # Loop through each letter of the entry and build a hint for each
    # letter in our guess by comparing it to our solutions
    hint = ""
    for i in range(0, 5):
        if guess[i] == solution[i]:
            hint += "$"
        elif guess[i] in solution:
            hint += "-"
        else:
            hint += "*"

    return hint


########################## EVENT LISTENERS ##############################
def handle_typing(event):

    # TODO: If the player hits BackSpace, delete the last character from the
    # 'current_guess' key in the game_data dictionary
    if event.keysym == "BackSpace":
        game_data['current_guess'] = game_data['current_guess'][:-1]

    # TODO: If the player hits Return...
    elif event.keysym == "Return":
        # First check that 5 letters have been entered
        if len(game_data['current_guess']) == 5:
            pass
        # Next check if it's a valid word in our word list
        elif game_data['current_guess'] not in game_data['word_list']:
            pass
        # If we make it past those two checks, it's a valid guess
        else:
            # First generate a hint, then finalize the guess
            hint = generate_hint(
                game_data['current_guess'], game_data['solution'])
            finalize_guess(canvas, game_data['current_guess'], hint)

    # If the player hits any other letter/number/symbol on the keyboard
    elif len(event.keysym) == 1:
        # TODO: If the user hasn't entered 5 letters, add the entered symbol
        # to the current guess (make sure to convert it to upper case!)
        if len(game_data['current_guess']) < 5:
            game_data['current_guess'] += event.keysym.upper()

    render_game_board(canvas)


# Ask the computer to listen for key presses
KEY_PRESS = '<Key>'
canvas.bind(KEY_PRESS, handle_typing)

########################## GAME SETUP ##############################
# Read in the wordlist and set the secret word
read_in_words('wordlist.txt')
# Print the solution for debugging
print(game_data['solution'])
# Render the game board!
render_game_board(canvas)
canvas.mainloop()
