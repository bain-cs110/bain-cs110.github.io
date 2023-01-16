# ---------------------------------------
# 4. functions with multiple parameters
# ---------------------------------------
# function definition with 2 required parameters:
def say_hello(name, time_of_day):
    print('Hello there,', name + "!")
    print('How are you this ' + time_of_day + "?")

# function calls:
say_hello('Varun', "afternoon")
say_hello('Grace', "afternoon")
say_hello('Charlie', "afternoon")
say_hello('Jazmin', "morning")


# function definition with 1 required parameter and 1 optional/keyword:
def say_hello_alt(name, time_of_day = "morning"):
    print('Hello there,', name + "!")
    print('How are you this ' + time_of_day + "?")

# function calls:
say_hello_alt('Varun')
say_hello_alt('Grace')
say_hello_alt('Charlie', "afternoon")
say_hello_alt('Jazmin', "evening")
