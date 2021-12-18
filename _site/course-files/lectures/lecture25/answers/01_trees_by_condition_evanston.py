from csv import reader
import utilities

file_path = utilities.get_file_path('Trees_data.csv')
f = open(file_path, 'r', encoding='utf8', errors='ignore')
rows = list(reader(f)) # save all the rows as a list

condition_dict = {}
for row in rows[1:]: # don't include the first row
    condition = row[16].replace('\n', '').lower()
    common_name = row[39].replace('"', '').lower()
    # print(condition)
    if condition in condition_dict:
        # add one to existing entry:
        condition_dict[condition] += 1
    else:
        # add new entry to the dictionary:
        condition_dict[condition] = 1

condition_dict_sorted = utilities.sort_dictionary(condition_dict)
for key in condition_dict_sorted:
    print('{0:<12} {1:,.0f}'.format(key + ':',  condition_dict[key]))
