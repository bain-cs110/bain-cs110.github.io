### IGNORE EVERYTHING THAT STARTS WITH A _
from random import randint
def _get_coordinates(canvas, id):
    return canvas.coords(id)

def _set_coordinates(canvas, id, coordinates):
    canvas.coords(id, coordinates)

def _update_position_by_id(canvas, id, x=2, y=0):
    coords = _get_coordinates(canvas, id)
    # update coordinates:
    for i in range(0, len(coords)):
        if i % 2 == 0:
            coords[i] += x
        else:
            coords[i] += y
    # set the coordinates:
    _set_coordinates(canvas, id, coords)

def _get_x_coordinates(canvas, tag):
    return _get_coordinates_by_dimension(canvas, tag, dimension='x')

def _get_y_coordinates(canvas, tag):
    return _get_coordinates_by_dimension(canvas, tag, dimension='y')

def _get_coordinates_by_dimension(canvas, tag, dimension='x'):
    '''
    updates the x and y position of all shapes that have been tagged
    with the tag argument
    '''
    if dimension == 'x':
        pos = 0
    else:
        pos = 1
    shape_ids = canvas.find_withtag(tag)
    coords = []
    for id in shape_ids:
        shape_coords = _get_coordinates(canvas, id)
        for i in range(0, len(shape_coords)):
            if i % 2 == pos:
                coords.append(shape_coords[i])
    return coords


### THESE ARE THE ONES THAT WILL BE HELPFUL

def update_position(canvas, tag, x=2, y=0):
    '''
    Name: update_position
    Purpose: updates the x and y position of all shapes that have been tagged
    with the tag argument
    Inputs:
      1. a canvas (Canvas) to search
      2. a tag (str) to move
      3. x (int; optional) amount to move in the x direction
      4. y (int; optional) amount to move in the y direction
    '''
    shape_ids = canvas.find_withtag(tag)
    for id in shape_ids:
        _update_position_by_id(canvas, id, x, y)

def get_left(canvas, tag):
    '''
    Name: get_left
    Purpose: returns the left boundary (minimum x-value) of the shape group
    Inputs:
      1. a canvas (Canvas) to search
      2. a tag (str) to search for
    '''
    return min(*_get_x_coordinates(canvas, tag))

def get_right(canvas, tag):
    '''
    Name: get_right
    Purpose: returns the right boundary (maximum x-value) of the shape group
    Inputs:
      1. a canvas (Canvas) to search
      2. a tag (str) to search for
    '''
    return max(*_get_x_coordinates(canvas, tag))

def get_width(canvas, tag):
    '''
    Name: get_width
    Purpose: returns the width (left to right distance) of a shape group
    Inputs:
      1. a canvas (Canvas) to search
      2. a tag (str) to search for
    '''
    x_coords = _get_x_coordinates(canvas, tag)
    return max(*x_coords) - min(*x_coords)

def get_height(canvas, tag):
    '''
    Name: get_width
    Purpose: returns the height (top to bottom distance) of a shape group
    Inputs:
      1. a canvas (Canvas) to search
      2. a tag (str) to search for
    '''
    y_coords = _get_y_coordinates(canvas, tag)
    return max(*y_coords) - min(*y_coords)

## Examples of helper functions that correctly use the tag parameter
def make_circle(canvas, center, radius, fill_color='white', tag=None, stroke_width=2, outline="white"):
    make_oval(
        canvas, center, radius, radius, color=fill_color, tag=tag,
        stroke_width=stroke_width, outline=outline
    )

def make_oval(canvas, center, radius_x, radius_y, color='#FF4136', tag=None, stroke_width=1, outline=None):
    x, y = center
    return canvas.create_oval(
        [x - radius_x, y - radius_y, x + radius_x, y + radius_y],
        fill=color,
        width=stroke_width,
        tags=tag,
        outline=outline
    )

def make_cloud(canvas, center, tag=None):
      '''
    Name: make_cloud
    Purpose: draws a cloud to a given canvas object
    Inputs:
      1. a canvas (Canvas) to draw on
      2. a center (tuple) to center the cloud at
      3. a tag (str) to give the cloud a name
    '''
    for i in range(randint(0, 10)):
        x_offset = randint(-40, 40)
        y_offset = randint(0, 20)
        make_circle(canvas, (center[0] + x_offset,
                    center[1] + y_offset), randint(10, 50))
