#!/usr/bin/env python3

from tkinter import Canvas, Tk, messagebox

import helpers

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 600

CORRECT_COLOR = "#6BA965"
PARTIAL_COLOR = "#C8B458"
WRONG_COLOR = "#787C7E"
DEFAULT_COLOR = "white"

game_data = {
  "solution": "HELLO",
  "current_guess": "",
  "previous_guesses": []
}

word_list = None

# initialize window
gui = Tk()
gui.title('W0rdle')
canvas = Canvas(gui, width=CANVAS_WIDTH,
                height=CANVAS_HEIGHT, background='white')
canvas.pack()

KEY_PRESS = '<Key>'


def read_in_dictionary(file_path: str):
    # TODO:
    global word_list
    word_list = None
    pass


def finalize_guess(canvas: Canvas):
    current_guess = game_data['current_guess']

    game_data['current_guess'] = ""

    game_data['previous_guesses'].append(current_guess)

    if current_guess == game_data['solution']:
        helpers.game_over(canvas, happy=True)
    elif len(game_data['previous_guesses']) == 6:
        helpers.game_over(canvas)


def render_previous_guess(canvas: Canvas, previous_guess: str, guess_number: int, solution: str):
    for i in range(0, 5):
        current_letter = previous_guess[i]

        if current_letter == solution[i]:
            helpers.color_a_grid_square(
                canvas, CORRECT_COLOR, (i, guess_number))

        elif current_letter in solution:
            helpers.color_a_grid_square(
                canvas, PARTIAL_COLOR, (i, guess_number))
        else:
            helpers.color_a_grid_square(canvas, WRONG_COLOR, (i, guess_number))

        helpers.draw_letter_in_grid(canvas, current_letter,
                                    (i, guess_number), finalized=True)


def render_game_board(canvas):
    canvas.delete("all")

    helpers.make_grid(canvas, CANVAS_WIDTH, CANVAS_HEIGHT)

    # TODO: load in the current guess and previous guesses from the game_data
    #       dictionary. Then calculate the current guess count (how many words
    #       has the user tried).

    current_guess = game_data['current_guess']
    previous_guesses = game_data['previous_guesses']
    guess_count = len(game_data['previous_guesses'])

    # TODO: using a loop, render all of the previous guesses using the function
    #       called render_previous_guess
    for i in range(0, guess_count):
        helpers.render_previous_guess(
            canvas, previous_guesses[i], i, game_data['solution'])

    # TODO: using a loop, render the current guess
    for i in range(0, 5):
        if i >= len(current_guess):
            break
        helpers.color_a_grid_square(canvas,
                                    DEFAULT_COLOR,    (i, guess_count))
        helpers.draw_letter_in_grid(canvas,
                                    current_guess[i], (i, guess_count))


def handle_typing(event):
    if event.keysym == "BackSpace":
        game_data['current_guess'] = game_data['current_guess'][:-1]

    # If the player hits return
    elif event.keysym == "Return" and len(game_data['current_guess']) == 5:
        # First check that 5 letters have been entered
        # Also check to see if the word they entered is a valid word in our
        # word list.
        # If both of these conditions are met, then call finalize_guess()
        finalize_guess(canvas)
    elif len(game_data['current_guess']) < 5 and len(event.keysym) == 1:
        game_data['current_guess'] += event.keysym.upper()

    render_game_board(canvas)


canvas.bind(KEY_PRESS, handle_typing)

render_game_board()

canvas.focus_set()
########################## YOUR CODE ABOVE THIS LINE ##############################
# makes sure the canvas keeps running:
canvas.mainloop()
