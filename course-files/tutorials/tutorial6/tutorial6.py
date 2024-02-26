game_data = {
  "solution": "VAGUE",
  "current_guess": "",
  "past_guesses": [],
  "word_list": []
  }

## Helper Functions
def read_in_words(file_path):
    # TODO: Read the wordlist.txt file and append 5 letter words to the word_list entry
    # (which is a list) of our game_data dictionary. Make sure to convert each of these words
    # to UPPER CASE (Hint: you can convert a string to upper case by using upper() method:
    # test_string = "hello"
    # upper_case = test_string.upper()

    my_file = open(file_path, "r")
    for line in my_file:
        # Remove the end line character from each line we read
        word = line.strip('\n')
        print(word)

    # Print out the list of valid words for debugging
    # print("Valid word list:", game_data['word_list'])

    ## TODO
    ## Pick a random word out of the list stored inside of game_data to serve as the solution
    ## Save that newly picked solution in the appropriate place in the game_data dictionary

    ## Reminder...
    # some_list = ['hello', 'there', 'general', 'kenobi']
    # print(random.choice(some_list))

    ## FYI, when you implement this...it might be wise to print it out for debugging!

def generate_hint(guess, solution):
    '''
    Generates a hint from a guess and a solution.

    This should be the same as the one from the Tutorial. A hint string will
    be 5 letters long, where each character represents the "correctness" of the
    guess:
      1. 🟩 for correct letters
      2. 🟨 for partially correct letters
      3. ⬜ for incorrect letters

    Args:
        guess (`str`): The guess to be evaluated
        solution (`str`): The solution to be compared to

    Returns:
        hint (`str`): The hint for the user
    '''

    # TODO: Loop through each letter of the entry and build a hint for each
    # letter in our guess by comparing it to our solutions. Then return the hint.
    hint = ""

    for i in range(0, 5):
        # TODO: If that letter matches the corresponding one in the solution
        # then add a dollar sign to our hint (hint += "🟩")
        print(guess[i] == solution[i])

        # TODO: Else-if that letter is IN that word anywhere,
        # then add a 🟨 to our hint (use the `in` operator!)

        # TODO: Else, that letter isn't in our word so add an ⬜ to our hint

    return hint

# Print Instructions
print("Welcome to Wordle!")
print("You need to guess a secret 5 letter word.")
print("You have 6 guesses.")
print("For each guess, we'll tell you whether or not the letters in your guess...")
print("   1. exactly match the secret word (you'll see a 🟩)")
print("   2. are in the secret word but in a different location (you'll see a 🟨)")
print("   3. or not in the word at all (you'll see a ⬜).")
print("Good luck!")
print()

# First read in the words
read_in_words("wordlist.txt")

# Start a counter for the number of guesses
guess_count = 0
# Load the solution from the game_data dictionary
solution = game_data['solution']

# Start Infinite loop:
while guess_count < 6:
    guess = input("What is your guess? ")

    # TODO: Convert the guess to uppercase
    # print("test".upper())

    # TODO: Change this to see if the input is exactly 5 letters long
    # Else, print an "invalid guess" message and continue
    if False:
        print("invalid guess")
        continue

    # TODO: Check to see if the input is a valid word in our dictionary
    # Else, print a different error message and continue (use the `in` operator)

    # Example:
    ## print("test" in ["hello", "test", "me"])

    # Loop through each letter of the entry and build a hint for each
    # letter in our guess by comparing it to our solutions
    hint = generate_hint(guess, solution)

    # Print the user's guess
    print(guess)
    # Now print the hint for that guess
    print(hint)

    if hint == "🟩🟩🟩🟩🟩":
        print("You've won!")
        break

    # Add one to the count of the guesses
    guess_count = guess_count + 1
    # Print a message saying how many guesses are left
    print("You have", 6 - guess_count, "guesses left.\n")