from csv import reader
import utilities

file_path = utilities.get_file_path('Trees_data.csv')
f = open(file_path, 'r', encoding='utf8', errors='ignore')
rows = list(reader(f)) # save all the rows as a list

for row in rows[1:]: # don't include the first row
    print(row)


