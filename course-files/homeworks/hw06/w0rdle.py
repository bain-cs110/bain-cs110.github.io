from tkinter import Canvas, Tk
import hw6_utilities
########################## CANVAS SETUP CODE ##############################
# initialize window
gui = Tk()
gui.title('W0rdle')

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 600

the_canvas = Canvas(gui, 
                width=CANVAS_WIDTH,
                height=CANVAS_HEIGHT, 
                background='white')

the_canvas.pack()
the_canvas.focus_set()

# the next thing is a list of all the functions in this file. It's so we can
# generate that cool web version of the documentation. You don't need to
# worry about it.
__all__ = [
    "read_in_words", "generate_hint", "finalize_guess", "show_past_guess",
    "show_game_board", "handle_typing" 
]

########################## GAMEPLAY FUNCTIONS ##############################

CORRECT_COLOR = "#6BA965"
PARTIAL_COLOR = "#C8B458"
WRONG_COLOR = "#787C7E"
DEFAULT_COLOR = "#FFFFFF"

# Dictionary to store all of the game data
game_data = {
  "solution": "",         # a string that is the secret solution
  "current_guess": "",    # a string that contains the current guess
  "past_guesses": [],     # a list that contains all of the past guesses
  "word_list": []         # a list that will contain all the valid 5 letter words
  }

def read_in_words(file_path):
    '''
    Function that reads in a list of words and adds them to the `game_data`. Then,
    picks a random word to set as the 'solution' key in the `game_data` dictionary.
    
    Parameters:
      * `file_path` (`str`): The file to be read in

    Returns:
        `None`(has side effects)
    '''

    # TODO: Loop through in the *INPUTTED* file and append all of the 5 letter
    # words (**converted to UPPER CASE**) to the 'word_list' key of the game_data dictionary.
    my_file = open(file_path, 'r')

    # TODO: Pick a random word as a solution and save it in the game dictionary in the appropriate
    # attribute.
    # print(random.choice(["test", "this", "function"]))


def generate_hint(guess, solution):
    '''
    Generates a hint from a guess and a solution.

    This should be the same as the one from the Tutorial. A hint string will
    be 5 letters long, where each character represents the "correctness" of the
    guess:
      1. `$` for correct letters
      2. `+` for partially correct letters
      3. `*` for incorrect letters

    Parameters:
      * `guess` (`str`): The guess to be evaluated
      * `solution` (`str`): The solution to be compared to

    Returns:
      * `hint` (`str`): The hint for the user
    '''

    # TODO: Loop through each letter of the entry and build a hint for each
    # letter in our guess by comparing it to our solutions. Then return the hint.
    hint = ""

    return hint


def finalize_guess(a_canvas, guess, hint):
    '''
    Finalizes a valid user guess.

    This function does a few things:
      1. It saves the current guess as a past guess
      2. It clears out the current guess
      3. It checks to see if the guess matches the solution
      4. It checks to see if the user has reached the max number of guesses

    Parameters:
      * `a_canvas` (`Canvas`): The canvas being used for the game.
      * `guess` (`str`): The guess to be showed on the screen.
      * `hint` (`str`): The evaluated hint so that we can color the blocks correctly.

    Returns:
      * `None` (Has side effects)
    '''
    # Append the inputted guess to the past_guesses list in game_data
    game_data['past_guesses'].append(guess)

    # Clear out the current guess
    game_data['current_guess'] = ""

    # Set the current_guess key in game_data to the empty string ("")
    if hint == "$$$$$":
        hw6_utilities.game_over(a_canvas, happy=True)
    elif len(game_data['past_guesses']) == 6:
        hw6_utilities.game_over(a_canvas)


