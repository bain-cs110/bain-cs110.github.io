f = open('moby_dick.txt', 'r')

for line in f.readlines():
    print(line)
f.close()