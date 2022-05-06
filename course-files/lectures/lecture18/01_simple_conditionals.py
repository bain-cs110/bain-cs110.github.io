# Example of a Boolean
result = 5 == 5
print(result, type(result))

# Example of a Boolean
result = 6 > 10
print(result, type(result))

# Example of AND logical operator
result = "hello" == "hello" and 5 >= 3
print(result, type(result))

# Example of NOT logical operator
result = not True
print(result, type(result))

# Example of OR Logical Operator
result = "bad" == "hello" or 5 >= 3
print(result, type(result))

# Example of If-else
testing = 123
if testing == 123:
    print("TESTING")
else:
    print("uh oh")

# Example of If-elseif-else
grade = 87
if grade > 90:
    print("A")
elif grade > 80:
    print("B")
elif grade > 70:
    print("C")
else:
    print("Wasn't greater than 90 or 80 or 70")
