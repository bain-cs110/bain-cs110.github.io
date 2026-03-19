
######## Functions with and without Return Values


### THIS IS NOT A REPORTER
# Here is an example of a function that has no return value. In this case, it takes
# one input (an integer stored in a variable called points) and does not return
# any value but instead prints directly to the interpreter window.
def yay_hufflepuff(points):
    print(points, "to Hufflepuff!!!!")

# This function does not return anything so we can't use its result to do anything
# afterwards. For example, if we try to store the result in a variable, you'll
# see that the variable ends up empty ("None")

result = yay_hufflepuff(100)
print(result)




### THIS IS A REPORTER
# Here is an example of a function that has a RETURN value. You can tell this by
# the fact that the function body concludes with a return statement.
# In this case, this function takes one required input (an integer stored in
# variable named number) and will return a string.

def iron_man_movie_title(number):
	return "Iron Man" + str(number)

# Since it returns a string, we can store that output in a variable or pass it
# to another function.
result = iron_man_movie_title(5)
print(result)

print(iron_man_movie_title(5))
