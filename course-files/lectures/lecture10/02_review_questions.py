## Example 1
def function_1(a:float, b:float):
    return a * b
def function_2(a:float, b:float):
    return b - a
def function_3(a:float):
    3 * a

x = function_1(3, 2)
y = function_3(2)
z = function_2(x, function_1(x, x))
print(x, y, z)


## Example 2
def make_mario(center:tuple, width:int=50, fill:str='hotpink'):
    print("Luigi", width, fill, center)

make_mario((25, 25)) # first output
make_mario((20, 20), fill='yellow', width=150) # second output
make_mario(fill='pink', width=50) # 3rd output
