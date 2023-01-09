num_1 = input("1st number: ")
num_2 = input("2nd number: ")
num_3 = input("3rd number: ")

# Since the input function gives us back strings
# we need to convert them to numbers
num_1 = int(num_1)
num_2 = int(num_2)
num_3 = int(num_3)

print(max(num_1, num_2, num_3))
