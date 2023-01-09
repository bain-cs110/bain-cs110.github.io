# Ask the user to input 3 strings
str_1 = input("1st str: ")
str_2 = input("2nd str: ")
str_3 = input("3rd str: ")

# Calculate the length of each string entered
length_1 = len(str_1)
length_2 = len(str_2)
length_3 = len(str_3)

# Calculate the minimum length
min_length = min(length_1, length_2, length_3)

# Print out the minimum length we calculated
print(min_length)
