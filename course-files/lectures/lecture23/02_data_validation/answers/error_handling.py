'''
You're working for the city and want to identify all of the senior
citizens in your district to send out a mailer -- as they may qualify
for a special tax waiver. You are given a (messy and incomplete) data
set. Your boss wants you to create 2 files:

  * One for people with a complete data profile (no obvious mistakes)
  * One for people with an incomplete / suspect data profile

Write a program to do this.
'''

f_source = open('people.csv', 'r')
f_valid = open('people_valid.csv', 'w')
f_invalid = open('people_invalid.csv', 'w')


# Note, this is a different way of reading files that converts the file into
# a list ahead of time so that you can, for instance, skip particular lines
for line in f_source.readlines()[1:]:
    cells = line.split(',')
    name = cells[0]
    age = cells[1]
    address = cells[2]

    if len(cells) != 3:
        f_invalid.write(line)
        continue
    
    try:
        age = int(age)
    except:
        f_invalid.write(line)
        continue

    if age < 0 or age > 120:
        f_invalid.write(line)
        continue
    
    f_valid.write(line)

f_source.close()
f_valid.close()
f_invalid.close()