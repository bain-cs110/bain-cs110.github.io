from cs110_ex7 import *
from random import choice
########################## CANVAS SETUP CODE ##############################
# initialize window
gui = Tk()
gui.title("SUPER Wordle!")

canvas = Canvas(gui,background="white")
setup_window(canvas)

# the next thing is a list of all the functions in this file. It's so we can
# generate that cool web version of the documentation. You don"t need to
# worry about it.
__all__ = [
    "get_difficulty", "read_in_words", "generate_hint", "finalize_guess",
    "show_past_guess", "show_game_board", "handle_typing" 
]
########################## GAMEPLAY FUNCTIONS ##############################

# Dictionary to store all of the game data
GAME_DATA = {
  "solution": "",      # a string that is the secret solution
  "current_guess": "", # a string that contains the current guess
  "past_guesses": [],  # a list that contains all of the past guesses
  "word_list": [],     # a list that will contain all the valid n letter words
  "num_letters": 5,    # how many letters does each solution contain
  }


def get_difficulty():
    """
    Uses a pop-up window to ask the user to input the desired difficulty (length of words).
  

    Returns:
      * `int`: The number of letters (the difficulty) to use for the secret word
      * or `"invalid"`: the string `"invalid" indicating that the person did not enter a valid number
    """
  
    user_input = simpledialog.askstring(
        title="Difficulty Level", prompt="What length word should we use?"
    )

    ## TODO: Use try-except to try and see if user_input is a number
        ## TODO: If they did, check to see if it's at least 2 or at most 15.
            ## TODO: If it is, then **return** that number
        ## TODO: In all other cases, **return** the string "invalid"


def read_in_words(file_path, num_letters):
    """
    Function that reads in a list of words and adds them to the `GAME_DATA`. Then,
    picks a random word to set as the "solution" key in the `GAME_DATA` dictionary.
    
    Args:
      * file_path (`str`): The file to be read in
      * num_letters (`int`): How many letters should be in a word

    Returns:
      * a `list` containing the words with the correct number of letters
    """
    list_of_words = []
    
    ## TODO: Open the file stored in the file_path variable
    
    ## TODO: loop through each line of the file
        ## TODO: Split the line by " " using the split method of the String class
        ## TODO: If the number of letters in that word matches num_letters
            ## TODO Append the 0th element of that list into list_of_words

    ## TODO: Close the file!

    # You can print out the list of valid words if you need to for debugging
    # print("A random word in our list:", choice(list_of_words))
    # print("Number of valid words:", len(list_of_words))
    
    return list_of_words

    
def generate_hint(guess, solution):
    """
    Generates a hint from a guess and a solution.

    A hint string will be however many letters long the guess
    and solution are, where each character represents the "correctness"
    of the guess:
      1. 🟩 for correct letters
      2. 🟨 for partially correct letters
      3. ⬜ for incorrect letters

    Args:
      * guess (`str`): The guess to be evaluated
      * solution (`str`): The solution to be compared to

    Returns:
      * `hint` (`str`): The hint for the user
    """

    # Loop through each letter of the entry and build a hint for each
    # letter in our guess by comparing it to our solutions. Then return the hint.
    hint = ""

    ## ACTIVITY 5 TODO: Change this range to account for the fact that the solution / guess
    ##         could have more or less than 5 letters.
    for i in range(0, 5, 1):
        pass ## TODO: remove this pass once you're working here
    
        # TODO: If that letter matches the corresponding one in the solution
        # then add a 🟩 to our hint (hint = hint + "🟩")
        # Here"s an example of comparing specific letters
        #   guess[i] == solution[i]

        # TODO: Else-if that letter is IN that word anywhere,
        # then add a 🟨 to our hint (use the `in` operator!)

        # TODO: Else, that letter isn"t in our word so add an ⬜ to our hint

    return hint

def finalize_guess(guess, hint):
    """
    Finalizes a valid user guess.

    This function does a few things:
      1. It saves the current guess as a past guess
      2. It clears out the current guess
      3. It checks to see if the guess matches the solution
      4. It checks to see if the user has reached the max number of guesses

    Args:
      * guess (`str`): The guess to be showed on the screen.
      * hint (`str`): The evaluated hint so that we can color the blocks correctly.

    Side-Effects:
      * Appends a guess to GAME_DATA["past_guesses"] and checks to see if the game is over.

    """
    # Append the inputted guess to the past_guesses list in GAME_DATA
    GAME_DATA["past_guesses"].append(guess)

    # Clear out the current guess
    GAME_DATA["current_guess"] = ""

    # ACTIVITY 5 TODO: Change the one line below to account for the fact that a guess might have
    ##         greater or fewer than the number letters in the guess.
    if hint == "🟩" * 5:
        game_over(happy=True)
        
    elif len(GAME_DATA["past_guesses"]) == 6:
        game_over()


