from tkinter import Canvas, Tk
import cs110_hw7

########################## CANVAS SETUP CODE ##############################
# initialize window
gui = Tk()
gui.title('Wordle!')

canvas = Canvas(gui,
                background='white')
cs110_hw7.setup_window(canvas)

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

def read_in_words(file_path, num_letters = 5):
    '''
    Function that reads in a list of words and adds them to the `game_data`. Then,
    picks a random word to set as the 'solution' key in the `game_data` dictionary.
    
    Args:
      * file_path (`str`): The file to be read in
      * num_letters (`int`): The number of letters in the target solution.

    Returns:
      * `None`, updates the value of `game_data['word_list']` and `game_data['solution']`
    '''

    # TODO: Loop through in the *INPUTTED* file and append all of the 5 letter
    # words (**converted to __UPPER CASE__**) to the 'word_list' key of the game_data dictionary.
    my_file = open(file_path, 'r')

    # TODO: Pick a random word as a solution and save it in the game dictionary in the appropriate
    # attribute.
    # print(random.choice(["test", "this", "function"]))

    ## Note, you can double check to make sure this function is doing what it
    ##   needs to by printing out the game_data value for the "solution" key
    ##   and by checking the length of the list in the "word_list" key.
    
    
    my_file.close()

def generate_hint(guess, solution):
    '''
    Generates a hint from a guess and a solution.

    This should be the same as the one from the Tutorial. A hint string will
    be however many letters long the guess and solution are, where each
    character represents the "correctness" of the guess:
      1. 🟩 for correct letters
      2. 🟨 for partially correct letters
      3. ⬜ for incorrect letters

    Args:
      * guess (`str`): The guess to be evaluated
      * solution (`str`): The solution to be compared to

    Returns:
      * `hint` (`str`): The hint for the user
    '''

    # TODO: Loop through each letter of the entry and build a hint for each
    # letter in our guess by comparing it to our solutions. Then return the hint.
    hint = ""

    return hint

def finalize_guess(guess, hint):
    '''
    Finalizes a valid user guess.

    This function does a few things:
      1. It saves the current guess as a past guess
      2. It clears out the current guess
      3. It checks to see if the guess matches the solution
      4. It checks to see if the user has reached the max number of guesses

    Args:
      * guess (`str`): The guess to be showed on the screen.
      * hint (`str`): The evaluated hint so that we can color the blocks correctly.

    Returns:
      * `None`, instead appends a guess to `game_data['past_guesses']` and checks to see if the game is over.

    '''
    # Append the inputted guess to the past_guesses list in game_data
    game_data['past_guesses'].append(guess)

    # Clear out the current guess
    game_data['current_guess'] = ""

    # Set the current_guess key in game_data to the empty string ("")
    if hint == "🟩"*len(guess):
        cs110_hw7.game_over(happy=True)
    elif len(game_data['past_guesses']) == 6:
        cs110_hw7.game_over()


def show_past_guess(past_guess, guess_number, hint):
    '''
    Shows a past guess on the screen.

    Parameters:
      * past_guess (`str`): The past guess to be showed (you can assume it's valid and the correct length)
      * guess_number (`int`): The number of the guess to be drawn (y-coordinate)
      * hint (`str`): The hint string that was generated from that guess

    Returns:
      * `None` (Draws to the screen)
    '''
    for i in range(0, 5):
        # Print out the current coordinate being processed
        # print("Coordinate:", (i, guess_number))

        if hint[i] == "🟩":
            # TODO: replace pass with a call to `cs110_hw7.color_a_grid_square` to color the
            # square with the CORRECT_COLOR.
            pass

        elif hint[i] == "🟨":
            # TODO: replace pass with a call to `cs110_hw7.color_a_grid_square` to color the
            # square with the PARTIAL_COLOR.
            pass
        else:
            # TODO: replace pass with a call to `cs110_hw7.color_a_grid_square` to color the
            # square with the WRONG_COLOR.
            pass

        # TODO: Draw the letter in the right grid (since these are past guesses,
        # they should be marked as finalized) by calling `cs110_hw7.draw_letter_in_grid`.


def show_game_board(num_letters=5):
    '''
    Shows the game board.

    Returns:
      * `None`, draws to the screen.
    '''
    # Clear the screen.
    cs110_hw7.delete("all")
    
    # Resize the window to accommodate for the correct number of characters
    SCREEN_WIDTH = 100 * num_letters
    SCREEN_HEIGHT = 600
    canvas.config(width=100 * num_letters, height=600)

    # Draw the grid
    cs110_hw7.make_grid(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Load in the current guess from our game_data dictionary
    current_guess = game_data['current_guess']

    # Load in the list of past guesses from our game_data dictionary
    past_guesses = game_data['past_guesses']

    # Calculate how many guesses there have been by finding the length of the
    # past_guesses list in our game_data dictionary
    guess_count = len(game_data['past_guesses'])

    # Loop through all of the past guesses
    for i in range(0, guess_count):
        # print("Drawing... Guess Num:", i, "Guess to draw:", past_guesses[i])
        # print("Hint:", generate_hint(past_guesses[i], game_data['solution']))

        # TODO: Use the `show_past_guess` function to draw each of the
        # past guesses to the canvas.
        pass # you can delete this place holder line once you've started working

    # Now loop through each letter of the current guess and draw it to the board
    for i in range(0, 5):
        if i >= len(current_guess):
            break
        cs110_hw7.color_a_grid_square(DEFAULT_COLOR, (i, guess_count))
        cs110_hw7.draw_letter_in_grid(current_guess[i], (i, guess_count))

    # Update the game board
    canvas.mainloop()

########################## EVENT LISTENERS ##############################
def handle_typing(event):
    '''
    Event handler for key presses in W0rdle.

    We need to handle 3 specific types of key presses:
      1. `event.keysym == "BackSpace"`
      2. `event.keysym == "Return"`
      3. `len(event.keysym) == 1` (single character keys)

    Args:
      * `event`: The event to process.

    Returns:
      * `None` (Draws to the screen and also has side effects)
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
            finalize_guess(game_data['current_guess'], hint)

    # If the player hits any other letter/number/symbol on the keyboard
    elif len(event.keysym) == 1:
        # If the user hasn't entered 5 letters, add the entered symbol
        # to the current guess (make sure to convert it to upper case!)
        if len(game_data['current_guess']) < 5:
            game_data['current_guess'] += event.keysym.upper()

    # As long as the user hasn't made 6 guesses, show the game board
    if len(game_data['past_guesses']) < 7:
        show_game_board()

########################## GAME SETUP AND PLAY ##############################
# Ask the computer to listen for key presses
cs110_hw7.setup_listener('<Key>', handle_typing)

# Step 0. Set the number of characters in your target word
NUM_LETTERS = 5

# Step 1. Read in the wordlist and set the secret word
# you can change this to different wordlists and num_letters values
read_in_words('eng_wordlist.txt', num_letters = NUM_LETTERS) 

# Step 2. Print the solution for debugging
print("Solution:", game_data['solution'])

# Step 3. show the game board!
show_game_board(num_letters = NUM_LETTERS)
