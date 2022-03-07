# write a program that reads the contents of the Food_Establishment_Violations
# for the City of Evanston and counts the number of violations that have occurred
# for each restaurant code. The, print out the restaurant code and the number of violations

import csv

file_path = "Food_Establishment_Violations.csv"


f = open(file_path, 'r', encoding='utf8', errors='ignore')

## Instead of writing our own program to deal with each line, we use the
## csv library and the reader function to convert each row to a list!
for row in csv.reader(f):
    print(type(row))
    print(row)
    break
