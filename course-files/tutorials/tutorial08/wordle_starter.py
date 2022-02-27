game_data = {
  "solution": "vague",
  "current_guess": "",
  "previous_guesses": [],
  "word_list": []
  }

print("Welcome to W0RDLE!")
print("You need to guess a secret 5 letter word.")
print("You have 6 guesses.")
print("For each guess, we'll tell you whether or not the letters in your guess...")
print("   1. exactly match the secret word (you'll see a $)")
print("   2. are in the secret word but in a different location (you'll see a -)")
print("   3. or not in the word at all (you'll see a *).")
print("Good luck!")
print()

# TODO: Read the wordlist.csv file and append 5 letter words to the word_list entry
# (which is a list) of our game_data dictionary
my_file = open("wordlist.txt", "r")
for line in my_file:
    # Remove the end line character from each line we read
    word = line.strip('\n')

    print(word)

# Print out the list of valid words
print("Valid word list:", game_data['word_list'])

# Start a counter for the number of guesses
guess_count = 0
# Load the solution from the game_data dictionary
solution = game_data['solution']

# Start Infinte loop:
while guess_count < 6:
    guess = input("What is your guess? ")

    # TODO: Convert the guess to lowercase
    # print("TEST".lower())

    # TODO: Change this to see if the input is exactly 5 letters long
    # Else, print an error message and continue
    if False:
        print("invalid guess")
        continue

    # TODO: Check to see if the input is a valid word in our dictionary
    # Else, print a different error message and continue (use the `in` operator)

    # Example:
    ## print("test" in ["hello", "test", "me"])

    # Loop through each letter of the entry and build a hint for each
    # letter in our guess by comparing it to our solutions
    hint = ""
    for i in range(0, 5):
        # TODO: If that letter matches the corresponding one in the solution
        # then add a dollar sign to our hint (hint += "$")
        print(guess[i] == solution[i])

        # TODO: Else-if that letter is IN that word anywhere,
        # then add a hyphen to our hint (use the `in` operator!)

        # TODO: Else, that letter isn't in our word so add an asterisk to our hint

    # Print the user's guess
    print(guess)
    # Now print the hint for that guess
    print(hint)

    if hint == "$$$$$":
        print("You've won!")
        break

    # Add one to the count of the guesses
    guess_count = guess_count + 1
    # Print a message saying how many guesses are left
    print("You have", 6 - guess_count, "guesses left.\n")
