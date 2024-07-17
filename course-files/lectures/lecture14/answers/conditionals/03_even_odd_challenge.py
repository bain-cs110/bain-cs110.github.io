'''
Practice:
Write a function called even_or_odd that takes 1
positional parameter —  an int called num — and
returns a string that says either 'even' or 'odd'
Prove that your function works by printing the results
of several function calls to the screen
'''



def even_or_odd(num:int):

    answer = ""

    # if the number is divisible by 2, then it's even
    if num % 2 == 0:
        answer = "even"
    # otherwise it's odd!
    else:
        answer = "odd"

    return answer


result1 = even_or_odd(-2)
result2 = even_or_odd(0)
result3 = even_or_odd(3)
result4 = even_or_odd(5)
result5 = even_or_odd(5+9)

print(result1, result2, result3, result4, result5)
