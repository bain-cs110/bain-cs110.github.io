# --------------------------------------------------------------------------------
# ## Using Python to control text
# --------------------------------------------------------------------------------

# print is a FUNCTION that takes as input (argument)_ any piece of data and then outputs that
# data in the interpreter window
print('Hello CS 110!')
print('Checkout my cool program')


# Python can also be a super powerful calculator for numerical stuff
print(36 + 64)
print(1234*1234)
print(56 / 8)

# input is a special type of function called a REPORTER. That means when you run
# that function, you can expect it to REPORT BACK a new piece of data you could
# then store in a variable (or container).

# Like print, input also takes in a piece of data as an "argument,", namely the prompt
# you'd like the user to see in the interpreter window.
awesomeness = input("On a scale of 1 to 5, how awesome is Python? ")

# awesomeness is a VARIABLE or a container in which to store data. We store a
# a piece of data in a variable by using the equals sign which is called the ASSIGNMENT
# operator.

# If we want to see what data was stored inside that variable, we have to print it back out
print(awesomeness)

# Say we wanted to convert this to a percentage awesomeness. The problem with the input function
# is that it "reports back" a string instead of a number.
print(type(awesomeness))

# If we want to use this thing as a number, we need to first ask Python to convert it
# and then also UPDATE the data in our container:
awesomeness = int(awesomeness)

# Now we can create a new container called percentage_awesomeness and calculate the percentage
percentage_awesomeness = awesomeness / 5 * 100

# But don't forget to print it so we can see the result!
print(percentage_awesomeness)

# P.S. Notice that many of these lines are preceded by a hashtag (or pound symbol)
# These are called "comments" – it's a way of telling Python that the stuff on this
# line isn't part of our program. Instead, it's just notes to ourselves.
