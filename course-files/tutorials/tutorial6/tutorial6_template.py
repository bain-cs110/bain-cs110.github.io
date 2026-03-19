from random import choice

GAME_DATA = {
  "solution": "YOU FORGOT TO PICK A SOLUTION!!!!",
  "current_guess": "",
  "past_guesses": [],
  "word_list": []
  }

def read_in_words(file_path):
    list_of_words = []
    
    ## TODO: Open the file stored in the file_path variable
    
    ## TODO: loop through each line of the file
        ## TODO: Split the line by " " using the split method of the String class
        ## TODO: Append the 0th element of that list into list_of_words

    ## TODO: Close the file!

    # You can print out the list of valid words if you need to for debugging
    # print("A random word in our list:", choice(list_of_words))
    # print("Number of valid words:", len(list_of_words))
    
    return list_of_words


def generate_hint(guess, solution):
    # Loop through each letter of the entry and build a hint for each
    # letter in our guess by comparing it to our solutions. Then return the hint.
    hint = ""
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

# First read in the words and save it in the GAME_DATA dictionary
GAME_DATA["word_list"] = read_in_words("5_letter_words.txt")


# Next pick a solution
## TODO: Use the choice function to pick a random word from the 
#        word_list you saved in the GAME_DATA dict

## TODO: Save it in the "solution" key of the GAME_DATA dictionary


# Start our game loop!
while len(GAME_DATA["past_guesses"]) < 6:
    guess = input("What is your guess? ")

    # Convert the guess variable to uppercase!
    guess = guess.upper()

    # Check if the guess is exactly 5 letters long
    # Else, print an "invalid guess" message and continue
    if len(guess) != 5:
        print("INVALID GUESS. Not 5 letters!")
        continue # send it back to the top of the loop

    # Check to see if the input is a valid word in our dictionary. If it's
    # not then continue (ask the user to guess again)
    if guess not in GAME_DATA["word_list"]:
        print("Not a valid word!")
        continue

    # Use our earlier defined function to generate a hint based on the guess
    hint = generate_hint(guess, GAME_DATA["solution"])

    # Print the user"s guess and its "hint"!
    print("Here's what you guessed:", guess)
    print("And here's the hint:    ", hint)

    if hint == "🟩🟩🟩🟩🟩":
        print("!"*80)
        print("You've won!")
        print("!" * 80)
        break

    # Add one to the count of the guesses
    GAME_DATA["past_guesses"].append(guess)

    # Print a message saying how many guesses are left
    print("You have", 6 - len(GAME_DATA["past_guesses"]), "guesses left.")
    print("*"*80 + "\n")
