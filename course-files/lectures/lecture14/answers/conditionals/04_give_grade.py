'''
Practice:
Write a function called give_grade that takes 1
positional parameter —  a float called score that
can range from 0 to 100 — and returns a letter grade
(a string).

Assume:
90 - 100:	A
80 - 89:	B
70 - 79:	C
60 - 69:	D
< 60:		F

Proved that your function works by printing the
results of several function calls to the screen...
'''

def give_grade(score:float):

    grade = ""

    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    return grade


print(give_grade(90))
print(give_grade(85))
print("Letter grade for", 74, "is", give_grade(74))
