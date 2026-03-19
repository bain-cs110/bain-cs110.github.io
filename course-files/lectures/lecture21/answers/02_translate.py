#example: print all keys and values one by one:
from json import loads, dumps
from utilities import get_file_path

# open and read file:
f = open(get_file_path("eng2fr.json"), "r")
eng2fr = loads(f.read())
f.close()

# Your job
while True:
    word = input("Enter a word in English and I will tell you the French translation: ")
    if word.upper() == "Q":
        print("quitting...\n")
        break
    if not eng2fr.get(word):
        translation = input("     Teach me the translation is so that I will remember it for the future: ")
        engfr[word] = translation
    print("     The translation for", word, "is", eng2fr[word], "\n")


# overwrite eng2fr with new dictionary:
f = open(get_file_path("eng2fr.json"), "w")
f.write(dumps(eng2fr))
f.close()