from json import loads, dumps
from utilities import get_file_path

# open and read file:
f = open(get_file_path("eng2fr.json"), "r")
eng2fr = loads(f.read())
f.close()

print(eng2fr)
# Your job:
# Modify the translation program below so that if the translation is not in
# the dictionary, your program will:
# 1. Ask the user to type in the translation so that it can "learn" how to 
#    translate the word.
# 2. Store the new translation in its dictionary,
# 3. When the user asks to quit the program, the program will overwrite
#    the old dictionary with the more comprehensive version of the dictionary
#    (already done for you).
 
while True:
    word = input("Enter a word in English and I will tell you the French translation: ")
    if word.upper() == "Q":
        print("quitting...\n")
        break
    # YOUR CODE HERE 


    # END YOUR CODE HERE
    print("The translation for", word, "is", eng2fr.get(word), "\n")


# overwrite eng2fr.json with new dictionary:
f = open(get_file_path("eng2fr.json"), "w")
f.write(dumps(eng2fr))
f.close()