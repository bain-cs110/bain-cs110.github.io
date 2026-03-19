numbers = [65, 1800, 12, 20, 1963, 5000, 260, 0, 40, 953, 775]
other_test = [-1, -2, -3, -4, -5]
# Challenge: write a program that finds the biggest number
# in the numbers list above

largest_yet = numbers[0]

for num in numbers:
    if num > largest_yet:
        largest_yet = num

print('The largest number in the list is:', largest_yet)
