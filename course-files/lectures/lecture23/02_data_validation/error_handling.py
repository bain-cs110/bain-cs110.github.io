'''
You're working for the city and want to identify all of the senior
citizens in your district to send out a mailer -- as they may qualify
for a special tax waiver. You are given a (messy and incomplete) data
set. Your boss wants you to create 2 files:

  * One for people with a complete data profile (no obvious mistakes)
  * One for people with an incomplete / suspect data profile

Write a program to do this.
'''
f = open('people.csv', 'r')

line_counter = 0
for line in f:
    
    # Skip the first line of the file
    if line_counter == 0:
        line_counter += 1
        continue

    cells = line.split(',')
    name = cells[0]
    age = cells[1]
    address = cells[2]

    if len(cells) != 3:
        print("invalid: too much data")
        continue

    # Need to check age
    # is it a number?
    # is it a valid age?
    line_counter = line_counter + 1

f.close()