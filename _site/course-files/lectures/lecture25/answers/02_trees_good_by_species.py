from csv import reader
import utilities

file_path = utilities.get_file_path('Trees_data.csv')
f = open(file_path, 'r', encoding='utf8', errors='ignore')
rows = list(reader(f)) # save all the rows as a list

species_dict = {}
for row in rows[1:]: # don't include the first row
    condition = row[16].replace('\n', '').lower()
    common_name = row[39].replace('"', '').lower()

    if condition != 'good':
        continue
    if common_name in species_dict:
        species_dict[common_name] += 1
    else:
        species_dict[common_name] = 1

species_dict_sorted = utilities.sort_dictionary(species_dict)
for key in species_dict_sorted:
    print('{0:<25} {1:,.0f}'.format(key + ':',  species_dict_sorted[key]))
