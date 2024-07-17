# Ask the user to input two floats, the bill and the percentage of tip
bill = input("How much did dinner cost? ")
tip = input("What % tip do you want to leave? (0 to 100)")

# Convert them to floats (numbers with decimals)
bill = float(bill)
tip = float(tip)

# Calculate total bill
total_bill = bill + (tip / 100 * bill)

# Print out the total_bill
print(total_bill)
