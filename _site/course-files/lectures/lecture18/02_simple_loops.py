### While Loops
counter = 10
sum = 0
while counter > 0:
    sum = sum + 1
print(sum)

counter = 0
while True:
    print("Hello there!")
    counter +=1
    if counter == 5:
        break

### For Loops
for pizza in ["Mario", "Peach", "Goomba", "Toad", "Luigi"]:
    print("Hello", pizza)

sum = 0
for pineapple in (13, 17, 19, 5, 6, 10):
    sum = sum + pineapple
print(sum)

#### RANGE EXAMPLES
print("Trying range...")
for i in range(3, 10, 3):
    print(i)

some_list = [True, False, True, False, True, False]
for i in range(0, 6, 2):
    print(some_list[i])
