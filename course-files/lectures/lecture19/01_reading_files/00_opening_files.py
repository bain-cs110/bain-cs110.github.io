# if we just use open, then we get a IOWrapper object that the computer only reads
# through one line at a time.
my_file_1 = open("moby_dick.txt", "r")
print(type(my_file_1))
my_file_1.close()

# Readlines reads the whole file from top to bottom and puts each line in a list
# for us to loop through.
my_file_2 = open("moby_dick.txt", "r")
the_contents = my_file_2.readlines()
print(type(the_contents))
print(the_contents[1337])
my_file_2.close()
# This second one is especially useful if you only want to look at particular lines
