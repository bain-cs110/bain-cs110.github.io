# print a single argument:
print("Hi there")
print(44)
print(2.5)
print(None) # None is a special data type we"ll talk about later

x = 5
message = "I like the number..."
# to_print = message + x # can't do this because they're different types!
to_print = message + str(x)
print(to_print)

# print multiple arguments with a space in between each argument
# # (a space character is the default separator):
print("Hello", "how", "are", "you", "doing", "?\n")
print("The answer is:", 22)

# optional "sep" (separator) argument prints whatever you set
# as your separator string between each word.
print(1, 2, 3, 4, 5, sep=" + ", end=" = 15\n")
print("Hello", "how", "are", "you", "doing", "?", sep=":::")

# optional "end" argument prints whatever you set
# as your end string as the very last character
print("Hello", "how", "are", "you", "doing", sep="  |  ", end="?")
print("Hello", "how", "are", "you", "doing", sep="  |  ", end="?\n")
