def only_letters(a_string):
    """
    Takes in a string and returns it with only letters
    """
    return ''.join([i for i in a_string if i.isalpha()])

# Challenge:
#   1. How many unique words are there in the entirety of Moby Dick?
#   2. How many times does each word occur?

file_name = "moby_dick.txt"
file = open(file_name, "r")

word_count = 0

memory = {}

for line in file:
    words = line.split(" ")
    for word in words:
        
        clean_word = only_letters(word)
        clean_word = clean_word.lower()
        
        if clean_word in memory:
            memory[clean_word] = memory[clean_word] + 1
        else:
            memory[clean_word] = 1

for word in memory:
    print(word + ":", memory[word])
