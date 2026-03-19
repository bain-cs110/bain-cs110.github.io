'''
Practice:
Write a function called even_or_odd that takes 1 
positional parameter —  an int called num — and 
returns a string that says either 'even' or 'odd'
Prove that your function works by printing the results 
of several function calls to the screen
'''

def even_or_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
    
result_1 = even_or_odd(1)
print(result_1)

result_2 = even_or_odd(2)
print(result_2)

result_3 = even_or_odd(1005884)
print(result_3)
