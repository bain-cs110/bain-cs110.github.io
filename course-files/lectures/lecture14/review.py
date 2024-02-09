x = 0

## Example 1
if 0 < x and x < 10:
    print('WASSUP')

## Example 1a
if x > 0:
    print("x is greater than 0")
    print("Done with the if statement.")
elif x < 0:
    print("x is less than 0")
    print("Done with the if statement.")
else:
    print("x is 0")
    print("Done with the if statement.")

##
#### Example 2
##if 0 < x:
##    if x < 9:
##        print('hello')
##
##
#### Example 3
##if 0 < x or x == -31:
##    print("yo")
##
##
#### Example 4
##n = 5
##while n > 0:
##    print(n)
##    n = n - 1
##print('Blastoff!')
##
##
#### Example 5
##my_list = [76, 76, 76, 72]
##counter = 0
##while counter < len(my_list):
##    print(my_list[counter])
##
##
#### Example 6
##counter = 5
##while counter < 5:
##    print(counter)
##    counter += 1
##
##
##
#### Example 7
##super_heroes = ["ironheart", "wonder woman", "spider gwen",  "storm"]
##for name in super_heroes:
##    if " " not in name:
##        print(name)