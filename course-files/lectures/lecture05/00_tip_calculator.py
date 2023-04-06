bill = 13.00
tip = 20 # percentage points

tip_amount = tip / 100 * bill

bill = bill + tip_amount

print("Your tip amount is:", tip_amount)
print("Your total is:", bill)

# Note...this WON'T work
# print("Your total is:" + bill)