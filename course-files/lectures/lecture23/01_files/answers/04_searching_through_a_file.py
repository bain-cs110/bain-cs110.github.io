f = open('moby_dick.txt', 'r')

count = 0
for line in f:
    words = line.split(' ')
    for word in words:
        if word.upper() == 'MOBY':
            count += 1
            # print(line)

print('Moby appears ', count, 'times in the file.')