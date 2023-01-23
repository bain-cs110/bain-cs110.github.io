
### INPUT APPROACH
# first ask the person for their age
user_input = input("What's your current age? ")

# convert that string into a number
age = int(user_input)
future_age = age + 27
print("You will be", future_age, "in the year 2050.")


### REPORTER APPROACH

def calculate_new_age(age):
    return age + 27

my_age = 20
future_age = calculate_new_age(my_age)
print("You will be", future_age, "in the year 2050.")