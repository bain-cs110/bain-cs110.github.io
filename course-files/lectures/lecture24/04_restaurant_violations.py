# write a program that reads the contents of the Food_Establishment_Violations
# for the City of Evanston and counts the number of violations that have occurred
# for each restaurant code. The, print out the restaurant code and the number of violations

import csv

# This starts by creating a lookup table where
# the key is the business license
# and the value is the name of the business. Stored in the variable
# named business_license_lookup
print("Creatinging business_license_lookup dictionary...")
business_license_lookup = {}

file_path = 'Food_Establishment_Businesses.csv'
f_businesses = open(file_path, 'r', encoding='utf8', errors='ignore')
for row in csv.reader(f_businesses):
    business_license_lookup[row[0]] = row[1]

### YOUR TASK WILL BE BELOW HERE

file_path = "Food_Establishment_Violations.csv"
f = open(file_path, 'r', encoding='utf8', errors='ignore')

## Instead of writing our own program to deal with each line, we use the
## csv library and the reader function to convert each row to a list!
for row in csv.reader(f):
    print(type(row))
    print(row)
    break
