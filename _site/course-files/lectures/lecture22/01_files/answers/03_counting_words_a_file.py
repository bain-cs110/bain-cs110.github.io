f = open('moby_dick.txt', 'r')

counter = 0
for line in f:
    words = line.split(' ')
    counter += len(words)


print('there are ', counter, 'words in the file.')