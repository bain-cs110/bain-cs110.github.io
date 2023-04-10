# Challenge:
#   1. How many unique words are there in the entirety of Moby Dick?
#   2. How many times does each word occur?

file_name = "moby_dick.txt"
file = open(file_name, "r")

word_count = 0

for line in file:
    words = line.split(" ")
    word_count = word_count + len(words)

print(word_count)