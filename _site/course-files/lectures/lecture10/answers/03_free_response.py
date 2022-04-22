## Program 1
first_names = ['Kim', 'Brenda', 'Karlo']
last_names = ['Jones', 'Jauregui', 'Imper']

full_names = []
full_names.append(first_names[0] + ' ' + last_names[0])
full_names.append(first_names[1] + ' ' + last_names[1])
full_names.append(first_names[2] + ' ' + last_names[2])
print(full_names)


## Program 2
def shift_coordinates(my_list, x_units=0, y_units=0):
    return [
        (my_list[0][0] + x_units, my_list[0][1] + y_units),
        (my_list[1][0] + x_units, my_list[1][1] + y_units),
        (my_list[2][0] + x_units, my_list[2][1] + y_units)
    ]

print(shift_coordinates([(20, 20), (30, 30), (40, 40)], x_units=100, y_units=200))
print(shift_coordinates([(40, 40), (100, 100), (200, 200)], x_units=50, y_units=100))
print(shift_coordinates([(40, 40), (100, 100), (200, 200)]))
