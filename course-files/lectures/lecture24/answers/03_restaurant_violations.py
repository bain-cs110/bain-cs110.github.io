# write a program that reads the contents of the Food_Establishment_Violations
# for the City of Evanston and counts the number of violations that have occurred
# for each restaurant code. The, print out the restaurant code and the number of violations

import csv
# 1. start by creating a lookup table where
# the key is the business license
# and the value is the name of the business
business_license_lookup = {}

file_path = 'Food_Establishment_Businesses.csv'
f_businesses = open(file_path, 'r', encoding='utf8', errors='ignore')
for row in csv.reader(f_businesses):
    business_license_lookup[row[0]] = row[1]

# 2. opened the violations file:
file_path = 'Food_Establishment_Violations.csv'
f_violations = open(file_path, 'r', encoding='utf8', errors='ignore')
counts_dict = {}

for row in csv.reader(f_violations):
    license = row[0]
    business_name = business_license_lookup.get(license)
    if counts_dict.get(business_name) is None:
        # add a new element:
        counts_dict[business_name] = 1
    else:
        counts_dict[business_name] += 1

for key in counts_dict:
    print(str(key) + ":", counts_dict[key])
