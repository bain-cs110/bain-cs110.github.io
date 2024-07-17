f = open('moby_dick.txt', 'r')


# Your job: can you write some code to
# count how many words there are this file?
for line in f:
    words = line.split(' ')
    print(words)
f.close()


# print('there are ', ?????, 'words in the file.')