# Just an example of how some of the functions in the
# random module work:

## Offical Docs: https://docs.python.org/3/library/random.html
## Unofficial Docs: https://www.w3schools.com/python/module_random.asp

from random import randint, uniform, choice

def print_title(text):
    print()
    print('*' * len(text))
    print(text)
    print('*' * len(text))

print_title('randint(a, b): Picks a random integer between a and b (including endpoints)')
num1 = randint(30, 50)
num2 = randint(30, 50)
num3 = randint(30, 50)
print(num1, num2, num3)

print_title('uniform(a, b): Picks a random float between a and b (including endpoints)')
num4 = uniform(50, 400)
num5 = uniform(50, 400)
num6 = uniform(50, 400)
print(num4, num5, num6)


print_title("choice('abcde'): Picks a random element from a sequence")
letters = 'abcde'
letter1 = choice(letters)
letter2 = choice(letters)
letter3 = choice(letters)
print(letter1, letter2, letter3)
