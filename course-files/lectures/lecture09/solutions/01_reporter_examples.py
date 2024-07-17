##### Examples of Writing your Own Reporter Functions
## Example 1
def get_square_area(height):
    area = height * height
    return area

# Invoking the function. Here we store its reported value in variable
result = get_square_area(5)
# Then print the variable
print(result)

# But we can also just directly print the reported value
print("Area of a square with height 7 is...", get_square_area(7))
print("Area of a square with height 13 is...", get_square_area(13))

## Example 2
def get_pyramid_area(width):
    area = width * width * 6
    return area

pyramid_area_result = get_pyramid_area(5)
print("Area of a pyramid with height 5 is...", pyramid_area_result)