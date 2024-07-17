## Part 1 - Variable Tracing + Operators
x = 0
y = 6
z = 2
x = z ** z
y = (y % 2) + 5
z = x - (y - 4) // 3 

print("x:", x)
print("y:", y)
print("z:", z)


## Part 2 (Sequence Accessing)
some_stuff = [(8, 9, 8), (1, "b", 3), ("a", 6), [0, 7]]

result_a = some_stuff[2][0]
result_b = some_stuff[some_stuff[1][0]][1]

thing = 1
result_c = some_stuff[2 + 2 - thing]

print("result_a", result_a)
print("result_b", result_b)
print("result_c", result_c)


## Part 3 (Function Tracing)
def never(a, b):
    return a % b

def gonna(a, b=1.0):
    return b + a

def give():
    return 5

def you(a=5):
    return a

def up(pizza):
    print("pizza")

x = gonna(5)
y = never(3, x)
z = gonna(x, b=give())

pineapple = up("hello")

print("x:", x)
print("y:", y)
print("z:", z)
print("pineapple:", pineapple)


## Part 4 (Do you know how functions work)
colors = ["red", "pink", "purple", "orange", "teal", "blue"]

def car(coordinates, size, color="brown"):
    print(coordinates, color, size)

car((10, 10), 50, color="blue")
car((500, 500), 80, color=colors[5 % 3])
car((100, 130), 60)
#car((100, 100), color="yellow", 80)
#car((354, 487), 10, color=colors[len(colors)])
car((100, 100), "blue", color=10)