def show_past_guess(a_canvas, past_guess, guess_number, hint):
    '''
    shows a past guess on the canvas.

    Parameters:
      * `a_canvas` (`Canvas`): The canvas to play the game on.
      * `past_guess` (`str`): The past guess to be showed
      * `guess_number` (`int`): The number of the guess to be drawn (y-coordinate)
      * `hint` (`str`): The hint string that was generated from that guess

    Returns:
      * `None` (Draws to the canvas)
    '''
    for i in range(0, 5):
        # Print out the current coordinate being processed
        # print("Coordinate:", (i, guess_number))

        if hint[i] == "$":
            # TODO: replace pass with a call to `hw6_utilities.color_a_grid_square` to color the
            # square with the CORRECT_COLOR.
            pass

        elif hint[i] == "+":
            # TODO: replace pass with a call to `hw6_utilities.color_a_grid_square` to color the
            # square with the PARTIAL_COLOR.
            pass
        else:
            # TODO: replace pass with a call to `hw6_utilities.color_a_grid_square` to color the
            # square with the WRONG_COLOR.
            pass

        # TODO: Draw the letter in the right grid (since these are past guesses,
        # they should be marked as finalized) by calling `hw6_utilities.draw_letter_in_grid`.


def show_game_board(a_canvas):
    '''
    shows the game board.

    Parameters:
      * `a_canvas` (`Canvas`): A canvas to play the game on.

    Returns:
      * `None` (Draws to the canvas)
    '''
    # Clear the canvas
    a_canvas.delete("all")

    # Draw the grid
    hw6_utilities.make_grid(a_canvas, CANVAS_WIDTH, CANVAS_HEIGHT)

    # Load in the current guess from our game_data dictionary
    current_guess = game_data['current_guess']

    # Load in the list of past guesses from our game_data dictionary
    past_guesses = game_data['past_guesses']
    # Calculate how many guesses there have been by finding the length of the
    # past_guesses list in our game_data dictionary
    guess_count = len(game_data['past_guesses'])

    # Loop through all of the past guesses
    for i in range(0, guess_count):

        print("Drawing past guess...")
        # print("Guess to draw:", past_guesses[i], i)
        # print("Hint:", generate_hint(past_guesses[i], game_data['solution']))

        # TODO: Use the `show_pass_guess` function to draw each of the
        # past guesses to the canvas.

    # Now loop through each letter of the current guess and draw it to the board
    for i in range(0, 5):
        if i >= len(current_guess):
            break
        hw6_utilities.color_a_grid_square(a_canvas,
                                    DEFAULT_COLOR,    (i, guess_count))
        hw6_utilities.draw_letter_in_grid(a_canvas,
                                    current_guess[i], (i, guess_count))

########################## EVENT LISTENERS ##############################
def handle_typing(event):
    '''
    Event handler for key presses in W0rdle.

    We need to handle 3 specific types of key presses:
      1. `event.keysym == "BackSpace"`
      2. `event.keysym == "Return"`
      3. `len(event.keysym) == 1` (single character keys)

    Parameters:
      * `event`: The canvas event to process.

    Returns:
      * `None` (Draws to the canvas and also has side effects)
    '''
    # print("handle_typing called!")

    # If the player hits BackSpace, delete the last character from the
    # 'current_guess' key in the game_data dictionary
    if event.keysym == "BackSpace":
        game_data['current_guess'] = game_data['current_guess'][:-1]

    # If the player hits Return...
    elif event.keysym == "Return":
        # First check that 5 letters have been entered
        if len(game_data['current_guess']) != 5:
            print("not enough letters")
            # Next check if it's a valid word in our word list
        elif game_data['current_guess'] not in game_data['word_list']:
            print("not a valid word")
        # If we make it past those two checks, it's a valid guess
        else:
            # First generate a hint, then finalize the guess
            hint = generate_hint(game_data['current_guess'], game_data['solution'])
            finalize_guess(the_canvas, game_data['current_guess'], hint)

    # If the player hits any other letter/number/symbol on the keyboard
    elif len(event.keysym) == 1:
        # If the user hasn't entered 5 letters, add the entered symbol
        # to the current guess (make sure to convert it to upper case!)
        if len(game_data['current_guess']) < 5:
            game_data['current_guess'] += event.keysym.upper()

    # As long as the user hasn't made 6 guesses, show the game board
    if len(game_data['past_guesses']) < 7:
        show_game_board(the_canvas)

# Ask the computer to listen for key presses
KEY_PRESS = '<Key>'
the_canvas.bind(KEY_PRESS, handle_typing)

########################## GAME SETUP AND PLAY ##############################
# Step 1. Read in the wordlist and set the secret word
#read_in_words('wordlist.txt')

# Step 1a. Print the solution for debugging
#print(game_data['solution'])

# Step 2. show the game board!
#show_game_board(the_canvas)
#the_canvas.mainloop()
