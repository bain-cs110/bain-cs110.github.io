from cs110_t3_shapes import *
_ignore = setup_shapes('Tutorial 3', background="white", width=800, height=800)
#### YOUR CODE BELOW THIS LINE ##########

## Reporter and Sequence Practice goes here
my_favorite_things = [70,
                      "olive drab",
                      "Gilmore Girls",
                      "PSYCH", 101,
                      ["COMP_SCI 110",
                       "HIST 201",
                       "ART 103",
                       "MATH 210"]]

bains_favorite_things = [13, "green", "The West Wing", 
                        "COMP_SCI", 111, 
                        ["COMP_SCI 110", "COMP_SCI 396", 
                         "COMP_SCI 399"]]

def get_favorite_color(fave_things):
    return fave_things[1]

my_fave_color = get_favorite_color(my_favorite_things)
print("My favorite color is: " + my_fave_color)

bains_fave_color = get_favorite_color(bains_favorite_things)
print("Dr. Bain's favorite color is: " + bains_fave_color)

def multiply_favorite_numbers(list1, list2):
    return list1[0] * list2[0]

print("The product of my our fave numbers is...") 
print(multiply_favorite_numbers(my_favorite_things, bains_favorite_things))

from random import choice
def rando_class(list1):
    chance = choice(list1[-1])
    return chance

print("Rando class: " + rando_class(my_favorite_things))
print("Rando class: " + rando_class(my_favorite_things))
print("Rando class: " + rando_class(my_favorite_things))
### End Reporter and Sequence Practice

### Shape Example

circle1 = circle(center=(200, 200), radius=50, color="red")
a_square = square(size=25, color="blue")
a_square = rotate(a_square, degrees=45)
overlay(a_square, circle1)

## Flag of Chicago Challenge!

bg = rectangle((200, 400), width=400, height=200, color="white", outline="black")
stripe_1 = rectangle(width=400, height=40, color="#40B0DF")
stripe_2 = duplicate(stripe_1)
overlay(stripe_1, bg, offset_y = -50)
overlay(stripe_2, bg, offset_y = 50)

star1 = star(radius = 8, color = "red", outer_radius=20, points = 6)
overlay(star1, bg, offset_x=-125)
star2 = duplicate(star1)
beside(star2, star1, offset_x=40)
star3 = duplicate(star1)
overlay(star3, bg, offset_x=40)
star4 = duplicate(star3)
beside(star4, star3, offset_x=40)



#### IGNORE BELOW
_ignore.mainloop()