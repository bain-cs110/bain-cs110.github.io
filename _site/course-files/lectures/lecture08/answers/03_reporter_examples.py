##### Examples of Writing your Own Reporter Functions
## Example 1
def get_square_area(height:int):
    area = height * height
    return area

# Invoking the function. Here we store its reported value in variable
result = get_square_area(5)
# Then print the variable
print(result)

# But we can also just directly print the reported value
print(get_square_area(7))
print(get_square_area(13))

## Example 2
def get_house_area(height:int):
    square_part = height * height
    roof = 1 / 2 * (height / 2) * height
    return square_part + roof

# Invoking the function AND outputting the result
print(get_house_area(1))
print(get_house_area(4))
print(get_house_area(8))
print(get_house_area(12))

## Example 3
def get_4_house_areas(list_of_heights:list):
    list_of_areas = []
    list_of_areas.append(get_house_area(list_of_areas[0]))
    list_of_areas.append(get_house_area(list_of_areas[1]))
    list_of_areas.append(get_house_area(list_of_areas[2]))
    list_of_areas.append(get_house_area(list_of_areas[3]))

    return list_of_areas

# Invoking the function AND outputting the result
print(get_4_house_areas([1,4,8,12]))
