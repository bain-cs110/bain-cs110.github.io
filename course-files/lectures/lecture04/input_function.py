# The built-in input() function prompts the user for an input,
# and returns what the user typed as a string, that can be stored
# in a variable. If you want to treat what the user typed as a number,
# you need to manually convert it to the correct data type:

# simple example: store the result of the user's input
# in a variable named "answer"
answer = input("How old are you? ")
print(answer, type(answer))

### without any data conversion:
num_1 = input("What is your first number? ")
num_2 = input("What is your second number?")
answer = num_1 + num_2
message = "The sum of your numbers is: " + answer
print(message)

# after converting the user's input to a string:
num_1 = int(input("What is your first number? "))
num_2 = int(input("What is your second number?"))
answer = num_1 + num_2
# remember, answer is now an int!
message = "The sum of your numbers is: " + str(answer)
print(message)
