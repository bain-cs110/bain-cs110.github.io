numbers = [
    76, 76, 76, 72, 76, 79, 67, 72, 67, 64, 69, 71,
    70, 69, 67, 76, 79, 81, 77, 79, 76, 72, 74, 71
]

# Challenge: skip over all of the numbers that equal 67 or 76

for num in numbers:
    if num == 67 or num == 76:
        continue
        print("lol")  # we'll never see this continue makes us go back to the top of the loop
    print(num) # we only make it here if it's not 67 or 76
