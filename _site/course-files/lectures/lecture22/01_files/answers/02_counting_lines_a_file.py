f = open('moby_dick.txt', 'r')

counter = 0
for line in f:
    counter += 1

print('there are ', counter, 'lines in the file.')