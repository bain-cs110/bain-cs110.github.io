## Example 1
nums = [3.3, 4, 6, 3, 1.2, 1.4]
result = nums[0] + nums[2] + nums[4]
print(result)


## Example 2
import random
print(random.randint(0, 10) + 6 * 3)


## Example 3
my_list = [(0, 1), (1, 8), (3, 9), (4, -5)]
print(my_list[0])


## Example 4
print(my_list[2][1])


## Example 5
jedi = ['anakin', 'obi-wan', 'ashoka', 'yoda']
jedi.append('mace windu')
save = jedi.pop(1)
jedi.append(save)
jedi.append('luke')
jedi.pop(0)
jedi.append('darth vader')
print(jedi)
