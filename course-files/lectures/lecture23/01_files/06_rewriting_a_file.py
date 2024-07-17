source_file = open('moby_dick.txt', 'r')
destination_file = open('moby_dick_line_numbers.txt', 'w')

linenum = 1
for line in source_file:
    destination_file.write(str(linenum) + '. ')
    destination_file.write(line)
    linenum += 1
source_file.close()
destination_file.close()