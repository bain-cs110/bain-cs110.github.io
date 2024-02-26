f = open('moby_dick.txt', 'r')

# Your job: can you write some code to see
# how many times the word "Moby" appears in
# the file?
for line in f:
    print(line)
f.close()

# print('Moby appears ', ?????, 'times in the file.')