tuple_of_strings = ("first year", "sophomore", "junior", "senior")
tuple_of_ints = (12, 24, 36, 48, 60)
tuple_of_tuples = ((20, 20), (20, 40), (40, 40), (40, 20))
tuple_of_mixed_data_types = ("a", 123, (40, 40), 34.5)

# ## Example 1: Items of a tuples can be of any type
print("\n\ntuples of different types...")
print(tuple_of_strings)
print(tuple_of_ints)
print(tuple_of_tuples)
print(tuple_of_mixed_data_types)
# ## End Example 1


# ## Example 2: A tuple can be of any length
print("\n\ncalculating length of a tuple...")

print(tuple_of_strings.__len__())
print(tuple_of_ints.__len__())
print(tuple_of_tuples.__len__())
print(tuple_of_mixed_data_types.__len__())

# But that looks weird, so there's a shortcut. 
print(len(tuple_of_strings))
print(len(tuple_of_ints))
print(len(tuple_of_tuples))
print(len(tuple_of_mixed_data_types))
# ## End Example 2


# ## Example 3: You can access any tuple element through 0-based indexing
print("\n\naccessing...")
first_word = tuple_of_strings.__getitem__(0)
second_word = tuple_of_strings.__getitem__(1)
third_word = tuple_of_strings.__getitem__(2)
fourth_word = tuple_of_strings.__getitem__(3)

print(first_word)
print(second_word)
print(third_word)
print(fourth_word)

# But that's pretty verbose so the people who made Python support a shortcut
first_word = tuple_of_strings[0]
second_word = tuple_of_strings[1]
third_word = tuple_of_strings[2]
fourth_word = tuple_of_strings[3]

print(first_word)
print(second_word)
print(third_word)
print(fourth_word)


# You can also do this backwards....
last_word = tuple_of_strings[-1]
penultimate_word = tuple_of_strings[-2]
# etc...
# ## End Example 3


# ## Example 4: You can slice tuples
print("\n\nslicing...")
first_2_words = tuple_of_strings[0:2]
last_2_words = tuple_of_strings[-2:]
all_but_first_word = tuple_of_strings[1:]
all_but_last_word = tuple_of_strings[:-1]
print(first_2_words)
print(last_2_words)
print(all_but_first_word)
print(all_but_last_word)
# ## End Example 4

## Example 5: You CANNOT update data in a tuple:
##print('\n\nupdating data in a tuple...')
##tuple_of_strings = ('freshman', 'sophomore', 'junior', 'senior')
##print(tuple_of_strings)
##tuple_of_strings[0] = 'first year'
##
### The only thing you can do is *completely* wipe out the variable
###tuple_of_strings = tuple_of_strings + ('masters', 'doctorate')
###print(tuple_of_strings)
##
###tuple_of_strings = (1, 2, 3, 4)
###print(tuple_of_strings)
## End Example 5