def show_past_guess(past_guess, guess_number, hint):
    """
    Shows a past guess on the screen.

    Parameters:
      * past_guess (`str`): The past guess to be showed (you can assume it"s valid and the correct length)
      * guess_number (`int`): The number of the guess to be drawn (y-coordinate)
      * hint (`str`): The hint string that was generated from that guess

    Side-Effect:
      * Draws to the screen
    """
    # ACTIVITY 5 TODO: Change the one line below to account for the fact that a guess might have
    ##         greater or fewer than the right number of letters (Currently works for 5 letters)
    for i in range(0, 5):

        if hint[i] == "🟩":
            color_a_grid_square(CORRECT_COLOR, (i, guess_number))

        elif hint[i] == "🟨":
            color_a_grid_square(PARTIAL_COLOR, (i, guess_number))
        else:
            color_a_grid_square(WRONG_COLOR, (i, guess_number))

        draw_letter_in_grid(past_guess[i], (i, guess_number), past_guess=True)

def show_game_board():
    """
    Shows the game board.

    Side-Effect:
      * Draws to the screen
    """
    # Clear the screen.
    delete("all")

    # Resize the window to accommodate for the correct number of characters
    # ACTIVITY 5 TODO: Change the one line below to account for the fact that a guess might have
    # greater or fewer than right number of letters letters (Currently works for 5 letters)
    screen_width = 100 * 5
    screen_height = 600

    # ACTIVITY 5 TODO: Change the one line below to account for the fact that a guess might have
    # greater or fewer than the right number of letters (Currently works for 5 letters)
    canvas.config(width=100 * 5, height=600)

    # Draw the grid
    make_grid(screen_width, screen_height)

    # Load in the current guess from our GAME_DATA dictionary
    current_guess = GAME_DATA["current_guess"]

    # Load in the list of past guesses from our GAME_DATA dictionary
    past_guesses = GAME_DATA["past_guesses"]

    # Calculate how many guesses there have been by finding the length of the
    # past_guesses list in our GAME_DATA dictionary
    guess_count = len(GAME_DATA["past_guesses"])

    # Loop through all of the past guesses
    for i in range(0, guess_count, 1):
        show_past_guess(past_guesses[i], i, generate_hint(past_guesses[i], GAME_DATA["solution"]))

    # Now loop through each letter of the current guess and draw it to the board
    for i in range(0, len(current_guess), 1):
        color_a_grid_square(DEFAULT_COLOR, (i, guess_count))
        draw_letter_in_grid(current_guess[i], (i, guess_count))

    # Update the game board
    canvas.mainloop()

########################## EVENT HANDLERS ##############################
def handle_typing(event):
    """
    Event handler for key presses in Wordle.

    We need to handle 3 specific types of key presses:
      1. `event.keysym == "BackSpace"`
      2. `event.keysym == "Return"`
      3. `len(event.keysym) == 1` (single character keys)

    Args:
      * `event`: The event to process.

    Side-Effect:
      * Draws to the screen and updates current_guess inside of GAME_DATA
    """
    # If the player hits BackSpace, delete the last character from the
    # "current_guess" key in the GAME_DATA dictionary
    if event.keysym == "BackSpace":
        GAME_DATA["current_guess"] = GAME_DATA["current_guess"][:-1]

    # If the player hits Return...
    elif event.keysym == "Return":
        # First check that right num letters have been entered
        # ACTIVITY 5 TODO: Change the one line below to account for the fact that a guess might have
        # greater or fewer than the right number of letters (Currently works for 5 letters)
        if len(GAME_DATA["current_guess"]) != 5:
            print("not enough letters")
            # Next check if it"s a valid word in our word list
        elif GAME_DATA["current_guess"] not in GAME_DATA["word_list"]:
            print("not a valid word")
        # If we make it past those two checks, it's a valid guess
        else:
            # First generate a hint, then finalize the guess
            hint = generate_hint(GAME_DATA["current_guess"], GAME_DATA["solution"])
            finalize_guess(GAME_DATA["current_guess"], hint)

    # If the player hits any other letter/number/symbol on the keyboard
    elif len(event.keysym) == 1:
        # If the user hasn't entered the right num letters, add the entered symbol
        # to the current guess (make sure to convert it to upper case!)
        # ACTIVITY 5 TODO: Change the one line below to account for the fact that a valid guess might have
        # greater or fewer than right number of letters (Currently works for 5 letters)
        if len(GAME_DATA["current_guess"]) < 5:
            GAME_DATA["current_guess"] += event.keysym.upper()

    # As long as the user hasn"t made 6 guesses, show the game board
    if len(GAME_DATA["past_guesses"]) < 7:
        show_game_board()


########################## GAME SETUP AND PLAY ##!!##########################
# Step 0. Set the number of characters in your target word
difficulty = get_difficulty()

if difficulty == "invalid":
    # This function purposefully causes an Error to stop our program
    raise Exception("You entered an invalid difficulty rating.")
else:
    GAME_DATA["num_letters"] = difficulty

# Ask the computer to listen for key presses
listen_for("Key", handle_typing)

# Step 1. Read in the wordlist
GAME_DATA["word_list"] = read_in_words("NWL2023.txt", num_letters=GAME_DATA["num_letters"])

# Step 2. Pick a random solution
GAME_DATA["solution"] = choice(GAME_DATA["word_list"])

# Step 3. Print the solution for debugging
print("Solution:", GAME_DATA["solution"])

# Step 4. show the game board!
show_game_board()
