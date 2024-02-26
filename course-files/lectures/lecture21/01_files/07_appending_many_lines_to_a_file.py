f = open('my_new_file.txt', 'a')

colors = ['red', 'pink', 'purple', 'orange', 'teal', 'blue']
for color in colors:
    f.write(color)
    f.write('\n')

f.close()
